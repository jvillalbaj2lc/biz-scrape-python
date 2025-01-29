# Biz-Scrape-Python

## Overview

**Biz-Scrape-Python** is a REST API built with **FastAPI** that scrapes business information using Google Places API. It allows users to find business details by specifying a business type, location (latitude/longitude + radius), and returns structured business information.

## Features

- 📍 Search businesses by **latitude/longitude** + radius
- 🔎 Filter results by **business type** (Hotels, Restaurants, Lawyers, etc.)
- 📦 Store business data in a database for future updates
- 📊 Return structured JSON containing:
  - Name
  - Website (if available)
  - Email (if available)
  - Place ID
  - Address
  - Phone number (if available)
  - Rating and reviews
  - Opening hours

## Prerequisites

Before running the application, you'll need:
1. Python 3.8 or higher
2. Google Places API credentials (see [API Keys Setup](#api-keys-setup))
3. pip or another package manager

## API Keys Setup

This project requires Google Places API credentials to function. We support two authentication methods:

1. **API Key** (simpler, good for development)
2. **Service Account** (more secure, recommended for production)

The project includes a `keys` directory structure for managing these credentials:
```
keys/
├── google/
│   ├── service-account.json  # Your Google service account key (if using service account)
│   └── README.md            # Detailed setup instructions
└── README.md                # General keys management info
```

Follow these steps to set up your credentials:

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Choose your authentication method:
   - For API Key: Add your key to `.env`
   - For Service Account: Place your JSON key file in `keys/google/`

Detailed setup instructions can be found in:
- `keys/README.md` - General credentials management
- `keys/google/README.md` - Google-specific setup instructions

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/biz-scrape-python.git
   cd biz-scrape-python
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API credentials** (see [API Keys Setup](#api-keys-setup))

5. **Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access API documentation**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Security Notes

- Never commit API keys or service account files to version control
- Use different credentials for development and production
- Regularly rotate your credentials
- Consider using a secrets management service in production

## Contributing

Feel free to submit pull requests or open issues for suggestions and improvements. 🚀

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

