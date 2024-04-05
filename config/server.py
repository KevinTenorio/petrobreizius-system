import os
from dotenv import load_dotenv

load_dotenv()

port: int = int(os.getenv('DB_PORT') or 5432)
