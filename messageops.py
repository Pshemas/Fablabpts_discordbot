from errors import *


def extractdata(message):
    ''' extracts data for Google Sheets from message, 
    removes command used to invoke bot. Returns dict.'''

    withoutprefix = message.clean_content
    cleaned = withoutprefix.split(' ', 2)
    if len(cleaned) != 2:
        raise CommandError("Brak informacji za co te fabcoiny :( .")

    else:
        try:
            cleaned[1] = int(cleaned[1])
            dataset = {"discordid": message.author.id, "name": message.author.name + '#' +
                       message.author.discriminator, "nick": message.author.nick, "amount": cleaned[1], "body": cleaned[2]}
            return dataset
        except TypeError:
            raise CommandError("Wartość po poleceniu nie jest liczbą :( .")


def scores_enumarated_withtitle(title, scorelist):
    '''Takes list (of lists) with scores and returns it as enumerated string'''

    message = str(title)+'\n'
    counter = 1
    for item in scorelist:
        message += str(counter)+'. '+item[0]+' '+item[1]+'fbc \n'
        counter += 1
    return message


def showhelp():
    return ("FabcoinBot zrozumie te polecenia:\n**$dodaj ilość za_co** \n - doda ci fabcoiny (pojawią się na liście po zaakceptowaniu przez Wojtka / Abdu). \n**$wydaj ilość za_co** \n- zarejestruje wydanie Twoich fabcoinów. \n**$top5** \nwyświetli listę 5 osób z największą ilością fabcoinów. \n**$moje** \n-wyświetli ile masz fabcoinów. \nWażne! Zmiany nie są wprowadzane od razu. Każda transakcja przechodzi weryfikację - co może potrwać do 2 dni. \nPrzykładowa poprawne polecenie dodania:\n$dodaj 5 sprzątanie pracowni ")
