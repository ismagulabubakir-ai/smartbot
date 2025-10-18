from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your frontend (React) to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with ["http://localhost:5173"] later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from your SmartBot backend!"}

@app.post("/chat")
def chat(message: dict):
    user_message = message.get("text", "")
    response = f"You said: {user_message}. I'm your SmartBot 🤖"
    return {"reply": response}
