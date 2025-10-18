from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai.summarizer import process_candidate

app = FastAPI()

vacancy = {
    "город": "Алматы",
    "опыт": 3,
    "образование": "бакалавр",
    "языки": ["английский", "русский"],
    "формат": "полный день",
    "зарплата": 500000,
    "описание": "Ищем backend-разработчика с опытом работы с Python и FastAPI."
}
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
    if user_message:
        summary = process_candidate(vacancy, user_message)
        ai_reply = ""
        for question in summary["questions"]:
            ai_reply += question
    else:
        ai_reply = f"You said: {user_message}. I'm your SmartBot 🤖"
    return {"reply": ai_reply}
