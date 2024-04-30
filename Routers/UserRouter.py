from typing import List

from fastapi import APIRouter
from Database.core import create_tables
from Database import UserRepo, PetRepo
from Dtos.PetDTO import PetAddDTO, PetDTO
from Dtos.UserDTO import UserAddDTO, UserDTO

router = APIRouter(
    tags=["user"],
    prefix="/user"
)


@router.get("", response_model=List[UserDTO])
def get_users() -> list[UserDTO]:
    return UserRepo.get_all_users()


@router.get("/{user_id}", response_model=UserDTO)
def get_user_by_id(user_id: int) -> UserDTO:
    return UserRepo.get_user_by_id(user_id)


@router.post("", response_model=UserDTO)
def create_user(user: UserAddDTO) -> UserDTO:
    return UserRepo.add_user(user)


@router.post("/{user_id}/pet", response_model=PetDTO)
def create_pet(pet: PetAddDTO, user_id: int) -> PetDTO:
    return PetRepo.add_pet(pet, user_id)


@router.put("/{id}", response_model=UserDTO)
def update_user(id: int, user: UserAddDTO) -> UserDTO:
    return UserRepo.update_user(id, user)


@router.delete("/{id}", response_model=dict[str, str])
def delete_user(id: int) -> dict[str, str]:
    UserRepo.delete_user(id)
    return {
        "Status code: ": "204",
        "Message": "User has been deleted"
    }