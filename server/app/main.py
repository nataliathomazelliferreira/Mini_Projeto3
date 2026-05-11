from random import choice
from fastapi import FastAPI, HTTPException

def create_app():
    app = FastAPI(title="Word of the Day")

    words = [
        {
            "id": 1,
            "word": "improve",
            "translation": "melhorar",
            "example": "I want to improve my English.",
            "level": "basic"
        },
        {
            "id": 2,
            "word": "challenge",
            "translation": "desafio",
            "example": "Learning a new language is a challenge.",
            "level": "intermediate"
        },
        {
            "id": 3,
            "word": "achieve",
            "translation": "alcançar",
            "example": "You can achieve your goals with practice.",
            "level": "intermediate"
        }
    ]

    @app.get("/")
    def get_home():
        return {"Welcome to Word of the Day"}

    @app.get("/status")
    def get_status():
        return {"status": "online"}

    @app.get("/words")
    def get_words():
        return words

    @app.get("/words/random")
    def get_random_word():
        return choice(words)

    @app.get("/words/{word_id}")
    def get_word_by_id(word_id: int):
        for word in words:
            if word["id"] == word_id:
                return word

        raise HTTPException(status_code=404, detail="Palavra não encontrada")

    return app

app = create_app()