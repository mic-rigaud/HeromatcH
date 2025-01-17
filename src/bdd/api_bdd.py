#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/02/2023 14:28
# @Author  : Michael
# @File    : api_bdd.py.py
# @Project: HeromatcH

from peewee import Model
from playhouse.sqlite_ext import SqliteDatabase

db = SqliteDatabase("./data/bdd.db")


class BaseModel(Model):
    """Classe BaseModel."""

    class Meta:
        """Classe Meta."""

        database = db
