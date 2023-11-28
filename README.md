# Cloud billing service and client

## Setup and install

* Homebrew: https://brew.sh/
* pyenv: https://github.com/pyenv/pyenv#installation
* Poetry: https://python-poetry.org/docs/#installing-with-the-official-installer
* Docker: https://www.docker.com/

## Development

### Activate virtual environment:

```bash
poetry shell
```

### Exit virtual environment:

```bash
exit
```

### Install dependencies:

```bash
make install
```

To add new dependencies:
```bash
poetry add <dependency>
```

### Run server

```bash
make server
```

See API docs at http://localhost:8000/docs

### Teardown containers

```bash
make teardown
```

### Run tests

```bash
make test
```

### Database

#### Create migration

```bash
alembic revision -m "migration name"
```

#### Run migrations

```bash
alembic upgrade head
```

## Future considerations TODO

- [ ] Setup for configurable environment variables
- [ ] Add logging
- [ ] Add monitoring
- [ ] Add metrics
- [ ] Create table for normalized services
- [ ] Productionalize server and database for performance and async
- [ ] Containerize server
- [ ] Add customer authentication
- [ ] Add customer authorization
- [ ] Add customer rate limiting
- [ ] Potentially separate request and response schemas for even tigher type validation
- [ ] Linting
- [ ] Formatting
- [ ] Type checking
- [ ] Pre-commit hooks
- [ ] Continuous integration with test coverage
- [ ] Continuous deployment
- [ ] Consider NoSQL or NewSQL database like CockroachDB for more horizontal scalability
- [ ] Remove customers table if not needed as part of a larger cloud prvoider organization which likely already has customer stored somewhere
- [ ] Integration tests for billing service
- [ ] Retry logic in client SDK
- [ ] Improve exception handling and error messages
