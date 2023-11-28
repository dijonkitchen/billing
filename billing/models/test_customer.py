from billing.models.customer import Customer, create_customer


class TestCustomer:
    def test_customer_should_exist(self):
        subject = Customer()

        assert subject


class TestCustomerCRUD:
    def test_create_customer_should_return_a_customer(self):
        name = "Test Customer"
        customer = Customer(name=name)

        subject = create_customer(customer=customer)

        assert isinstance(subject, Customer)
        assert subject.name == name
        assert subject.id
        assert subject.created_at
        assert subject.updated_at

    def test_create_customer_should_not_use_a_given_id(self):
        id = "test id"
        name = "Test Customer"
        customer = Customer(id=id, name=name)

        subject = create_customer(customer=customer)

        assert subject.id != id
