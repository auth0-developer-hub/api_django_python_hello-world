# Hello World API: Django + Python Sample

You can use this sample project to learn how to secure a simple Django API server using Auth0.

The `starter` branch offers a working API server that exposes three public endpoints. Each endpoint returns a different type of message: public, protected, and admin.

The goal is to use Auth0 to only allow requests that contain a valid access token in their authorization header to access the protected and admin data. Additionally, only access tokens that contain a `read:admin-messages` permission should access the admin data, which is referred to as [Role-Based Access Control (RBAC)](https://auth0.com/docs/authorization/rbac/).

[Check out the `add-authorization` branch](https://github.com/auth0-developer-hub/api_django_python_hello-world/tree/add-authorization) to see authorization in action using Auth0.

[Check out the `add-rbac` branch](https://github.com/auth0-developer-hub/api_django_python_hello-world/tree/add-rbac) to see authorization and Role-Based Access Control (RBAC) in action using Auth0.

## Get Started

Prerequisites:
    
* Python >= 3.7

Initialize a python virtual environment:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Setup virtual environments:
Copy the `.env.example` file to `.env` and edit it to populate its variables.
```bash
cp .env.example .env
```

Run the following command to generate a random secret key and add it to your `.env` file.
```bash
python manage.py generate_secret

# .env
DJANGO_SECRET_KEY=<generated_key>
```

Run DB migrations:

```bash
python manage.py migrate
```

Run the project:

```bash
gunicorn
```

## Security Configuration
### HTTP Headers
- __X-XSS-Protection__

  Default set to `0`.

  See the [documentation](https://docs.djangoproject.com/en/3.2/ref/settings/#secure-browser-xss-filter) for more details.

- __HTTP Strict Transport Security (HSTS)__

  Disabled by default, so we need to add this configuration:
  ```python
  SECURE_HSTS_INCLUDE_SUBDOMAINS = True
  SECURE_HSTS_SECONDS = 31536000
  ```

  See the [documentation](https://docs.djangoproject.com/en/3.2/ref/middleware/#http-strict-transport-security) for more details.

- __X-Frame-Options (XFO)__

  Default set to `DENY`. 

  See the [documentation](https://docs.djangoproject.com/en/3.2/ref/clickjacking/#setting-x-frame-options-for-all-responses) for more details.

- __X-Content-Type-Options__

  Default set to `nosniff`.

  See the [documentation](https://docs.djangoproject.com/en/3.2/ref/middleware/#x-content-type-options-nosniff) for more details.

- __Content-Security-Policy (CSP)__

  Not enabled by default, we need to install the `django-csp` dependency and add it to the `MIDDLEWARES`. It comes pre-configured with the directives:
    - `default-src: self`
    - `frame-ancestors: none`

  See the [documentation](https://django-csp.readthedocs.io/en/latest/configuration.html#policy-settings) for more details.

- __Cache-Control__

  We need to add a custom middleware to call `add_never_cache_headers` on all responses. This will add the header:
  
  ```
  Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private
  ```

  See the [documentation](https://docs.djangoproject.com/en/3.2/ref/utils/#django.utils.cache.add_never_cache_headers) for more details.

- __Content-Type__

  By setting the default renderer to `JSONRenderer`, it will use `utf-8` encoding by default.

  See the [documentation](https://www.django-rest-framework.org/api-guide/renderers/#jsonrenderer) for more details.

### Remove HTTP Headers

  - `X-Powered-By`: Not added by Django.
  - `Server`: There is no easy way to remove this header since it's mostly the responsibility of the environment server. On development it doesn't matter, but on production its usually `NGINX`, `Apache`, etc. which handles this header.

### CORS
Django doesn't have CORS built-in, so we need to install the `django-cors-headers` dependency and add the configuration needed on the settings.

It comes pre-configured with:
- `Access-Control-Max-Age: 86400`

See the [documentation](https://pypi.org/project/django-cors-headers) for more details.

## API Endpoints

The API server defines the following endpoints:

### 🔓 Get public message

```bash
GET /api/messages/public
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "text": "The API doesn't require an access token to share this message."
}
```

### 🔓 Get protected message

> You need to protect this endpoint using Auth0.

```bash
GET /api/messages/protected
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "text": "The API successfully validated your access token."
}
```

### 🔓 Get admin message

> You need to protect this endpoint using Auth0 and Role-Based Access Control (RBAC).

```bash
GET /api/messages/admin
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "text": "The API successfully recognized you as an admin."
}
```

## Error Handling

### 400s errors

```bash
Status: Corresponding 400 status code
```

```json
{
  "message": "Not Found"
}
```

**Request without authorization header**
```bash
curl localhost:6060/api/messages/admin
```
```json
{
  "message":"Authentication credentials were not provided.",
}
```
HTTP Status: `401`

**Request with malformed authorization header**
```bash
curl localhost:6060/api/messages/admin --header "authorization: <valid_token>"
```
```json
{
  "message":"Authentication credentials were not provided.",
}
```
HTTP Status: `401`

**Request with wrong authorization scheme**
```bash
curl localhost:6060/api/messages/admin --header "authorization: Basic <valid_token>"
```
```json
{
  "message":"Authentication credentials were not provided.",
}
```
HTTP Status: `401`

**Request without token**
```bash
curl localhost:6060/api/messages/admin --header "authorization: Bearer"
```
```json
{
  "message":"Authorization header must contain two space-delimited values",
}
```
HTTP Status: `401`

**JWT validation error**
```bash
curl localhost:6060/api/messages/admin --header "authorization: Bearer asdf123"
```
```json
{
  "message":"Given token not valid for any token type",
}
```
HTTP Status: `401`

**Token without required permissions**
```bash
curl localhost:6060/api/messages/admin --header "authorization: Bearer <token_without_permissions>"
```
```json
{
  "error":"insufficient_permissions",
  "error_description":"You do not have permission to perform this action.",
  "message":"Permission denied"
}
```
HTTP Status: `403`

### 500s errors


```bash
Status: 500 Internal Server Error
```

```json
{
  "message": "Server Error"
}
```
