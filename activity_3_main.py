from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import json
import os

app = FastAPI()

# 1. Definição do Modelo User
class User(BaseModel):
    uname: str = Field(min_length=3)
    email: EmailStr
    full_name: Optional[str] = None

# Lista em memória
users_list: list[User] = []
FILE_PATH = "users.json"

@app.post("/users")
async def create_user(user: User):
    # Adiciona na lista
    users_list.append(user)
    
    # Salva no arquivo JSON
    with open(FILE_PATH, "w") as f:
        # Converte a lista de objetos Pydantic para lista de dicts
        json_data = [u.model_dump() for u in users_list]
        json.dump(json_data, f, indent=4)
    
    return {"message": "Usuário criado com sucesso", "user": user}

# Rodar com: uvicorn activity_3_main:app --reload