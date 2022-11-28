import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "25852823"))
    API_HASH = os.environ.get("API_HASH", "499699f4-1128-4658-b9d0-f0607bf5e137")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5677591277:AAFuBckIwbBUc2cxje4MKmM9pOBvRAvn1N0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGcBuy7r31gWcZ6fvmmetlvpTtR9-P96C4wvcrz2jkAuibhQu7cXCk4-dPgTYgDtgiZtCGHxLeIQFBRpgkU5xZ4E8OtNO5lGlUnoc4aU2J5SANuLL5PB0PcybuHXD220qxJHvd0zhoH5o3LW0Jh_Wg037RL0bpDOcaRjAo2l8lRj5uqzSYoOKH2CpqAS8KDC_XhUr8o1I3f4CQ2pBkMybUzlk4QgN08qYaOFzlCx9lcGFuE09iHAP7LZ-Y55iRJe_-EuWNdpzmMK2uFad8TfGrfpNrWJWTiQoBew0QsLknX4uTwG6GPrN6tB9gUhQ5C5sQWg_DLTbSZAcQkyCYIauguxlPo=")#pastw string session 
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
