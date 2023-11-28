from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import cast

from sqlalchemy.exc import IntegrityError
from sqlmodel import Field, Session, SQLModel

from billing.database import engine


class Service(str, Enum):
    """Cloud services that can be billed for."""

    DATABASE_HOSTING = "Database Hosting"
    LOAD_BALANCER = "Load Balancer"
    LINUX_INSTANCE = "Linux Instance"
    CDN_STORAGE = "CDN Storage"
    DOMAIN_NAME_REGISTRATION = "Domain Name Registration"


class Usage(SQLModel, table=True):
    """Usage of a cloud service by a customer."""

    id: str = Field(primary_key=True)
    customer_id: str = Field(foreign_key="customer.id")
    service: Service
    units_consumed: int
    price_per_unit: Decimal
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


def create_usage(
    usage: Usage,
) -> Usage:
    with Session(engine) as session:
        try:
            session.add(usage)
            session.commit()
            session.refresh(usage)

            return usage
        except IntegrityError:
            session.rollback()
            query = session.query(Usage).filter(Usage.id == usage.id)

            return cast(Usage, query.first())
