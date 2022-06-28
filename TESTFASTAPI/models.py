from database import Base
import sqlalchemy as db
from sqlalchemy import DateTime,Column, Integer, String


class Customers(Base):  # pojo
 
    __tablename__ = 'customer_test_tab'

    ID=db.Column(db.Integer,primary_key=True)
    
    FIRST_NAME = db.Column(db.String,
                           primary_key=False)
    LAST_NAME = db.Column(db.String(50),
                          primary_key=False)
    EMAIL = db.Column(db.String(50),
                       primary_key=False)

    CUSTOMER_TYPE = db.Column(db.String(50),
                       primary_key=False)
    
    CREATED_ON = db.Column(db.DateTime)

