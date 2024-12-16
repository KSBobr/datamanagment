from sqlalchemy import create_engine, text
from tkinter import *
from tkinter import ttk
from functools import reduce

def anti_sqlin(text):
    #так как у пользователея мало свободного ввода (только ввод того где точно не может быть сочетания '};' то с помощью replace я просто удалю все возможные попытки sql инъекции)
    text=text.replace('};','')
    text=text.replace(';','')
    return text
auth = {
    'user' : 'tquser',
    'password': '777'
}

engine = create_engine(
    'postgresql+psycopg2://{}:{}@localhost/teamq'.format(auth['user'], auth['password']),
    echo=False,
    isolation_level='SERIALIZABLE',
)
str1,str2,str3,str4,str5,str6='','','','','',''
DP, DA = {},{}
players = []
authors = []
reasons =[]
types=[]
topics=[]
tournaments=[]
Realtables=[]
query_RT=text("select * from show_tables()")
with engine.connect() as connect:
    Rtable=connect.execute(query_RT)
    connect.commit
for x in Rtable: Realtables.append(x[0])
param = ['1','2']
def update_ainfo():
    global DA,DP,authors,players
    DA,DP={},{}
    authors, players=[],[]
    pi = "SELECT * FROM player_info()"
    ai="SELECT * FROM author_info()"
    with engine.connect() as connect:
        Rpi= connect.execute(text(pi))
        Ra=connect.execute(text(ai))
        connect.commit()
    for x in Rpi:
        DP[x[0]]=x[1]
        players.append(x[1])
    for x in Ra:
        DA[x[0]]=x[1]
        authors.append(x[1])
def update_info():
    global reasons, types, topics, tournaments
    reasons, types, topics, tournaments=[],[],[],[]
    tyi = "SELECT * FROM type_info()"
    ri="SELECT * FROM reason_info()"
    ti="SELECT * FROM tur_info()"
    topi="SELECT * FROM topic_info()"
    with engine.connect() as connect:
        Rtyi= connect.execute(text(tyi))
        Rri=connect.execute(text(ri))
        Rti=connect.execute(text(ti))
        Rtopi=connect.execute(text(topi))
        connect.commit()
    for x in Rtyi:
        types.append(x[1])
    for x in Rri:
        reasons.append(x[1])
    for x in Rti:
        tournaments.append(x[0])
    for x in Rtopi:
        topics.append(x[1])
    update_ainfo()      
