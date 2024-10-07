# src/logger/logger.py
import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = os.path.join(os.getcwd(), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Create a log file with a timestamp
log_file = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Basic configuration for logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,  # You can change this to DEBUG, ERROR, etc.
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def get_logger(name):
    """Function to get a logger instance."""
    logger = logging.getLogger(name)
    return logger
