import discord
import constants
from sheetops import *  # I know - not the suggested way to import
from messageops import *

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as %s" % client.user)


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$dodaj'):
        newentry = SheetData.parse_obj(extractdata(message))
        SheetOps.addentry(newentry.as_row())
        await message.channel.send(f'+{newentry.amount} dla {newentry.name} oczekuje na rozliczenie')

    if message.content.startswith('$wydaj'):
        newentry = SheetData.parse_obj(extractdata(message))
        newentry.negativevalue()
        SheetOps.addentry(newentry.as_row())
        await message.channel.send(f'{newentry.amount} dla {newentry.name} oczekuje na rozliczenie')

    if message.content.startswith('$moje'):
        await message.channel.send('Ilość Twoich fabcoinów to: %s' % SheetOps.myscore(str(message.author)))

    if message.content.startswith('$top5'):
        await message.channel.send(scores_enumarated_withtitle("Top5",SheetOps.topscores(5)))

    if message.content.startswith('$pomoc'):
        await message.channel.send(showhelp())


def main():
    client.run(constants.DISCORDTOKEN)


if __name__ == '__main__':
    main()
