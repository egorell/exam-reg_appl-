from typing import List
from fastapi import APIRouter
from .models import Basemodel_user, Basemodel_NewUser, Update_user, NewId
from regAppl.src.server.user.resolvers import (get_users, get_user, add_new_users,
                                               update_user, delete_user)


router = APIRouter()

@router.get('/', tags=["user"])
def router_users() -> List[Basemodel_user]:
    return get_users()

@router.get('/{user_id}', tags=["user"])
def router_user(id: int) -> Basemodel_NewUser:
    return get_user(id)

@router.post('/', tags=["user"])
def router_new_users(Basemodel_NewUser: Basemodel_user) -> NewId:
    return add_new_users(Basemodel_NewUser)

@router.put('/{user_id}', tags=["user"])
def router_new_user(id: int, user: Update_user) -> NewId:
    return update_user(id, user)


@router.delete('/{user_id}', tags=["user"])
def router_delete_user(id: int) -> NewId:
    return delete_user(id)