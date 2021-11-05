![IMDb Bot](./image.png)
# IMDb Discord Bot

## how to run this bot.
1. the first step you must create `prefixes.json` file

2. the second step you must create a `virtualenv`
    1. if you use windows :
        - ```bash
            python -m venv .venv
            # for activate virtualenv
            .\.venv\Scripts\activate
            ```
    2. if you use linux :
        - ```bash
            sudo apt install virtualenv
            virtualenv -p py3 .venv
            # for activate virtualenv
            source ./.venv/bin/activate
            ```
    3. if you use macos :
        - ```bash
            brew install virtualenv
            virtualenv -p py3 .venv
            # for activate virtualenv
            source ./.venv/bin/activate
            ```
3. the third step you must install `requirements.txt`
    1. if you use windows :
        - ```bash
            python -m pip install -r requirements.txt
            ```
    2. if you use linux :
        - ```bash
            pip3 install -r requirements.txt
            ```
    3. if you use macos :
        - ```bash
            pip install -r requirements.txt
            ```
4. the last step you must run this bot
    - ```bash
        python bot.py
        ```
----
## bot commands
1. **`help`** => this command for show help

2. **`prefix`** => this command change command prefix on your server, need administrator role, default prefix => `i>`, if you mention bot, bot say your now prefix

3. **`movie`**, **`MOVIE`**, **`film`**, **`FILM`**, **`series`**, **`SERIES`**, **`tvshow`**, **`TVSHOW`**, **`animation`**, **`ANIMATION`** => this command search your movies and return a select box, with 10 of result, you must select a movie and bot return url of movie
----
# writed by metidotpy
## I hope you enjoy that <3
