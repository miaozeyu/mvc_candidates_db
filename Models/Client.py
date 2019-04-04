from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from Model import Model

class Client(Model):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    phone = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    interviews = relationship("Interview")
    positions = relationship("Position")


#
# Methods
#

    def serialize(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "position": self.position
        }


