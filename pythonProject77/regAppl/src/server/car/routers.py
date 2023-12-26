from typing import List
from fastapi import APIRouter
from .models import Basemodel_car, restored_car, Update_car, NewId
from regAppl.src.server.car.resolvers import (get_cars, get_car, add_new_car,
                                              update_car, delete_car)

router = APIRouter()

@router.get('/', tags=['car'])
def router_cars() -> List[Basemodel_car]:
    return get_cars()

@router.get('/{car_id}', tags=["car"])
def router_car(id: int) -> restored_car:
    return get_car(id)

@router.post('/', tags=["car"])
def router_new_cars(restored_car: Basemodel_car) -> NewId:
    return add_new_car(restored_car)

@router.put('/{car_id}', tags=["car"])
def router_new_car(id: int, car: Update_car) -> NewId:
    return update_car(id, car)


@router.delete('/{car_id}', tags=["car"])
def router_delete_car(id: int) -> NewId:
    return delete_car(id)

