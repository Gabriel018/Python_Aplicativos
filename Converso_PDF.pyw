

from pdf2docx import parse
from typing import Tuple
import PySimpleGUI as py


py.theme("DarkBlue")

class convert:

    def __init__(self):

     def pdf_convert(arq_pfd: str, arq_convert: str, pages: Tuple = None):
            super(convert, self).pdf_convert(arq_pfd: str, arq_convert: str, pages: Tuple = None)

       result = parse(pdf_file=arq_pfd,
                       docx_file=arq_convert,
                       pages=pages)

       return result

    def comvert(self):
        # Quando salvar o arquivo salvar ele com a extençao  " .docx "

                 layout = [
                       [py.Text("Conversor de PDF para DOCX",font="arial 14")],
                      [py.Input(size=(30),key='pdf'),py.FileBrowse(font="Arial ")],
                      [py.Input(size=(30),key='doc'),py.FileSaveAs(font="Arial ")],
                      [py.Button("Converter",key="convert",font="Arial 12 "),] ]


                 janela = py.Window("Conversor de PDF", layout, size=(330, 300))

                 while True:

                  event,values = janela.read()
                  if event == "convert":
                    py.popup("Quando for salvar o arquivo salve com o final .docx ",font="arial 14")
                    arq_pfd = values['pdf']
                    arq_convert = values['doc']
                    py.popup_notify("Aguarde seu Arquivo sera convertido")
                    self.pdf_convert(arq_pfd, arq_convert)
                    py.popup("Concluido",font="arial 12")
                  if event == "Exit" or event == py.WIN_CLOSED:
                      break

    def pdf_convert(self, arq_pfd, arq_convert):
        pass


if __name__ == '__main__':
