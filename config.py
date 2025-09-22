import os

class Config:
    API_ID = int(os.getenv("API_ID","21519702" ))
    API_HASH = os.getenv("API_HASH", '20fcf051ad48130f35fe01e82f5417cd')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '7976010249:AAHX1GvKqNOuUq2QxOBqgOtzYs7yabD6l00')
