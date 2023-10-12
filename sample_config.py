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
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5123039648 5821628687").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "Delete User Bot")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "BQEsG5cAqHFdAzfuT7FtpkYqkgkCSsDEniz5qhRdFv05YTWPAjBmlHMSOfwrTtF-QjxXj8UlSdiyF1kKqkUpgmYLQASOM4JZ00FYk8fE1RvROWiDYycxMLykPFJPK4tbVh3kZS9avxxh8AAjFgZtTwdbub_b2f6ZwMtHxMhrMXtrgqj0kMQHF9xcqBXxslDVt4shYsUkZ0DTbLYMG7sG2M6V9fQ4nHIXOLQh5sSm2ABJvkS29WK1EVLD0gVBDu2OmRDDz4PJS9ICHHn1Z9QGhFeFCHXoeSssVU0mxHuHZ8Tj7sYKx5vBz7cCoFI4gkmAHfK33hMxCYhH3afI2uz-5-lxOtzpbwAAAAFa_wEPAA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
