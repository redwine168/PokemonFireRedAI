
import pyreadstat

class SaveFileReaderService:

    def __init__(self):
        self.SaveFilename = "pokemonblue.sav"
    


    def ReadSaveFile(self):
        x = 3
        #df, meta = pyreadstat.read_sav("pokemonblue.sav")