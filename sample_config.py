import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6577956480:AAHEZpz7dKXWqaMXjO8jhJRngV8Dyn6Msek")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "19667863"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "94b097998834f20d21e5fed8a1586c18")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5123039648").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "Delete User Bot")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "BQEsG5cAuELcD60gt5HBp-ld38zWsxe26O0CFo6i34BVzQW5XYxdxrOSF1g6tsFe_WtxWTghifKEl7tI9B4eV51wzacu8JdDenj--ghkZEjraZ6_RJmCsu6gReczSA1gK65ndtT-yRwOoX7q-V4UcSIJbr6N26f4BxF-_sWVxxunPFariISTJW7iXZqtCOcMg-dfB5EMmWcd6oczZStOM2xvys7hK8IG-9sQYhjmlkV7OtWffa4-1AtAvSR2fiJPpj2ugXtmoIXb0FXBsTUzMoGgBzkC8ePjPB9IvbrPMYDMYqTB2qZ0oxY4ZzDFukAJld2lPI1JVExqQhrutEjKLLPl9evQYQAAAAGHcvUbAQ")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
