import logging
import random
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

ERROR_MESSAGES = [
    "Database connection failed",
    "Timeout while calling payment service",
    "Null pointer exception",
    "Disk space low"
]

while True:
    if random.random() < 0.15:
        logging.error(random.choice(ERROR_MESSAGES))
    else:
        logging.info("Request processed successfully")

    time.sleep(1)