from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class ApiV1Prefix(BaseModel):
    prefix: str = '/users'
    users: str = '/users'


class ApiPrefix(BaseModel):
    prefix: str = '/api'
    v1: ApiV1Prefix = ApiV1Prefix()

class AuthJWT(BaseModel):
    private_key_path : Path = BASE_DIR / "certs" / "jwt_key"
    public_key_path : Path = BASE_DIR / "certs" / "jwt_key.pub"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15

class DatabaseConfig(BaseModel):
    url: PostgresDsn = "postgresql+asyncpg://user:password@localhost:5432/shop"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 10
    max_overflow: int = 50

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("C:/Users/takeb/TypingTest/Backend/app/.env"),
        case_sensitive=False,
        env_nested_delimiter='__',
        env_prefix='TYPETEST__',
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig
    auth_jwt: AuthJWT = AuthJWT()

settings = Settings()
print(settings.db.echo)