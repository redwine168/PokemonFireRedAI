
from Services.PokemonBankService import PokemonBankService

class Agent:

    def __init__(self):
        self.PokemonBankService = PokemonBankService()
        self.AgentName = self.PokemonBankService.GenerateSelfName()