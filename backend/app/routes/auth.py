from fastapi import APIRouter, HTTPException
from app.services.email_service import send_email
from app.services.username_service import generate_username

router = APIRouter()

@router.post("/register")
async def register(email: str):
    # Gerar nome de usuário e senha temporária
    username = generate_username()
    password = "TempPass123!"  # Substituir por geração segura

    # Simular envio de e-mail (substituir por lógica SES real)
    send_email(email, username, password)

    return {"message": "Check your email for username and password."}

@router.post("/login")
async def login(username: str, password: str):
    # Validação fictícia (substituir por lógica real)
    if username == "valid_user" and password == "TempPass123!":
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
