import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from math import *
import pyperclip
import qrcode
from PIL import Image, ImageTk
import webbrowser
import functools
rnd = -1

def main():
    global rnd
    root = tk.Tk()

    root.title("Smart Calc")
    # root.geometry('260x400')

    root.iconbitmap('icon.ico')
    root.resizable(width=False, height=False)
    tabControl = ttk.Notebook(root)

    tab1 = tk.Frame(tabControl, width=260, height=400)
    tab2 = tk.Frame(tabControl, width=400, height=400)
    tab3 = tk.Frame(tabControl, width=260, height=400, relief=tk.RAISED)
    #tab4 = tk.Frame(tabControl, width=260, height=400, relief=tk.RAISED)

    tabControl.add(tab1, text='Калькулятор')
    tabControl.add(tab2, text='Квадр. уравн.')
    tabControl.add(tab3, text='Графики')
    #tabControl.add(tab4, text='Новая вкладка')
    tabControl.pack(fill=BOTH, expand=1)

    def add_digit(digit):
        value = calc.get()
        if value[0] == '0' and len(value) == 1:
            value = value[1:]
        calc.delete(0, END)
        calc.insert(0, value + digit)

    def add_operation(operation):
        value = calc.get()
        if value[-1] in '-+/*':
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            calculate()
            value = calc.get()
        calc.delete(0, END)
        calc.insert(0, value + operation)
    def round_rnd(n):
        global rnd
        return round(n, rnd)


    def calculate():
        value = calc.get()
        if value[-1] in '-+/*':
            value = value + value[:-1]
        calc.delete(0, END)
        try:
            ans = eval(value)
            if ans == int(ans):
                ans = int(ans)
            global rnd
            if rnd != -1:
                ans = round_rnd(ans)
            calc.insert(0, ans)
        except (NameError, SyntaxError):
            messagebox.showinfo('Внимание!', 'Нужно вводить только числа!')
            calc.insert(0, 0)
        except ZeroDivisionError:
            messagebox.showinfo('Внимание!', 'На ноль делить нельзя!')
            calc.insert(0, 0)
        #понять как получается вывод в поле calc и сохранить его в буфер обмена
    def add_sqrt():
        value = calc.get()
        value = float(value)
        ans = sqrt(value)
        if ans == int(ans):
            ans = int(ans)
        global rnd
        if rnd != -1:
            ans = round_rnd(ans)
        calc.delete(0, END)
        calc.insert(0, ans)

    def add_ln():
        value = calc.get()
        value = eval(value)
        try:
            value = log(value)
            ans = value
            if ans == int(ans):
                ans = int(ans)
            global rnd
            if rnd != -1:
                ans = round_rnd(ans)
            calc.delete(0, END)
            calc.insert(0, ans)
        except:
            messagebox.showinfo("Ошибка!", 'Не удалось вычислить')

    def clear():
        calc.delete(0, END)
        calc.insert(0, 0)

    def make_calc_button(operation):
        return Button(tab1, text=operation, bd=5, font=('Times New Roman', 13),
                      command=calculate, bg='#ed7e15')

    def make_clear_button(operation):
        return Button(tab1, text=operation, bd=5, font=('Times New Roman', 13),
                      command=clear, bg='#ed7e15')

    def make_operation_button(operation):
        return Button(tab1, text=operation, bd=5, font=('Times New Roman', 13),
                      command=lambda: add_operation(operation), bg='#ed7e15')

    def make_sqrt_button(operation):
        return Button(tab1, text=operation, bd=5, font=('Times New Roman', 13),
                      command=add_sqrt, bg='#ed7e15')

    def make_ln_button(operation):
        return Button(tab1, text=operation, bd=5, font=('Times New Roman', 13),
                      command=add_ln, bg='#ed7e15')

    def make_digit_button(digit):
        return Button(tab1, text=digit, bd=5, font=('Times New Roman', 13),
                      command=lambda: add_digit(digit), bg='#ed7e15')

    # делаем всё, что касается первой вкладки, то есть обычного калькулятора
    calc = Entry(tab1, justify=RIGHT, font=('Times New Roman', 15), fg='#ed7e15', width=15,
                 highlightbackground='#ed7e15', highlightthickness=1)
    calc.insert(0, '0')
    calc.place(x=15, y=20, width=220, height=30)

    # Числа от 1 до 9 и точка

    make_digit_button('1').place(x=20, y=250, width=40, height=40)
    make_digit_button('2').place(x=80, y=250, width=40, height=40)
    make_digit_button('3').place(x=140, y=250, width=40, height=40)
    make_digit_button('4').place(x=20, y=190, width=40, height=40)
    make_digit_button('5').place(x=80, y=190, width=40, height=40)
    make_digit_button('6').place(x=140, y=190, width=40, height=40)
    make_digit_button('7').place(x=20, y=130, width=40, height=40)
    make_digit_button('8').place(x=80, y=130, width=40, height=40)
    make_digit_button('9').place(x=140, y=130, width=40, height=40)
    make_digit_button('0').place(x=20, y=310, width=100, height=40)
    make_digit_button('.').place(x=140, y=310, width=40, height=40)

    # Основные математические действия

    make_operation_button('+').place(x=200, y=310, width=40, height=40)
    make_operation_button('-').place(x=200, y=250, width=40, height=40)
    make_operation_button('*').place(x=200, y=190, width=40, height=40)
    make_operation_button('/').place(x=200, y=130, width=40, height=40)

    # синус
    make_sqrt_button('sqrt').place(x=80, y=70, width=40, height=40)

    # Модуль
    make_ln_button('ln').place(x=140, y=70, width=40, height=40)

    # Кнопка очистки
    make_clear_button('C').place(x=20, y=70, width=40, height=40)

    # Равно
    make_calc_button('=').place(x=200, y=70, width=40, height=40)

    #сделать округление пользуясь global
    def round_to():
        window_rnd = tk.Toplevel(root)
        root.withdraw()
        window_rnd.deiconify()
        window_rnd.iconbitmap('icon.ico')
        window_rnd.geometry('220x200')

        label_rnd = tk.Label(window_rnd, text="введите число знаков после ','", fg='#ed7e15', font=('Times New Roman', 13))
        label_rnd.grid(column=1, row = 1)
        label_rnd2 = tk.Label(window_rnd, text="до которого округлять", fg='#ed7e15',
                             font=('Times New Roman', 13))
        label_rnd2.grid(column=1, row=2)

        def save_rnd():
            global rnd
            try:
                rnd = int(entry_rnd.get())
                if not (0 <= rnd < 10):
                    b = 1 / 0
                status_round.config(text=f"Округление до {rnd} знаков после запятой",width=400)
                window_rnd.destroy()
                root.deiconify()
            except:
                messagebox.showinfo('Внимание!', 'Введите целое число от 0 до 9!!!')
                entry_rnd.delete(0, END)


        def reset_rnd():
            global rnd
            rnd = -1
            messagebox.showinfo('Успешно!', 'Результаты больше не окргуляются')
            status_round.config(text="Округление не производиться", width=400)
            window_rnd.destroy()
            root.deiconify()
        entry_rnd = Entry(window_rnd, justify=RIGHT, font=('Times New Roman', 15), fg='#ed7e15', width=15,
                     highlightbackground='#ed7e15', highlightthickness=1)
        entry_rnd.grid(column=1, row=3)

        round = Button(window_rnd, text="окргулять", command=save_rnd, bg='#ed7e15', font=('Times New Roman', 11), bd=5)
        round.grid(column=1, row = 4)

        reset = Button(window_rnd, text="сбросить", command=reset_rnd, bg='#ed7e15', font=('Times New Roman', 11), bd=5)
        reset.grid(column=1, row=5)




    round_to = Button(tab1, text="окргулять", command=round_to, bg='#ed7e15', font=('Times New Roman', 11), bd=5)
    round_to.place(x=250, y=190, width=70, height=40)

    #работа с буфером

    def copy_txt():
        txt = calc.get()
        pyperclip.copy(txt)
        messagebox.showinfo('Успешно!', 'результат скопирован')

    def paste_txt():
        print(pyperclip.paste())
        try:
            txt = int(pyperclip.paste())
            calc.delete(0, END)
            calc.insert(0, txt)
        except:
            messagebox.showinfo('Внимание!', 'Нужно вводить только числа!')
            calc.delete(0, END)
            calc.insert(0, 0)

    Copy = Button(tab1, text="copy", command = copy_txt, bg = '#ed7e15', font=('Times New Roman', 13), bd = 5)
    Copy.place(x = 250, y = 70, width = 70, height = 40)

    Paste = Button(tab1, text="paste", command=paste_txt, bg='#ed7e15', font=('Times New Roman', 13), bd = 5)
    Paste.place(x=250, y= 130, width=70, height=40)

    #статус округления
    status_round = tk.Label(tab1, text="Округление не производиться",
                            font=('Constantia', 11), justify="left")
    status_round.place(x=20, y=370, width= 300, height=40)







    def solver(a, b, c):
        """ Решает квадратное уравнение и выводит отформатированный ответ """
        # находим дискриминант
        global rnd
        d = b * b - 4 * a * c
        if rnd != -1:
            d = round_rnd(d)

        if d > 0 and a != 0:
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            if rnd != -1:
                x1 = round_rnd(x1)
                x2 = round_rnd(x2)
            text = "Дискриминант равен: %s \n X1 =: %s \n X2 =: %s \n" % (d, x1, x2)
        elif a != 0 and d == 0:
            x1 = (-b) / (a * 2)
            if rnd != -1:
                x1 = round_rnd(x1)
            text = f'Дискриминант = 0 \n X = {x1} \n'
        elif d < 0 and a != 0:
            text = "Дискриминант равен: %s \n Это выражение не имеет решений" % d
        else:
            text = 'Это не квадратное уравнение!!!'
        return text


    def inserter(value):
        output.delete("0.0", "end")
        global rnd
        if rnd != -1:
            value = value + f"\n Округление до {rnd} знаков после запятой"
        else:
            value = value + "\n Округление не производиться"
        output.insert("0.0", value)

    def handler():
        try:
            a_val = float(a.get())
            b_val = float(b.get())
            c_val = float(c.get())
            inserter(solver(a_val, b_val, c_val))
        except ValueError:
            inserter("Убедитесь что введены три числа!")

    def print_graph():
        try:
            a_val = float(a.get())
            b_val = float(b.get())
            c_val = float(c.get())
            # Создаём экземпляр класса figure и добавляем к Figure область Axes

            # Добавим заголовок графика

            # Название оси X:
            # ax.set_xlabel('x')
            # Название оси Y:
            # ax.set_ylabel('y')
            # Начало и конец изменения значения X, разбитое на 100 точек


            x = np.linspace((-b_val) / (2 * a_val) - 5, (-b_val) / (2 * a_val) + 5, 200)
            # Построение прямой
            y1 = a_val * x ** 2 + b_val * x + c_val
            y2 = 0 * x
            fig, ax = plt.subplots()
            fig.set_size_inches(4, 4)
            ax.set_title('График функции')

            a1 = a_val
            b1 = b_val
            c1 = c_val

            d = b1 * b1 - 4 * a1 * c1

            if d > 0 and a1 != 0:
                x1_1 = (-b1 + sqrt(d)) / (2 * a1)
                x2_2 = (-b1 - sqrt(d)) / (2 * a1)
                ax.plot(x1_1, 0, color = 'red', marker = '.', label = f'A({x1_1}, {0}) - пересечение Ox')
                ax.plot(x2_2, 0, color='red', marker='.', label = f'B({x2_2}, {0}) - пересечение Ox')

            elif a1 != 0 and d == 0:
                x1_1 = (-b1) / (a1 * 2)
                ax.plot(x1_1, 0, color='red', marker = '.', label = f'A({x1_1}, {0}) - пересечение Ox')

            # y = 0
            # Вывод графика параболы
            ax.vlines(0, min(y1.min() - 20, -20), max(y1.max() + 20, 20), color='blue')
            ax.plot(x, y1, label=f'y = {a_val} * x ** 2 + {b_val} * x + {c_val}')
            ax.plot(x, y2, label="ось y, x", color='blue')
            ax.grid(axis='both')
            # ax.set_xlabel("x")  # подпись у горизонтальной оси х
            # ax.set_ylabel("y")  # подпись у вертикальной оси y
            ax.legend()  # показывать условные обозначения

            plt.show()
            clear_printgraph_cache()

        except:
            inserter("Убедитесь что введены три числа!")

    but = Button(tab2, text="Решить", command=handler).grid(row=2, column=1, padx=(10, 0))
    btn_kv_print = Button(tab2, text="график", command=print_graph).grid(row=2, column=2, padx=(10, 0))
    a = 0
    a = Entry(tab2, width=3)
    a.grid(row=1, column=1)

    # текст после первого аргумента
    a_lab = Label(tab2, text="x^2+", font=('Times New Roman', 13)).grid(row=1, column=2)

    # поле для ввода второго аргумента уравнения (b)
    b = 0
    b = Entry(tab2, width=3)
    b.grid(row=1, column=3)
    # текст после второго аргумента
    b_lab = Label(tab2, text="x+", font=('Times New Roman', 13)).grid(row=1, column=4)

    # поле для ввода третьего аргумента уравнения (с)
    c = 0
    c = Entry(tab2, width=3)
    c.grid(row=1, column=5)
    # текст после третьего аргумента
    c_lab = Label(tab2, text="= 0", font=('Times New Roman', 13)).grid(row=1, column=6)

    # кнопка решить
    # but = Button(tab2, text="Solve").grid(row=1, column=7, padx=(10, 0))

    # место для вывода решения уравнения
    output = Text(tab2, bg="#f2670a", font=('Times New Roman', 13), width=35, height=10)
    output.grid(row=3, columnspan=7)

    def draw():
        #clear_draw_cache()
        try:
            func1 = str(getfunc.get())
            func = func1[3::]
            # Создаём экземпляр класса figure и добавляем к Figure область Axes

            # Добавим заголовок графика

            # Название оси X:

            # Начало и конец изменения значения X, разбитое на 100 точек
            x = np.linspace(-20, 20, 200)  # X от -5 до 5
            try:
                y1 = eval(func)
            except Exception as exx:
                messagebox.showinfo("dfdf", exx)
                y1 = exec(func)


            y2 = 0 * x
            fig, ax = plt.subplots()
            fig.set_size_inches(4, 4)
            ax.set_title(f'График функции y = {func}')
            # y = 0
            # Вывод графика
            ax.vlines(0, min(y1.min() - 20, -20), max(y1.max() + 20, 200), color='blue')
            ax.plot(x, y1, label=f'y = {func}')
            ax.plot(x, y2, label='оси x и y', color='blue')
            ax.grid(axis='both')
            ax.legend()  # показывать условные обозначения
            plt.show()
        except Exception as ex:

            messagebox.showinfo('Внимание!', f'{ex}!!!')

            getfunc.delete(0, END)


    # для вкладки графики
    text_inp = tk.Label(tab3, text="Задайте уравнение функции y = (x)...", fg='#ed7e15', font=('Times New Roman', 13))
    text_inp2 = tk.Label(tab3, text="'y =' через пробел", fg='#ed7e15', font=('Times New Roman', 13))
    text_inp.grid(row=0, column=1)
    text_inp2.grid(row=1, column=1)
    getfunc = Entry(tab3, justify=RIGHT, font=('Times New Roman', 15), fg='#ed7e15', width=15,
                    highlightbackground='#ed7e15', highlightthickness=1)
    getfunc.grid(row=2, column=1)

    btn_graph = Button(tab3, text="Построить!", command=draw)
    btn_graph.grid(column=1, row=3)

    qr_lable = tk.Label(tab3, text="пока мы можем строить не все ф-ции", fg='#ed7e15', font=('Times New Roman', 13))
    qr_lable2 = tk.Label(tab3, text="сканируйте или нажмите на qr код и постройте", fg='#ed7e15', font=('Times New Roman', 13))
    #qr code
    def callback(url):
        webbrowser.open_new(url)

    qr_lable.grid(column = 1, row = 4)
    qr_lable2.grid(column=1, row = 5)

    qr_data = "https://www.mathway.com/ru/Algebra"
    qr_img = qrcode.make(qr_data)
    smaller_image = qr_img.resize((150, 150))
    qr_img = smaller_image
    qr_photo = ImageTk.PhotoImage(qr_img)

    qr_panel = Label(tab3, image = qr_photo, width=160, height=160)
    qr_panel.grid(column = 1, row = 6)
    qr_panel.bind("<Button-1>", lambda e: callback(qr_data))



    # запускаем главное окно
    root.mainloop()

if __name__ == '__main__':
    main()