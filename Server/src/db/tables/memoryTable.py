from db.databaseProvider import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Memory(Base):
    __tablename__ = 'memories'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String)
    position = Column(String)  # Json representation of the area of the memory. Null if no area is set.
    startDate = Column(Integer)
    endDate = Column(Integer)

    def __repr__(self):
        return f"Memory(id={self.id}, name={self.name}, description={self.description}, position={self.position}, startDate={self.startDate}, endDate={self.endDate})"


class Moment(Base):
    __tablename__ = 'moments'

    id = Column(Integer, primary_key=True)
    memory_id = Column(Integer, ForeignKey('memories.id'))
    file_id = Column(String) # ID linking to minio file.
    position = Column(String)  # Json representation of the location of the memory. Null if no area is set.
    date = Column(Integer)
    description = Column(String)

    def __repr__(self):
        return f"Moment(id={self.id!r}, memory_id={self.memory_id!r})"
