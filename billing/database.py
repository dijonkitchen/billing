from sqlmodel import create_engine

DATABASE_URL = "postgresql://postgresuser:longpassphrase@localhost:5432/billingdb"

engine = create_engine(DATABASE_URL)
