import PySimpleGUI as pg
import googletrans
import textblob

class Tradutor:
    def __init__(self):
        languages = googletrans.LANGUAGES

        lang_list = list(languages.values())

        self.layout = [ [pg.Output(size=(60,15),key='txt_original')],
                        [pg.Combo(lang_list,key='lang_atual')],
                        [pg.Button('Traduzir'),pg.Button('Limpar')],
                        [pg.Output(size=(60,15),key='txt_traduzir')],
                        [pg.Combo(lang_list,key='lang_traduzir')]
                        ]

    def iniciar(self):
        self.janela = pg.Window('Tradutor',self.layout,size=(600,600) )

        languages = googletrans.LANGUAGES



        while True:
            event,values = self.janela.read()
            languages = googletrans.LANGUAGES

            lang_list = list(languages.values)
            for key, value in languages.items():
                if (value == values['lang_atual'].get()):
                    from_languege_key = key

            for key, value in languages.items():
                if (value == values['lang_traduzir'].get()):
                    to_languege_key = key
            txt_original = values['txt_original']
            txt_traduzir = values['txt_traduzir']
            words = textblob.TextBlob(txt_original.get())
            words = words.translate(from_lang=from_languege_key, to=to_languege_key)
            txt_traduzir.insert()



            if event == pg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
             break






Traduzir = Tradutor()

Traduzir.iniciar()
