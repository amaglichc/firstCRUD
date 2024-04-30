from typing import List

from fastapi import APIRouter

from Database import UserRepo, PetRepo
from Dtos.PetDTO import PetDTO, PetAddDTO
from Dtos.UserDTO import UserAddDTO, UserDTO

router = APIRouter(
    tags=["pet"],
    prefix="/pet"
)


@router.get("", response_model=List[PetDTO])
def get_pets() -> list[PetDTO]:
    return PetRepo.get_all_pets()


@router.get("/{id}", response_model=PetDTO)
def get_pet_by_id(id: int) -> PetDTO:
    return PetRepo.get_pet_by_id(id)


@router.put("/{id}", response_model=UserDTO)
def update_pet(id: int, pet: PetAddDTO) -> PetDTO:
    return PetRepo.update_pet(id, pet)


@router.delete("/{id}", response_model=dict[str, str])
def delete_pet(id: int) -> dict[str, str]:
    PetRepo.delete_pet(id)
    return {
        "Status code: ": "204",
        "Message": "Pet has been deleted"
    }
