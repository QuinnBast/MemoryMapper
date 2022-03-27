from db.databaseProvider import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Memory(Base):
    __tablename__ = 'memories'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    latitude = Column(Integer)
    longitude = Column(Integer)
    date = Column(Integer)

    def __repr__(self):
        return f"Memory(id={self.id}, name={self.name}, latitude={self.latitude}, longitude={self.longitude}, date={self.date})"

class Moment(Base):
    __tablename__ = 'moments'

    id = Column(Integer, primary_key=True)
    memory_id = Column(Integer, ForeignKey('memories.id'))

    def __repr__(self):
        return f"Moment(id={self.id!r}, memory_id={self.memory_id!r})"
