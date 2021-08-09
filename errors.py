import discord

class CommandError(Exception):
    def __init__(self, message):
        self.message = message
        message.channel.send("Twój FabcoinBot nie wie co zrobić. Wpisz $pomoc żeby zobaczyć poprawną składnię dostępnych poleceń %s" % message)
        super().__init__(message)
