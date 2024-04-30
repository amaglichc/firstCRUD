from typing import List
from pydantic import BaseModel, EmailStr

from Dtos.PetDTO import  PetDTO


class UserAddDTO(BaseModel):
    name: str
    age: int
    email: EmailStr
    pets: List[PetDTO] = []


class UserDTO(UserAddDTO):
    id: int
