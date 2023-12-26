from regAppl.src.server.db_manager import base_manager
from .models import Basemodel_user, Basemodel_NewUser, Update_user, NewId


def get_users():
    res = base_manager.execute("SELECT U.id, U.name, U.surname, U.phone " 
                               "FROM users U ", many=True)
    users = []
    for u in res['data']:
        print()
        users.append(Basemodel_user(id=u[0], name=u[1], surname=u[2], phone=u[3]))
    return users

def get_user(id: int):
    res = base_manager.execute("SELECT U.id, U.name, U.surname, U.phone "
                               "FROM users U WHERE U.id = ? ",
                               args=(id,))
    print(res)
    return Basemodel_user(id=id, name=res['data'][0][1], surname=res['data'][0][2], phone=res['data'][0][3])

def add_new_users(new_user: Basemodel_NewUser):
    res = base_manager.execute("INSERT INTO users(name, surname, phone) "
                               "VALUES (?,?,?) "
                               "RETURNING id ", args=(new_user.name, new_user.surname, new_user.phone))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])

def update_user(id: int, user: Update_user):
    res = base_manager.execute("UPDATE users SET name = ?, surname = ?, phone = ? "
                               "WHERE id = ? ",
                               args=(user.name, user.surname, user.phone, id,))
    return NewId(code=res['code'], id=id)

def delete_user(id: int):
    res = base_manager.execute("DELETE FROM users WHERE id = ? ",
                               args=(id,))
    return NewId(code=res['code'], id=id)