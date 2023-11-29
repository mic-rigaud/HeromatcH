#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/02/2023 14:35
# @Author  : Michael
# @File    : task.py.py
# @Project: HeromatcH
import json
import logging
import os

from invoke import task

import src.bdd.api_bdd as bdd
from src.bdd.Hero_BDD import Hero
from src.bdd.Joueur_BDD import Joueur
from src.bdd.Vote_BDD import Vote


@task
def install(c):
    """Install blueberry."""
    config_bdd(c)
    c.run("touch log/HeromatcH.log")


@task
def config_bdd(c):
    """Permet l'installation de la BDD automatise."""
    try:
        var = bdd.db.connect
        bdd.db.create_tables([Hero, Vote, Joueur])
        logging.info("Creation de la BDD")
        import_personnage()
    except Exception as e:
        print("=== La base SQL existe déjà ===")
        print(e)


def import_personnage():
    lst_import = os.listdir("Heroes")
    for hero_file in sorted(lst_import):
        if ".json" in hero_file:
            with open(f"Heroes/{hero_file}") as json_data:
                hero_data = json.load(json_data)
                if Hero.select().where(Hero.nom == hero_data["nom_court"]).count() == 0:
                    Hero(nom=hero_data["nom_court"], manga=hero_data["manga"], nom_long=hero_data["nom_long"]).save()
                    print(f"{hero_data['nom_court']} ajouté dans la Bdd")
                json_data.close()


@task
def start_local(c):
    """Demarre en local."""
    c.run("python3 main.py", pty=True, warn=True)
