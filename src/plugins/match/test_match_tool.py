#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 02/12/2023 14:19
# @Author  : Michael
# @File    : test_match_tool.py
# @Project: HeromatcH

from src.plugins.match.match_tool import get_image_match


def test_get_image_match():
    assert get_image_match("toto", "tata") == "error"
