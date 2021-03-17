# qs: how to specify the length of integer
import sqlalchemy
from sqlalchemy import create_engine 
from datetime import datetime
engine = create_engine('sqlite:///:memory:', echo = True)
engine = create_engine('sqlite:///bankloans.db') 
engine.connect() 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 

#Create a Table Mapping

from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey 
from sqlalchemy.orm import relationship, sessionmaker 

class Clients(Base): 
    __tablename__ = "Clients"
    CLIENTNUMBER = Column(Integer, primary_key = True)
    FIRSTNAME = Column(String(20))
    SURNAME = Column(String(20))
    EMAIL = Column(String(100))
    PHONE = Column(String)
    def __repr__(self):
        return "<Clients(CLIENTNUMBER={0}, FIRSTNAME={1}, SURNAME={2})>".format(self.CLIENTNUMBER, self.FIRSTNAME, self.SURNAME)
    
class Loans(Base): 
    __tablename__= "Loans"
    ACCOUNTNUMBER = Column(Integer, primary_key = True)
    CLIENTNUMBER = Column(Integer,  ForeignKey('Clients.CLIENTNUMBER'))
    STARTDATE = Column(DateTime)
    STARTMONTH= Column(Integer) 
    TERM = Column(Integer) 
    REMAINING_TERM = Column(Integer)
    PRINCIPALDEBT= Column(Numeric(11, 2)) 
    ACCOUNTLIMIT = Column(Numeric(11, 2)) 
    BALANCE = Column(Numeric) 
    STATUS = Column(String(11))
    Clients = relationship(Clients)
    
Base.metadata.create_all(engine)
print("------------tables are created now")
from sqlalchemy.orm import sessionmaker  

Session = sessionmaker(bind=engine)
session = Session() 
print('------------starting insert')
session.add_all([Clients(CLIENTNUMBER = 1, FIRSTNAME='Robert',SURNAME= 'Warren',EMAIL= 'RobertDWarren@teleworm.us',PHONE = '(251) 546-9442'), 
                Clients(CLIENTNUMBER = 2, FIRSTNAME='Vincent', SURNAME= 'Brown', EMAIL= 'VincentHBrown@rhyta.com', PHONE ='(125) 546-4478'), 
                Clients(CLIENTNUMBER = 3,FIRSTNAME= 'Janet', SURNAME= 'Prettyman', EMAIL= 'JanetTPrettyman@teleworm.us',PHONE = '(949) 569-4371'), 
                Clients(CLIENTNUMBER = 4, FIRSTNAME='Martina', SURNAME= 'Kershner', EMAIL= 'MartinaMKershner@rhyta.com', PHONE ='(630) 446-8851'), 
                Clients(CLIENTNUMBER = 5, FIRSTNAME='Tony', SURNAME= 'Schroeder', EMAIL= 'TonySSchroeder@teleworm.us', PHONE ='(226) 906-2721'),
                Clients(CLIENTNUMBER = 6, FIRSTNAME='Harold', SURNAME= 'Grimes', EMAIL= 'HaroldVGrimes@dayrep.com', PHONE ='(671) 925-1352'), 
                Loans(ACCOUNTNUMBER = 1, CLIENTNUMBER =1,STARTDATE = datetime(2017,11,1, 0,0,0),  STARTMONTH= 201712,TERM = 36, REMAINING_TERM = 35,PRINCIPALDEBT=  10000.00,ACCOUNTLIMIT =  15000.00,BALANCE =  9800.00, STATUS = 'NORMAL'), 
                Loans(ACCOUNTNUMBER = 2, CLIENTNUMBER =2,STARTDATE = datetime(2018,1,1, 0,0,0),  STARTMONTH= 201802, TERM =24, REMAINING_TERM = 24, PRINCIPALDEBT= 1000.00, ACCOUNTLIMIT = 1500.00,BALANCE = 1000.00, STATUS = 'NORMAL'), 
                Loans(ACCOUNTNUMBER = 3, CLIENTNUMBER =1,STARTDATE = datetime(2016,11,1, 0,0,0),  STARTMONTH= 201612, TERM =12, REMAINING_TERM = -3, PRINCIPALDEBT= 2000.00, ACCOUNTLIMIT = 15000.00,BALANCE =  4985.12, STATUS = 'ARREARS'), 
                Loans(ACCOUNTNUMBER = 4, CLIENTNUMBER =3,STARTDATE = datetime(2018,1,1, 0,0,0),  STARTMONTH= 201802, TERM =24, REMAINING_TERM = 24, PRINCIPALDEBT= 3500.00, ACCOUNTLIMIT = 5000.00, BALANCE = 1300.00, STATUS = 'NORMAL'), 
                Loans(ACCOUNTNUMBER = 5, CLIENTNUMBER =4,STARTDATE = datetime(2017,11,1, 0,0,0),  STARTMONTH= 201712, TERM =12, REMAINING_TERM = 35, PRINCIPALDEBT= 10000.00, ACCOUNTLIMIT = 15000.00, BALANCE = 0.00,STATUS =  'PAID OFF'), 
                Loans(ACCOUNTNUMBER = 6, CLIENTNUMBER =5,STARTDATE = datetime(2018,1,1, 0,0,0),  STARTMONTH= 201802, TERM =48, REMAINING_TERM = 24, PRINCIPALDEBT= 1000.00, ACCOUNTLIMIT = 1500.00,BALANCE =  0.00, STATUS = 'PAID OFF')])

print('------------finished insert')
print('------------QUERY: Everyone who owes more than $5,000 on an account:')
for u, l in session.query(Clients, Loans).\
                   filter(Clients.CLIENTNUMBER==Loans.CLIENTNUMBER).\
                   filter(Loans.BALANCE>5000).\
                   all():
    print(u, l)
print('------------FINISH QUERY')

client1 = session.query(Clients).filter_by(FIRSTNAME="Martina")
print('------------NAME WAS CHANGED')
client1.FIRSTNAME="Martin"
session.commit()
# refelctng
from sqlalchemy import Table, MetaData
metadata = MetaData()
users = Table('clients', metadata, autoload=True, autoload_with=engine)
print(repr(users))