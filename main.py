'''
以下の機能をもつプログラムを作成する
・コマンドラインで7つの引数を指定する
・最初の引数が月曜日のタスク、最後の引数が日曜日のタスクとして以下の形式で出力する
    月曜日：（１つ目の引数）
    火曜日：（２つ目の引数）
    ～
    日曜日：（７つ目の引数）
・但し、上記の出力は月曜日に実行した際の出力順序で
    プログラムが実行された曜日を先頭にしてタスクを出力する
    例）土曜日に実行された場合
    土曜日：（６つ目の引数）
    日曜日：（７つ目の引数）
    月曜日：（１つ目の引数）
    ～
    金曜日：（５つ目の引数）
・引数が７つ以外であれば利用法を表示する

'''
from sys import argv
from datetime import datetime


def print_weekday(tasks):
    """_summary_
    曜日を出す関数

    Args:tasks
        arg (_type_): 複数のタスク
    """

    weekday = datetime.now().weekday()

    tasks = []
    for index in tasks:
        tasks.append(index)

    for index in range(weekday, weekday + 7):

        if index >= 7:
            index = index - 7

        if index == 0:
            week_title = '月曜日'
        elif index == 1:
            week_title = '火曜日'
        elif index == 2:
            week_title = '水曜日'
        elif index == 3:
            week_title = '木曜日'
        elif index == 4:
            week_title = '金曜日'
        elif index == 5:
            week_title = '土曜日'
        elif index == 6:
            week_title = '日曜日'

        print(f'{week_title}:{tasks[index]}')


if __name__ == '__main__':

    if len(argv) != 8:
        print('曜日毎のタスクを７つ入力してください')
        exit(0)

    print_weekday(argv[1:])