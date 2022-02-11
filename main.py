from algorithms import *
from colors import *
import random
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox as mb

window = Tk()
window.title("Клиентская база онлайн сервиса")
window.geometry("500x300")
window.config(bg=WHITE)

tab_control = ttk.Notebook(window)
tab_menu = ttk.Frame(tab_control)
tab_res = ttk.Frame(tab_control)
tab_control.add(tab_menu, text='Меню')
tab_control.add(tab_res, text='База')

sub_name = StringVar()
sub_list = ['Стандартный', 'Золотой', 'Платиновый']

BasDan = data_base()
Users_text = Text(tab_res, height=14, width=60, padx=0, pady=5, wrap=WORD)
Users_text.place(x=0, y=35)
scroll = Scrollbar(command=Users_text.yview)
scroll.pack(side=RIGHT, fill=Y)
Users_text.config(yscrollcommand=scroll.set)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
for i in range(len(data)):
    BasDan.add_User(data[str(i)]["name"], data[str(i)]["age"], data[str(i)]["level"])

string = ""
for i, temp in enumerate(BasDan):
    string += f"Id:{i} {str(temp)}\n"
Users_text.delete("1.0", "end")
Users_text.insert(INSERT, string)

def Refresh():
    string = ""
    for i, temp in enumerate(BasDan):
        string += f"Id:{i} {str(temp)}\n"
    Users_text.delete("1.0", "end")
    Users_text.insert(INSERT, string)


def Generate():  # метод для заполнения базы случайными пользователями для тестов
    names = {1: "Анатолий", 2: "Евгений", 3: "Вера", 4: "Нина", 5: "Сергей"}  # список имен для генерации
    levels = {1: "Стандартный", 2: "Золотой", 3: "Платиновый"}  # список подписок для генерации
    for i in range(random.randint(30, 50)):  # выбор количества пользователей для генерации
        num_name = random.randint(1, 5)  # выбор имени из списка
        num_level = random.randint(1, 3)  # выбор уровня тоже из списка
        num_age = random.randint(10, 80)  # выбор возраста в диапазоне
        BasDan.add_User(names[num_name], num_age, levels[num_level])


refresh = Button(tab_res, text="Обновить", command=Refresh, bg=LIGHT_GRAY, width=12)
refresh.place(x=97, y=5)

generate = Button(tab_res, text="Сгенерировать", command=Generate, bg=LIGHT_GRAY, width=12)
generate.place(x=289, y=5)


def AddUser():
    def Add_User():
        name = str(txt_name.get())
        age = str(txt_age.get())
        level = str(combo.get())
        BasDan.add_User(name, age, level)

    temp_window = Toplevel()  # Создание нового окна
    temp_window.title("Add User Window")
    temp_window.geometry("425x80")
    temp_window.grab_set()

    name_label = Label(temp_window, text='Имя пользователя', width=20)  # Надписи над виджетами ввода
    name_label.grid(column=0, row=0, padx=5, pady=5)
    sub_label = Label(temp_window, text='Уровень подписки')
    sub_label.grid(column=1, row=0)
    age_label = Label(temp_window, text='Возраст')
    age_label.grid(column=2, row=0)

    txt_name = Entry(temp_window, width=20)  # Ввод имени пользователя
    txt_name.grid(column=0, row=1, padx=0, pady=5)

    combo = Combobox(temp_window)
    combo['values'] = sub_list  # Выбор уровня подписки
    combo.current(0)  # установите вариант по умолчанию
    combo.grid(column=1, row=1)

    txt_age = Entry(temp_window, width=4)  # Ввод возраста
    txt_age.grid(column=2, row=1)

    b1 = Button(temp_window, text="Добавить", command=Add_User, bg=LIGHT_GRAY)  # Кнопка добавления ползователей
    b1.grid(row=1, column=3)


