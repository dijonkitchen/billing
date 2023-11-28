# Decision record 2023-07: Server

## Status

Accepted

## Context and Problem Statement

Given the need to create a cloud provider's billing service,
we needed to have a spike to make a proof of concept.

## Considered Options

1. Use Python and FastAPI
2. Use Go and a microframework
3. Use Typescript and Express, Remix, NestJS, RedwoodJS, or Next.js
4. Use Ruby on Rails

## Decision Outcome

Chose Python and FastAPI given it's
broad and popular ecosystem, that should allow it to be easily extended to other domains,
my familiarity with it,
it's ability to complete the task at hand with ease, simplicity, and performance.

Python has precision with Decimal types that is useful for dealing with money values.
The Javascript/Typescript ecosystem is good, but lacks this.

Go could be more performant,
but I'm less familiar with it
and it might be too low-level for this proof-of-concept spike.

Ruby on Rails would be really quick too and covers previously mentioned points,
but might not be as performant or as extensible as Python and FastAPI.
Similar to Django,
I thought a full-stack framework might be too heavy
for this billing service as it'd be just used as a back-end API.
