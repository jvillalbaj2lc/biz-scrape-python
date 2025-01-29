# Google API Keys

This directory is for storing Google Places API credentials. You'll need either an API key or a service account key file to use the application.

## Required Files

Place one of the following in this directory:

1. `service-account.json` - Service account key file (recommended for production)
   ```json
   {
     "type": "service_account",
     "project_id": "your-project-id",
     "private_key_id": "key-id",
     "private_key": "-----BEGIN PRIVATE KEY-----\n.....\n-----END PRIVATE KEY-----\n",
     "client_email": "your-service-account@your-project.iam.gserviceaccount.com",
     "client_id": "client-id",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account%40your-project.iam.gserviceaccount.com"
   }
   ```

## How to Get the Credentials

### Service Account (Recommended for Production)

1. Go to the [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select an existing one
3. Enable the Places API for your project
4. Go to "IAM & Admin" > "Service Accounts"
5. Click "Create Service Account"
6. Fill in the details and grant appropriate roles (usually "Places API User")
7. Create a new key (JSON format)
8. Download and save the JSON file as `service-account.json` in this directory

### API Key (Alternative for Development)

If you're using an API key instead:
1. Go to the [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select an existing one
3. Enable the Places API for your project
4. Go to "APIs & Services" > "Credentials"
5. Click "Create Credentials" > "API Key"
6. Copy the key and add it to your `.env` file

## Security Notes

- Never commit these files to version control
- Restrict API key usage by IP and API in Google Cloud Console
- Use different credentials for development and production
- Regularly rotate your credentials
- Consider using environment variables for maximum security 