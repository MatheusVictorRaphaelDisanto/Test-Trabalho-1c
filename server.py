# server.py - Servidor simples para testar
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    model: str
    timestamp: str

@app.get("/")
def root():
    return {"message": "✅ Servidor Python está RODANDO!", "status": "online"}

@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/api/v1/chat")
def chat(request: ChatRequest):
    print(f"📨 Mensagem recebida: {request.message}")
    
    # Resposta de teste
    resposta = f"🤖 **CLANS BOT RESPONDE**: Você disse: '{request.message}'. Esta é uma resposta de teste do servidor Python!"
    
    return ChatResponse(
        reply=resposta,
        model="python-test",
        timestamp=datetime.now().isoformat()
    )

if __name__ == "__main__":
    import uvicorn
    print("🚀 SERVIDOR INICIADO!")
    print("📍 Acesse: http://localhost:8000")
    print("📍 Health: http://localhost:8000/health")
    uvicorn.run(app, host="0.0.0.0", port=8000)