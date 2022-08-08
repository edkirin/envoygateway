# Envoy Gateway POC

## Overview

### Unprotected route

```mermaid
sequenceDiagram
    participant client as Client
    participant gateway as Envoy Proxy Gateway :10000
    participant service as Pinger Service :8000
    participant jwks_provider as JWKS Provider :8010
    client->>gateway: GET Unprotected Resource
        activate gateway
        gateway->>service: GET Unprotected
        deactivate gateway
        activate service
        service->>gateway: Response
        deactivate service
        activate gateway
        gateway->>client: Response
        deactivate gateway
```

### Protected route

```mermaid
sequenceDiagram
    participant client as Client
    participant gateway as Envoy Proxy Gateway :10000
    participant service as Pinger Service :8000
    participant jwks_provider as JWKS Provider :8010
    client->>gateway: GET Protected Resource
        activate gateway
        gateway->>jwks_provider: GET JWT Keys [cached]
        deactivate gateway
        activate jwks_provider
        jwks_provider->>gateway: JWT Keys
        deactivate jwks_provider
        activate gateway
        gateway->>gateway: Check JWT Token
        gateway->>service: GET Protected
        deactivate gateway
        activate service
        service->>gateway: Response
        deactivate service
        activate gateway
        gateway->>client: Response
        deactivate gateway
```


## Installation

```sh
make build-all
```

## Run
```sh
docker-compose up
```

## Tests

**Note**: Make yourself a favor and use [httpie](https://httpie.io/cli) instead of curl

### Protected route

```sh
http http://localhost:10000/pinger-service/protected Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.b34h75BHF04QKEMBiiKZ1H8vVJMBWv3JybA9LT-GF9s"
```

```sh
http http://localhost:10000/pinger-service/protected/ping Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.b34h75BHF04QKEMBiiKZ1H8vVJMBWv3JybA9LT-GF9s"
```

### Unprotected route

```sh
http http://localhost:10000/pinger-service/unprotected
```

```sh
http http://localhost:10000/pinger-service/unprotected/pong
```


## Docs

- Envoy Proxy:
  - [JWT Authentication](https://www.envoyproxy.io/docs/envoy/v1.23.0/configuration/http/http_filters/jwt_authn_filter.html?highlight=local_jwks)

- JWKS:
  - [How to generate a JSON Web Key](https://connect2id.com/products/nimbus-jose-jwt/examples/jwk-generation)

## Tools

- [Create token with jwt.io](https://jwt.io)
  - When creating token, set *secret base64 encoded*
