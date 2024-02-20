import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "reddis://localhost:6379")
QUEUES = ["emails", "default"]