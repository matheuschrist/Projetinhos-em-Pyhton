from pygal.maps.world import COUNTRIES


def get_country_code(country_name): 
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome.""" 
    for code, name in COUNTRIES.items(): 
        if name == country_name: 
            return code 
    # Se o país não foi encontrado, devolve None x  
   
    return None 

