"""Lance le match des héros"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler

from src.api.Restricted import restricted
from src.api.button import bot_send_message, bot_send_image, build_menu, bot_edit_message
from src.plugins.match.match_tool import get_image_match, get_hero_match, ajout_victoire


async def button_victoire(update: Update, context: CallbackContext):
    query = update.callback_query
    id_gagant = query.data.split("_")[2]
    id_perdant = query.data.split("_")[3]
    reponse = ajout_victoire(id_gagant, id_perdant)
    await bot_edit_message(update, context, text=reponse)


def creer_bouton(heroes):
    """Creer la liste de boutons."""
    button_list = [
        InlineKeyboardButton(f"{heroes[1]['name']}", callback_data=f"m_vic_{heroes[1]['id']}_{heroes[2]['id']}"),
        InlineKeyboardButton(f"{heroes[2]['name']}", callback_data=f"m_vic_{heroes[2]['id']}_{heroes[1]['id']}"),
        ]
    return InlineKeyboardMarkup(build_menu(button_list, n_cols=2))


@restricted
async def match(update: Update, context: CallbackContext):
    """Lance le match des héros"""
    heroes = get_hero_match()
    image_match = get_image_match(heroes[1]["name"], heroes[2]["name"])
    await bot_send_image(update, context, image=image_match)
    await bot_send_message(update, context, text="Qui gagne ?", reply_markup=creer_bouton(heroes))


def add(application):
    """
    Lance le match des héros
    """
    application.add_handler(CommandHandler('match', match))
    application.add_handler(CallbackQueryHandler(button_victoire, pattern="^m_vic_."))
