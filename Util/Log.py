import logging
import logging.config
from Config.ProjVar import log_conf_path


logging.config.fileConfig(log_conf_path)
logging.getLogger("log1")



if __name__ == "__main__":
    logging.debug("debug")
