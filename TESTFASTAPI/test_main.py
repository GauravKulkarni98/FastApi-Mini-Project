from main import app
from fastapi.testclient import TestClient


client = TestClient(app)

data = {
  "ID": 108,
  "EMAIL": "Demo1",
  "LAST_NAME": "Demo1",
  "CREATED_ON": "12-APR-16",
  "CUSTOMER_TYPE": "New",
  "FIRST_NAME": "Demo1"
}

def test_read_customer():
    response = client.get("/getCustomerById/107",json=data)
    assert response.status_code == 200
    # assert response.json() == data
    # print(response)

def test_read_customers():
    response = client.get("/getAllCustomers")
    assert response.status_code == 200

def test_add_customer():
    response = client.post("/addCustomer")
    assert response.status_code == 200

def test_update_customer():
    response = client.put("/updateCustomer/108")
    assert response.status_code == 200

def test_delete_customer():
    response = client.get("/deleteCustomerById/106")
    assert response.status_code == 200
