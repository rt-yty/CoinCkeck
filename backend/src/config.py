from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    CMC_API_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env")
    
    def __init__(self) -> None:
        super().__init__()

settings = Settings()