update_info()        
str1 
root = Tk()
root.title("ЧГК")
root.geometry("250x200") 
tables = ["Вопросы","Тема вопроса", "Тип вопроса", "Причина невзятия", "Турнир", "Игроки","Авторы"]
destr=[]
def click1():
    window = Toplevel()
    window.title("Управление таблицей")
    window.geometry("1300x1000")
    def selec(event):
        global destr
        for el in destr:
            el.destroy()
        destr.clear()
        selection_add =  combobox_add.get()
        if selection_add == "Тема вопроса":
            l_themeq=ttk.Label(window,text="Тема вопроса")
            l_themeq.place(relx=0.1, rely=0.46, relheight=0.05)
            entry_themeq = ttk.Entry(window)
            entry_themeq.place(relx=0.1, rely=0.5)
            def addtop():
                q="SELECT instop('{}')".format( entry_themeq.get())
                q=anti_sqlin(q)
                with engine.connect() as connect:
                    connect.execute(text(q))
                    connect.commit()
            button_add1=ttk.Button(window, text="Добавить", command = addtop)
            button_add1.place(relx=0.6, rely=0.4)
            destr.append(l_themeq)
            destr.append(entry_themeq)
            destr.append(button_add1)
        elif selection_add == "Тип вопроса":
            l_typeq=ttk.Label(window,text="Тип вопроса")
            l_typeq.place(relx=0.1, rely=0.46, relheight=0.05)
            entry_typeq = ttk.Entry(window)
            entry_typeq.place(relx=0.1, rely=0.5)
            destr.append(l_typeq)
            destr.append(entry_typeq)
            def addty():
                q="SELECT insty('{}')".format( entry_typeq.get())
                q=anti_sqlin(q)
                with engine.connect() as connect:
                    connect.execute(text(q))
                    connect.commit()
            button_add2=ttk.Button(window, text="Добавить", command = addty)
            button_add2.place(relx=0.6, rely=0.4)
            destr.append(button_add2)
        elif selection_add == "Причина невзятия":
            l_reas=ttk.Label(window,text="Причина невзятия")
            l_reas.place(relx=0.1, rely=0.46, relheight=0.05)
            entry_reas = ttk.Entry(window)
            entry_reas.place(relx=0.1, rely=0.5)
            destr.append(l_reas)
            destr.append(entry_reas)
            def addr():
                q="SELECT insr('{}')".format( entry_reas.get())
                q=anti_sqlin(q)
                with engine.connect() as connect:
                    connect.execute(text(q))
                    connect.commit()
            button_add3=ttk.Button(window, text="Добавить", command = addr)
            button_add3.place(relx=0.6, rely=0.4)
            destr.append(button_add3)
            
        elif selection_add == "Турнир":
            l_tourn=ttk.Label(window,text="Турнир")
            l_tourn.place(relx=0.4, rely=0.46, relheight=0.05)
            entry_tourn = ttk.Entry(window)
            entry_tourn.place(relx=0.4, rely=0.5)
            destr.append(l_tourn)
            destr.append(entry_tourn)
            def addt():
                q="SELECT inst('{}')".format(entry_tourn.get())
                q=anti_sqlin(q)
                with engine.connect() as connect:
                    connect.execute(text(q))
                    connect.commit()
            button_add4=ttk.Button(window, text="Добавить", command = addt)
            button_add4.place(relx=0.6, rely=0.4)
            destr.append(button_add4)
        elif selection_add == "Игроки":
            l_PID=ttk.Label(window,text="ID")
            l_PID.place(relx=0.1, rely=0.46, relheight=0.05)
            entry_PID = ttk.Entry(window)
            entry_PID.place(relx=0.1, rely=0.5)
            l_nameP=ttk.Label(window,text="Имя")
            l_nameP.place(relx=0.4, rely=0.46, relheight=0.05)
            entry_nameP = ttk.Entry(window)
            entry_nameP.place(relx=0.4, rely=0.5)
            l_surnameP=ttk.Label(window,text="Фамилия")
            l_surnameP.place(relx=0.7, rely=0.46, relheight=0.05)
            entry_surnameP = ttk.Entry(window)
            entry_surnameP.place(relx=0.7, rely=0.6)
            destr.append(l_PID)
            destr.append(entry_PID)
            destr.append(l_nameP)
            destr.append(entry_nameP)
            destr.append(l_surnameP)
            destr.append(entry_surnameP)
            def addp():
                q="SELECT insp({},'{}','{}')".format(entry_PID.get(),entry_nameP.get(),entry_surnameP.get())
                q=anti_sqlin(q)
                with engine.connect() as connect:
                    connect.execute(text(q))
                    connect.commit()
            button_add5=ttk.Button(window, text="Добавить", command = addp)
            button_add5.place(relx=0.6, rely=0.5)
            destr.append(button_add5)
        elif selection_add == "Авторы":
            l_AID=ttk.Label(window,text="ID")
            l_AID.place(relx=0.1, rely=0.56, relheight=0.05)
            entry_AID = ttk.Entry(window)
            entry_AID.place(relx=0.1, rely=0.6)
            l_nameA=ttk.Label(window,text="Имя")
            l_nameA.place(relx=0.4, rely=0.56, relheight=0.05)
            entry_nameA = ttk.Entry(window)
            entry_nameA.place(relx=0.4, rely=0.6)
            l_surnameA=ttk.Label(window,text="Фамилия")
            l_surnameA.place(relx=0.7, rely=0.56, relheight=0.05)
            entry_surnameA = ttk.Entry(window)
            entry_surnameA.place(relx=0.7, rely=0.6)
            destr.append(l_AID)
            destr.append(entry_AID)
            destr.append(l_nameA)
            destr.append(entry_nameA)
            destr.append(l_surnameA)
            destr.append(entry_surnameA)
            def adda():
                q="SELECT insa({},'{}','{}');".format(entry_AID.get(),entry_nameA.get(),entry_surnameA.get())
                q=anti_sqlin(q)
                with engine.connect() as connect:
                    connect.execute(text(q))
                    connect.commit()
            button_add6=ttk.Button(window, text="Добавить", command = adda)
            button_add6.place(relx=0.6, rely=0.5)
            destr.append(button_add6)
            
        elif selection_add == "Вопросы":
            update_info()     
            l_text=ttk.Label(window,text="Текст вопроса")
            l_text.place(relx=0.05, rely=0.41, relheight=0.05)
            entry_text = ttk.Entry(window,)
            entry_text.place(relx=0.05, rely=0.45, relwidth=0.6)
            l_ans=ttk.Label(window,text="Ответ")
            l_ans.place(relx=0.67, rely=0.41, relheight=0.05)
            entry_ans = ttk.Entry(window)
            entry_ans.place(relx=0.67, rely=0.45)
            l_num=ttk.Label(window,text="Номер")
            l_num.place(relx=0.9, rely=0.41, relheight=0.05)
            entry_num = ttk.Entry(window)
            entry_num.place(relx=0.9, rely=0.45, relwidth=0.08)

            l_aut=ttk.Label(window,text="Автор")
            l_aut.place(relx=0.05, rely=0.51, relheight=0.05)
            authors_var = StringVar(window)   
            label_authors = ttk.Label(window,textvariable=authors_var)
            label_authors.place(relx=0.05, rely=0.55, height=25)
            combobox_authors = ttk.Combobox(window, textvariable=authors_var, values=authors)
            combobox_authors.place(relx=0.05, rely=0.55, height=25)
            def s1(event):
                global str1
                str1=combobox_authors.get()
            combobox_authors.bind("<<ComboboxSelected>>", s1)

            l_pl=ttk.Label(window,text="Кто взял?")
            l_pl.place(relx=0.25, rely=0.51, relheight=0.05)
            players_var = StringVar(window)   
            label_player = ttk.Label(window,textvariable=players_var)
            label_player.place(relx=0.25, rely=0.55, height=25)
            combobox_player = ttk.Combobox(window, textvariable=players_var, values=players)
            combobox_player.place(relx=0.25, rely=0.55, height=25)
            def s5(event):
                global str5
                str5=combobox_player.get()
            combobox_player.bind("<<ComboboxSelected>>", s5)

            l_r=ttk.Label(window,text="Причина невзятия")
            l_r.place(relx=0.4, rely=0.51, relheight=0.05)
            reasons_var = StringVar(window)   
            label_r = ttk.Label(window,textvariable=reasons_var)
            label_r.place(relx=0.4, rely=0.55, height=25)
            combobox_r = ttk.Combobox(window, textvariable=reasons_var, values=reasons)
            combobox_r.place(relx=0.4, rely=0.55, height=25)
            def s6(event):
                global str6
                str6=combobox_r.get()
            combobox_r.bind("<<ComboboxSelected>>", s6)

            l_type=ttk.Label(window,text="Тип вопроса")
            l_type.place(relx=0.52, rely=0.51, relheight=0.05)
            type_var = StringVar(window)   
            label_ty = ttk.Label(window,textvariable=type_var)
            label_ty.place(relx=0.52, rely=0.55, height=25)
            combobox_ty = ttk.Combobox(window, textvariable=type_var, values=types)
            combobox_ty.place(relx=0.52, rely=0.55, height=25)
            def s3(event):
                global str3
                str3=combobox_ty.get()
            combobox_ty.bind("<<ComboboxSelected>>", s3)

            l_top=ttk.Label(window,text="Тема вопроса")
            l_top.place(relx=0.64, rely=0.51, relheight=0.05)
            top_var = StringVar(window)   
            label_top = ttk.Label(window,textvariable=top_var)
            label_top.place(relx=0.64, rely=0.55, height=25)
            combobox_top = ttk.Combobox(window, textvariable=top_var, values=topics)
            combobox_top.place(relx=0.64, rely=0.55, height=25)
            def s2(event):
                global str2
                str2=combobox_top.get()
            combobox_top.bind("<<ComboboxSelected>>", s2)

            l_tur=ttk.Label(window,text="Турнир")
            l_tur.place(relx=0.77, rely=0.51, relheight=0.05)
            tur_var = StringVar(window)   
            label_tur = ttk.Label(window,textvariable=top_var)
            label_tur.place(relx=0.77, rely=0.55, height=25)
            combobox_tur = ttk.Combobox(window, textvariable=tur_var, values=tournaments)
            combobox_tur.place(relx=0.77, rely=0.55, height=25)
            def s4(event):
                global str4
                str4=combobox_tur.get()
            combobox_top.bind("<<ComboboxSelected>>", s2)

            vz = BooleanVar()
            vz_checkbutton = ttk.Checkbutton(window, text="Взяли?", variable=vz)
            vz_checkbutton.place(relx=0.9, rely=0.52)

            raz = BooleanVar()
            raz_checkbutton = ttk.Checkbutton(window, text="Раздатка?", variable=raz)
            raz_checkbutton.place(relx=0.9, rely=0.55)

            l_nuans=ttk.Label(window,text="Нюанс")
            l_nuans.place(relx=0.75, rely=0.45, relheight=0.05)
            entry_nuans = ttk.Entry(window)
            entry_nuans.place(relx=0.75, rely=0.5, relwidth=0.15)
            destr.append(l_text)
            destr.append(entry_text)
            destr.append(l_ans)
            destr.append(entry_ans)
            destr.append(l_num)
            destr.append(entry_num)
            destr.append(l_aut)
            destr.append(label_authors)
            destr.append(combobox_authors)
            destr.append(l_pl)
            destr.append(label_player)
            destr.append(combobox_player)
            destr.append(l_r)
            destr.append(label_r)
            destr.append(combobox_r)
            destr.append(l_nuans)
            destr.append(vz_checkbutton)
            destr.append(raz_checkbutton)
            destr.append(entry_nuans)
            destr.append(l_type)
            destr.append(l_top)
            destr.append(l_tur)
            destr.append(label_ty)
            destr.append(label_top)
            destr.append(label_tur)
            destr.append(combobox_ty)
            destr.append(combobox_top)
            destr.append(combobox_tur)
            def add():
                q="SELECT insq('{}','{}',{},'{}','{}','{}','{}','{}','{}',{},{},'{}')".format(entry_text.get(),entry_ans.get(),entry_num.get(),str1,str2,str3,str4,str5,str6,vz.get(),raz.get(),entry_nuans.get())
                q=anti_sqlin(q)
                with engine.connect() as connect:
                    connect.execute(text(q))
                    connect.commit()
                print(entry_text.get(),entry_ans.get(),entry_num.get(),str1,str2,str3,str4,str5,str6,vz.get(),raz.get(),entry_nuans.get())
            button_add=ttk.Button(window, text="Добавить", command = add)
            button_add.place(relx=0.6, rely=0.4)
            destr.append(button_add)

            

            
    button_delete = ttk.Button(window,text="Удалить базу данных", command=delete)
    button_delete.place(relx=0.1, rely=0.05)
    button_clear= ttk.Button(window,text="Очистить всё", command=clear_all)
    button_clear.place(relx=0.1, rely=0.15)

    label_clearp = ttk.Label(window,text="Очистить таблицу ")
    label_clearp.place(relx=0.1, rely=0.3, height=25)
    tables_var1 = StringVar(window, value=tables[0])   
    label_clearp = ttk.Label(window,textvariable=tables_var1)
    label_clearp.place(relx=0.32, rely=0.3, height=25)
    combobox_clearp = ttk.Combobox(window, textvariable=tables_var1, values=Realtables)
    combobox_clearp.place(relx=0.32, rely=0.3, height=25)
    def selclear(event):
        var=combobox_clearp.get()
        button_clearp = ttk.Button(window,text="Очистить", command=clear(var))
        button_clearp.place(relx=0.6, rely=0.3, height=25)
    combobox_clearp.bind("<<ComboboxSelected>>",selclear)
    
    
    label_add = ttk.Label(window,text="Добавить в таблицу ")
    label_add.place(relx=0.1, rely=0.4, height=25)
    tables_var2 = StringVar(window, value=tables[0])   
    label_add = ttk.Label(window,textvariable=tables_var2)
    label_add.place(relx=0.32, rely=0.4, height=25)
    combobox_add = ttk.Combobox(window, textvariable=tables_var2, values=tables)
    combobox_add.place(relx=0.32, rely=0.4, height=25)
    combobox_add.bind("<<ComboboxSelected>>", selec)
    




    def find(target):
        query=text("SELECT * from sq('{}')".format(target))
        with engine.connect() as connect:
            Mega=connect.execute(query)
            connect.commit()
        col=("id","text","ans")
        tree = ttk.Treeview(window,columns=col, show="headings")
        tree.place(relx=0.1, rely=0.65, relheight=0.2)
        tree.heading("id", text="ID")
        tree.heading("text", text="Вопрос")
        tree.heading("ans", text="Ответ")
        for cor in Mega:
            print(cor[0],cor[1],cor[2])
            tree.insert("", END, values=(cor[0],cor[1],cor[2]))
    def find_del(target):
        query1=text("SELECT * from dsq('{}')".format(target))
        with engine.connect() as connect:
            connect.execute(query1)
            connect.commit()
        print("dewde")
    def search_button_clicked():
        target = anti_sqlin(entry_search.get())
        find(target)
    def search_button_del():
        target = anti_sqlin(entry_search.get())
        find_del(target)
    entry_search=ttk.Entry(window)
    entry_search.place(relx=0.1, rely=0.6)
    button_search1=ttk.Button(window, text="Найти", command = search_button_clicked)
    button_search1.place(relx=0.4, rely=0.6)
    button_search_del=ttk.Button(window, text="Удалить найденное", command = search_button_del)
    button_search_del.place(relx=0.7, rely=0.6)
 
