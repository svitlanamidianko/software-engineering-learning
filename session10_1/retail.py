# qs: how to specify the length of integer
# how do we do quantity + 99
import sqlalchemy
from sqlalchemy import create_engine 
from datetime import datetime
engine = create_engine('sqlite:///:memory:', echo = True)
engine = create_engine('sqlite:///retail.db') 
engine.connect() 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 

#Create a Table Mapping

from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey 
from sqlalchemy.orm import relationship, sessionmaker 


class Product(Base): 
    __tablename__ = "Product"
    ProductID = Column(Integer, primary_key = True)
    Title = Column(String)
    Description  = Column(String)
    Price = Column(Integer)
    Cost = Column(Integer)

class Customer(Base): 
    __tablename__="Customer"
    CustomerID  = Column(Integer, primary_key = True)
    FirstName = Column(String)
    Surname = Column(String)
    AddressLine1 = Column(String)
    AddressLine2= Column(String)
    AddressLine3 = Column(String)
    PhoneNumber = Column(String)
    Email = Column(String)

class Orders(Base): 
    __tablename__= "Orders"
    OrderID  = Column(Integer, primary_key = True)
    CustomerID= Column(Integer, ForeignKey("Customer.CustomerID"))
    DateOrdered  = Column(DateTime)
    MonthOrdered=Column(Integer)
    Customer = relationship(Customer)


class OrderItems(Base): 
    __tablename__  = "OrdersItems"
    OrderID  = Column(Integer, primary_key = True)
    ProductID  = Column(Integer, ForeignKey("Product.ProductID"))
    Quantity  = Column(Integer)
    Product= relationship(Product)

class Warehouse(Base): 
    __tablename__ = "Warehouse"
    WarehouseID  = Column(Integer, primary_key = True)
    Name  = Column(String)
    AddressLine1  = Column(String)
    AddressLine2  = Column(String)
    AddressLine3  = Column(String)

class Inventory(Base): 
    __tablename__ = 'Inventory'
    WarehouseID = Column(Integer, ForeignKey("Warehouse.WarehouseID"), primary_key = True)
    ProductID = Column(Integer, ForeignKey("Product.ProductID"), primary_key = True)
    Quantity = Column(Integer)
    Warehouse = relationship(Warehouse)
    Product = relationship(Product)

class Supplier(Base): 
    __tablename__ = 'Supplier'
    SupplierID  = Column(Integer, primary_key = True)
    Name= Column(String)
    AddressLine1 = Column(String)
    AddressLine2 = Column(String)
    AddressLine3 = Column(String)
    PhoneNumber = Column(String)
    Email = Column(String)

class SupplierProduct(Base): 
    __tablename__="SupplierProduct"
    SupplierID = Column(Integer, ForeignKey("Supplier.SupplierID"), primary_key = True)
    ProductID = Column(Integer, ForeignKey("Product.ProductID"), primary_key = True)
    DaysLeadTime = Column(Integer)
    Cost= Column(Integer)
    Supplier = relationship(Supplier)
    Product = relationship(Product)
 
class SupplierOrders(Base): 
    __tablename__= "SupplierOrders"
    SupplierOrderID = Column(Integer, primary_key = True)
    SupplierID = Column(Integer, ForeignKey("Supplier.SupplierID"))
    ProductID= Column(Integer, ForeignKey("Product.ProductID"))
    WarehouseID = Column(Integer, ForeignKey("Warehouse.WarehouseID"))
    Quantity = Column(Integer)
    Status = Column(String)
    DateOrdered = Column(DateTime)
    DateDue = Column(DateTime)
    Supplier=relationship(Supplier)
    Product = relationship(Product)
    Warehouse = relationship(Warehouse)


