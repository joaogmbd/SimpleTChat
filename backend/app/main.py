from fastapi import FastAPI
from app.routes import auth, queue, chat

app = FastAPI(title="Temporary Chat API")

# Register routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(queue.router, prefix="/queue", tags=["Queue"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Temporary Chat API!"}
