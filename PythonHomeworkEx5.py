bestRappers= ["Kendrick", "J.Cole", "JID"]
print("Best rappers are: ", bestRappers)
userInput = input("Add an artist or press q to quit")



while userInput != 'q':
    def newBestRappers():
        for rappers in bestRappers:
            bestRappers.append(userInput)

    userInput = newBestRappers()



