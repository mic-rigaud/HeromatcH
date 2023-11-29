# @Author: michael
# @Date:   01-Sep-2019
# @Filename: Restricted.py
# @Last modified by:   michael
# @Last modified time: 22-Nov-2020
# @License: GNU GPL v3


"""Creer le decorateur restricted."""

import logging
from functools import wraps

from telegram import Update
from telegram.ext import ContextTypes

import config as cfg
from src.api.button import bot_send_message
from src.bdd.Joueur_BDD import Joueur


def restricted(func):
    """Rends les commandes en restricted."""

    @wraps(func)
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = update.callback_query if update.message is None else update.message
        user_id = message.from_user.id
        record = Joueur.select().where(Joueur.user_id == user_id)
        if not record.exists():
            logging.info(f"Access non autorisé pour {user_id}.")
            reponse = ("Hey! Mais on se connait pas tout les deux.\nTa maman ne t'as jamais dit qu'on commence "
                       "toujours une conversation par /start. ")
            await bot_send_message(context=context, update=update, text=reponse)
            return
        return await func(update, context)

    return wrapped


def restricted_admin(func):
    """Rends les commandes en restricted."""

    @wraps(func)
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if user_id not in cfg.admin_chatid:
            logging.info(f"Access non autorisé pour {user_id} sur une fonction d'admin.")
            reponse = "C'est une fonction d'admin. C'est pas pour toi, désolé."
            await bot_send_message(context=context, update=update, text=reponse)
            return
        return await func(update, context)

    return wrapped
