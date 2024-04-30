from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from Database.core import Base, intpk

if TYPE_CHECKING:
    from Database.PetOrm import PetOrm


class UserOrm(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    name: Mapped[str]
    age: Mapped[int]
    email: Mapped[str]
    pets: Mapped[List["PetOrm"]] = relationship(back_populates="owner", lazy='selectin',
                                                cascade='all,delete-orphan,delete')
