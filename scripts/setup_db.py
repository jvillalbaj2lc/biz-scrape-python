import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.database import init_db

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Database setup complete!")
