import joblib
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, BaseSettings
import uvicorn
from typing import Dict, Optional


class Settings(BaseSettings):
    app_name: str = "prof"
    debug: bool = True
    host: str = ""

class InputData(BaseModel):
    height: Optional[int]
    weight: Optional[int]
    shoe_size: Optional[int]

app = FastAPI(title="prof", debug=True)

# load model at startup and store it in app.state
@app.on_event("startup")
def load_model():
     app.state.model = joblib.load("a_model.joblib")
    
@app.get("/")
async def root():
    return "Welcome to the weight predictor API"

@app.post("/predict")
async def predict(request: Request, data: InputData):
    model = app.state.model
    prediction = model.predict([[data.height, data.weight, data.shoe_size]])
    return JSONResponse(
        status_code=200,
        content={"prediction": prediction[0]},
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# the_model = joblib.load("a_model.joblib")

# prediction = the_model.predict([[190, 70, 43]])
# print(prediction)