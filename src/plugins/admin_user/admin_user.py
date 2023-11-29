"""Renvoi la liste des utilisateurs actuels."""

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from src.api.Restricted import restricted_admin
from src.api.button import bot_send_message
from src.bdd.Joueur_BDD import Joueur


def get_liste_user():
    record = Joueur.select().where(True)
    reponse = "Voici la liste des utilisateurs:\n"
    for person in record:
        reponse += f"{person.nom}\n"
    return reponse


@restricted_admin
async def admin_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Renvoi la liste des joueurs."""
    await bot_send_message(context=context,
                           update=update,
                           text=get_liste_user())


def add(application):
    """
    Renvoi la liste des joueurs.
    """
    application.add_handler(CommandHandler("admin_user", admin_user))
