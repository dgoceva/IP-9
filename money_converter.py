import PySimpleGUI as sg
from PIL import Image
import time

BGN_EUR = 0.51129188
EUR_BGN = 1.95583

# bgn = float(input('BGN='))
# print('EUR', round(bgn*BGN_EUR, 6))

if not (7 < time.localtime(time.time()).tm_hour < 18):
    sg.theme('Topanga')
else:
    sg.theme('TealMono')

layout = [
    [sg.Combo(('BGN', 'EUR'), default_value='BGN', key='-IN-CURRENCY-'),
     sg.InputText(size=20, key='-IN-'), sg.Button('Convert')],
    [sg.Text('EUR', size=5, key='-OUT-CURRENCY-'),
     sg.InputText(size=20, readonly=True, key='-OUT-')],
    [sg.Image('lovepik-villain-carrying-euro-symbol-png-image_401759462_wh300.png', key='-OUT-IMAGE-')]
]

window = sg.Window('Money Converter', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Convert' and values['-IN-'] != '':
        if values['-IN-CURRENCY-'] == 'BGN':
            # print(round(float(values['-IN-'])*BGN_EUR, 6))
            window['-OUT-'].update(round(float(values['-IN-'])*BGN_EUR, 6))
            window['-OUT-CURRENCY-'].update('EUR')
            window['-OUT-IMAGE-'].update(
                'lovepik-villain-carrying-euro-symbol-png-image_401759462_wh300.png')
        else:
            window['-OUT-'].update(round(float(values['-IN-'])*EUR_BGN, 6))
            window['-OUT-CURRENCY-'].update('BGN')
            window['-OUT-IMAGE-'].update('Belgium.png')
window.close()
