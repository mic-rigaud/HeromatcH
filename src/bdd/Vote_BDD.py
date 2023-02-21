#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/02/2023 19:41
# @Author  : Michael
# @File    : Vote_BDD.py.py
# @Project: HeromatcH


from peewee import CharField, ForeignKeyField, IntegerField

from src.bdd.Personnage_BDD import Personnage
from src.bdd.api_bdd import BaseModel


class Vote(BaseModel):
    """Objet definissant les Votes dans la BDD."""

    gagnant = ForeignKeyField(Personnage, backref="vote")
    perdant = ForeignKeyField(Personnage, backref="vote")



