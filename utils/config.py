import os
from dotenv import load_dotenv

load_dotenv() 

PLAYER_FILE = os.getenv("PLAYER_FILE")
GAME_FILE = os.getenv("GAME_FILE")