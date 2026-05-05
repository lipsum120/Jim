from unittest import result

from fastapi import APIRouter, Depends
from api.v1.deps import get_user_service
from schemas.user import User, UserCreate, UserUpdate
from services.user_service import UserService

router = APIRouter (
    prefix = "/users", tags = ["users"] 
)

@router.get("/")
def get_users(
    service: UserService = Depends(get_user_service)
):
    return service.get_users()

@router.get("/{id}")
def get_user(
    id: int,
    service: UserService = Depends(get_user_service)
):
    return service.get_user(id)

@router.post("/", response_model=User)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return service.create_user(data)

@router.put("/{id}", response_model=User)
def update_user(
    id: int,
    data: UserUpdate,
    service: UserService = Depends(get_user_service)
):
    return service.update_user(id, data)

@router.delete("/{id}")
def delete_user(
    id: int,
    service: UserService = Depends(get_user_service)
):
    return service.delete_user(id)