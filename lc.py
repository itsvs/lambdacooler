#!env/bin/python

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

import click, json, os
import random, slack
import variables as var
from datetime import datetime


@click.group()
def cli():
    pass


def get_users():
    full_info = slack.all_users()
    lc_users = slack.lambdacooler_users()
    lc_users = [u for u in lc_users if not full_info[u]["is_bot"]]
    return lc_users, full_info


@cli.command(name="users")
@click.option(
    "--lc-hub",
    is_flag=True,
    help="Only get user IDs and names in var.LAMBDACOOLER_CHANNEL.",
)
def get_users_cmd(lc_hub):
    """Get all user IDs and names in the current workspace."""
    users = get_users()
    use = users[0] if lc_hub else users[1]
    for user in use:
        print(f"{user}: {users[1][user]['profile']['real_name']}")


@cli.command(name="channels")
def get_channels():
    """Get all channel IDs and names in the current workspace."""
    channels = slack.get_channels()
    for channel in channels:
        print("id:", channel["id"], "\tname:", channel["name"])


def generate(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


@cli.command(name="prepare")
@click.argument("size", type=int, default=var.GROUP_SIZE)
@click.option(
    "--name", type=str, default=None, help="Optional name to store groups as."
)
def prepare(size, name):
    """Prepare some coolers of SIZE or greater. If NAME is provided, store as
    data/NAME.json, otherwise store as data/TIMESTAMP.json.
    """
    users, full_info = get_users()
    random.shuffle(users)
    groups = list(generate(users, size))

    extras = []
    for g in groups:
        if len(g) == 1:
            groups.remove(g)
            extras.extend(g)

    for e, g in zip(extras, groups):
        g.append(e)

    groups = [
        [{"id": i, "name": full_info[i]["profile"]["real_name"]} for i in g]
        for g in groups
    ]

    for g in groups:
        print(f"Will group: {', '.join([m['name'] for m in g])}")
        print("-------")

    id = int(datetime.now().timestamp()) if not name else name
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(f"data/{id}.json", "w") as f:
        json.dump(groups, f, indent=2)

    print(f"Grouping saved in data/{id}.json! To use, call the `cool` command")
    return groups


@cli.command(name="cool")
@click.option("--id", "-i", prompt="Cooler ID", help="The cooler ID to cool.")
@click.option("--test", is_flag=True)
def send_cooler_messages(id, test):
    """Send cooler messages to the groups in ID."""
    with open(f"data/{id}.json") as f:
        groups = json.load(f)
    for g in groups:
        ids = [m["id"] for m in g]
        if test:
            ids = [var.ADMIN]
        dm_group = slack.open_dm(ids)
        dm_group(var.COOLER_MSG)
    if not test:
        slack.send_message(var.LAMBDACOOLER_CHANNEL, var.COOLERS_SENT_MSG)


@cli.command(name="test")
@click.option("--message", type=str, default=var.COOLER_MSG, help="Message to send.")
@click.option("--to", type=str, default=None, help="User/channel to send message to.")
@click.option(
    "--group",
    is_flag=True,
    help="Whether or not to create a group with TO and sensitive.ADMIN.",
)
def send_test_message(message, to, group):
    """Send a test message. By default, sends var.COOLER_MSG to sensitive.ADMIN."""
    if to:
        uids = [to]
        if group:
            uids.append(var.ADMIN)
    else:
        uids = [var.ADMIN]
    dm_group = slack.open_dm(uids)
    dm_group(message)


@cli.command(name="channel")
@click.option("--message", type=str, required=True, help="The message to send.")
def send_channel_message(message):
    """Send a message to var.LAMBDACOOLER_CHANNEL."""
    slack.send_message(var.LAMBDACOOLER_CHANNEL, message)


@cli.command(name="join-reminder")
@click.option(
    "--message", type=str, default=var.JOIN_REMINDER_MSG, help="The message to send."
)
def send_join_reminder(message):
    """Send a message to var.SOCIAL_CHANNEL reminding people that this exists."""
    slack.send_message(var.SOCIAL_CHANNEL, message)


@cli.command(name="welcome")
def send_welcome_message():
    """Send var.WELCOME_MSG to var.LAMBDACOOLER_CHANNEL."""
    slack.send_message(var.LAMBDACOOLER_CHANNEL, var.WELCOME_MSG)


if __name__ == "__main__":
    cli()
