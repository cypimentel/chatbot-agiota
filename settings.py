from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "BillingBot"
    env: str = "dev"
    database_url: str
    redis_url: str

    messaging_adapter: str = "console"
    payment_provider: str = "mock"

    api_key: str

    class Config:
        env_file = ".env"

settings = Settings()
