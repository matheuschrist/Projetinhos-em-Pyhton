import pyautogui



#abrir google chrome

#pyautogui.press(['win','r'])
pyautogui.PAUSE=2

pyautogui.alert("O Código vai começar não utilize seu Computador!")
with pyautogui.hold('win'):
        pyautogui.press('r')
        


pyautogui.write('Chrome')

pyautogui.press('enter')

pyautogui.write("https://drive.google.com/drive/u/0/my-drive")
pyautogui.press('enter')


pyautogui.hotkey('win','d')
pyautogui.moveTo(x=1076, y=134)
pyautogui.mouseDown()
pyautogui.moveTo(x=700, y=594)
pyautogui.hotkey('alt','tab')

pyautogui.mouseUp()


pyautogui.alert("O Código finalizou!")


