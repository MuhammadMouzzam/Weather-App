from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    token : str
    class config:
        env_file = '.env'
    
settings = Settings()