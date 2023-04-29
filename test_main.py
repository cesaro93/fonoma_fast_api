from fastapi.testclient import TestClient
from main import app
import models

client = TestClient(app)

# Test data
def test_data_example():    
    data_request: models.DataRequest = {
    "orders": [
        {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
        {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
        {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
        {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
    ],
    "criterion": "completed"
    }

    data_response = 1299.69

    response = client.post("/solutions", json=data_request)
    assert response.status_code == 200
    assert response.json() == data_response

# Test data with incorrect criterion
def test_incorrect_criterion():    
    data_request: models.DataRequest = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"}
        ],
        "criterion": "okkk"
    }

    data_response = {
        "detail": [
            {
            "loc": [
                "body",
                "criterion"
            ],
            "msg": "unexpected value; permitted: 'completed', 'pending', 'canceled'",
            "type": "value_error.const",
            "ctx": {
                "given": "okkk",
                "permitted": [
                "completed",
                "pending",
                "canceled"
                ]
            }
            }
        ]
    }

    response = client.post("/solutions", json=data_request)
    assert response.status_code == 422
    assert response.json() == data_response

# Test data with incorrect order id
def test_incorrect_order():    
    data_request: models.DataRequest = {
        "orders": [
            {"id": -1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"}
        ],
        "criterion": "completed"
    }

    data_response = {
        "detail": [
            {
            "loc": [
                "body",
                "orders",
                0,
                "id"
            ],
            "msg": "ensure this value is greater than 0",
            "type": "value_error.number.not_gt",
            "ctx": {
                "limit_value": 0
            }
            }
        ]
    }

    response = client.post("/solutions", json=data_request)
    assert response.status_code == 422
    assert response.json() == data_response