button1 = ttk.Button(text="Управление таблицей", command=click1)
button1.place(relx=.5, rely=.30, anchor="c")

def click2():
    update_ainfo()      
    def St_pl(key):
        ptop = "SELECT * FROM anptop({})".format(key)
        ptype = "SELECT * FROM anptype({})".format(key)
        pauthor="SELECT * FROM anauthor({})".format(key)
        with engine.connect() as connect:
            pauthors= connect.execute(text(pauthor))
            ptops=connect.execute(text(ptop))
            ptypes=connect.execute(text(ptype))
            connect.commit()
        window = Toplevel()
        window.title("Статистика по игроку")
        window.geometry("600x600")
        columns = ("name", "parametr")
        tree = ttk.Treeview(window,columns=columns, show="headings")
        tree.place(relx=0, rely=0, relheight=0.3)
        tree.heading("name", text="Автор")
        tree.heading("parametr", text="Взятия")
        for person in pauthors:
            tree.insert("", END, values=(person[0],person[1]))
        
        tree1 = ttk.Treeview(window,columns=columns, show="headings")
        tree1.place(relx=0, rely=0.33, relheight=0.3)
        tree1.heading("name", text="Тема")
        tree1.heading("parametr", text="процент")
        for t in ptops:
            tree1.insert("", END, values=(t[0],t[1]))
        
        tree2 = ttk.Treeview(window,columns=columns, show="headings")
        tree2.place(relx=0, rely=0.66, relheight=0.3)
        tree2.heading("name", text="Тип")
        tree2.heading("parametr", text="процент")
        for t in ptypes:
            tree2.insert("", END, values=(t[0],t[1]))
    window = Toplevel()
    window.title("Аналитика")
    window.geometry("600x600")
    label_player1 = ttk.Label(window,text="Статистика по игроку:")
    label_player1.place(relx=0.1, rely=0.2, height=25)
    players_var = StringVar(window)
    combobox_player = ttk.Combobox(window, textvariable=players_var, values=players)
    combobox_player.place(relx=0.32, rely=0.2, height=25)
    def selected(event):
        val=combobox_player.get()
        St_pl(reduce(lambda k, v: k if DP[k] == val else v, DP))
    combobox_player.bind("<<ComboboxSelected>>", selected)   
    label_player = ttk.Label(window,textvariable=players_var)
    label_player.place(relx=0.32, rely=0.2, height=25)
    
    
    

    
    label_team1 = ttk.Label(window,text="Статистика команды по: ")
    label_team1.place(relx=0.1, rely=0.5, height=25)
    param_var = StringVar(window, value=param[0])   
    label_type2 = ttk.Label(window,textvariable=param_var)
    label_type2.place(relx=0.34, rely=0.5)
    button_team = ttk.Button(window,text="Показать", command=St_team)
    button_team.place(relx=0.6, rely=0.5, height=25)  


    label_player1 = ttk.Label(window,text="Статистика по автору: ")
    label_player1.place(relx=0.1, rely=0.8, height=25)  
    authors_var = StringVar(window, value=authors[0])   
    label_author = ttk.Label(window,textvariable=authors_var)
    label_author.place(relx=0.32, rely=0.8)
    combobox_author = ttk.Combobox(window, textvariable=authors_var, values=authors)
    combobox_author.place(relx=0.32, rely=0.8) 
    def s(event):
        val=combobox_author.get()
        St_aut(reduce(lambda k, v: k if DA[k] == val else v, DA))
    combobox_author.bind("<<ComboboxSelected>>", s)  



