from pydantic import BaseModel, conint, confloat
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class Order(BaseModel):
    id: conint(strict=True, gt=0)
    item: str
    quantity: conint(strict=True, gt=0)
    price: confloat(strict=True, gt=0)
    status: Literal['completed', 'pending', 'canceled']
    
class DataRequest(BaseModel):
    orders: list[Order]
    criterion: Literal['completed', 'pending', 'canceled']