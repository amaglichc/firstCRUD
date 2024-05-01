from typing import List, Annotated

from fastapi import APIRouter, Path

from Database import PetRepo
from Dtos.PetDTO import PetDTO, PetAddDTO

router = APIRouter(
    tags=["pet"],
    prefix="/pet"
)


@router.get("", response_model=List[PetDTO])
def get_pets() -> list[PetDTO]:
    return PetRepo.get_all_pets()


@router.get("/{id}", response_model=PetDTO)
def get_pet_by_id(id: Annotated[int, Path(ge=1)]) -> PetDTO:
    return PetRepo.get_pet_by_id(id)


@router.put("/{id}", response_model=PetDTO)
def update_pet(id: Annotated[int, Path(ge=1)], pet: PetAddDTO) -> PetDTO:
    return PetRepo.update_pet(id, pet)


@router.delete("/{id}", response_model=dict[str, str])
def delete_pet(id: Annotated[int, Path(ge=1)]) -> dict[str, str]:
    PetRepo.delete_pet(id)
    return {
        "Status code: ": "204",
        "Message": "Pet has been deleted"
    }
