from fastapi import FastAPI

def create_app():
    app = FastAPI(title="Mini Projeto 3")

    @app.get("/status")
    def get_status():
        return {"status": "online"}

    return app

app = create_app()