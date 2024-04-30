from typing import List

from sqlalchemy import select, delete

from Database.PetOrm import PetOrm
from Database.UserOrm import UserOrm
from Dtos.PetDTO import PetDTO, PetAddDTO
from Database.core import session_maker


def get_all_pets() -> List[PetDTO]:
    with session_maker() as session:
        res = session.execute(select(PetOrm))
        return [PetDTO.model_validate(row, from_attributes=True) for row in res.scalars().all()]


def get_pet_by_id(pet_id: int) -> PetDTO:
    with session_maker() as session:
        return PetDTO.model_validate(session.get(PetOrm, pet_id), from_attributes=True)


def add_pet(pet_data: PetAddDTO, user_id: int) -> PetDTO:
    with session_maker() as session:
        pet = PetOrm(**pet_data.model_dump())
        pet.owner_id = user_id
        session.add(pet)
        session.flush()
        owner: UserOrm = session.get(UserOrm, user_id)
        owner.pets.append(pet)
        session.commit()
        return PetDTO.model_validate(pet, from_attributes=True)


def update_pet(pet_id: int, pet: PetAddDTO) -> PetDTO:
    with session_maker() as session:
        old_pet: PetOrm = session.get(PetOrm, pet_id)
        old_pet.name = pet.name
        old_pet.age = pet.age
        session.commit()
        return PetDTO.model_validate(old_pet, from_attributes=True)


def delete_pet(id: int) -> None:
    with session_maker() as session:
        query = delete(PetOrm).where(PetOrm.id == id)
        session.execute(query)
        session.commit()
    return None