def delete():
    pass
def clear_all():
    query="SELECT clear_all_tables()"
    with engine.connect() as connect:
        connect.execute(query)
        connect.commit()

def clear(var):
    queryc=text("SELECT clear_table('{}');".format(var))
    with engine.connect() as connect:
        connect.execute(queryc)
        connect.commit()


def St_team():
    ttop = "SELECT * FROM alltop()"
    ttype = "SELECT * FROM alltype()"
    tauthor="SELECT * FROM alla()"
    with engine.connect() as connect:
        tauthors= connect.execute(text(tauthor))
        ttops=connect.execute(text(ttop))
        ttypes=connect.execute(text(ttype))
        connect.commit()
    window = Toplevel()
    window.title("Статистика по команде")
    window.geometry("800x800")
    columns = ("name", "total", "taken", "percentage")
    tree = ttk.Treeview(window,columns=columns, show="headings")
    tree.place(relx=0, rely=0, relheight=0.3)
    tree.heading("name", text="Автор")
    tree.heading("total", text="всего")
    tree.heading("taken", text="взято")
    tree.heading("percentage", text="процент")
    for t in tauthors:
        tree.insert("", END, values=(t[0],t[1],t[2],t[3]))
    col=("name","parametr")
    tree1 = ttk.Treeview(window,columns=col, show="headings")
    tree1.place(relx=0, rely=0.33, relheight=0.3)
    tree1.heading("name", text="Тема")
    tree1.heading("parametr", text="доля в невзятых")
    for t in ttops:
        tree1.insert("", END, values=(t[0],t[1]))
    
    tree2 = ttk.Treeview(window,columns=col, show="headings")
    tree2.place(relx=0, rely=0.66, relheight=0.3)
    tree2.heading("name", text="Тип")
    tree2.heading("parametr", text="доля в невзятых")
    for t in ttypes:
        tree2.insert("", END, values=(t[0],t[1]))
   
