# Create me a fast api healthcheck 
from fastapi import FastAPI

def create_healthcheck_app():
    
    app = FastAPI()

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    return app

def create_app():
    app = FastAPI()
    healthcheck_app = create_healthcheck_app()
    app.mount("/health", healthcheck_app)
    return app


