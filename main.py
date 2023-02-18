import random
import config as cfg

import logging

from src.matchup import do_match


logging.basicConfig(
        filename="heromatch.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s",
        )

if __name__ == '__main__':
    logging.info("Démarrage HeromatcH")
    do_match()
    logging.info("Extinction HeromatcH")
