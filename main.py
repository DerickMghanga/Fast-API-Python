from fastapi import FastAPI

# Create an Instance for fastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}