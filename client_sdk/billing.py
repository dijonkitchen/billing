import httpx

from billing.models.usage import Service

BILLING_BASE_URL = "http://localhost:8000"


def create_customer(name: str):
    return httpx.post(f"{BILLING_BASE_URL}/customers", json=dict(name=name))


def create_usage(
    idempotency_key: str,
    customer_id: str,
    service: Service,
    units_consumed: int,
    price_per_unit: str | float,
):
    return httpx.post(
        f"{BILLING_BASE_URL}/usages",
        json=dict(
            id=idempotency_key,
            customer_id=customer_id,
            service=service,
            units_consumed=units_consumed,
            price_per_unit=price_per_unit,
        ),
    )
