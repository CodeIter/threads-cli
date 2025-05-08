import sys
import os

# Append project root directory to sys.path to import modules from src
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))
