from fastapi import FastAPI
from app.api.endpoints import router


app = FastAPI(title="FastAPI LangChain API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run(app, host="127.0.0.1", port=8000)
