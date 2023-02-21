#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/02/2023 19:36
# @Author  : Michael
# @File    : test_matchup.py
# @Project: HeromatcH

from unittest import TestCase

from src.matchup import set_vote


class Test(TestCase):

    def test_set_vote(self):
        self.assertFalse(set_vote(1000000, 2000000))
