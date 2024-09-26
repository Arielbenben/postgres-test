from sqlalchemy.orm import relationship
from config.base import Base
from sqlalchemy import Column, Integer, ForeignKey, String




class Target(Base):
    __tablename__ = 'targets'

    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String(255), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)  # Fixed case
    target_type_id = Column(Integer, ForeignKey('target_types.target_type_id'))  # Fixed case
    target_priority = Column(Integer)

    city = relationship('City', back_populates='targets')
    target_type = relationship('TargetType', back_populates='targets')

    def __repr__(self):
        return (f"<Target(id={self.target_id}, industry={self.target_industry}, "
                f"city_id={self.city_id}, target_type_id={self.target_type_id}, "
                f"priority={self.target_priority})>")