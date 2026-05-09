from fastapi import FastAPI

def create_app():
    app = FastAPI(title="Mini Projeto 3 API")

    return app

app = create_app()