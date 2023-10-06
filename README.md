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

This API exposes a single endpoint that accepts both GET and POST HTTP requests and returns a JSON response.

#### Requests using GET

 <summary><code>GET</code> <code><b>/num_to_english?number=12345678</b></code></summary>

##### Responses

> | http code | content-type               | response                                                                                                              |
> | --------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------- |
> | `200`     | `application/json`         | `{ "status": "ok", "num_in_english": "twelve million three hundred forty five thousand six hundred seventy eight" }`  |
> | `400`     | `application/json`         | `{ "status": "error", "message": "Conversion limit was exceeded. Please enter a value that has 24 digits or less." }` |
> | `400`     | `text/html; charset=utf-8` | `The 'number' parameter must have be a valid integer`                                                                 |
> | `400`     | `text/html;charset=utf-8`  | `Please provide a 'number' parameter`                                                                                 |

##### Example cURL

> ```javascript
>  curl -X GET -H "Content-Type: application/json" http://localhost:8000/num_to_english?number=12345678
> ```

#### Requests using POST

 <summary><code>POST</code> <code><b>/num_to_english</b></code></summary>

> | name     | type     | data type | description                         |
> | -------- | -------- | --------- | ----------------------------------- |
> | `number` | required | string    | The number to be converted to words |

##### Responses

> | http code | content-type               | response                                                                                                              |
> | --------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------- |
> | `200`     | `application/json`         | `{ "status": "ok", "num_in_english": "twelve million three hundred forty five thousand six hundred seventy eight" }`  |
> | `400`     | `application/json`         | `{ "status": "error", "message": "Conversion limit was exceeded. Please enter a value that has 24 digits or less." }` |
> | `400`     | `text/html; charset=utf-8` | `The 'number' parameter must have be a valid integer`                                                                 |
> | `400`     | `text/html;charset=utf-8`  | `Please provide a 'number' parameter`                                                                                 |

##### Example cURL

> ```javascript
>  curl -X POST -H "Content-Type: application/json" --data '{ "number": 12345678 }' http://localhost:8000/num_to_english
> ```

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

This app can be deployed through Vercel:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fjpedulino%2Fnumbers-to-words)
