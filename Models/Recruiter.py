from sqlalchemy import Column, String, Numeric, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from Model import Model

class Recruiter(Model):
    __tablename__ = 'recruiters'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(30), nullable=False)
    interview = relationship("Interview")
    positions = relationship("Position")