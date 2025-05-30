

import logging
import os
from datetime import datetime
LOG_FILE = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_PATH = os.path.join("logs", LOG_FILE)
os.makedirs("logs", exist_ok=True)
# Configure logging once
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
)
def get_logger(name: str) -> logging.Logger:
    """Returns a logger that logs to both file and console (optional)."""
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
    return logger
