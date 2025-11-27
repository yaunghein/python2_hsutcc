from datetime import datetime


def logger(log_filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"[{timestamp}] Running: {func.__name__}"

            try:
                with open(log_filename, "a", encoding="utf-8") as f:
                    f.write(message + "\n")
            except Exception as e:
                print(f"[LOGGER ERROR] Could not write to {log_filename}: {e}")

            return func(*args, **kwargs)
        return wrapper
    return decorator
