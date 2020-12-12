import PySimpleGUI as sg
import datetime

# 定数の設定
START = False
FINISH = False
IDEANUMBER = 1
IDEAS = [['None','None']]
IDEASRIGHT = ''
TIME_START = datetime.datetime.now()
TIME_LASTIDEA = datetime.datetime.now()
EXPERIMENT_TIME = 15
EXPRAIN = '使用方法：空欄に記入して、エンターキーを押すと入力されます。'
THEME = 'テーマ：'
THEMELIST = ['新しい消しごむのアイデア','新しい冷蔵庫の機能とデザインのアイデア','新しい洗濯機の機能とデザインのアイデア']
THEME += THEMELIST[2]

#残り時間を返す関数
def remaining_time(seconds):
    experiment_seconds = EXPERIMENT_TIME*60
    rem_time = experiment_seconds - seconds
    if rem_time < 0:
        rem_time = 0
    rem_minute, rem_seconds = divmod(rem_time,60)

    return "残り{0}分{1}秒".format(rem_minute,rem_seconds)

#  セクション1 - オプションの設定と標準レイアウト
sg.theme('SystemDefault')

layout = [
    [sg.Text(THEME,font=(20))],
    [sg.Text(EXPRAIN)],
    [sg.Text('はじめに実行ボタンを押すかエンターキーを押してください。押した時点からスタートします。',key='-STTEXT-')],
    [sg.Text('アイデアを入力',size=(15,1)),sg.InputText(size=(100,1),key='-IDEA-')],
    [sg.Submit(button_text='実行ボタン')],
    [sg.Table(IDEAS, headings=['番号','アイデア'], key='-TABLE-', num_rows=2)],
]

# セクション 2 - ウィンドウの生成
# FinalizeとMaximizeで最大化する
window = sg.Window('アイデア出し', layout,resizable=True,return_keyboard_events=True).Finalize()
window.Maximize()
window['-TABLE-'].expand(True,True)
#window['-IDEAS-'].expand(True,True)
#window['-IDEASRIGHT-'].expand(True,True)

# セクション 3 - イベントループ
while True:
    event, values = window.read(timeout=100,timeout_key='-timeout-')
    now = datetime.datetime.now()
    split = (now - TIME_START).seconds

    #実験時間を越えたら、もう書き込み出来ないようにする。
    #実験終了時の処理をする。
    if split > EXPERIMENT_TIME*60 and FINISH == False:
        FINISH = True

    if event in (None,):
        print('exit')
        break
    elif event in '-timeout-':
        if START == True:
            window['-STTEXT-'].update(remaining_time(split))


    if event == '実行ボタン':
        if START == True and FINISH == False:
            idea = values['-IDEA-']
            if idea != '':
                if IDEANUMBER == 1:
                    IDEAS.clear()
                IDEAS.append([IDEANUMBER,idea])
                IDEANUMBER += 1
                window['-IDEA-'].update('')
                window['-TABLE-'].update(values=IDEAS)


                mergin = (now - TIME_LASTIDEA).seconds
                TIME_LASTIDEA = now
                print(idea,split,mergin)
        elif START == False:
            START = True
            window['-STTEXT-'].update('')
            TIME_START = datetime.datetime.now()
            TIME_LASTIDEA = datetime.datetime.now()
            print('アイデア','アイデアを出した時間','アイデア間隔')

            

# セクション 4 - ウィンドウの破棄と終了
window.close()