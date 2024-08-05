# Coconut Oil Architecture

<img src="https://telegra.ph/file/9bca6e694402f0e337270.jpg" alt="memio-icon" width="600" height="600"/>

## Prerequirements

copy .env.example to .env and edit it with your data

```
cp .env.example .env
```

## Run

```
docker-compose up --build -d
```


## Functionality:

### Auth
* POST /api/v1/register/{id}: Sign up
* POST /api/v1/login: Sign in
* POST /api/v1/refresh: Refresh token

### Binary
* GET /api/v1/binary/{id}: Retrieve a specific binary by its ID.
* POST /api/v1/binary: Add a new binary.
* DELETE /api/v1/binary/{id}: Delete a binary

### Tags
* GET /api/v1/tags: Retrieve a list of all tags (with pagination).
* GET /api/v1/tags/{id}: Retrieve a specific tag by its ID.
* POST /api/v1/tags: Add a new tag.
* PUT /api/v1/tags/{id}: Update an existing tag.
* DELETE /api/v1/tags/{id}: Delete a tag

### Obj
* GET /api/v1/obj: Retrieve a list of all objs (with pagination).
* GET /api/v1/obj/{id}: Retrieve a specific obj by its ID.
* POST /api/v1/obj: Add a new obj.
* PUT /api/v1/obj/{id}: Update an existing obj.
* DELETE /api/v1/obj/{id}: Delete a obj
