from fastapi import FastAPI
import models
from config import engine
from routes import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    '*',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

models.Base.metadata.create_all(bind = engine)




@app.get("/api")
def hello():
    return "Hello"  

app.include_router(router, prefix="/book", tags=["book"])