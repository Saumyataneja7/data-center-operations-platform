import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent / "DataCenter_AI"
sys.path.insert(0, str(APP_DIR))

from main import run

run()
