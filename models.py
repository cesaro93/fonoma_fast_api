from pydantic import BaseModel, conint, confloat
from typing import Literal, List

class Order(BaseModel):
    id: conint(strict=True, gt=0)
    item: str
    quantity: conint(strict=True, gt=0)
    price: confloat(strict=True, gt=0)
    status: Literal['completed', 'pending', 'canceled']
    
class DataRequest(BaseModel):
    orders: List[Order]
    criterion: Literal['completed', 'pending', 'canceled']