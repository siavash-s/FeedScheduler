import dependencies
import signal
from config import get_conf
from utils import init_logging


def graceful_exit(sig=None, frame=None):
    dependencies.main_loop.exit()


signal.signal(signal.SIGTERM, graceful_exit)
signal.signal(signal.SIGINT, graceful_exit)

if __name__ == "__main__":
    init_logging(level=get_conf().log_level.value)
    dependencies.main_loop.loop()
