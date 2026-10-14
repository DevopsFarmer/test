# Create me a fast api healthcheck 
from fastapi import FastAPI

def create_healthcheck_app():
    
    app = FastAPI()

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    return app