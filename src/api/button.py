# @Author: michael
# @Date:   27-Apr-2019
# @Filename: button.py
# @Last modified by:   michael
# @Last modified time: 14-Jun-2020
# @License: GNU GPL v3


import json
import logging

from telegram.constants import MessageLimit


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    """Permet de construire un menu interactif."""
    menu = [buttons[i: i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def build_callback(data):
    return_value = json.dumps(data)
    if len(return_value) > 64:
        raise TelegramCallbackError("Les data ont une taille supérieur à 64 bytes")
    return return_value


class TelegramCallbackError(Exception):
    def __init__(self, message=""):
        self.message = message


async def bot_send_message(update, context, text, reply_markup=None, chat_id=None):
    """Envoi un message

    :param int chat_id: Chat id si on veut en specifier un
    :param Update or None update: update du bot
    :param CallbackContext context: context du bot
    :param str text: text a envoyer
    :param ReplyMarkup reply_markup: reply_markup
    """
    if len(text) > MessageLimit.MAX_TEXT_LENGTH - 1:
        text = text[:MessageLimit.MAX_TEXT_LENGTH - 1]
        logging.warning("Tentative d'envoyer un texte trop long. Il a été réduit à la taille maximale possible.")
    if update is None and chat_id is None:
        logging.error("Il manque un argument")
    elif update is not None:
        query = update if update.callback_query is None else update.callback_query
        if text == query.message.text:
            text += "."
        if not chat_id:
            chat_id = query.message.chat_id
    await context.bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup,
            )


async def bot_edit_message(update, context, text, reply_markup=None, message_id=None):
    """Edit le dernier message

    :param int message_id: id du message a modifier sinon prend le dernier
    :param Update update: update du bot
    :param CallbackContext context: context du bot
    :param str text: text a envoyer
    :param ReplyMarkup reply_markup: reply_markup"""

    query = update if update.callback_query is None else update.callback_query
    message_id = query.message.message_id if message_id is None else message_id
    if len(text) > MessageLimit.MAX_TEXT_LENGTH - 1:
        text = text[:MessageLimit.MAX_TEXT_LENGTH - 1]
        logging.warning("Tentative d'envoyer un texte trop long. Il a été réduit à la taille maximale possible.")
    if text == query.message.text:
        text += "."
    await context.bot.edit_message_text(
            chat_id=query.message.chat_id,
            message_id=message_id,
            text=text,
            reply_markup=reply_markup,
            )


async def bot_send_image(update, context, image):
    """Edit le dernier message

    :param Update update: update du bot
    :param CallbackContext context: context du bot
    :param file_object image: image a envoyer
    """
    query = update if update.callback_query is None else update.callback_query
    await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=image
            )
