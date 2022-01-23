from tkinter import *
import googletrans
import textblob
from tkinter import  ttk, messagebox

def Translater():
     for key, value in languages.items():
         if (value == choice_language_origen.get()):
             from_languege_key = key


     for key, value in languages.items():
        if (value == choice_language_Translater.get()):
            to_languege_key = key

     words = textblob.TextBlob(texto.get(1.0,END))
     words = words.translate(from_lang=from_languege_key,to=to_languege_key)
     Traducion.insert(1.0,words)

def Clear():
    texto.delete(1.0,END)
    Traducion.delete(1.0,END)
languages =  googletrans.LANGUAGES

lang_list = list(languages.values())

root = Tk()
root.title('Tradutor')
root.geometry('600x400')

texto =  Text(root,height='10',width='60')
texto.grid(row='0',column='0')

Translater =  Button(root,text='Traduzir',font='40', command=Translater)
Translater.grid(row='1',column='1')

Clear_btn =  Button(root,text='Limpar',font='40',command=Clear)
Clear_btn.grid(row='1',column='2')

Traducion =  Text(root,height='10',width='60')
Traducion.grid(row='2',column='0')



choice_language_origen = ttk.Combobox(root,width=20, value=lang_list)
choice_language_origen.current(1)
choice_language_origen.grid(row=1,column=0)

choice_language_Translater = ttk.Combobox(root,width=20, value=lang_list)
choice_language_Translater.current(1)
choice_language_Translater.grid(row='3',column='0')




root.mainloop()