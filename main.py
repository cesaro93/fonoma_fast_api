from fastapi import FastAPI
import models

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/solutions")
async def process_orders(request:models.DataRequest):
    total_revenue: float = 0
    for order in request.orders:
        if request.criterion == order.status:
            total_revenue = total_revenue + (order.quantity*order.price)

    return total_revenue