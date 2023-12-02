# @Author: michael
# @Date:   19-Apr-2019
# @Filename: config.py
# @Last modified by:   michael
# @Last modified time: 22-Nov-2020
# @License: GNU GPL v3

import json
import os

# Bot token avec le token de dev
bot_token = os.environ['HEROMATCH_BOT_TOKEN']

admin_chatid = json.loads(os.environ['HEROMATCH_ADMINS'])
