# SQLAlchemy Setup Tutorial: A Friendly Intro 

# Local Setup 

First, install SQLAlchemy in terminal with:

`$ pip install sqlalchemy`

# Setup on a Python Module 

## Import SQLALchemy 

`import sqlalchemy` 

## Create Engine 

```python
from sqlalchemy import create_engine 
engine = create_engine('sqlite:///:memory:', echo = TRUE)
```
 
What's happening with the create_engine() function?

The engine connects to the database, and this function specifies which database it should connect to.

What is 'sqlite:///'? Firstly, this initialises an SQLite Database, which allows us to use SQLite syntax the way we have learnt in prior classes.

:memory: simply implies that the SQLite database will not persist beyond individual sessions.
The database will only persist as long as the application instance is running. 

If we do: 

```python
engine = create_engine('sqlite:///try_database.db') 
```

Then this creates a local .db file named 'try_database.db' (if it doesn't exist already on your path). We will learn how to use SQLAlchemy to open up the .db file and see if there are any new entries. This database.db file will persist locally.

## Connect to engine 

Now, connect to the engine interface that you created using the default connect() function. 

```python
engine.connect() 
```

## Declare a Base 

The base maintains a catalogue of classes and tables in the base; each application will usually have one. 

```python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() 
```

After declaring a base, we will be able to define classes relative to the base. So each class should be created as class 'tablename'(Base).

## Create a Table Mapping

Let's initialise a simple table 'Users' by initialising a User class and writing a __repr__() method to represent the schema. 

```python
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship, sessionmaker 

class User(Base):
	__table__ = 'users'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	insurance_id = Column(Integer)

	def __repr__():
		return "<User(id={0}, name={1}, insurance_id={2})>".format(self.id, self.name, self.insurance_id)
```

Let's create another table to display foreign relationships.

```python
class Insurance(Base):
	__table__ = 'insurance'
	id = Column(Integer, primary_key = True, ForeignKey('users.insurance_id'))
	claim_id = Column(Integer)
	users = relationship(User)
```

## Create the Table Schema

After defining the schema of the table, we will need to actually create it in our database.

We have to call: 

`Base.metadata.create_all(engine)`

This is very important, as without calling create_all(engine) and binding it to the engine, the schema will not be initialised. Your table should now be created, and you will be able to add elements to it. 

# Adding Elements to the SQLAlchemy 

In the same file, call the imports with: 

```python
from sqlalchemy.orm import sessionmaker 

from sqlalchemy_declarative import Base, User
```

Create an instance of your User class with: 

`user = User(id = 0, name='sterne', insurance_id='1234')`

And then add it to your DB, by starting a session. 

```python
from sqlalchemy.orm import sessionmaker  

Session = sessionmaker(bind=engine)
session = Session() 
session.add(user)
session.commit()
```

'user' should now be in your database! 

# Querying your Table

See the SQLALchemyQuery.py file for a working implementation of a basic SQLAlchemy query.

Let's check if 'user' is in the database.

```python
print(session.query(User).filter_by(name='sterne').first())
```

It should print out: 

```
<User(id=1, name=Sterne, insurance_id=1)>
```
 
Great! 

# Reflecting an Existing Database with SQLAlchemy

Reflecting a table simply means being able to read its metadata, and being able to use SQLAlchemy to read the contents of the table. 

```python
from sqlalchemy import Table
```

'Table' is the name of the table you are referencing. Make sure that you are connected to the same engine that has the table you are aiming to reflect.

## Reflect table from the engine: Table

`users = Table('users', metadata, autoload=True, autoload_with=engine)`

Load the table 'users' that you initialised before with the above function.

The autoload_with = engine parameter ensures that it's connecting to the right engine interface.

## Print table metadata

The __repr__() method that you defined in your User(Base) class will return a string detailing the details of your database in the format you chose.

`print(repr(users))` 

