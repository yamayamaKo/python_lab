import PySimpleGUI as sg

"""
   PySimpleGUIのテーマをPySimpleGUIを使って確認することができます。
   いずれかのテーマ名をクリックすると、選択したテーマを使用したウィンドウが出ます。
"""

sg.theme('Dark Brown')

layout = [[sg.Text('Look and Feel Browser')],
         [sg.Text('Click a look and feel color to see demo window')],
         [sg.Listbox(values=sg.theme_list(),
                     size=(20, 12), key='-LIST-', enable_events=True)],
         [sg.Button('Exit')]]

window = sg.Window('Look and Feel Browser', layout)

while True:  # Event Loop
   event, values = window.read()
   if event in (None, 'Exit'):
       break
   sg.theme(values['-LIST-'][0])
   sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()