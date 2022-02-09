import PySimpleGUI as pg


class Tradutor:
    def __init__(self):

        self.layout = [ [pg.InputText(size=(100,20))]
                        ]

    def iniciar(self):

        self.janela = pg.Window('Tradutor',self.layout,size=(600,600) )
        while True:
            event,values = self.janela.read()
            if event == pg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
             break

Traduzir = Tradutor()

Traduzir.iniciar()
