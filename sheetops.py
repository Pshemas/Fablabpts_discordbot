# All the things thar do something with Google Spreadsheet
import gspread
import constants

gconnection = gspread.service_account(filename=constants.GOOGLESHEETSKEYFILE)
spreadsheet = gconnection.open_by_key(constants.SPREADSHEET_ID)
scores = spreadsheet.worksheet(constants.SCORES)
log = spreadsheet.worksheet(constants.LOG)

class SheetOps:

    def addentry(row):
        '''adds entry to the Google Spreadsheet / logs. 
        Should be passed as a list [name, pts, body, status]'''

        log.append_row(row)

    def top5():
        '''Returns list of lists with top 5 scores recorded'''
        query = scores.get("A2:B6")
        return query

    def myscore(discord_username):
        '''Returns user score'''
        query = scores.get_all_records()
        for entry in query:
            if entry[constants.DISCORDNAME] == discord_username:
                return entry[constants.TOTALUSERSCORE]
                break