def St_aut(key):
    atop = "SELECT * FROM anatop({})".format(key)
    atype = "SELECT * FROM anatype({})".format(key)
    aplayer="SELECT * FROM anap({})".format(key)
    with engine.connect() as connect:
        aplayers= connect.execute(text(aplayer))
        atops=connect.execute(text(atop))
        atypes=connect.execute(text(atype))
        connect.commit()
    window = Toplevel()
    window.title("Статистика по автору")
    window.geometry("600x600")
    columns = ("name", "parametr")
    tree = ttk.Treeview(window,columns=columns, show="headings")
    tree.place(relx=0, rely=0, relheight=0.3)
    tree.heading("name", text="Игрок")
    tree.heading("parametr", text="Взятых")
    for t in aplayers:
        
        tree.insert("", END, values=(t[0],t[1]))
    
    tree1 = ttk.Treeview(window,columns=columns, show="headings")
    tree1.place(relx=0, rely=0.33, relheight=0.3)
    tree1.heading("name", text="Тема")
    tree1.heading("parametr", text="процент")

    for t in atops:
        tree1.insert("", END, values=(t[0],t[1]))
    
    tree2 = ttk.Treeview(window,columns=columns, show="headings")
    tree2.place(relx=0, rely=0.66, relheight=0.3)
    tree2.heading("name", text="Тип")
    tree2.heading("parametr", text="процент")
    for t in atypes:
        
        tree2.insert("", END, values=(t[0],t[1]))
    
button2 = ttk.Button(text="Аналитика", command=click2)
button2.place(relx=.5, rely=.60, anchor="c")
 
root.mainloop()
