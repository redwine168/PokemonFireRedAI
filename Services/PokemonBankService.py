import csv
import random
import os
from Models.PokemonModel import Pokemon

class PokemonBankService:

    def __init__(self):
        self.AllPokemonFilename =  "/Users/jonathanredwine/Desktop/Python/PokemonBlueAI/Services/allpokemon.csv"
        self.PokemonNameDictionary = {
            0: {},
            1: {},
            2: {}
        }
        self.MaxLetterOrder = 2
        self.PossibleChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.MinSelfNameLength = 2
        self.MaxSelfNameLength = 7
        self.MinPokemonNameLength = 3
        self.MaxPokemonNameLength = 10
        self.Pokemon = self.ImportPokemonNames()
        self.ReadPokemonNames()
        
        

    def ImportPokemonNames(self):
        print(os.path.dirname(__file__))
        with open(self.AllPokemonFilename, newline = '') as csvfile:
            allPokemon = []
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                joinedRow = ', '.join(row)
                splitRow = joinedRow.split(',')
                if (("Mega" not in splitRow[1]) or (splitRow[1] == "Meganium")):
                    allPokemon.append(Pokemon(splitRow[1].upper(),splitRow[2].upper(),splitRow[3].upper()))
        return allPokemon



    def ReadPokemonNames(self):
        for pokemon in self.Pokemon:
            for i in range(len(pokemon.Name)):
                self.ReadChar(pokemon.Name, i, 0)
                if (i >= 1):
                    self.ReadChar(pokemon.Name, i, 1)
                if (i >= 2):
                    self.ReadChar(pokemon.Name, i, 2)
            self.ReadChar(pokemon.Name + "0", len(pokemon.Name), self.MaxLetterOrder)


    def ReadChar(self, name, i, order):
        try:
            self.PokemonNameDictionary[order][name[i-order:i+1]] += 1
        except:
            self.PokemonNameDictionary[order][name[i-order:i+1]] = 1


    def GenerateSelfName(self):
        name = ""
        currLen = 0
        order = 0
        keepGoing = True
        while (keepGoing):
            letter = self.ChooseLetter(name, order)
            if (letter != "0"):
                name += letter
                currLen += 1
            else:
                if (currLen >= self.MinSelfNameLength):
                    keepGoing = False

            if (currLen >= self.MaxSelfNameLength):
                keepGoing = False

            # increment order if we're not at max order yet
            if (order < self.MaxLetterOrder):
                order += 1
        return name


    def GeneratePokemonName(self):
        name = ""
        currLen = 0
        order = 0
        keepGoing = True
        while (keepGoing):
            letter = self.ChooseLetter(name, order)
            if (letter != "0"):
                name += letter
                currLen += 1
            else:
                if (currLen >= self.MinPokemonNameLength):
                    keepGoing = False

            if (currLen >= self.MaxPokemonNameLength):
                keepGoing = False

            # increment order if we're not at max order yet
            if (order < self.MaxLetterOrder):
                order += 1
        return name


    def ChooseLetter(self, name, order):
        allOptions = self.PokemonNameDictionary[order]
        options = self.FindPossibleOptions(allOptions, name, order)
        maxNum = sum(options.values())
        randInt = random.randrange(maxNum)
        i = 0
        cum = list(options.values())[i]
        while(randInt < maxNum):
            if (randInt < cum):
                return list(options.keys())[i][-1]
            elif (cum < maxNum):
                i += 1
                cum += list(options.values())[i]
        return list(options.keys())[-1][-1]


    def FindPossibleOptions(self, allOptions, name, order):
        # Return all options if order is 0
        if (order == 0):
            return allOptions
        # Otherwise, find options conditioned on previous letters
        prevLetters = name[len(name)-(order):]
        options = {}
        for k in allOptions.keys():
            if (k[0:order] == prevLetters):
                options[k] = allOptions[k]
        return options
            
            


x = PokemonBankService()
    
