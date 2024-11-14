# utils/logger.py

import logging

def initialize_logger(log_level="INFO"):
    """Initializes the logging system with a specified log level."""
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()]
    )

def log_event(event_name, details=""):
    """Logs a general event with optional details."""
    logging.info(f"Event: {event_name} - Details: {details}")

def log_error(error_message):
    """Logs an error with an error message."""
    logging.error(f"Error: {error_message}")

# Usage example
if __name__ == "__main__":
    initialize_logger()
    log_event("Difficulty Adjustment", "Increased difficulty to level 3")
    log_error("Connection failed with multiplayer server")

