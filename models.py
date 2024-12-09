from datetime import datetime
from pydantic import BaseModel, Field


class BaseInfo(BaseModel):
    id: int = Field(..., title="Id")
    username: str = Field(..., title="Username")
    age: int = Field(..., title="Age")
    cellphone: str = Field(..., title="CellPhone")

    class Config:
        extra = 'allow'

    @classmethod
    def get_template_name(cls):
        return "BaseInfo"


class EmailInfo(BaseInfo):
    email: str = Field(..., title="Email")
    username: str = Field(..., title="Username", min_length=3)
    password: str = Field(..., title="Password", min_length=8)
    register_date: datetime = Field(..., title="RegisterDate")

    class Config:
        extra = 'allow'

    @classmethod
    def get_template_name(cls):
        return "EmailInfo"


class User(BaseModel):
    username: str = Field(..., title="Name")
    usersurname: str = Field(..., title="Surname")
    bdate: datetime = Field(..., title="Birthday date")
    issubscriber: bool = Field(..., title="IsSubcriber")

    class Config:
        extra = 'allow'

    @classmethod
    def get_template_name(cls):
        return "UserInfo"

class Order(BaseModel):
    order_id: int = Field(..., title="OrderId")
    email: str = Field(..., title="Email")
    product_name: str = Field(..., title="product_name")
    quantity: int = Field(..., title="quantity")

    class Config:
        extra = 'allow'

    @classmethod
    def get_template_name(cls):
        return "OrderInfo"