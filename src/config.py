"""
Configuration module for SportEval Pro
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Base configuration"""
    
    # Project paths
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / "data"
    LOGS_DIR = BASE_DIR / "logs"
    
    # Create directories if they don't exist
    DATA_DIR.mkdir(exist_ok=True)
    LOGS_DIR.mkdir(exist_ok=True)
    
    # Application
    APP_NAME = os.getenv("APP_NAME", "SportEval Pro")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    DEBUG = os.getenv("APP_DEBUG", "False").lower() == "true"
    
    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{DATA_DIR / 'database.db'}"
    )
    
    # Server
    SERVER_HOST = os.getenv("SERVER_HOST", "127.0.0.1")
    SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    JWT_SECRET = os.getenv("JWT_SECRET", "dev-jwt-secret")
    
    # Features
    ENABLE_AI = os.getenv("ENABLE_AI", "False").lower() == "true"
    ENABLE_CLOUD_SYNC = os.getenv("ENABLE_CLOUD_SYNC", "False").lower() == "true"
    ENABLE_MOBILE_API = os.getenv("ENABLE_MOBILE_API", "False").lower() == "true"
    
    # Cloud services
    GOOGLE_DRIVE_CREDENTIALS = os.getenv("GOOGLE_DRIVE_CREDENTIALS")
    ONEDRIVE_API_KEY = os.getenv("ONEDRIVE_API_KEY")
    
    # AI services
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = LOGS_DIR / os.getenv("LOG_FILE", "app.log")


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration"""
    DATABASE_URL = "sqlite:///:memory:"
    DEBUG = True


# Select configuration based on environment
ENV = os.getenv("ENVIRONMENT", "development")
config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

CONFIG = config_map.get(ENV, DevelopmentConfig)
