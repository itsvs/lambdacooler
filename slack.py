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

import requests, urllib
import variables as var


def get(url):
    return requests.get(url, headers={"Authorization": f"Bearer {var.TOKEN}"}).json()


def get_channels():
    api_url = var.BASE_URL.format("conversations.list")
    return get(api_url)["channels"]


def all_users():
    api_url = var.BASE_URL.format("users.list")
    members = get(api_url)["members"]
    res = {}
    for member in members:
        res[member["id"]] = member
    return res


def user_from_email(email):  # unused
    api_url = var.BASE_URL.format("users.lookupByEmail")
    api_url += "?email=" + email
    return get(api_url)["user"]


def lambdacooler_users():
    api_url = var.BASE_URL.format("conversations.members")
    api_url += "?channel=" + var.LAMBDACOOLER_CHANNEL
    return get(api_url)["members"]


def open_dm(users):
    api_url = var.BASE_URL.format("conversations.open")
    api_url += "?users=" + ",".join(users)
    id = get(api_url)["channel"]["id"]
    return lambda message: send_message(id, message)


def send_message(channel, message):
    api_url = var.BASE_URL.format("chat.postMessage")
    api_url += "?channel=" + channel
    api_url += "&text=" + urllib.parse.quote_plus(message)
    get(api_url)
