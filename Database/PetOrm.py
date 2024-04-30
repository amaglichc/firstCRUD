from typing import TYPE_CHECKING

from pydantic import PositiveInt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from Database.core import Base
from Database.core import intpk

if TYPE_CHECKING:
    from Database.UserOrm import UserOrm


class PetOrm(Base):
    __tablename__ = 'pets'
    id: Mapped[intpk]
    name: Mapped[str]
    age: Mapped[PositiveInt]
    owner: Mapped["UserOrm"] = relationship(back_populates="pets", lazy='selectin')
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'))
