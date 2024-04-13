import random
import src.globals as globals
import tkinter
from time import perf_counter

def create_text():
    '''функция, генерирующая случайный набор слов для пользователя,
       причём слов в тексте не больше разрешенного text_size'''

    f = open('src/dictionary.txt')
    words = f.read().split(' ')
    f.close()
    text = ""

    i = 0
    while i < globals.cnt_words:
        j = 0
        while j < globals.string_size:
           index = random.randint(0, len(words) - 1)
           text += words[index] + ' '
           j += len(words[index]) + 1
           i += 1
           if i >= globals.cnt_words:
               break
        if i != globals.cnt_words:
            text += '\n'

    return text

def create_field(text):
    '''функция, создающая поле для отображения текста для пользователя'''

    field = tkinter.Label(
        foreground=globals.fore_color,
        font=("Times New Roman", 18),
        text=text
    )
    field.pack()

    return field

def calculate_result(time):
    '''функция, показывающая результат пользователя.
       результат обновляется, если он оказался лучше рекордного'''

    current_speed = len(create_text()) / time

    return current_speed

def key_down(event):
    '''функция, обрабатывающая нажатия клавиш пользователем'''
    index = 0
    if event.char == globals.current_text[index]:
        if len(globals.current_text) == 1:
            globals.window.unbind("<KeyPress>")
            globals.finish_time = perf_counter()
            current_speed = calculate_result(globals.finish_time - globals.start_time)
            show_record(current_speed)


        globals.text_field.destroy()
        globals.current_text = globals.current_text[(index + 1)::]
        globals.text_field = create_field(globals.current_text)

def start_testing():
    '''функция, запускающая само тестирование'''
    if globals.is_testing:
        globals.text_field.destroy()
        globals.current_text = create_text()
        globals.text_field = create_field(globals.current_text)
    else:
        globals.is_testing = True
        globals.text_field = create_field(globals.current_text)

    globals.window.bind("<KeyPress>", key_down)
    globals.start_time = perf_counter()

def show_record(current_speed):
    if current_speed < globals.record_speed or globals.record_speed == 0:
        globals.record_speed = current_speed

    str_result = f"current result: {current_speed}"

    if globals.record_speed == 0:
        str_record = "best result: ____"
    else:
        str_record = f"best result: {globals.record_speed}"

    user_record = tkinter.Label(
        text=f"{str_result}\n{str_record}",
        font=("Times New Roman", 18)
    )
    globals.user_record.destroy()
    user_record.place(x=50, y=320)
    globals.user_record = user_record

def reset_record():
    '''функция, сбрасывающая рекорд'''
    show_record(0)