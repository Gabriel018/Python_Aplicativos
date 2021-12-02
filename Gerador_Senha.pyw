import random
import PySimpleGUI as py


class Gerador:
    def __init__(self):

        self.layout = [ [py.Text("Quantos numeros deseja na senha?",
                                 background_color='black',
                                 font='Arial 14',
                                 text_color='yellow')],
                        [py.Input(key='pass',
                                  font="Arial,12")],
                        [py.Button("Gerar",
                                   font="Arial,12"),
                         py.Button("Cancel",
                                   font="Arial,12")]
]

    def Iniciar(self):

        self.janela = py.Window("Gerador de Senhas:",self.layout,size=(400,300),background_color='black')

        while True:
         self.event, self.values = self.janela.read()
         self.password = self.values['pass']
         while self.event == "Gerar":


           self.words = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
           self.newpass = "".join(random.sample(self.words, int(self.password)))
           py.popup("Sua senha e: ",self.newpass,font='Arial 14',)
           break

Geradores = Gerador()
Geradores.Iniciar()
