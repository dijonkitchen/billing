from decimal import Decimal
from uuid import uuid4

from billing.models.customer import Customer, create_customer
from billing.models.usage import Service, Usage, create_usage


class TestUsage:
    def test_usage_should_exist(self):
        subject = Usage()

        assert subject


class TestUsageCRUD:
    def test_create_usage_should_return_a_usage(self):
        customer = create_customer(customer=Customer(name="John Doe"))
        usage = Usage(
            id=str(uuid4()),
            customer_id=customer.id,
            service=Service.DATABASE_HOSTING,
            units_consumed=2,
            price_per_unit=3.4,
        )

        subject = create_usage(usage)

        assert isinstance(subject, Usage)
        assert subject.id == usage.id
        assert subject.customer_id == usage.customer_id
        assert subject.service == usage.service
        assert subject.units_consumed == usage.units_consumed
        assert subject.price_per_unit == usage.price_per_unit
        assert subject.created_at
        assert subject.updated_at

    def test_create_usage_should_be_idempotent(self):
        customer = create_customer(customer=Customer(name="John Doe"))
        usage = Usage(
            id=str(uuid4()),
            customer_id=customer.id,
            service=Service.DATABASE_HOSTING,
            units_consumed=0.123,
            price_per_unit=3.14159,
        )

        subject1 = create_usage(usage)
        subject2 = create_usage(usage)

        assert subject1 == subject2

    def test_create_usage_should_be_idempotent_if_same_uuid(self):
        customer = create_customer(customer=Customer(name="John Doe"))
        uuid = str(uuid4())
        usage1 = Usage(
            id=uuid,
            customer_id=customer.id,
            service=Service.DATABASE_HOSTING,
            units_consumed=0.123,
            price_per_unit=3.14159,
        )
        usage2 = Usage(
            id=uuid,
            customer_id=customer.id,
            service=Service.DATABASE_HOSTING,
            units_consumed=99999,
            price_per_unit=0.000000000001,
        )

        subject1 = create_usage(usage1)
        subject2 = create_usage(usage2)

        assert subject1 == subject2
