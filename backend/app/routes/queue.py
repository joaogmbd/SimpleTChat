from fastapi import APIRouter

router = APIRouter()

@router.post("/join")
async def join_queue(username: str):
    # Adicionar usuário à fila (lógica real substituirá isso)
    return {"message": f"{username} joined the queue"}

@router.get("/pair")
async def pair_users():
    # Emparelhar dois usuários disponíveis
    return {"message": "Pairing users..."}
