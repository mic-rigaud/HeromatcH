# @Author: michael
# @Date:   13-Feb-2018
# @Project: Major_Home
# @Filename: main.py
# @Last modified by:   michael
# @Last modified time: 14-Nov-2020
# @License: GNU GPL v3


import logging
import os
import sys
from warnings import filterwarnings

from pytz import timezone
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (Application, CommandHandler, ContextTypes, Defaults, MessageHandler,
                          PicklePersistence,
                          filters)
from telegram.warnings import PTBUserWarning

import config as cfg
from src.api.button import bot_send_message

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())

logging.basicConfig(
        filename="./log/HeromatcH.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
        )
logging.getLogger('httpx').setLevel(logging.WARNING)

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)
filterwarnings(action="ignore", message=r".*days", category=PTBUserWarning)

HELP_LIST = []


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gere la reponse pour une commande inconnue."""
    await bot_send_message(update,
                           context,
                           text="Désole, je ne comprends pas bien ce que vous me demandez")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Affiche l'aide."""
    demande = " ".join(context.args).lower().split(" ")[0]
    reponse = "Voici les actions possibles:\n\n"
    for mod in HELP_LIST:
        doc = mod.__doc__
        nom = mod.__name__.replace("src.plugins.", "").split(".")[0]
        if doc and (
                (
                        update.message.from_user.id not in cfg.admin_chatid
                        and nom not in ["start"] and "admin_" not in nom
                )
                or update.message.from_user.id in cfg.admin_chatid):
            if demande == "":
                reponse += f"/{nom} : {doc}" + "\n"
            elif demande in nom:
                reponse = mod.add.__doc__
    await bot_send_message(update, context, text=reponse)


def charge_module(application_telegram):
    """Charge l'ensemble des actions."""
    lst_import = os.listdir("./src/plugins")
    for module_name in sorted(lst_import):
        if "__" not in module_name:
            mod = __import__(f"src.plugins.{module_name}.{module_name}", fromlist=[""])
            mod.add(application_telegram)
            HELP_LIST.append(mod)
    help_handler = CommandHandler("help", help)
    application_telegram.add_handler(help_handler)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application_telegram.add_handler(unknown_handler)


if __name__ == "__main__":
    logging.info("Demarrage de HeromatcH")
    defaults = Defaults(parse_mode=ParseMode.HTML, tzinfo=timezone("Europe/Paris"))
    my_persistence = PicklePersistence(filepath="data/persistence-data")
    application = (
        Application.builder()
        .token(cfg.bot_token)
        .defaults(defaults)
        .persistence(persistence=my_persistence)
        .build()
    )

    charge_module(application)
    application.run_polling()
    logging.info("Extinction de HeromatcH")
