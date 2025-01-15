import logging
import sys
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def divide_numbers(a, b):
    logger.info(f"Attempting to divide {a} by {b}")
    try:
        result = a / b
        logger.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"Division by zero error: {e}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        raise

file_handler = logging.FileHandler('application.log')
file_handler.setLevel(logging.WARNING)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

app_logger = logging.getLogger('app')
app_logger.addHandler(file_handler)
app_logger.addHandler(console_handler)
app_logger.setLevel(logging.DEBUG)

def process_data(data):
    app_logger.debug(f"Processing data: {data}")
    
    if not data:
        app_logger.warning("Empty data provided")
        return []
    
    processed = []
    for item in data:
        try:
            processed_item = item * 2
            processed.append(processed_item)
            app_logger.debug(f"Processed item: {item} -> {processed_item}")
        except Exception as e:
            app_logger.error(f"Error processing item {item}: {e}")
    
    app_logger.info(f"Processed {len(processed)} items")
    return processed

print(divide_numbers(10, 2))
print(divide_numbers(10, 0) if False else "Skipping division by zero")

test_data = [1, 2, 3, 4, 5]
result = process_data(test_data)
print(f"Final result: {result}")

empty_result = process_data([])
print(f"Empty result: {empty_result}")

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
    
    def log_function_call(self, func_name, *args, **kwargs):
        self.logger.info(f"Calling function: {func_name} with args: {args}, kwargs: {kwargs}")
    
    def log_error(self, error):
        self.logger.error(f"Error occurred: {error}")

custom = CustomLogger("custom_app")
custom.log_function_call("test_function", 1, 2, 3, key="value")
custom.log_error("Sample error message")
