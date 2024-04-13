import tkinter
import src.functions as functions
import src.globals as globals

'''генерация текста для пользователя'''
globals.current_text = functions.create_text()

'''создание окна'''
globals.window.geometry('900x500')
globals.window.title('typing trainer')
globals.window.configure(background=globals.back_color)

'''создание кнопки для запуска тренажёра'''
start_button = tkinter.Button(
    globals.window,
    text="start",
    font=("Times New Roman", 20),
    command=functions.start_testing
)
start_button.place(x=700, y=320)

'''создание поля, отображающего текущий и лучший результаты'''
globals.user_record = tkinter.Label(
    globals.window,
    text="current result: ____\nbest result: ____",
    font=("Times New Roman", 18)
)
globals.user_record.place(x=50, y=320)

'''создание кнопки для сброса рекорда'''
reset_button = tkinter.Button(
    globals.window,
    text="reset",
    font=("Times New Roman", 20),
    command=functions.reset_record
)
reset_button.place(x=700, y=380)

globals.window.mainloop()
