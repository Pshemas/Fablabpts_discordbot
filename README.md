# Fablabpts_discordbot
a simple bot that takes commands from Discord and registers them in Google Sheets.
Designed to easily add / spend reward points in local Fablab (Warsaw). Probably not the cleanest code as it is one of my very first attempts to write something - so use with caution.
Requires gspread and discord.py.

It is split into following parts:
1. main.py - main runfile, contains app logic and functions used to get data from Discord
2. sheetops.py - contains functions that relate to registering data in Google Sheets
3. messageops.py - contains functionc etc related to messages handling, retrieving data from Discord
4. constants - contains all the environment variables needed for all those to operate correctly, like your json access file , name of the columns in Sheets and so on.
5. errors.py - file with custom error messages

For all this to work you need to create a bot on discord and also register an app in Google platform.
