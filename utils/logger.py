import logging

# Basic configuration for logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',  # Adding custom date format
    filename='app.log',  # Log to a file instead of the console
    filemode='a'  # Append mode, which will add to the file instead of overwriting it
)

def get_logger(name):
    """
    Obtain a logger instance associated with the given name.
    This function configures the logger to log INFO and higher level messages.
    """
    return logging.getLogger(name)
