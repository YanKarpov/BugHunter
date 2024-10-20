import os

if os.getenv('ENV') != 'production':
    from dotenv import load_dotenv
    load_dotenv()

ENV = os.getenv('ENV', 'production')

if ENV == 'development':
    TELEGRAM_TOKEN = os.getenv('DEV_BOT_TOKEN')
else:
    TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')

DATABASE_URL = os.getenv('DATABASE_URL')

if not TELEGRAM_TOKEN:
    raise ValueError(f"TELEGRAM_TOKEN is not set for {ENV} environment")