from sqlalchemy import create_engine, text
def anti_sqlin(text):
    #так как у пользователея мало свободного ввода (только ввод того где точно не может быть сочетания '};' то с помощью replase я просто удалю все возможные попытки sql инъекции)
    text=text.replase('};','')
    return text
auth = {
    'user' : 'postgres',
    'password': '777'
}

engine = create_engine(
    'postgresql+psycopg2://{}:{}@localhost/teamq'.format(auth['user'], auth['password']),
    echo=True,
    isolation_level='SERIALIZABLE',
)
query_sel = "SELECT * FROM authors;"
with engine.connect() as connect:
    result = connect.execute(text(query_sel))
    connect.commit()
res=list(result)
print(res)
for x in result:
    print(x)
from tkinter import *
from tkinter import ttk
languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C", 
             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]

root = Tk()
root.title("ЧГК")
root.geometry("250x200") 

languages = ["Python", "C#", "Java", "JavaScript"]
# по умолчанию будет выбран первый элемент из languages
players = ["Максим Бобровицкий", "Кирилл Бобровицкий", "Игорь Соколов"]
authors = ["Максим Мерзляков", "Антон Саксонов"]
types = ["61 секунда", "неотбор"]
tables = ["1", "2"]
   
def click1():
    window = Toplevel()
    window.title("Управление таблицей")
    window.geometry("600x600")
    def add():
        len_t = 3 # колво столбцов в таблице
        entry_add1=ttk.Entry(window)
        entry_add2=ttk.Entry(window)
        entry_add3=ttk.Entry(window)
        if len_t==1:
            entry_add1.place(relx=0.1, rely=0.65)
        if len_t==2:
            entry_add1.place(relx=0.1, rely=0.65)
            entry_add2.place(relx=0.35, rely=0.65)
        if len_t==3:
            entry_add1.place(relx=0.1, rely=0.65)
            entry_add2.place(relx=0.35, rely=0.65)
            entry_add3.place(relx=0.6, rely=0.65)
            
    button_delete = ttk.Button(window,text="Удалить таблицу", command=delete)
    button_delete.place(relx=0.1, rely=0.1)
    button_clear= ttk.Button(window,text="Очистить всё", command=clear)
    button_clear.place(relx=0.1, rely=0.25)

    label_clearp = ttk.Label(window,text="Очистить таблицу ")
    label_clearp.place(relx=0.1, rely=0.40, height=25)
    tables_var1 = StringVar(window, value=tables[0])   
    label_clearp = ttk.Label(window,textvariable=tables_var1)
    label_clearp.place(relx=0.32, rely=0.4, height=25)
    combobox_clearp = ttk.Combobox(window, textvariable=tables_var1, values=tables)
    combobox_clearp.place(relx=0.32, rely=0.4, height=25)
    button_clearp = ttk.Button(window,text="Очистить", command=clearp)
    button_clearp.place(relx=0.6, rely=0.4, height=25)
    
    label_add = ttk.Label(window,text="Добавить в таблицу ")
    label_add.place(relx=0.1, rely=0.5, height=25)
    tables_var2 = StringVar(window, value=tables[0])   
    label_add = ttk.Label(window,textvariable=tables_var2)
    label_add.place(relx=0.32, rely=0.5, height=25)
    combobox_add = ttk.Combobox(window, textvariable=tables_var2, values=tables)
    combobox_add.place(relx=0.32, rely=0.5, height=25)
    button_add=ttk.Button(window, text="Добавить", command = add)
    button_add.place(relx=0.6, rely=0.5)




        


    button_search=ttk.Button(window, text="Найти", command = find)
    button_search.place(relx=0.4, rely=0.8)
    entry_search=ttk.Entry(window)
    entry_search.place(relx=0.1, rely=0.8)
    button_search_del=ttk.Button(window, text="Удалить найденное", command = find_del)
    button_search_del.place(relx=0.7, rely=0.8)
 
button1 = ttk.Button(text="Управление таблицей", command=click1)
button1.place(relx=.5, rely=.30, anchor="c")

