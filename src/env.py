import os

from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
BASE_URL = os.getenv("BASE_URL", "https://graph.threads.net/v1.0")

DRAFTS_FILE = os.getenv("DRAFTS_FILE", "drafts.json")
