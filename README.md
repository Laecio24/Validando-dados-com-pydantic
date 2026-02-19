# Validando Dados com Pydantic

Este repositório contém as atividades de refatoração de modelos e criação de API com validação.

## Atividades

### 1. Refatoração de Dicionário
- **Arquivo:** `activity_1_creature.py`
- Refatoração de um dicionário comum para um modelo `BaseModel` do Pydantic.

### 2. Quebrando o Modelo (ValidationErrors)
- **Arquivo:** `activity_2_test.py`
- **Erro de Tipo:** Ocorreu ao enviar uma `list` para o campo `description` (esperava `str`). O Pydantic retornou `Input should be a valid string`.
- **Erro de Valor:** Ocorreu ao enviar uma string com mais de 15 caracteres. O Pydantic retornou `String should have at most 15 characters`.

### 3. Validando um Endpoint (FastAPI)
- **Arquivo:** `activity_3_main.py`
- Rota POST que valida `uname` (mín. 3 chars) e `email` (formato válido).
- Salva os dados automaticamente no arquivo `users.json`.

## Como executar
1. Instale as dependências: `pip install fastapi uvicorn "pydantic[email]"`
2. Execute a API: `uvicorn activity_3_main:app --reload`
3. Teste via: `http://127.0.0.1:8000/docs`