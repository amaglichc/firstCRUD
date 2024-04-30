from pydantic import BaseModel


class PetAddDTO(BaseModel):
    name: str
    age: int


class PetDTO(PetAddDTO):
    id: int
