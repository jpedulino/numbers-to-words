# numbers-to-words

Simple API to convert numbers into words

## Project Setup

The requirements to run this API are:

- [Just a command runner](https://github.com/casey/just)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose (included with Docker)](https://docs.docker.com/get-docker/)

Make sure you have a copy of the .env.example (without the .example suffix) with the proper variables.

To have the project up and running with docker, simply run:

```bash
just build
```

After that, you can run the project with:

```bash
just run
```

## Features

This API exposes a single endpoint that accepts GET and POST HTTP requests.

## Testing

To execute the tests:

```bash
just test
```

The command accepts arguments and it is using pytest. If you need to run a single test file, for example:

```bash
just test converter/tests/test_english_conversion_service.py
```

## Deploy
