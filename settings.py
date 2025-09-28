from pydantic_settings import BaseSettings
from pydantic import StrictStr

class BotSettings(BaseSettings):
    # Проверяем, что bot_token != None
    bot_token: StrictStr = "token" 

    class Config:
        env_file = ".env"
