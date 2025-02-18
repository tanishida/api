from fastapi import FastAPI
from pydantic import BaseModel
from services.scraping import scraping_categories
from services.scraping import scraping_image_url
import uvicorn

app = FastAPI()

class Item(BaseModel):
    url: str

@app.get("/api/v1/categories")
def read_categories():
    result = scraping_categories()
    return result

@app.post("/api/v1/image-url")
def image_url(item: Item):
    result = scraping_image_url(item.url)
    return result

if __name__ == "__main__":
  uvicorn.run("main:app", reload=True)