def RemoveUser():
    def Remove_User():
        Id = str(txt_id.get())
        string = BasDan.remove_User(Id)
        if len(string) == 0:
            msg = "Нет пользователя с таким ID"
            mb.showerror("Ошибка", msg)

    temp_window = Toplevel()  #
    temp_window.title("Remove User Window")  # Создание нового окна
    temp_window.geometry("195x80")  #
    temp_window.grab_set()  #

    id_label = Label(temp_window, text='ID пользователя', width=15)  # Надпись над виджетами ввода
    id_label.grid(column=0, row=0, padx=5, pady=5)  #

    txt_id = Entry(temp_window, width=6)  # Ввод id пользователя
    txt_id.grid(column=0, row=1, padx=0, pady=5)  #

    b1 = Button(temp_window, text="Удалить", command=Remove_User, bg=RED)  # Кнопка удаления ползователей
    b1.grid(row=1, column=3)  #


def Safe():
    BasDan.safe()
    mb.showinfo("Информация", "Сохрание успешно")


def CheckUser():
    def Check_User():
        Id = str(txt_id.get())
        string = BasDan.check_user(Id)
        if len(string) == 0:
            msg = "Нет пользователя с таким ID"
            mb.showerror("Ошибка", msg)
        else:
            mb.showinfo("Информация", string)

    temp_window = Toplevel()  #
    temp_window.title("Интерфейс получения информации о пользователе")  # Создание нового окна
    temp_window.geometry("210x80")  #
    temp_window.grab_set()  #

    id_label = Label(temp_window, text='ID пользователя', width=15)  # Надпись над виджетами ввода
    id_label.grid(column=0, row=0, padx=5, pady=5)  #

    txt_id = Entry(temp_window, width=6)  # Ввод id пользователя
    txt_id.grid(column=0, row=1, padx=0, pady=5)  #

    b1 = Button(temp_window, text="Получить", command=Check_User, bg=LIGHT_GRAY)  # Кнопка добавления ползователей
    b1.grid(row=1, column=3)


def UsersCurrentLevel():
    def Users_Current_Level():
        level = str(combo.get())
        string = BasDan.users_current_level(level)
        if len(string) == 0:
            msg = "Нет пользователей с таким уровнем подписки"
            mb.showerror("Ошибка", msg)
        else:
            Users_text.delete("1.0", "end")
            Users_text.insert(INSERT, string)
            msg = 'Список сформировн, проверьте вкладку "База"'
            mb.showinfo("Информация", msg)

    temp_window = Toplevel()  #
    temp_window.title("Интерфейс вывода пользователей определенного уровня подписки")  # Создание нового окна
    temp_window.geometry("240x80")  #
    temp_window.grab_set()  #

    sub_label = Label(temp_window, text='Уровень подписки')  # Надписи над виджетами ввода
    sub_label.grid(column=0, row=0)  #

    combo = Combobox(temp_window)  #
    combo['values'] = sub_list  # Выбор уровня подписки
    combo.current(0)  # установите вариант по умолчанию                                       #
    combo.grid(column=0, row=1)  #

    b1 = Button(temp_window, text="Отсеять", command=Users_Current_Level,
                bg=LIGHT_GRAY)  # Кнопка добавления ползователей
    b1.grid(row=1, column=3)  #


