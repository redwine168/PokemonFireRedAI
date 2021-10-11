
from AI.Agent import Agent
from Services.SaveFileReaderService import SaveFileReaderService

def main():

    agent = Agent()
    print(agent.AgentName)


    sfrs = SaveFileReaderService()
    
    while(True):
        print("1 - Self name")
        print("2 - Pokemon name")

        i = input("Choice: ")
        if (i == "1"):
            print(agent.PokemonBankService.GenerateSelfName())
        if (i == "2"):
            print(agent.PokemonBankService.GeneratePokemonName())


main()