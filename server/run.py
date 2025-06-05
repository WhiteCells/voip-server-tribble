import uvicorn
from app import app
from app.config import Config


if __name__ == "__main__":
    uvicorn.run("app:app", 
                reload=True,
                host=Config.SERVER_HOST, 
                port=(Config.SERVER_PORT))
