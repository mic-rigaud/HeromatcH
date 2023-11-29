"""Montre le classement des héros"""

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from src.api.Restricted import restricted
from src.api.button import bot_send_message
from src.bdd.Hero_BDD import Hero


def creer_classement():
    reponse = "".join(
            f"{hero_selected.nom} - {hero_selected.total_point} pts\n"
            for hero_selected in Hero.select().order_by(Hero.total_point.desc())
            )
    return reponse or "Aucun Hero"


@restricted
async def classement(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Montre le classement des héros"""
    await bot_send_message(update, context, text=creer_classement())


def add(application):
    """
    Montre le classement des héros
    """
    handler = CommandHandler('classement', classement)
    application.add_handler(handler)
