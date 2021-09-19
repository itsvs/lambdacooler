# lambdacooler, the open-source slack watercooler.
# Copyright (C) 2021 Vanshaj Singhania

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from sensitive import *

### The following may need changing ###

GROUP_SIZE = 3

STARTER = "What's your favorite Greek letter and why?"

### The following probably don't need changing ###

WELCOME_MSG = (
    "Hello! I'm :sparkles: lambdacooler :sparkles:, your 61A-inspired "
    "watercooler. I know what it's like to be one in a crowd, so I'm going to "
    "help make you feel like you're a valuable part of staff (because you are!)"
    ".\n\nHow it works is simple. Each week, I'm going to group you with "
    f"{GROUP_SIZE-1} other people (hopefully unique each time), and give you a "
    "conversation starter to get you started. Want to be involved one week? "
    "Join this channel. Don't want to be involved a different week? Leave this "
    "channel and come back again when you want!\n\nThe first grouping will "
    "occur tomorrow. I'll make group DMs with all of the groups in the morning"
    ". See you then! Let me know if you have any questions :tada:"
)

COOLER_MSG = (
    "Hi! It's time to meet some cool people on staff :thefastestparrot:\n\n"
    "Find a time to meet this week for >= 20 minutes, and get to know each "
    "other :tada: When you meet, take a cool photo or screenshot and send it "
    f"in <#{LAMBDACOOLER_CHANNEL}>!\n\nHere's this week's starter: {STARTER}"
)

### The following definitely don't need changing ###

APP_NAME = "lambdacooler"  # unused
BASE_URL = "https://slack.com/api/{}"
