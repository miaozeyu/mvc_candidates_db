from sqlalchemy import Integer, String, Column, Date, ForeignKey
from sqlalchemy.orm import relationship
from Model import Model

class Interview(Model):
    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(Integer, ForeignKey('positions.id'))
    feedback = Column(String(1000), nullable=False)
    date = Column(Date, nullable=False)
    recruiter_id = Column(Integer, ForeignKey('recruiters.id'))
    # the below relationship allows you to access recruiter as an object and its columns
    recruiter = relationship('Recruiter')
    # the below foreign key doesn't necessarily allow you to access candidate as an object but only the key
    candidate_id = Column(Integer, ForeignKey('candidates.id', ondelete='CASCADE'))
    #test if I can access interview.candidate.first_name because relationship is defined on
    #Candidate's side
    client = Column(Integer, ForeignKey('clients.id'))