import tkinter as tk
import mysql.connector
from tkinter import *
import re

font_header = ('Consolas', 15)
font_entry = ('Consolas', 12)
label_font = ('Consolas', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.add_img = tk.PhotoImage(file="add.gif")
        self.delete_img = tk.PhotoImage(file="delete.gif")
        self.refresh_img = tk.PhotoImage(file="refresh.gif")
        self.search_img = tk.PhotoImage(file="search.gif")
        self.update_img = tk.PhotoImage(file="update.gif")
        self.open_window()

    def show_tables(self, cursor):
        '''Вывод всех таблиц БД на экран'''
        self.kind_of_sport(cursor)
        self.gyms(cursor)
        self.name_rank(cursor)
        self.schedule(cursor)
        self.student(cursor)
        self.student_group(cursor)
        self.trainer(cursor)

    @staticmethod
    def kind_of_sport(cursor):
        w = tk.Toplevel()
        w.geometry("300x300")
        w.title("Виды спорта")
        cursor.execute("select * from Kind_of_sport")
        headers = [i[0] for i in cursor.description]
        for i in range(len(headers)):
            l = tk.Label(w, text=str(headers[i]))
            l.grid(row=0, column=i)
        data = (row for row in cursor.fetchall())
        print(data)
        for y, row in enumerate(data):
            for x, item in enumerate(row):
                l = tk.Label(w, text=str(item))
                l.grid(row=y + 1, column=x)
        w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
        w.grab_set()

    @staticmethod
    def gyms(cursor):
        w = tk.Toplevel()
        w.geometry("300x300")
        w.title("Спортивные залы")
        cursor.execute("select * from Gyms")
        headers = [i[0] for i in cursor.description]
        for i in range(len(headers)):
            l = tk.Label(w, text=str(headers[i]))
            l.grid(row=0, column=i)
        data = (row for row in cursor.fetchall())
        print(data)
        for y, row in enumerate(data):
            for x, item in enumerate(row):
                l = tk.Label(w, text=str(item))
                l.grid(row=y + 1, column=x)
        w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
        w.grab_set()

    @staticmethod
    def name_rank(cursor):
        w = tk.Toplevel()
        w.geometry("300x300")
        w.title("Разряды")
        cursor.execute("select * from Name_rank")
        headers = [i[0] for i in cursor.description]
        for i in range(len(headers)):
            l = tk.Label(w, text=str(headers[i]))
            l.grid(row=0, column=i)
        data = (row for row in cursor.fetchall())
        print(data)
        for y, row in enumerate(data):
            for x, item in enumerate(row):
                l = tk.Label(w, text=str(item))
                l.grid(row=y + 1, column=x)
        w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
        w.grab_set()

    def schedule(self, cursor):
        w = tk.Toplevel()
        w.geometry("300x300")
        w.title("Расписание")
        cursor.execute("select * from Schedule")
        headers = [i[0] for i in cursor.description]
        for i in range(len(headers)):
            self.l = tk.Label(w, text=str(headers[i]))
            self.l.grid(row=0, column=i)
        data = (row for row in cursor.fetchall())
        print(data)
        for y, row in enumerate(data):
            for x, item in enumerate(row):
                self.l = tk.Label(w, text=str(item))
                self.l.grid(row=y + 1, column=x)
        w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
        w.grab_set()

    def student(self, cursor):
        w = tk.Toplevel()
        w.geometry("300x300")
        w.title("Спортсмены")
        cursor.execute("select * from Student")
        headers = [i[0] for i in cursor.description]
        for i in range(len(headers)):
            self.l = tk.Label(w, text=str(headers[i]))
            self.l.grid(row=0, column=i)
        data = (row for row in cursor.fetchall())
        print(data)
        for y, row in enumerate(data):
            for x, item in enumerate(row):
                self.l = tk.Label(w, text=str(item))
                self.l.grid(row=y + 1, column=x)
        w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
        w.grab_set()

    def student_group(self, cursor):
        w = tk.Toplevel()
        w.geometry("300x300")
        w.title("Учебные Группы")
        cursor.execute("select * from Student_group")
        headers = [i[0] for i in cursor.description]
        for i in range(len(headers)):
            self.l = tk.Label(w, text=str(headers[i]))
            self.l.grid(row=0, column=i)
        data = (row for row in cursor.fetchall())
        print(data)
        for y, row in enumerate(data):
            for x, item in enumerate(row):
                self.l = tk.Label(w, text=str(item))
                self.l.grid(row=y + 1, column=x)
        w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
        w.grab_set()

    def trainer(self, cursor):
        w = tk.Toplevel()
        w.geometry("300x300")
        w.title("Тренеры")
        cursor.execute("select * from Trainer")
        headers = [i[0] for i in cursor.description]
        for i in range(len(headers)):
            self.l = tk.Label(w, text=str(headers[i]))
            self.l.grid(row=0, column=i)
        data = (row for row in cursor.fetchall())
        print(data)
        for y, row in enumerate(data):
            for x, item in enumerate(row):
                self.l = tk.Label(w, text=str(item))
                self.l.grid(row=y + 1, column=x)
        w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
        w.grab_set()

    def commands(self, mod_access, command=None):
        '''Возможные команды на странице БД'''
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="1",
                                     db="sport_school")
        cursor = db.cursor()
        if mod_access == 1:
            if command is None:
                self.show_tables(cursor)
            elif re.match("INSERT INTO", command) is not None or re.match("insert into", command) is not None:
                w = tk.Toplevel()
                w.geometry("300x300")
                w.title("Результат запроса")
                cursor.execute(command)
                self.messagebox.showinfo(title="Сообщение", message="Запись добавлена!")
                db.commit()
            elif re.match("CREATE TABLE", command) is not None or re.match("create table", command):
                w = tk.Toplevel()
                w.geometry("300x300")
                w.title("Результат запроса")
                cursor.execute(command)
                self.messagebox.showinfo(title="Сообщение", message="Запись добавлена!")
                db.commit()
            else:
                w = tk.Toplevel()
                w.geometry("300x300")
                w.title("Результат запроса")
                cursor.execute(command)
                data = (row for row in cursor.fetchall())
                print(data)
                for y, row in enumerate(data):
                    for x, item in enumerate(row):
                        l = tk.Label(w, text=str(item))
                        l.grid(row=y, column=x)
                w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
                w.grab_set()
        if mod_access == 0:
            if command is None:
                self.show_tables(cursor)
            elif re.match("INSERT INTO", command) is not None or re.match("insert into", command) is not None:
                self.messagebox.showwarning(title="ОШИБКА", message="Данную операцию выполнить невозможно!")
            elif re.match("CREATE TABLE", command) is not None or re.match("create table", command):
                self.messagebox.showwarning(title="ОШИБКА", message="Данную операцию выполнить невозможно!")
            else:
                w = tk.Toplevel()
                w['bg'] = '#F4F4ED'
                w.geometry("430x380")
                w.title("Результат запроса")
                cursor.execute(command)
                data = (row for row in cursor.fetchall())
                print(data)
                for y, row in enumerate(data):
                    for x, item in enumerate(row):
                        l = tk.Label(w, text=str(item))
                        l.grid(row=y, column=x)
                w.protocol("WM_DELETE_WINDOW", lambda: w.destroy())
                w.grab_set()

    def open_dialog(self):
        mod_access = 1
        bd = tk.Toplevel()
        bd['bg'] = '#F4F4ED'
        bd.geometry("800x200")
        bd.title("База Данных Спортивной школы")
        command_label_1 = Label(bd, text='Введите запрос', font=label_font, bg='#F4F4ED', **base_padding)
        command_label_1.place(x=0, y=10)
        # поле ввода команд
        command_entry_1 = Entry(bd, bg='#fff', fg='#444', font=font_entry, width=80)
        command_entry_1.place(x=10, y=50)
        send_btn_1 = Button(bd, text='Ввод', height=1, width=6, background='#457B9D',
                               command=lambda: self.commands(mod_access, command_entry_1.get()))
        send_btn_1.place(x=10, y=90)
        bd.protocol("WM_DELETE_WINDOW", lambda: bd.destroy())

    def bd_window_1(self):
        '''Окно БД для админов'''
        mod_access = 1
        data_base = tk.Toplevel()
        data_base['bg'] = '#F4F4ED'
        data_base.geometry("800x500")
        data_base.title("База Данных Спортивной школы")
        toolbar = tk.Frame(data_base, bg='#F4F4ED', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить таблицу', command=self.open_dialog,
                                    bg='#F4F4ED', bd=0, compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)
        btn_open_dialog = tk.Button(toolbar, text='Удалить таблицу', command=self.open_dialog,
                                    bg='#F4F4ED', bd=0, compound=tk.TOP, image=self.delete_img)
        btn_open_dialog.place(x=170, y=0)
        btn_open_dialog = tk.Button(toolbar, text='Обновить данные', command=self.open_dialog,
                                    bg='#F4F4ED', bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_open_dialog.place(x=330, y=0)
        btn_open_dialog = tk.Button(toolbar, text='Поиск данных', command=self.open_dialog,
                                    bg='#F4F4ED', bd=0, compound=tk.TOP, image=self.search_img)
        btn_open_dialog.place(x=500, y=0)
        btn_open_dialog = tk.Button(toolbar, text='Редактировать таблицу', command=self.open_dialog,
                                    bg='#F4F4ED', bd=0, compound=tk.TOP, image=self.update_img)
        btn_open_dialog.place(x=650, y=0)
        # метка для поля ввода имени
        tfp_label_1 = Label(data_base, text='Поле для создания триггеров, процедур и функций',
                               font=label_font, bg='#F4F4ED', **base_padding)
        tfp_label_1.place(x=230, y=110)
        # поле ввода триггеров, прцедур и функций
        tfp_entry_1 = Text(data_base, bg='#fff', fg='#444', font=font_entry)
        tfp_entry_1.place(x=160, y=150, width=500, height=120)
        # кнопка отправки формы
        send_tfp_btn_1 = Button(data_base, text='Ввод', background='#457B9D',
                                   command=lambda: self.commands(mod_access, tfp_entry_1.get("1.0", "end")))
        send_tfp_btn_1.place(x=380, y=290)
        # метка для поля ввода имени
        table_label_1 = Label(data_base, text='Вывод всех таблиц базы данных', bg='#F4F4ED',
                                 font=label_font, **base_padding)
        table_label_1.place(x=270, y=320)
        # кнопка отправки формы
        tables_btn_1 = Button(data_base, text='Ввод', background='#457B9D',
                                 command=lambda: self.commands(mod_access))
        tables_btn_1.place(x=380, y=360)
        data_base.protocol("WM_DELETE_WINDOW", lambda: data_base.destroy())

    def bd_window_2(self):
        '''Окно БД для обычных пользователей'''
        mod_access = 0
        bd = tk.Toplevel()
        bd['bg'] = '#F4F4ED'
        bd.geometry("800x200")
        bd.title("База Данных Спортивной школы")
        # метка для поля ввода имени
        command_label_1 = Label(bd, text='Введите запрос: ', font=label_font, bg='#F4F4ED', **base_padding)
        command_label_1.place(x=0, y=10)
        # поле ввода команд
        command_entry_1 = Entry(bd, bg='#fff', fg='#444', font=font_entry, width=80)
        command_entry_1.place(x=10, y=60, width=700)
        # кнопка отправки формы
        send_btn_1 = Button(bd, text='Ввод', background='#457B9D',
                               command=lambda: self.commands(mod_access, command_entry_1.get()))
        send_btn_1.place(x=735, y=56)
        bd.protocol("WM_DELETE_WINDOW", lambda: bd.destroy())

    # обработчик нажатия на клавишу 'Войти'
    def clicked(self, username, password):
        f1 = open("Пользователи.txt", 'r')
        lines_f1 = f1.readlines()
        for line in lines_f1:
            line = line.replace('\n', '').split(' ')
            if not line:
                break
            if line[0] == username and line[1] == password and line[2] == '0':
                self.bd_window_2()
            if line[0] == username and line[1] == password and line[2] == '1':
                self.bd_window_1()

    def register_clicked(self, username, password, access_level):
        f = open("C:\\Users\\Аня\\Desktop\\deep_python_autumn_2022-main\\GUI\\Пользователи.txt", 'a+')
        s = username + ' ' + password + ' ' + access_level + '\n'
        f.write(s)
        self.messagebox.showinfo(title="Сообщение", message="Вы зарегистрированы!")
        f.close()

    # регистрация
    def register_window(self):
        # главное окно приложения
        reg = Tk()
        reg['bg'] = '#F4F4ED'
        # заголовок окна
        reg.title('Регистрация')
        # размер окна
        reg.geometry('500x300')
        # можно ли изменять размер окна - нет
        reg.resizable(False, False)
        reg_label = Label(reg, text='Регистрация', font=font_header, justify=CENTER, **header_padding)
        # помещаем виджет в окно по принципу один виджет под другим
        reg_label.pack()
        # метка для поля ввода имени
        username_label = Label(reg, text='Имя пользователя', font=label_font, **base_padding)
        username_label.pack()
        # поле ввода имени
        username_reg = Entry(reg, bg='#fff', fg='#444', font=font_entry)
        username_reg.pack()
        # метка для поля ввода пароля
        password_label = Label(reg, text='Пароль', font=label_font, **base_padding)
        password_label.pack()
        # поле ввода пароля
        password_reg = Entry(reg, bg='#fff', fg='#444', font=font_entry)
        password_reg.pack()
        # метка для поля ввода уровня доступа
        level_label = Label(reg, text='Ваш уровень доступа', font=label_font, **base_padding)
        level_label.pack()
        # поле ввода пароля
        level_reg = Entry(reg, bg='#fff', fg='#444', font=font_entry)
        level_reg.pack()
        # кнопка отправки формы
        send_btn = Button(reg, text='Зарегистрироваться', background='#914D76',
                               command=lambda: self.register_clicked(username_reg.get(), password_reg.get(),
                                                                     level_reg.get()))
        send_btn.place(x=185, y=250)
        # выводим в диалоговое окно введенные пользователем данные

    # окно авторизации
    def log_in_window(self):
        # главное окно приложения
        window = Tk()
        window['bg'] = '#F4F4ED'
        # заголовок окна
        window.title('Авторизация пользователя')
        # размер окна
        window.geometry('500x230')
        # можно ли изменять размер окна - нет
        window.resizable(False, False)
        # заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
        # для всех остальных виджетов настройки делаются также
        main_label_1 = Label(window, text='Авторизация', font=font_header, bg='#F4F4ED',
                             justify=CENTER, **header_padding)
        # помещаем виджет в окно по принципу один виджет под другим
        main_label_1.pack()

        # метка для поля ввода имени
        username_label = Label(window, text='Имя пользователя', font=label_font, bg='#F4F4ED', **base_padding)
        username_label.pack()

        # поле ввода имени
        username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
        username_entry.pack()

        # метка для поля ввода пароля
        password_label = Label(window, text='Пароль', font=label_font, bg='#F4F4ED', **base_padding)
        password_label.pack()

        # поле ввода пароля
        password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
        password_entry.pack()

        # кнопка отправки формы
        send_btn = Button(window, text='Войти', background='#457B9D',
                               command=lambda: self.clicked(username_entry.get(), password_entry.get()))
        send_btn.place(x=220, y=190)
        # запускаем главный цикл окна
        window.mainloop()

    def open_window(self):
        window = Tk()
        window['bg'] = '#F4F4ED'
        window.title('Приветственное окно')
        # размер окна
        window.geometry('500x150')
        # можно ли изменять размер окна - нет
        window.resizable(False, False)
        main_label_1 = Label(window, text='Добро Пожаловать!', font=font_header, bg='#F4F4ED', justify=CENTER,
                                **header_padding)
        # помещаем виджет в окно по принципу один виджет под другим
        main_label_1.place(x=150, y=5)
        reg_btn = Button(window, text='Авторизоваться', background='#457B9D',
                              command=(lambda: self.log_in_window()))
        reg_btn.place(x=200, y=70)
        reg_btn = Button(window, text='Зарегистрироваться', background='#914D76',
                              command=lambda: self.register_window())
        reg_btn.place(x=185, y=110)
        # запускаем главный цикл окна
        window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root['bg'] = '#F4F4ED'
    root.title("БАЗА ДАННЫХ СПОРТИВНОЙ ШКОЛЫ")
    root.geometry('500x100')
    main_label = Label(root, text='БАЗА ДАННЫХ СПОРТИВНОЙ ШКОЛЫ', font=font_header,
                       bg='#F4F4ED', justify=CENTER, **header_padding)
    main_label.place(x=80, y=25)
    root.resizable(False, False)
    app = Main(root)
    app.mainloop()
    root.mainloop()
