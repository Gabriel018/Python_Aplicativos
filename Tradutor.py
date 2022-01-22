from tkinter import *
import googletrans
import textblob

root = Tk()
root.title('Tradutor')
root.geometry('600x400')

texto =  Text(root,height='10',width='60')
texto.grid(row='0',column='0')

Translater =  Button(root,text='Traduzir',font='40')
Translater.grid(row='1',column='0')

Traducion =  Text(root,height='10',width='60')
Traducion.grid(row='2',column='0')


root.mainloop()