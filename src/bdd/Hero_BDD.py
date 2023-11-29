#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/02/2023 14:22
# @Author  : Michael
# @File    : Personnage.py.py
# @Project: HeromatcH


from peewee import CharField, IntegerField

from src.bdd.api_bdd import BaseModel


class Hero(BaseModel):
    """Objet definissant les Joueurs dans la BDD."""

    nom = CharField()
    nom_long = CharField()
    manga = CharField()
    total_point = IntegerField(default=0)
    total_match = IntegerField(default=0)
