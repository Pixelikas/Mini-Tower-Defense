# Em um jogo de Tower Defense, o castelo (torre) tem um total de 500 de HP. 
# Faça um programa no qual o usuário possa escolher entre 3 tipos de ataque e um de defesa: 

# 1) Ataque Bomba -100HP
# 2) Ataque Granada -80HP
# 3) Ataque Arqueiro -40HP
# 4) Defesa Escudo +20HP

# Mostrar o HP do castelo atualizado a cada rodada. 
# Caso o HP do castelo acabe, mostrar "Jogo encerrado, com X rodadas!"


# Create game variables
castleTotalHP = 500; castleMinimumHP = 0; actionOP = 0; roundCount = 0
bombAttack = 100; grenadeAttack = 80; archeryAttack = 40; shieldDefense = 20

# Create a function to the game turn
def startTurn(castleHP, actionType):

    # Match the actionType (actionOP)
    match (actionType):

        # Case action type equals bombAttack
        case 1:

            # Decrease bombAttack damage value from castle HP
            castleHP -= bombAttack

            # Print damage alert and update castle HP
            print(f'\nBOOM! Bomb attack, -{bombAttack}HP! >.<\nCastle HP -> {castleHP}')
                  
        # Case action type equals grenadeAttack
        case 2:

            # Decrease grenadeAttack damage value from castle HP
            castleHP -= grenadeAttack

            # Print damage alert and update castle HP
            print(f'\nPOW! Grenade attack, -{grenadeAttack}HP! >.<\nCastle HP -> {castleHP}')

        # Case action type equals archeryAttack
        case 3:

            # Decrease archeryAttack damage value from castle HP
            castleHP -= archeryAttack

            # Print damage alert and update castle HP
            print(f'\nFTH! Archery attack, -{archeryAttack}HP! >.<\nCastle HP -> {castleHP}')

        # Case action type equals shieldDefense
        case 4:

            # Increase shieldDefense damage value to castle HP
            castleHP += shieldDefense

            # Print damage alert and update castle HP
            print(f'\nUON! Shield defense, +{shieldDefense}HP! :D\nCastle HP -> {castleHP}')

        # Case invalid action number
        case other:

            # Print invalid action alert to player
            print('Invalid action! :(')

    # Function returns castle updated HP
    return castleHP

# Loop condition to finish the gameplay
while castleTotalHP > castleMinimumHP:

    # Player choose action number (action type)
    actionOP = int(input(f'\n(((((( ROUND {roundCount+1} ))))))\n\n1) Bomb Attack -100HP\n2) Grenade Attack -80HP\n3) Archery Attack -40HP\n4) Shield Defense +20HP\n\nAction Number: '))

    # Increase game rounds
    roundCount += 1

    # Castle Total HP update by function return 
    castleTotalHP = startTurn(castleTotalHP, actionOP)

# Game Over
print(f'\n____________________________________\nGAME OVER!!! Castle destroyed... :(\nTotal rounds: {roundCount}.\n\n')