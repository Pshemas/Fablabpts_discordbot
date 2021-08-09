# All the things thar do something with Google Spreadsheet
import gspread
import constants
from pydantic import BaseModel, ValidationError
from typing import Optional
from datetime import datetime

gconnection = gspread.service_account(filename=constants.GOOGLESHEETSKEYFILE)
spreadsheet = gconnection.open_by_key(constants.SPREADSHEET_ID)
scores = spreadsheet.worksheet(constants.SCORES)
log = spreadsheet.worksheet(constants.LOG)

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


class SheetOps:

    def addentry(row):
        '''adds entry to the Google Spreadsheet / logs. 
        Should be passed as a list [name, pts, body, status]'''

        log.append_row(row)

    def topscores(howmany):
        '''Returns list of lists with top scores recorded'''
        query = scores.get(f"A2:B{howmany+1}")
        #+1 because first row reserverd for titles
        return query

    def myscore(discord_username):
        '''Returns user score'''
        query = scores.get_all_records()
        for entry in query:
            if entry[constants.DISCORDNAME] == discord_username:
                return entry[constants.TOTALUSERSCORE]
                break