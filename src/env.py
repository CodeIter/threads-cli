import os

from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
DRAFTS_FILE = os.getenv("DRAFTS_FILE", "drafts.json")