def click2():
    window = Toplevel()
    window.title("Аналитика")
    window.geometry("600x600")
    label_player1 = ttk.Label(window,text="Статистика по игроку:")
    label_player1.place(relx=0.1, rely=0.2, height=25)
    players_var = StringVar(window, value=players[0])   
    label_player = ttk.Label(window,textvariable=players_var)
    label_player.place(relx=0.32, rely=0.2, height=25)
    combobox_player = ttk.Combobox(window, textvariable=players_var, values=players)
    combobox_player.place(relx=0.32, rely=0.2, height=25)
    button_player = ttk.Button(window,text="Показать", command=St_pl)
    button_player.place(relx=0.6, rely=0.2, height=25)

    label_team1 = ttk.Label(window,text="Статистика команды по: ")
    label_team1.place(relx=0.1, rely=0.5, height=25)
    types_var = StringVar(window, value=types[0])   
    label_type2 = ttk.Label(window,textvariable=types_var)
    label_type2.place(relx=0.34, rely=0.5)
    combobox_type2 = ttk.Combobox(window, textvariable=types_var, values=types)
    combobox_type2.place(relx=0.34, rely=0.5)
    button_team = ttk.Button(window,text="Показать", command=St_team)
    button_team.place(relx=0.6, rely=0.5, height=25)  

    label_player1 = ttk.Label(window,text="Статистика по автору: ")
    label_player1.place(relx=0.1, rely=0.8, height=25)  
    authors_var = StringVar(window, value=authors[0])   
    label_author = ttk.Label(window,textvariable=authors_var)
    label_author.place(relx=0.32, rely=0.8)
    combobox_author = ttk.Combobox(window, textvariable=authors_var, values=authors)
    combobox_author.place(relx=0.32, rely=0.8)
    button_team = ttk.Button(window,text="Показать", command=St_aut)
    button_team.place(relx=0.6, rely=0.8, height=25)  



def delete():
    pass
def clear():
    pass
def clearp():
    pass
def find():
    pass
def find_del():
    pass
def St_pl():
    window = Toplevel()
    window.title("Статистика по игроку")
    window.geometry("600x600")
    people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
    columns = ("name", "age", "email")
    tree = ttk.Treeview(window,columns=columns, show="headings")
    tree.place(relx=0, rely=0, relheight=0.3)
    t="Имя"
    tree.heading("name", text=t)
    tree.heading("age", text="Возраст")
    tree.heading("email", text="Email")
    for person in people:

        tree.insert("", END, values=person)
    
    tree1 = ttk.Treeview(window,columns=columns, show="headings")
    tree1.place(relx=0, rely=0.33, relheight=0.3)
    tree1.heading("name", text=t)
    tree1.heading("age", text="Возраст")
    tree1.heading("email", text="Email")
    for person in people:
        tree1.insert("", END, values=person)
    
    tree2 = ttk.Treeview(window,columns=columns, show="headings")
    tree2.place(relx=0, rely=0.66, relheight=0.3)
    tree2.heading("name", text=t)
    tree2.heading("age", text="Возраст")
    tree2.heading("email", text="Email")
    for person in people:
        tree2.insert("", END, values=person)

def St_team():
    window = Toplevel()
    window.title("Статистика по команде")
    window.geometry("600x600")
    people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
    columns = ("name", "age", "email")
    tree = ttk.Treeview(window,columns=columns, show="headings")
    tree.place(relx=0, rely=0, relheight=0.3)
    t="Имя"
    tree.heading("name", text=t)
    tree.heading("age", text="Возраст")
    tree.heading("email", text="Email")
    for person in people:
        
        tree.insert("", END, values=person)
    
    tree1 = ttk.Treeview(window,columns=columns, show="headings")
    tree1.place(relx=0, rely=0.33, relheight=0.3)
    tree1.heading("name", text=t)
    tree1.heading("age", text="Возраст")
    tree1.heading("email", text="Email")
    for person in people:
        tree1.insert("", END, values=person)
    
    tree2 = ttk.Treeview(window,columns=columns, show="headings")
    tree2.place(relx=0, rely=0.66, relheight=0.3)
    tree2.heading("name", text=t)
    tree2.heading("age", text="Возраст")
    tree2.heading("email", text="Email")
    for person in people:
        tree2.insert("", END, values=person)
   
def St_aut():
    window = Toplevel()
    window.title("Статистика по автору")
    window.geometry("600x600")
    people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
    columns = ("name", "age", "email")
    tree = ttk.Treeview(window,columns=columns, show="headings")
    tree.place(relx=0, rely=0, relheight=0.3)
    t="Имя"
    tree.heading("name", text=t)
    tree.heading("age", text="Возраст")
    tree.heading("email", text="Email")
    for person in people:
        
        tree.insert("", END, values=person)
    
    tree1 = ttk.Treeview(window,columns=columns, show="headings")
    tree1.place(relx=0, rely=0.33, relheight=0.3)
    tree1.heading("name", text=t)
    tree1.heading("age", text="Возраст")
    tree1.heading("email", text="Email")
    for person in people:
        tree1.insert("", END, values=person)
    
    tree2 = ttk.Treeview(window,columns=columns, show="headings")
    tree2.place(relx=0, rely=0.66, relheight=0.3)
    tree2.heading("name", text=t)
    tree2.heading("age", text="Возраст")
    tree2.heading("email", text="Email")
    for person in people:
        tree2.insert("", END, values=person)
    
button2 = ttk.Button(text="Аналитика", command=click2)
button2.place(relx=.5, rely=.60, anchor="c")
 
root.mainloop()
