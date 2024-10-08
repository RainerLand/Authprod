from sqlalchemy import TIMESTAMP, Column, Integer, MetaData, String, Table
from database import Base


class Operation(Base):
    __tablename__ = 'operation'

    id = Column(Integer, primary_key=True)
    quantity = Column(String)
    instrument_type = Column(String, nullable=True),
    date = Column(TIMESTAMP)
    type = Column(String)
