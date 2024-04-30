from typing import List

from sqlalchemy import select, delete

from Database.PetOrm import PetOrm
from Database.UserOrm import UserOrm
from Database.core import session_maker
from Dtos.PetDTO import PetDTO, PetAddDTO


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
        pet_from_db = session.get(PetOrm, pet_id)
        pet_from_db.name = pet.name
        pet_from_db.age = pet.age
        session.commit()
        return PetDTO.model_validate(pet_from_db, from_attributes=True)


def delete_pet(id: int) -> None:
    with session_maker() as session:
        query = delete(PetOrm).where(PetOrm.id == id)
        session.execute(query)
        session.commit()
    return None


def get_pets_by_user_id(owner_id: int) -> List[PetDTO]:
    with session_maker() as session:
        query = select(PetOrm).where(PetOrm.owner_id == owner_id)
        result = session.execute(query)
        res = result.scalars().all()

    return [PetDTO.model_validate(row, from_attributes=True) for row in res]
