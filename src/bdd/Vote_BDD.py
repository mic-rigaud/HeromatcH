#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/02/2023 19:41
# @Author  : Michael
# @File    : Vote_BDD.py.py
# @Project: HeromatcH


from peewee import ForeignKeyField

from src.bdd.Hero_BDD import Hero
from src.bdd.api_bdd import BaseModel


class Vote(BaseModel):
    """Objet definissant les Votes dans la BDD."""

    gagnant = ForeignKeyField(Hero, backref="vote")
    perdant = ForeignKeyField(Hero, backref="vote")
