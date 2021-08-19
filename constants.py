#Put all your constants like discord / google tokens here

DISCORDTOKEN = " "
GOOGLESHEETSKEYFILE = " "
SPREADSHEET_ID = " "
SCORES = "ranking" #name of a worksheet with summed up scores
LOG = "fbclog" #name of a worksheet with all the records


#constants with worksheet columns naming convention

DISCORDNAME = 'discord name' #column with discord usernames
DISCORDID = 'id'
TOTALUSERSCORE = 'SUM of ile' #pivot table column with summed scores
NEWENTRYSTATUS = 'nowy' #default status of a new entry

#command names - make sure to start with sign like $

ADDPOINTS = '$dodaj'
SUBTRACTPOINTS = '$wydaj'
TOP5 = '$top5'
USERSCORE = '$moje'
HELP = '$pomoc'

#custom messages
NOPMREPLY = "The bot is not accepting PMs"