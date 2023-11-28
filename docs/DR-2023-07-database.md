# Decision record 2023-07: Database

## Status

Accepted

## Context and Problem Statement

Need a data store for billing service data.

## Considered Options

1. Postgresql
2. MongoDB
3. CockroachDB

## Decision Outcome

Chose Postgresql given it's time and battle-tested usage,
popularity,
and familiarity.

Since this is more of a proof-of-concept spike,
I didn't think we needed to think about millions of users
and hundreds of services yet.
If the billing service works well with a smaller test set,
then we can consider a more scalable database like CockroachDB
which would still use the Postgres wire protocol.
We'll also have the option of a lot of experts online or elsewhere,
extensions,
and higher performance with managed services like AWS Aurora.
