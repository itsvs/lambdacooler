# lambdacooler

the open-source slack watercooler.

## purpose

right now, lambdacooler has a very simple purpose: create groups of some size
and provide them with a conversation starter. you can run this however often you
want to! over time, more cool social features will be added :) of course, feel
free to add your own and submit pull requests!

## motivation

if you've ever been in a large slack workspace, you know how hard it is to feel
included. over time, you might find your group, but in doing so you might even
pass up a chance to meet a lot of cool people. donut bot was created to help
make people feel connected, introducing a watercooler for slack that would help
spark conversation. unfortunately though, as with all good things, donut is now
mostly paid, and is closed-source.

so i made lambdacooler. it's an open-source watercooler for slack, originally
created for use by cs61a staff at uc berkeley. we tend to have a large staff
over at 61a, which makes it hard to spark social connections, so i made this in
an effort to help people get to know each other. i intend to keep adding cool
features to this and maybe bringing it to a point where i feel like i've added
enough to distribute this through the slack app marketplace. in the meantime,
though, i'll keep this open-source, because i believe all good software should
be open-source.

## setup

### on slack

[create a slack app](https://api.slack.com/apps) from scratch in the right
workspace. add the following bot token scopes:

- `channels:read` to allow access to information about channels, including user
  lists
- `chat:write` to allow sending messages as `@lambdacooler`
- `im:write` to allow sending individual direct messages as `@lambdacooler`
- `mpim:write` to allow sending group direct messages `@lambdacooler`
- `users:read` to allow reading user lists and profiles, minus email addresses

then, install the app in your workspace and copy the bot user oauth token.

### on your machine

1. clone this repo
2. run `python3 -m venv env` to create a virtual environment
3. run `source env/bin/activate` to activate the environment
4. run `pip install -r requirements.txt` to install some python packages
5. create a file called `sensitive.py` and add the following:

```python
TOKEN = "<the bot user oauth token>"
SOCIAL_CHANNEL = "<see below>"
LAMBDACOOLER_CHANNEL = "<see below>"
ADMIN = "<see below>"
```

6. to get the `LAMBDACOOLER_CHANNEL` id, use the `channels` command in `lc.py`
   and copy the id of the channel you want to treat as your lambdacooler hub.
   non-bot users in this channel will be included when you prepare a cooler.
8. to get the `SOCIAL_CHANNEL` id, do the same as above and copy the id of the
   channel where lambdacooler should remind people to join the lambdacooler hub
   channel if they want to be included when you prepare a cooler.
10. to get the `ADMIN` user id, use the `users` command in `lc.py` and copy the
    id of your slack user (or, if the admin is someone else, then that user's
    id).
12. you may need to run `chmod +x lc` in order to be able to use `./lc` instead
    of `python3 lc.py`. trust me, it's worth it.

## usage

```
(env) $ ./lc --help
Usage: lc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  channel        Send a message to var.LAMBDACOOLER_CHANNEL.
  channels       Get all channel IDs and names in the current workspace.
  cool           Send cooler messages to the groups in ID.
  join-reminder  Remind people in var.SOCIAL_CHANNEL about lambdacooler.
  prepare        Prepare some coolers of SIZE or greater.
  test           Send a test message.
  users          Get all user IDs and names in the current workspace.
  welcome        Send var.WELCOME_MSG to var.LAMBDACOOLER_CHANNEL.
```

### sample workflow

1. `./lc users` to get admin user ID
2. `./lc channels` to get lambdacooler channel id
3. `./lc test` to send yourself a test message
4. `./lc welcome` to send a welcome message to the lambdacooler channel
5. `./lc prepare` to prepare a grouping (let's assume it goes into
   `data/1632014965.json`)
7. Change `variables.STARTER` to a fun new starter question!
8. `./lc cool -i 1632014965` to send group direct messages to all the cooler
   groups in `data/1632014965.json` with the `variables.STARTER` starter
   question

## teardown

run `deactivate` when done to exit the virtual environment.

## license

in the spirit of open-source, this code is under the gnu gplv3 license.

```
lambdacooler, the open-source slack watercooler.
Copyright (C) 2021 Vanshaj Singhania

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

see [COPYING](./COPYING) for a full copy of the gnu general public license.
