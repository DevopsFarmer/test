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


def main():
    app = create_app()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# fix for pylint