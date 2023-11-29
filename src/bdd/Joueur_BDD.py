import logging

from peewee import CharField

from src.bdd.api_bdd import BaseModel


class Joueur(BaseModel):
    """Objet definissant les Joueurs dans la BDD."""

    nom = CharField()
    chat_id = CharField()
    user_id = CharField()


def get_joueur(chatid, userid):
    """get_joueur: permet de récuperer un joueur"""
    try:
        return (
            Joueur.select().where((Joueur.chat_id == chatid) & (Joueur.user_id == userid)).get())
    except Joueur.DoesNotExist:
        logging.warning(f"Le joueur demandé n'existe pas. Le chatid est {chatid} et le userid est "
                        f"{userid}")
        return None
