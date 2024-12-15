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
