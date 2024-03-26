from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    data_source: str = "http://data.phishtank.com/data/online-valid.csv"
    phishtank_username: str


settings = Settings()
