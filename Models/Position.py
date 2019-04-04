from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Model import Model

class Position(Model):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)
    tech_skills = Column(String(200), nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    salary = Column(Integer, nullable=False)
    interviews = relationship("Interview")

    #
    # Reference for the client
    #
    client = Column(Integer, ForeignKey('clients.id'))

    #
    # Reference for the recruiter
    #
    recruiter = Column(Integer, ForeignKey('recruiters.id'))