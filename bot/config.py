"""Configuration loading from environment variables."""

import os
from dotenv import load_dotenv


def load_config() -> dict[str, str]:
    """Load configuration from .env.bot.secret file.
    
    Returns:
        Dictionary with configuration values.
    """
    # Load environment variables from .env.bot.secret
    load_dotenv(".env.bot.secret")
    
    return {
        "BOT_TOKEN": os.getenv("BOT_TOKEN", ""),
        "LMS_API_BASE_URL": os.getenv("LMS_API_BASE_URL", ""),
        "LMS_API_KEY": os.getenv("LMS_API_KEY", ""),
        "LLM_API_KEY": os.getenv("LLM_API_KEY", ""),
    }
