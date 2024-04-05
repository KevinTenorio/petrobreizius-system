from fastapi import FastAPI
import uvicorn
from config.server import port

from controllers import routes

app = FastAPI(title="Sisteminha do Sr. Petrobreizius")

for router in routes:
    app.include_router(router)

@app.get("/", tags=["Root"], summary='Root endpoint')
def read_root():
    return {"message": "Go to http://127.0.0.1:8000/docs to see the API documentation."}

if __name__ == "__main__":
    uvicorn.run(app='main:app', reload=True, port=8000)

