# Any necessary installs/imports
import sqlalchemy
from sqlalchemy import create_engine 
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
engine = create_engine('sqlite:///table9.db', echo = True)
engine.connect()
Base = declarative_base()

# Create the tables
class Balances(Base):
    __tablename__ = "Balances"
    AccountID = Column(Integer,  primary_key = True) 
    Name = Column(String, nullable=False)
    Balance= Column(Numeric(10,2), nullable=False) # not sure abt insights

    
class Payments(Base):
    __tablename__='Payments'
    PaymentID = Column(Integer, primary_key=True)
    FromAccount = Column(Integer, ForeignKey('Balances.AccountID'), nullable=False)
    ToAccount = Column(Integer, ForeignKey('Balances.AccountID'), nullable=False)
    Amount = Column(Numeric(10,2))
    FromAccoun = relationship(Balances, foreign_keys = [FromAccount])
    ToAccoun = relationship(Balances, foreign_keys = [ToAccount])

                       
Base.metadata.create_all(engine)    
from sqlalchemy.orm import sessionmaker  
Session = sessionmaker(bind=engine)
session = Session() 
      
# Do the inserts
print("---beginning inserts")
session.add_all([Balances(AccountID =101, Name ="Chad E. Blair", Balance = 100.00),
                Balances(AccountID =102, Name ="Michael K. Taylor",Balance = 0.00)])
session.commit()
 # Do the transaction
try: 
    print('-- starting a transaction')
    # first query
    q1 = session.query(Balances).filter_by(AccountID =101).first()
    q1.Balance  -= 100
    q2 = session.query(Balances).filter_by(AccountID =102).first()
    q2.Balance += 100                   
    session.commit()
    print('--finished')
except: 
    session.rollback()
    raise                   
                       
                      
# Fetch everything from both tables