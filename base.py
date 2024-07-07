from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session
from sqlalchemy import MetaData,create_engine
from datetime import *
from config import url

engine = create_engine(url=url)
meta_data = MetaData
session = Session(engine)
class Base(DeclarativeBase):
    pass

class Workers(Base):
    __tablename__ = "Workers"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    telegram_id:Mapped[float]

class Open(Base):
    __tablename__ = "open"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    date:Mapped[datetime]
    money:Mapped[float]
    cars:Mapped[int]

class close(Base):
    __tablename__ = "close"
    id:Mapped[int] = mapped_column(primary_key=True)
    get_cars:Mapped[int]
    out_cars:Mapped[int]
    money_get:Mapped[float]

class cars_to_get(Base):
    __tablename__= "cars_to_get"
    id:Mapped[int]= mapped_column(primary_key=True)
    name_of_driver:Mapped[str]
    name_of_geter:Mapped[str]
    mark:Mapped[str]
    gos_number:Mapped[str]
    color:Mapped[str]
    address:Mapped[str]
    time:Mapped[datetime]

    def __repr__(self) -> str:
        return f"{self.mark!r} {self.gos_number!r} {self.color} {self.address!r} {self.time!r}"
    
class cars_to_out(Base):
    __tablename__ = 'cars_to_out'
    id:Mapped[int]= mapped_column(primary_key=True)
    name_of_outer:Mapped[str]
    time_to_out:Mapped[datetime]=mapped_column(default=None)
    time_of_get_police:Mapped[datetime]=mapped_column(default=None)
    name_of_police:Mapped[str]=mapped_column(default=None)
    name_of_car_owner:Mapped[str]=mapped_column(default=None)
    price:Mapped[float]=mapped_column(default=None)
    chek:Mapped[bool] =mapped_column(default=False)

Base.metadata.create_all(engine)