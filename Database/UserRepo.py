from typing import List

from sqlalchemy import select, delete

from Database.UserOrm import UserOrm
from Database.core import session_maker
from Dtos.UserDTO import UserDTO, UserAddDTO


def get_all_users() -> List[UserDTO]:
    with session_maker() as session:
        res = session.execute(select(UserOrm))
        return [UserDTO.model_validate(row, from_attributes=True) for row in res.scalars().all()]


def get_user_by_id(user_id: int) -> UserDTO:
    with session_maker() as session:
        return UserDTO.model_validate(session.get(UserOrm, user_id), from_attributes=True)


def add_user(user_data: UserAddDTO) -> UserDTO:
    with session_maker() as session:
        user = UserOrm(**user_data.model_dump())
        session.add(user)
        session.flush()
        session.commit()
        return UserDTO.model_validate(user, from_attributes=True)


def update_user(user_id: int, user: UserAddDTO) -> UserDTO:
    with session_maker() as session:
        old_user: UserOrm = session.get(UserOrm, user_id)
        old_user.name = user.name
        old_user.age = user.age
        old_user.email = user.email
        old_user.pets = user.pets
        session.commit()
        return UserDTO.model_validate(old_user, from_attributes=True)


def delete_user(id: int) -> None:
    with session_maker() as session:
        query = delete(UserOrm).where(UserOrm.id == id)

        session.execute(query)
        session.commit()
    return None


