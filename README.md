# Biz-Scrape-Python

## Overview

**Biz-Scrape-Python** is a REST API built with **FastAPI** that scrapes business information using OpenStreetMap's Nominatim API. It allows users to find business details by specifying a business type, location (latitude/longitude + radius or city/country + radius), and returns structured business information.

## Features

- 📍 Search businesses by **latitude/longitude** + radius.
- 🌍 Search businesses by **city/country** + radius.
- 🔎 Filter results by **business type** (Hotels, Restaurants, Lawyers, etc.).
- 📦 Store business data in a database for future updates.
- 📊 Return structured JSON containing:
  - Name
  - Website (if available)
  - Email (if available)
  - Unique ID (if available from OpenStreetMap)
  - Address
  - Phone number (if available)

## Tech Stack

- **FastAPI** 🚀 (Backend Framework)
- **SQLite / PostgreSQL** (Database)
- **Nominatim API** (OpenStreetMap API for location search)
- **BeautifulSoup & Scrapy (Future)** (For scraping business websites)

## Roadmap

### **Phase 1: MVP (Minimum Viable Product)**

-

### **Phase 2: Enhanced Features**

-

### **Phase 3: Scaling & Performance**

-

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

4. **Run the FastAPI server**

```bash
    uvicorn main:app --reload
```

5. **Access API documentation**

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Contribution

Feel free to submit pull requests or open issues for suggestions and improvements. 🚀

