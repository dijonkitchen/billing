from datetime import datetime
from uuid import uuid4

from sqlmodel import Field, Session, SQLModel

from billing.database import engine


def str_uuid4() -> str:
    return str(uuid4())


class Customer(SQLModel, table=True):
    id: str = Field(primary_key=True, default_factory=str_uuid4)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


def create_customer(customer: Customer) -> Customer:
    customer.id = str_uuid4()

    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)

        return customer
