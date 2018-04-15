"""Before you read this working implementation, 
please review the SQLAlchemyTutorial to walk through the steps of 
initialising a simple SQLAlchemy ORM on Python"""

import sqlalchemy 
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 

engine = create_engine('sqlite:///database.db')
engine.connect() 

Base = declarative_base() 

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	insurance_id = Column(Integer)

	def __repr__(self):
		return "<User(id={0}, name={1}, insurance_id={2})>".format(self.id, self.name, self.insurance_id)

class Insurance(Base):
	__tablename__ = 'insurance'
	id = Column(Integer, ForeignKey('users.insurance_id'), primary_key = True)
	claim_id = Column(Integer)
	users = relationship(User)

	def __repr__(self):
		return "<Insurance(id={0}, claim_id={1}>".format(self.id, self.claim_id)

Base.metadata.create_all(bind=engine) 

Session = sessionmaker(bind=engine)
session = Session()

session.add(User(id = 9, name = "What's His Name", insurance_id = 5))
session.add(Insurance(id = 5, claim_id = 1))
session.commit()

print(session.query(User).all())

"""You should see something like: 

[<User(id=1, name=What's Her Name, insurance_id=1)>, 
<User(id=2, name=What's His Name, insurance_id=2)>, 
<User(id=3, name=Sterne, insurance_id=3)>, 
"""

print(session.query(Insurance).filter_by(claim_id = 1).all())

"""
Here, you should see something like: 
[<Insurance(id=1, claim_id=1>, 
<Insurance(id=2, claim_id=2>, 
<Insurance(id=3, claim_id=3>,
<Insurance(id=4, claim_id=4>, 
<Insurance(id=5, claim_id=5>]
"""