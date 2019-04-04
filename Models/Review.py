from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from Model import Model

class Review(Model):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    review_date = Column(Date)
    content = Column(String(2000), nullable=False)
    reviewer_1 = Column(String(400))
    reviewer_2 = Column(String(400))
    candidate = Column(Integer, ForeignKey('candidates.id'))