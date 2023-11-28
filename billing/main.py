from fastapi import FastAPI

from billing.models.customer import Customer, create_customer
from billing.models.usage import Service, Usage, create_usage

app = FastAPI()


@app.post("/customers")
async def create_new_customer(customer: Customer) -> Customer:
    return create_customer(customer=customer)


@app.post("/usages")
async def create_new_usage(
    usage: Usage,
) -> Usage:
    return create_usage(usage=usage)
