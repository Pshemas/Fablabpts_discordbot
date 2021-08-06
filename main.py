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
        newentry = SheetEntry(message,7)
        SheetOps.addentry(newentry.row)
        await message.channel.send(f'+{newentry.row[4]} dla {newentry.row[2]} oczekuje na rozliczenie')

    if message.content.startswith('$wydaj'):
        newentry = SheetEntry(message,7)
        newentry.row[4] = -newentry.row[4]
        SheetOps.addentry(newentry.row)
        await message.channel.send(f'{newentry.row[4]} dla {newentry.row[2]} oczekuje na rozliczenie')

    if message.content.startswith('$moje'):
        await message.channel.send('Twoj wynik to %s' % SheetOps.myscore(str(message.author)))


def main():
    client.run(constants.DISCORDTOKEN)


if __name__ == '__main__':
    main()
