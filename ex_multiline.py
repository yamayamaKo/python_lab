import PySimpleGUI as sg
import datetime
import pyperclip

THEMENUMBER = int(input())

# 定数の設定
START = False
FINISH = False
IDEANUMBER = 1
IDEAS = ''
TIME_START = datetime.datetime.now()
TIME_LASTIDEA = datetime.datetime.now()
EXPERIMENT_TIME = 0.5
EXPRAIN = '使用方法：空欄に記入して、エンターキーを押すと入力されます。'
THEME = 'テーマ：'
THEMELIST = ['男性用ズボンを改善するアイデア','新しい消しごむのアイデア','新しいペンのアイデア','新しい冷蔵庫の機能とデザインのアイデア','新しい洗濯機の機能とデザインのアイデア']
# THEMELIST = ['朝早く起きるにはどうすればよいか','ダイエットを継続するにはどうすればよいか','忘れ物を減らすにはどうすればよいか','新聞社の新しい事業','マッサージ店を繁盛させるには']
THEME += THEMELIST[THEMENUMBER]
RESULT = ''

#残り時間を返す関数
def remaining_time(seconds):
    experiment_seconds = EXPERIMENT_TIME*60
    rem_time = experiment_seconds - seconds
    if rem_time < 0:
        rem_time = 0
    rem_minute, rem_seconds = divmod(rem_time,60)

    return "残り{0}分{1}秒".format(rem_minute,rem_seconds)

print(THEME)
RESULT += THEME + '\n'

#  セクション1 - オプションの設定と標準レイアウト
sg.theme('SystemDefault')

layout = [
    [sg.Text(THEME,font=(20))],
    [sg.Text(EXPRAIN)],
    [sg.Text('はじめに実行ボタンを押すかエンターキーを押してください。押した時点からスタートします。',key='-STTEXT-')],
    [sg.Text('アイデアを入力',size=(15,1)),sg.InputText(size=(100,1),key='-IDEA-')],
    [sg.Submit(button_text='実行ボタン')],
    [sg.Multiline(size=(70,1),font=('明朝体',20), autoscroll=True, key='-IDEAS-')]
]

# セクション 2 - ウィンドウの生成
# FinalizeとMaximizeで最大化する
window = sg.Window('アイデア出し', layout,resizable=True,return_keyboard_events=True,\
        keep_on_top=True).Finalize()
window.Maximize()
window['-IDEAS-'].expand(True,True)

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
                # IDEAS = str(IDEANUMBER)+' '+idea + '\n' + IDEAS
                IDEAS += str(IDEANUMBER)+' '+idea + '\n'
                window['-IDEA-'].update('')
                window['-IDEAS-'].update(IDEAS)
                mergin = (now - TIME_LASTIDEA).seconds
                TIME_LASTIDEA = now
                print(IDEANUMBER,idea,split,mergin)
                RESULT += str(IDEANUMBER)+' '+idea+' '+str(split)+' '+str(mergin)+'\n'
                IDEANUMBER += 1
        elif START == False:
            START = True
            window['-STTEXT-'].update('')
            TIME_START = datetime.datetime.now()
            TIME_LASTIDEA = datetime.datetime.now()
            print('アイデア','アイデアを出した時間','アイデア間隔')

            
pyperclip.copy(RESULT)
# セクション 4 - ウィンドウの破棄と終了
window.close()