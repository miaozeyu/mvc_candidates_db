from sqlalchemy import Column, String, Numeric, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from Model import Model
from pyld import jsonld

class Candidate(Model):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(30), nullable=False)
    birthday = Column(Date, nullable=True)
    phone = Column(String(30), nullable=True)
    skills = Column(String(1000), default="")
    languages = Column(String(500), default="")
    # the below relationship allows you to access interview as an object
    # bacref also set up an relationship on Interview's end and allows access to candidate as an object and its columns from Interview side
    interviews = relationship("Interview", cascade="all, delete, delete-orphan")
    reviews = relationship("Review")

#
# Methods
#

    def serialize(self):
        compacted_json = jsonld.compact(
        {
            "http://schema.org/first_name": self.first_name,
            "http://schema.org/last_name": self.last_name,
            "http://schema.org/email": self.email,
            "http://schema.org/birthDate": self.birthday.isoformat() if self.birthday else "",
            "http://schema.org/telephone": self.phone if self.phone else "",
            "http://schema.org/languages": self.languages,
            "http://schema.org/skills": self.skills,
            "http://schema.org/nr_of_reviews": len(self.reviews),
            "http://schema.org/nr_of_interviews": len(self.interviews)
        }, self.get_context())

        return compacted_json

    def get_context(self):
        return {
            "@context":{
                "frist_name": "http://schema.org/first_name",
                "last_name": "http://schema.org/last_name",
                "email": "http://schema.org/email",
                "birthday": "http://schema.org/birthDate",
                "phone": "http://schema.org/telephone",
                "languages": "http://schema.org/languages",
                "skills": "http://schema.org/skills",
                "nr_of_reviews": "http://schema.org/nr_of_reviews",
                "nr_of_interviews": "http://schema.org/nr_of_interviews"
            }
        }