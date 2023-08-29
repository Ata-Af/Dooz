from tkinter import *
import tkinter as tk

def reset():
    gamePage()

onclick = 1
def gamePage():
    gamePage = tk.Toplevel()
    gamePage.geometry('250x270')
    gamePage.config(bg='darkcyan')
    gamePage.title('Dooz Game')
    gamePage.resizable(0, 0)

    def restart():
        global onclick
        try:
            gamePage.destroy()
            onclick = 1
            reset()
        except ValueError:
            print('Error')

    def unusableB ():
        try:
            b1.configure(state=DISABLED)
            b2.configure(state=DISABLED)
            b3.configure(state=DISABLED)
            b4.configure(state=DISABLED)
            b5.configure(state=DISABLED)
            b6.configure(state=DISABLED)
            b7.configure(state=DISABLED)
            b8.configure(state=DISABLED)
            b9.configure(state=DISABLED)

        except ValueError:
            print(' Error ')

    def gameRoll(button):
        global onclick
        if button['text'] == '' and onclick == 1:
            button['text'] = 'X'
            onclick = 0
            gameRollInfo['text']='< Its '+n2_E.get()+'\'s turn >'
            winner()

        elif button['text'] == '' and onclick == 0:
            button['text'] = 'O'
            onclick = 1
            gameRollInfo['text']='< Its '+n1_E.get()+'\'s turn >'
            winner()

    def winner ():


        if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' ):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b1['bg']='lightgreen'; b2['bg']='lightgreen'; b3['bg']='lightgreen'
            unusableB()
        elif (b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X'):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b4['bg']='lightgreen'; b5['bg']='lightgreen'; b6['bg']='lightgreen'
            unusableB()
        elif (b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X'):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b7['bg']='lightgreen'; b8['bg']='lightgreen'; b9['bg']='lightgreen'
            unusableB()
        elif (b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X'):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b1['bg']='lightgreen'; b5['bg']='lightgreen'; b9['bg']='lightgreen'
            unusableB()
        elif (b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X'):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b3['bg']='lightgreen'; b5['bg']='lightgreen'; b7['bg']='lightgreen'
            unusableB()
        elif (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X'):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b1['bg']='lightgreen'; b2['bg']='lightgreen'; b3['bg']='lightgreen'
            unusableB()
        elif (b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X'):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b1['bg']='lightgreen'; b4['bg']='lightgreen'; b7['bg']='lightgreen'
            unusableB()
        elif (b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X'):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b2['bg']='lightgreen'; b5['bg']='lightgreen'; b8['bg']='lightgreen'
            unusableB()
        elif (b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
            gameRollInfo['text']='---> '+n1_E.get()+' Wins <---'; b3['bg']='lightgreen'; b6['bg']='lightgreen'; b9['bg']='lightgreen'
            unusableB()


        elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' ):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b1['bg']='lightgreen'; b2['bg']='lightgreen'; b3['bg']='lightgreen'
            unusableB()
        elif (b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O'):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b4['bg']='lightgreen'; b5['bg']='lightgreen'; b6['bg']='lightgreen'
            unusableB()
        elif (b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O'):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b7['bg']='lightgreen'; b8['bg']='lightgreen'; b9['bg']='lightgreen'
            unusableB()
        elif (b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O'):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b1['bg']='lightgreen'; b5['bg']='lightgreen'; b9['bg']='lightgreen'
            unusableB()
        elif (b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O'):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b3['bg']='lightgreen'; b5['bg']='lightgreen'; b7['bg']='lightgreen'
            unusableB()
        elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O'):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b1['bg']='lightgreen'; b2['bg']='lightgreen'; b3['bg']='lightgreen'
            unusableB()
        elif (b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O'):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b1['bg']='lightgreen'; b4['bg']='lightgreen'; b7['bg']='lightgreen'
            unusableB()
        elif (b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O'):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b2['bg']='lightgreen'; b5['bg']='lightgreen'; b8['bg']='lightgreen'
            unusableB()
        elif (b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
            gameRollInfo['text']='---> '+n2_E.get()+' Wins <---'; b3['bg']='lightgreen'; b6['bg']='lightgreen'; b9['bg']='lightgreen'
            unusableB()


    b1 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b1))
    b1.place(x=6, y=7)

    b2 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b2))
    b2.place(x=86, y=7)

    b3 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b3))
    b3.place(x=166, y=7)

    b4 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b4))
    b4.place(x=6, y=85)

    b5 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b5))
    b5.place(x=86, y=85)

    b6 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b6))
    b6.place(x=166, y=85)

    b7 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b7))
    b7.place(x=6, y=163)

    b8 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b8))
    b8.place(x=86, y=163)
    b9 = tk.Button(gamePage, text='', width=9, height=4, bd=5, bg='darkgrey', command=lambda: gameRoll(b9))
    b9.place(x=166, y=163)
    gameRollInfo = tk.Label(gamePage, text=('< its '+n1_E.get()+'\'s turn >'), bg='darkcyan', font='Calibri 12')
    gameRollInfo.pack(anchor='center', side='bottom', ipady=2)
    restartB = tk.Button(gamePage, bg='darkcyan', bd=0, activebackground='darkcyan', image=restartB_image, command=lambda :restart())
    restartB.place(x=225, y=243)
mainpage = tk.Tk()
mainpage.geometry('250x247')
mainpage.title('Dooz Game')
mainpage.config(bg='darkcyan')
mainpage.resizable(0, 0)
infoLabel = tk.Label(mainpage, text='''Hi Dear :)
This is Dooz game
Designed by Ata Aminifar''', fg='white', bg='darkcyan', justify='left')
infoLabel.config(font=('Arial', 12))
infoLabel.place(x=10, y=20)
getInfoLabel = tk.Label(mainpage, text='Pls Enter players name : ', bg='darkcyan', fg='white')
getInfoLabel.config(font=('times', 10))
getInfoLabel.place(x=10, y=100)
n1_l = tk.Label(mainpage, text='Player  ( X )  = ', bg='darkcyan', fg='white')
n1_l.config(font=('times', 10))
n1_l.place(x=10, y=130)
n1_E = tk.Entry(mainpage, width=20, bg='darkcyan', bd=3)
n1_E.place(x=100, y=130)
n2_E = tk.Entry(mainpage, width=20, bg='darkcyan', bd=3)
n2_E.place(x=100, y=160)

n2_l = tk.Label(mainpage, text='Player  ( O )  = ', bg='darkcyan', fg='white')
n2_l.config(font=('times', 10))
n2_l.place(x=10, y=160)

b_start = tk.Button(mainpage, width=30, text='Press to start', bg='darkcyan', fg='white', bd=3, command=gamePage)
b_start.config(font=('Times', 10))
b_start.place(x=13, y=210)

restartB_image = tk.PhotoImage(file='RestartB.png')

mainpage.mainloop()
