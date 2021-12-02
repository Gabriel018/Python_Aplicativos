import PySimpleGUI as py
import time

def timer_new():
    return int(round(time.time() * 100))

#Cria a janela

py.theme('Dark')


layout =  [ [py.Text('',size=(10,2),key='text',font='Arial 26',justification='center',text_color='yellow',
                        background_color='black')],
            [py.Button('Pausar',key='-Run-Pause-',font='Arial 14'),
             py.Button('Resetar',key='-Reset-',font='Arial 14')]
]

janela = py.Window("Cronometro",layout,size=(400,300),background_color='Black',element_justification='center')

current_time,pause_time, paused = 0,0, False
start_time = timer_new()
while True :
    if not paused:
        event,values = janela.read(timeout=10)
        current_time = timer_new() - start_time
    else:
        event,values = janela.read()
    if event in (py.WINDOW_CLOSED, 'Exit'):
        break

    if event == '-Reset-':
        pause_time = start_time = timer_new()
        current_time = 0
    elif event == '-Run-Pause-':
        paused = not paused
        if paused:
           pause_time = timer_new()
        else:
            start_time = start_time + timer_new() - pause_time
        janela['-Run-Pause-'].update('Iniciar' if paused else 'Pause')
    elif event == 'Edit Me':
            py.execute_editor(__file__)
    janela['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                        (current_time // 100) % 60,
                                                        current_time % 100))


janela.close()