#all the things that do something with the Discord message

from datetime import datetime


def cleanmessage(messagecontent, cutindex):
    ''' takes the message content and removes initial chars 
    (defined by cutindex) used to invoke discord bot from it. 
    Then it splits it and creates a list [int(amount), message body]'''

    withoutprefix = messagecontent[cutindex:]
    cleaned = withoutprefix.split(' ', 1)
    cleaned[0] = int(cleaned[0])
    return cleaned


class SheetEntry:
    ''' Creates a proper entry for google sheets from the Discord message. 
    [datetime, id, name#discriminator, nick, amount, msg body, status]'''

    def __init__(self, message, cutindex):
        self.row = []
        self.row.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.row.append(message.author.id)
        self.row.append(message.author.name + '#' +
                        message.author.discriminator)
        self.row.append(message.author.nick)
        self.row = self.row + (cleanmessage(message.clean_content, cutindex))
        self.row.append('nowy')
