import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import pygal 


#Faz uma chamada de API e armazena a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url) 
#print("Status code:", r.status_code)
# Processa informações sobre cada artigo submetido v 
submission_ids = r.json() 
submission_dicts = [] 
for submission_id in submission_ids[:30]:
    # Cria uma chamada de API separada para cada artigo submetido 
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url) 
    #print(submission_r.status_code)
    response_dict = submission_r.json() 
    submission_dict = { 'title': response_dict['title'], 
                       'link': 'http://news.ycombinator.com/item?id=' 
                       + str(submission_id), 
                       'comments': response_dict.get('descendants', 0) 
                       } 
    submission_dicts.append(submission_dict) 
#submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True) 

submission_dicts_names=[]
submission_dicts_info=[]
for submission_dict in submission_dicts:
   submission_dicts_names.append(submission_dict['title'])
   num_comments=int(submission_dict['comments'])
   #print(num_comments)
   submission_dict_info={
                'value': num_comments, 
                 'label': submission_dict['title'],
                 'xlink': submission_dict['link']
                 }  
    
   submission_dicts_info.append(submission_dict_info)
   
# Cria a visualização 
my_style = LS('#333366', base_style=LCS)


my_config = pygal.Config() 
my_config.x_label_rotation = 45 
my_config.show_legend = False 
my_config.title_font_size = 24 
my_config.label_font_size = 14 
my_config.major_label_font_size = 12 
my_config.truncate_label = 12 
my_config.show_y_guides = False 
my_config.width = 1000
    
chart = pygal.Bar(my_config, style=my_style) 
chart.title = 'Exibe as noticias mais relevantes' 
chart.x_labels = submission_dicts_names
chart.add('',submission_dicts_info)
chart.render_to_file('hacked-news.svg')

