from pydantic import BaseModel, ValidationError
from typing import Optional
from datetime import datetime


def extractdata(message):
    ''' extracts data for Google Sheets from message, 
    removes command used to invoke bot. Returns dict.'''

    withoutprefix = message.clean_content
    cleaned = withoutprefix.split(' ', 2)
    cleaned[1] = int(cleaned[1])
    dataset = {"discordid": message.author.id, "name": message.author.name + '#' +
               message.author.discriminator, "nick": message.author.nick,
               "amount": cleaned[1], "body": cleaned[2]}
    return dataset

def scores_enumarated_withtitle(title, scorelist):
    '''Takes list (of lists) with scores and returns it as enumerated string'''

    message = str(title)+'\n'
    counter = 1
    for item in scorelist:
        message+=str(counter)+'. '+item[0]+' '+item[1]+'fbc \n'
        counter +=1
    return message

class SheetData(BaseModel):
    '''Container for data used in GoogleSheets. Dataset goes through pydantic,
     so it could be validated more easily.'''

    datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    discordid: str
    name: str
    nick: Optional[str]
    amount: int
    body: str
    status = 'nowy'

    def as_row(self):
        '''returns data as a list so it could be added to 
        Google Sheets easily'''
        return [self.datetime, self.discordid, self.name, self.nick,
                 self.amount, self.body, self.status]

    def negativevalue(self):
        '''switches the amount to its negative value'''
        self.amount = -self.amount
