# Postman Collection Setup Guide

## Import the Collection

1. Open Postman
2. Click **Import** button (top left)
3. Select the file: `Personal_Notes_API.postman_collection.json`
4. The collection will be imported with all endpoints

## Environment Variables

The collection uses two variables:

1. **`base_url`** - Default: `http://localhost:8000`
   - Change this if your server runs on a different URL/port

2. **`jwt_token`** - Auto-populated after login
   - The Login request automatically saves the token to this variable
   - All other requests use this token for authentication

## Setup Steps

### 1. Set Base URL (if needed)
- Click on the collection name
- Go to **Variables** tab
- Update `base_url` if your server is not running on `http://localhost:8000`

### 2. Register a New User
- Go to **Authentication** → **Register**
- Update the email/password in the request body
- Click **Send**
- Save the token from the response

### 3. Login (Auto-saves Token)
- Go to **Authentication** → **Login**
- The token is automatically saved to `jwt_token` variable
- All subsequent requests will use this token

### 4. Use Other Endpoints
- All endpoints in the collection are ready to use
- JWT token is automatically included in the Authorization header
- Update IDs in URLs (replace `1` with actual IDs from your database)

## Endpoints Included

### Authentication
- ✅ Register
- ✅ Login (auto-saves token)

### Voice Notes
- ✅ Create (with file upload)
- ✅ Get All
- ✅ Get Single
- ✅ Update
- ✅ Delete
- ✅ Summarize (with text input)

### Image Notes
- ✅ Create (with file upload)
- ✅ Get All
- ✅ Get Single
- ✅ Update
- ✅ Delete

### Text Notes
- ✅ Create
- ✅ Get All
- ✅ Get Single
- ✅ Update
- ✅ Delete

### Saved URLs
- ✅ Create
- ✅ Get All
- ✅ Get Single
- ✅ Update
- ✅ Delete

### Tasks
- ✅ Create
- ✅ Get All
- ✅ Get Single
- ✅ Update
- ✅ Delete
- ✅ Carry Forward (move incomplete tasks to next day)

## Notes

- **File Uploads**: For voice notes and image notes, select a file in the form-data body
- **Date Format**: Use `YYYY-MM-DD` format (e.g., `2025-12-03`)
- **Authentication**: Login endpoint automatically saves the JWT token for all other requests
- **IDs**: Replace `1` in URLs with actual IDs from your database

## Testing the API

1. Start your Django server:
   ```bash
   python manage.py runserver
   ```

2. Import the collection in Postman

3. Register/Login to get a token

4. Test any endpoint!

