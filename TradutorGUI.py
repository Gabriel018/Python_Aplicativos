import PySimpleGUI as pg
import googletrans

class Tradutor:
    def __init__(self):
        languages = googletrans.LANGUAGES

        lang_list = list(languages.values())

        self.layout = [ [pg.Output(size=(60,15))],
                        [pg.Combo(lang_list,key='atual')],
                        [pg.Button('Traduzir'),pg.Button('Limpar')],
                        [pg.Output(size=(60,15))],
                        [pg.Combo(lang_list,key='traduzir')]
                        ]

    def iniciar(self):
        self.janela = pg.Window('Tradutor',self.layout,size=(600,600) )
        while True:
            event,values = self.janela.read()
            if event == pg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
             break

Traduzir = Tradutor()

Traduzir.iniciar()
