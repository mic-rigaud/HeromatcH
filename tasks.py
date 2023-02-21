#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/02/2023 14:35
# @Author  : Michael
# @File    : task.py.py
# @Project: HeromatcH

from invoke import task

from src.bdd.Vote_BDD import Vote
import src.bdd.api_bdd as bdd
from src.bdd.Personnage_BDD import Personnage
import config as cfg
import logging


logging.basicConfig(
        filename="heromatch.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s",
        )


@task
def config_bdd(c):
    """Permet l'installation de la BDD automatise."""
    try:
        var = bdd.db.connect
        bdd.db.create_tables([Personnage, Vote])
        logging.info("Creation de la BDD")
        import_personnage()
    except Exception:
        print("=== La base SQL existe déjà ===")


def import_personnage():
    for perso in cfg.names:
        if Personnage.select().where(Personnage.nom == perso).count() == 0:
            Personnage(nom=perso).save()
            logging.info(f"{perso} ajouté dans la Bdd")
