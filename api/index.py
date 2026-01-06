import sys
import os

# Add src to path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import app
from mangum import Mangum

# Vercel handler
handler = Mangum(app, lifespan="off")
