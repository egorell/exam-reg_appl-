from datetime import datetime
from regAppl.src.server.db_manager import base_manager
from .models import Basemodel_car, restored_car, Update_car, NewId


def get_cars():
    res = base_manager.execute("SELECT C.id, C.model, C.data, C.defect "
                               "FROM car C ", many=True)
    car = []
    for c in res['data']:
        print()
        car.append(Basemodel_car(id=c[0], model=c[1],
                                 data=datetime.strptime(c[2],'%Y-%m-%d %H:%M:%S.%f'), defect=c[3]))
    return car

def get_car(id: int):
    res = base_manager.execute("SELECT C.id, C.model, C.data, C.defect "
                               "FROM car C WHERE C.id = ? ",
                               args=(id,))
    print(res)
    return Basemodel_car(id=id, model=res['data'][0][1], data=res['data'][0][2], defect=res['data'][0][3])


def add_new_car(new_car: restored_car):
    res = base_manager.execute("INSERT INTO car(model, defect) "
                               "VALUES (?,?) "
                               "RETURNING id ", args=(new_car.model, new_car.defect))
    print(res)
    return NewId(code=res['code'], id=res['data'][0][0])

def update_car(id: int, car: Update_car):
    res = base_manager.execute("UPDATE car SET model = ?, defect = ? "
                               "WHERE id = ? ",
                               args=(car.model, car.defect, id,))
    return NewId(code=res['code'], id=id)

def delete_car(id: int):
    res = base_manager.execute("DELETE FROM car WHERE id = ? ",
                               args=(id,))
    return NewId(code=res['code'], id=id,)