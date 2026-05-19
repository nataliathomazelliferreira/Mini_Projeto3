from random import choice
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from server.app.data import words

def create_app():
    app = FastAPI(title="Word of the Day API")

    @app.get("/", response_class=HTMLResponse)
    def get_home():
        word = choice(words)

        return f"""
        <html>
            <head>
                <title>Word of the Day</title>

                <style>
                    body {{
                        background-color: #f4f4f4;
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }}

                    .card {{
                        background-color: white;
                        padding: 40px;
                        border-radius: 12px;
                        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                        width: 500px;
                    }}

                    h1 {{
                        color: #333333;
                        margin-bottom: 20px;
                    }}

                    h2 {{
                        color: #4a90e2;
                        margin-bottom: 20px;
                    }}

                    p {{
                        color: #555555;
                        font-size: 18px;
                    }}
                </style>
            </head>

            <body>
                <div class="card">
                    <h1>Word of the Day</h1>

                    <h2>{word["word"]}</h2>

                    <p>
                        <strong>Translation:</strong>
                        {word["translation"]}
                    </p>

                    <p>
                        <strong>Example:</strong>
                        {word["example"]}
                    </p>

                    <p>
                        <strong>Level:</strong>
                        {word["level"]}
                    </p>
                </div>
            </body>
        </html>
        """

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

        raise HTTPException(
            status_code=404,
            detail="Word not found"
        )

    return app

app = create_app()