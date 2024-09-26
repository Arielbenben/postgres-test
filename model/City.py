from sqlalchemy.orm import relationship
from config.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class City(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String(100), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)  # Fixed case
    latitude = Column(Float)
    longitude = Column(Float)

    country = relationship('Country', back_populates='cities')
    targets = relationship('Target', back_populates='city')

    def __repr__(self):
        return (f"<City(id={self.city_id}, name={self.city_name}, "
                f"country_id={self.country_id}, latitude={self.latitude}, "
                f"longitude={self.longitude})>")