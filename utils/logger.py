import logging
import atexit

log_initialized = False


def setup_logging():
    global log_initialized
    if not log_initialized:
        log = logging.getLogger()
        log.setLevel(logging.INFO)

        # File handler
        file_handler = logging.FileHandler('app.log', mode='a')
        file_formatter = logging.Formatter('[%(levelname)s:%(threadName)s %(asctime)s.%(msecs)03d] %(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(file_formatter)
        log.addHandler(file_handler)

        # Stream handler (console output)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(file_formatter)
        log.addHandler(stream_handler)

        def close_handlers():
            file_handler.close()
            stream_handler.close()
            log.removeHandler(file_handler)
            log.removeHandler(stream_handler)

        atexit.register(close_handlers)
        log_initialized = True


# Call this in your main entry point only
setup_logging()
