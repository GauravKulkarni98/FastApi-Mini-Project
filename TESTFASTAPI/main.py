from pydantic import BaseModel
from typing import Union

from colorama import Cursor
from database import session
from models import Customers
from fastapi import FastAPI, HTTPException
import datetime
# from fastapi.testclient import TestClient
import cx_Oracle
app = FastAPI()


# pydantic model - taking input data from user
class Customer(BaseModel):
    ID:int
    FIRST_NAME:str
    LAST_NAME:str
    EMAIL:str
    CUSTOMER_TYPE:str
    CREATED_ON: datetime.date



def get_connection():
    conn_meta = cx_Oracle.connect(f'soumyakp/soumyakp@illin659/DMCNV',threaded=True)
    return conn_meta


@app.get("/getAllCustomers")
def read_customers():
    con = get_connection()
    print(con)
    try:

        cursor=con.cursor()

        cursor.execute(f"select * from CUSTOMER_TEST_TAB")

        con.commit()

        res=[ dict(line) for line in [zip([ column[0] for column in cursor.description], row) for row in cursor.fetchall()] ]
        print(res)
        return res

    except Exception as e:

        raise HTTPException(status_code=504, detail=str(e))

       #alternate method
        
    # # session = Session(bind=engine, expire_on_commit=False)
    # todo_list = session.query(Customers).all()
    # session.close()
    # if not todo_list:
    #     raise HTTPException(status_code=404, detail=f"customer data could not be found!")
    # return todo_list



#get method

@app.get("/getCustomerById/{id}")
def read_customer(id: int):
    # session = Session(bind=engine, expire_on_commit=False)
    customer = session.query(Customers).get(id)
    session.close()
    if not customer:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    return customer


#post method

@app.post("/addCustomer")
def add_customer(customer: Customer):
    # session = Session(bind=engine, expire_on_commit=False)

    new_customer=Customers(
        ID=customer.ID,
        FIRST_NAME=customer.FIRST_NAME,
        LAST_NAME=customer.LAST_NAME,
        EMAIL=customer.EMAIL,
        CUSTOMER_TYPE=customer.CUSTOMER_TYPE,
        CREATED_ON=customer.CREATED_ON
        )
    session.add(new_customer)
    session.commit()
    session.close()
    if not new_customer:
        raise HTTPException(status_code=404, detail=f"new customer {customer.FIRST_NAME} could not be added!")
    return new_customer


#put method

@app.put("/updateCustomer/{customerId}")
def update_customer(customerId:int,customer: Customer):
    # session = Session(bind=engine, expire_on_commit=False)

    update_customer=session.query(Customers).filter(Customers.ID==customerId).first()
    # update_customer = session.query(Customers).get(id)
    update_customer.FIRST_NAME=customer.FIRST_NAME
    update_customer.LAST_NAME=customer.LAST_NAME
    update_customer.EMAIL=customer.EMAIL
    update_customer.CUSTOMER_TYPE=customer.CUSTOMER_TYPE
    update_customer.CREATED_ON=customer.CREATED_ON
    session.commit()
    if not update_customer:
        raise HTTPException(status_code=404, detail=f"customer with id {customerId} could not be updated!")
    return update_customer


#delete method

@app.delete("/deleteCustomerById/{id}")
def delete_customer(id: int):
    # session = Session(bind=engine, expire_on_commit=False)
    customer= session.query(Customers).get(id)
    session.delete(customer)
    session.commit()
    session.close()
    if not customer:
        raise HTTPException(status_code=404, detail=f"customer with id {id} could not be deleted!")
    return customer
