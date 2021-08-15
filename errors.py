#Some errors that should be catched...
#... and user should get some output

class AmountNotInt(Exception):
    def __init__(self):
        message = "Twoj FabcoinBot zgłupiał. Ilość fabcoinów nie jest liczbą. Po nazwie polecenia (np. $dodaj) powinna znaleźć się ilość fabcoinów wyrażona jako liczba całkowita (np. 5)."
        super().__init__(message)

class MissingArgument(Exception):
    def __init__(self):
        message = "Twoj FabcoinBot zgłupiał. Po nazwie polecenia (np. $dodaj) brakuje albo podanej ilości fabcoinów lub informacji za co / na co są one (lub obu). Prawidłowa składnia to $podaj (lub $wydaj) ilość za_co np. \n $dodaj 5 sprzątanie pracowni."
        super().__init__(message)
