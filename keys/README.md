# Keys Directory

This directory is used to store sensitive API keys and service account credentials. The contents of this directory are **not** tracked by Git.

## Structure

```
keys/
├── google/
│   └── service-account.json  # Google service account key file
└── README.md                # This file
```

## Setting Up Google Places API Keys

### Option 1: API Key (Development/Testing)

1. Get your API key from the [Google Cloud Console](https://console.cloud.google.com/)
2. Copy `.env.example` to `.env` in the project root
3. Add your API key to the `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

### Option 2: Service Account (Recommended for Production)

1. Create a service account in the [Google Cloud Console](https://console.cloud.google.com/)
2. Download the JSON key file
3. Place the file in `keys/google/` as `service-account.json`
4. Update your `.env` file:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=keys/google/service-account.json
   ```

## Security Notes

- Never commit keys to version control
- Keep your API keys and service account files secure
- Regularly rotate your keys and credentials
- Use different keys for development and production
- Consider using a secrets management service in production 