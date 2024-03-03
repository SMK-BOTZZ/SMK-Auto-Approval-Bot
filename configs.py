# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28243586"))
    API_HASH = getenv("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = getenv("BOT_TOKEN", "6812106698:AAGtDaint6SnowdD8tvgIEktg6Q-hzzhg50")
    FSUB = getenv("FSUB", "SMK_NETWORK")
    CHID = int(getenv("CHID", "-1002001054562"))
    SUDO = list(map(int, getenv("SUDO", "6168162777").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://madarazbotz:ZbVCR4tEzvjolZTj@cluster0.gfqwloi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
