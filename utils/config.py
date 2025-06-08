# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Esto se ejecuta solo una vez al importar

PLAYER_FILE = os.getenv("PLAYER_FILE")
GAME_FILE = os.getenv("GAME_FILE")