from decimal import Decimal
from uuid import uuid4

from billing.models.usage import Service
from client_sdk.billing import create_customer, create_usage


class TestBillingClientSDK:
    def test_create_customer_should_return_a_customer(self):
        name = "John Doe"

        subject = create_customer(name=name).json()

        assert subject["name"] == name
        assert subject["id"]
        assert subject["created_at"]
        assert subject["updated_at"]

    def test_create_usage_should_return_a_usage(self):
        customer = create_customer(name="John Doe").json()
        inputs = dict(
            idempotency_key=str(uuid4()),
            customer_id=customer["id"],
            service=Service.DATABASE_HOSTING,
            units_consumed=2,
            price_per_unit=3.4,
        )

        subject = create_usage(**inputs).json()

        assert subject["id"] == inputs["idempotency_key"]
        assert subject["customer_id"] == inputs["customer_id"]
        assert subject["service"] == inputs["service"]
        assert subject["units_consumed"] == inputs["units_consumed"]
        assert subject["price_per_unit"] == float(
            Decimal(inputs["price_per_unit"]).quantize(Decimal("1.00"))
        )
        assert subject["created_at"]
        assert subject["updated_at"]
