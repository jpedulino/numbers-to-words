build:
    docker compose build

run:
    docker compose up

test *args='':
    docker compose exec web py.test {{args}}