"""Permet d'ajouter l'utilisateur qui utilise la commande"""

import logging

from telegram import Update
from telegram.ext import (CommandHandler, ContextTypes, ConversationHandler, MessageHandler,
                          filters)

from src.api.button import bot_send_message
from src.bdd.Joueur_BDD import Joueur

ETAPE1, ETAPE2 = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gere les bonjour."""
    record = Joueur.select().where(
            (Joueur.user_id == update.message.from_user.id) & (
                    Joueur.chat_id == update.message.chat_id))
    if not record.exists():
        reponse = (
            "Bonjour!\nBienvenue sur HeromatcH l'application pour voter pour le plus grand hero de tous les temps. "
            "Pour jouer, il faut s'inscrire, et pour cela j'ai juste besoin de ton nom : ")
        await bot_send_message(context=context, update=update, text=reponse)
        return ETAPE1
    else:
        reponse = "Mais tu es déjà enregistré.😉\nFais /help si tu veux connaitre mes capacités."
        await bot_send_message(context=context, update=update, text=reponse)
        return ConversationHandler.END


async def etape1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nom = update.message.text
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    Joueur.create(nom=nom, chat_id=chat_id, user_id=user_id).save()
    logging.info(f"Ajout de l'utilisateur {nom}")
    reponse = f"Bienvenue à toi {nom}.\nMaintenant à toi de jouer! Si tu as besoin d'en savoir plus sur mes " \
              f"fonctionnalités fais /help "

    await bot_send_message(context=context, update=update, text=reponse)
    return ConversationHandler.END


async def conv_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await bot_send_message(context=context, update=update, text="Bon c'est fini")
    return ConversationHandler.END


def add(application):
    """
    Ajoute les utilisateurs
    """
    new_alarm_handler = ConversationHandler(entry_points=[CommandHandler("start", start)],
                                            states={ETAPE1: [MessageHandler(filters.TEXT, etape1)]},
                                            fallbacks=[CommandHandler("end", conv_cancel)],
                                            conversation_timeout=120, )
    application.add_handler(new_alarm_handler)
