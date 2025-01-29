from fastapi import FastAPI
from app.api.v1.endpoints import business

app = FastAPI(title="Biz Scrape API", version="1.0")

# Include routers
app.include_router(business.router, prefix="/businesses", tags=["Business"])

@app.get("/")
def root():
    return {"message": "Biz Scrape API is running!"}