def Sorti():
    def age_sort_vos():
        BasDan.age_sort_vos()
        string = ""
        for i, temp in enumerate(BasDan):
            string += f"Id:{i} {str(temp)}\n"
        Users_text.delete("1.0", "end")
        Users_text.insert(INSERT, string)
        msg = 'Список сформировн, проверьте вкладку "База"'
        mb.showinfo("Информация", msg)

    def age_sort_ub():
        BasDan.age_sort_ub()
        string = ""
        for i, temp in enumerate(BasDan):
            string += f"Id:{i} {str(temp)}\n"
        Users_text.delete("1.0", "end")
        Users_text.insert(INSERT, string)
        msg = 'Список сформировн, проверьте вкладку "База"'
        mb.showinfo("Информация", msg)

    temp_window = Toplevel()  #
    temp_window.title("Интерфейс сортировки")  # Создание нового окна
    temp_window.geometry("220x80")  #
    temp_window.grab_set()  #

    b1 = Button(temp_window, text="По возрастаню", command=age_sort_vos, bg=LIGHT_GRAY,
                width=12)  # Кнопка добавления ползователей
    b1.grid(row=0, column=0, padx=10, pady=20)  #
    b2 = Button(temp_window, text="По убыванию", command=age_sort_ub, bg=LIGHT_GRAY,
                width=12)  # Кнопка добавления ползователей
    b2.grid(row=0, column=1)  #


def AdultList():
    string = BasDan.adult_list()
    Users_text.delete("1.0", "end")
    Users_text.insert(INSERT, string)
    msg = 'Список сформировн, проверьте вкладку "База"'
    mb.showinfo("Информация", msg)


def CheckAge():
    def Check_Age():
        Id = str(txt_id.get())
        string = BasDan.check_age(Id)
        if len(string) == 0:
            msg = "Нет пользователя с таким ID"
            mb.showerror("Ошибка", msg)
        elif string == "True":
            mb.showinfo("Информация", "Пользователь совершеннолетний")
        else:
            mb.showinfo("Информация", "Пользователь не совершеннолетний")

    temp_window = Toplevel()  #
    temp_window.title("Интерфейс вывода пользователей определенного уровня подписки")  # Создание нового окна
    temp_window.geometry("210x80")  #
    temp_window.grab_set()  #

    id_label = Label(temp_window, text='ID пользователя', width=15)  # Надпись над виджетами ввода
    id_label.grid(column=0, row=0, padx=5, pady=5)  #

    txt_id = Entry(temp_window, width=6)  # Ввод id пользователя
    txt_id.grid(column=0, row=1, padx=0, pady=5)  #

    b1 = Button(temp_window, text="Проверить", command=Check_Age, bg=LIGHT_GRAY)  # Кнопка добавления ползователей
    b1.grid(row=1, column=3)


my_tag = Label(tab_menu, text='made by KeyKa. v1.0', font='Times 10', fg=LIGHT_GRAY)
my_tag.place(x=360, y=255)

canvas = Canvas(tab_menu, height=100, width=461)
img = PhotoImage(file='img1.png')
image = canvas.create_image(0, 0, anchor='nw', image=img)
canvas.pack(padx=7, pady=5)

b1 = Button(tab_menu, text="Добавить", bg=LIGHT_GRAY, width=22, command=AddUser)
b1.place(x=50, y=120)

b2 = Button(tab_menu, text="Удалить", command=RemoveUser, bg=LIGHT_GRAY, width=22)
b2.place(x=50, y=157)

b3 = Button(tab_menu, text="Сортировка по возрасту", command=Sorti, bg=LIGHT_GRAY, width=22)
b3.place(x=50, y=194)

b4 = Button(tab_menu, text="Информация о пльзователе", command=CheckUser, bg=LIGHT_GRAY, width=22)
b4.place(x=50, y=231)

b5 = Button(tab_menu, text="Сохранить", command=Safe, bg=LIGHT_GRAY, width=22)
b5.place(x=265, y=120)

b6 = Button(tab_menu, text="Пользователи подписки", command=UsersCurrentLevel, bg=LIGHT_GRAY, width=22)
b6.place(x=265, y=157)

b7 = Button(tab_menu, text="Список взрослых", command=AdultList, bg=LIGHT_GRAY, width=22)
b7.place(x=265, y=194)

b8 = Button(tab_menu, text="Проверка совершеннолетия", command=CheckAge, bg=LIGHT_GRAY, width=22)
b8.place(x=265, y=231)

tab_control.pack(expand=1, fill='both')

window.mainloop()
