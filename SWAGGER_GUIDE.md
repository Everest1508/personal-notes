# Swagger API Documentation Guide

## Access Swagger UI

Once your Django server is running, you can access the Swagger documentation at:

- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/
- **OpenAPI JSON**: http://localhost:8000/swagger.json
- **OpenAPI YAML**: http://localhost:8000/swagger.yaml

## Using Swagger UI

### 1. Authentication

1. Go to the **Authentication** section
2. Use the **Register** or **Login** endpoint to get a JWT token
3. Copy the token from the response

### 2. Authorize in Swagger

1. Click the **Authorize** button (top right of Swagger UI)
2. In the "Bearer" field, enter your JWT token (without the word "Bearer")
3. Click **Authorize**
4. Click **Close**

Now all authenticated endpoints will use your token automatically!

### 3. Testing Endpoints

1. Click on any endpoint to expand it
2. Click **Try it out**
3. Fill in the required parameters/request body
4. Click **Execute**
5. View the response below

## Features

- ✅ **Interactive API Testing**: Test all endpoints directly from the browser
- ✅ **JWT Authentication**: Built-in support for Bearer token authentication
- ✅ **Request/Response Examples**: See example requests and responses
- ✅ **Schema Validation**: Automatic validation of request/response schemas
- ✅ **File Upload Support**: Test file uploads for voice notes and image notes

## Endpoints Documented

All API endpoints are automatically documented:

- **Authentication**: Register, Login
- **Voice Notes**: CRUD + Summarize
- **Image Notes**: CRUD
- **Text Notes**: CRUD
- **Saved URLs**: CRUD
- **Tasks**: CRUD + Carry Forward

## Tips

- Use **Swagger UI** for interactive testing
- Use **ReDoc** for a cleaner, more readable documentation view
- Export the OpenAPI schema (JSON/YAML) to import into other tools like Postman

## Example: Testing Voice Note Summarize

1. First, login to get a token and authorize
2. Create a voice note (or use an existing one)
3. Go to **Voice Notes** → **POST /api/voice-notes/{id}/summarize/**
4. Click **Try it out**
5. Enter the voice note ID
6. In the request body, enter:
   ```json
   {
     "text": "Your transcribed text here"
   }
   ```
7. Click **Execute**
8. View the generated summary!

