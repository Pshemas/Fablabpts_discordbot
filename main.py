import discord
import constants
from sheetops import *  # I know - not the suggested way to import
from messageops import *
from errors import *

client = discord.Client()


async def create_entry(message, operationtype):
    '''Takes the message, prepares entry for Sheets and sends it.
    Requires "operationtype" as parameter as well - 
    so the value can be set to negative if needed.''' 
#    feels this def should be moved somewhere.
#    Both sheetops and messageops seem wrong.
#    Remains here for now.

    try:
        newentry = SheetData.parse_obj(extractdata(message))

    except MissingArgument as err:
        await message.channel.send(err)

    except AmountNotInt as err:
        await message.channel.send(err)

    else:
        if operationtype == "spend":
            newentry.negativevalue()
        SheetOps.sendentry(newentry.as_row())
        await message.channel.send(f'{newentry.amount} dla {newentry.name} oczekuje na rozliczenie')


@client.event
async def on_ready():
    print("We have logged in as %s" % client.user)


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if str(message.channel.type) == "private":
        await message.channel.send(constants.NOPMREPLY)
        return

    if message.content.startswith(constants.ADDPOINTS):
        await create_entry(message, "earn")

    if message.content.startswith(constants.SUBTRACTPOINTS):
        await create_entry(message, "spend")

    if message.content.startswith(constants.USERSCORE):
        await message.channel.send('Ilość Twoich fabcoinów to: %s' % SheetOps.myscore(str(message.author)))

    if message.content.startswith(constants.TOP5):
        await message.channel.send(scores_enumarated_withtitle("Top5",SheetOps.topscores(5)))

    if message.content.startswith(constants.HELP):
        await message.channel.send(showhelp())


def main():
    client.run(constants.DISCORDTOKEN)


if __name__ == '__main__':
    main()
