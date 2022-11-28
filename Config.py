import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25852823"))
    API_HASH = os.environ.get("API_HASH", "499699f4-1128-4658-b9d0-f0607bf5e137")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5677591277:AAFuBckIwbBUc2cxje4MKmM9pOBvRAvn1N0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIYBu1HIMljN1z0EZ0CHpq4N0rn50uZdlNbtL-_umMgtAL_6dBkRyNH0FpIczdpo1F15QRVefmEbd4Og2VkMkbjMc6WFARbARF55D5h91t3yy6k2NSAg3ODg4MHuliwLGjAQMJEp_20zdKrnTTTV4nnVOWE9ddia2Keb13JqIAGNh0p9uIlWTVBcCdbOE89ryASidxYI5G8VeLhmYLlyxhA4iN7YvU5MddViBXEl3Xpjtm1ro7j1ZXlYl6AFLVIomY8pid6BQV_LV-obAI2aOuw-gfNx1hSFe8EeJCCJUGYaJcKz6nIJjEVJQ0163gyNwruqVbARqEmmDgipxRyX-5q2drc=") 
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("OP_NJ_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "ROMEOBOT_OP") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ROMEOBOT_OP") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/74607f92f18218ae4d61e.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/261b8f5dc24de55be9bdd.jpg")
    ASSISTANT_ID = int(os.environ.get("5127230582")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