f
print("------------tables are created now")
from sqlalchemy.orm import sessionmaker  
Session = sessionmaker(bind=engine)
session = Session() 
print('------------starting insert')
# https://docs.sqlalchemy.org/en/13/orm/session_transaction.html
try: 
    session.add_all([Product(ProductID = 3001, Title = "Widget", Description  = "Widge all your worries away!",Price =99.95, Cost = 23.05),
                 Product(ProductID = 3002, Title = "Wodget", Description  = "Wodge all your worries away!", Price =199.95,Cost =  123.05), 
                 Orders(OrderID  =1000,CustomerID=  2000, DateOrdered  = datetime(2025, 1,1,1,1,1), MonthOrdered = 202501), 
                 OrderItems(OrderID  =1000,ProductID  =  3001, Quantity  =1), 
                 OrderItems(OrderID  =1001,ProductID  =  3002, Quantity  =2), 
                 Warehouse(WarehouseID  = 4001, Name  ="ABC Warehouse", AddressLine1 = "1374 Elkview Drive", AddressLine2 = "Fort Lauderdale", AddressLine3 = "FL 33301"), 
                 Warehouse(WarehouseID  = 4002, Name  ="XYZ Warehouse", AddressLine1 = "1576 Walnut Street", AddressLine2 = "Jackson",AddressLine3 =  "MS 39211"), 
                 Inventory(WarehouseID = 4001,ProductID = 3001,Quantity =3), 
                 Inventory(WarehouseID = 4001,ProductID = 3002,Quantity =1), 
                 Inventory(WarehouseID = 4002,ProductID = 3001,Quantity =1), 
                 Inventory(WarehouseID = 4002,ProductID = 3002,Quantity =4), 
                 Supplier(SupplierID  =5001, Name= "Widge Suppliers Ltd", AddressLine1 = "3316 Whitetail Lane", AddressLine2 = "Irving",AddressLine3 =  "TX 75039",PhoneNumber = "479-357-6159", Email ="TimothyCSilva@widge.com"), 
                 Supplier(SupplierID  =5002, Name= "Wodge Suppliers PLC", AddressLine1 = "390 Clarksburg Park Road", AddressLine2 = "Scottsdale",AddressLine3 =  "AZ 85256", PhoneNumber = "252-441-7555", Email ="JohnAWilley@wodge.co.uk"), 
                 SupplierProduct(SupplierID = 5001, ProductID =3001, DaysLeadTime =3, Cost= 23.05), 
                 SupplierProduct(SupplierID = 5001, ProductID =3002, DaysLeadTime =20, Cost= 999.99), 
                 SupplierProduct(SupplierID = 5002, ProductID =3001, DaysLeadTime =20, Cost= 9999.99), 
                 SupplierProduct(SupplierID = 5002, ProductID =3002, DaysLeadTime =5, Cost= 123.05), 
                 SupplierOrders(SupplierOrderID = 6001,SupplierID =  5001, ProductID= 3001, WarehouseID = 4001,Quantity =  99, Status = "ORDERED", DateOrdered = datetime(2025,1,15), DateDue =datetime(2025,1,21)), 
                 SupplierOrders(SupplierOrderID = 6002, SupplierID = 5001, ProductID= 3001, WarehouseID = 4002, Quantity = 99, Status = "DELIVERED",DateOrdered =  datetime(2025,1,16), DateDue =datetime(2025,1,23)), 
                 Customer(CustomerID  =2000, FirstName ="Gertrud",Surname =  "Karr", AddressLine1 = "1709 Woodridge Lane", AddressLine2= "Memphis", AddressLine3 = "TN 38110", PhoneNumber = "559-309-6624", Email ="gkarr@dayrep.com"), 
                 Customer(CustomerID  =2001, FirstName ="Clara",Surname =  "Tang", AddressLine1 = "500 Retreat Avenue",AddressLine2=  "York", AddressLine3 = "ME 03909", PhoneNumber = "312-367-6954", Email ="clara_tang@armyspy.com")
                 ])
    session.commit()
    print('------------finished insert')
except: 
    session.rollback()
    raise

# Rewrite all your transactions from the exercise to now use SQLAlchemy.
# (1) Write a transaction for a delivery from the Widge supplier which has just arrived 
# at the ABC warehouse and unloaded 99 new Widgets.
# (2) Write a transaction for a Customer order of 500 Wodgets which places an order with the cheapest supplier. 
# (3) What statements would be needed to update a customer's details to their new address,
#  while still maintaining referential integrity?
try: 
    print('---------------starting  a transaction for a delivery from the Widge supplier which has just arrived at the ABC warehouse and unloaded 99 new Widgets.')
    session.add_all([SupplierOrders(SupplierOrderID = 6003, SupplierID = 5001, ProductID = 3001, WarehouseID = 4001, Quantity = 99, Status = "DELIVERED", DateOrdered = datetime(2025,1,15), DateDue=datetime(2025, 1,15)), 
                    Inventory(WarehouseID=4001,ProductID = 3001, Quantity = Quantity+ 99)])
    session.commit()
    print('---------------finished')
except: 
    session.rollback()
    #raise

try: 
    print('---------------starting a transaction for a Customer order of 500 Wodgets which places an order with the cheapest supplier.')
    session.add_all([Orders(OrderID = 1002, CustomerID = 2000,  DateOrdered  = datetime(2025, 1,1,1,1,1), MonthOrdered = 202501),
                    OrderItems(OrderID = 1002,ProductID = 3002, Quantity = 500)])
    session.commit()
    print('---------------finished')
except: 
    session.rollback()
    raise

try: 
    print('---------------starting update a customer details to their new address')
    cust =  session.query(Customer).filter_by(CustomerID=2000)
    cust.AddressLine1 = "x"
    session.commit()
    print('---------------finished')
except: 
    session.rollback()
    raise

