from sqlalchemy.orm import relationship
from config.base import Base
from sqlalchemy import Column, Integer, String



class TargetType(Base):
    __tablename__ = 'target_types'

    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String(255), unique=True, nullable=False)

    targets = relationship('Target', back_populates='target_type')

    def __repr__(self):
        return f"<TargetType(id={self.target_type_id}, name={self.target_type_name})>"