import requests
from pydantic import BaseModel
from typing import Optional

class RandomGeneratorInput(BaseModel):
    height: Optional[int]
    weight: Optional[int]
    shoe_size: Optional[int]

url = "http://localhost:8000/predict"
data = RandomGeneratorInput(height = 181, weight = 80, shoe_size = 44).dict()

response = requests.post(url, json=data)
print(response.json())