import csv

# To use this tool, just click the "Run" triangle at the top of the window and type in the pokemon you are searching for

typeChart = {
    'Normal': {
        'Strong Against': 'Nothing',
        'Weak Against': ['Rock', 'Ghost', 'Steel'],
        'Resistant To': 'Ghost',
        'Vulnerable To': 'Fighting'
    },
    'Fighting': {
        'Strong Against': ['Rock', 'Steel', 'Ice', 'Dark', 'Normal'],
        'Weak Against': ['Poison', 'Flying', 'Bug', 'Ghost', 'Fairy'],
        'Resistant To': ['Dark', 'Rock', 'Bug'],
        'Vulnerable To': ['Psychic', 'Fairy', 'Flying']
    },
    'Flying': {
        'Strong Against': ['Bug', 'Grass', 'Fighting'],
        'Weak Against': ['Electric', 'Rock', 'Steel'],
        'Resistant To': ['Fighting', 'Bug', 'Ground', 'Grass'],
        'Vulnerable To': ['Ice', 'Electric', 'Rock']
    },
    'Poison': {
        'Strong Against': ['Grass', 'Fairy'],
        'Weak Against': ['Ghost', 'Steel', 'Rock', 'Ground', 'Poison'],
        'Resistant To': ['Fighting', 'Poison', 'Grass', 'Fairy'],
        'Vulnerable To': ['Psychic', 'Ground']
    },
    'Ground': {
        'Strong Against': ['Poison', 'Rock', 'Steel', 'Fire', 'Electric'],
        'Weak Against': ['Flying', 'Grass', 'Bug'],
        'Resistant To': ['Rock', 'Poison', 'Electric'],
        'Vulnerable To': ['Water', 'Grass', 'Ice']
    },
    'Rock': {
        'Strong Against': ['Psychic', 'Bug', 'Fire', 'Ice'],
        'Weak Against': ['Flying', 'Ground', 'Steel'],
        'Resistant To': ['Normal', 'Flying', 'Poison', 'Fire'],
        'Vulnerable To': ['Fighting', 'Ground', 'Steel', 'Water', 'Grass']
    },
    'Bug': {
        'Strong Against': ['Psychic', 'Dark', 'Grass'],
        'Weak Against': ['Fighting', 'Ghost', 'Steel', 'Fairy', 'Fire', 'Poison', 'Flying'],
        'Resistant To': ['Grass', 'Ground', 'Fighting'],
        'Vulnerable To': ['Flying', 'Rock', 'Fire']
    },
    'Ghost': {
        'Strong Against': ['Ghost', 'Psychic'],
        'Weak Against': ['Normal', 'Dark'],
        'Resistant To': ['Normal', 'Fighting', 'Poison', 'Bug'],
        'Vulnerable To': ['Normal', 'Fighting', 'Poison', 'Bug']
    },
    'Steel': {
        'Strong Against': ['Fairy', 'Ice', 'Rock'],
        'Weak Against': ['Electric', 'Water', 'Fire', 'Steel'],
        'Resistant To': ['Fairy', 'Dragon', 'Ice', 'Psychic', 'Steel', 'Grass', 'Poison', 'Normal', 'Flying', 'Rock'],
        'Vulnerable To': ['Ground', 'Fighting', 'Fire']
    },
    'Fire': {
        'Strong Against': ['Grass', 'Bug', 'Steel', 'Ice'],
        'Weak Against': ['Dragon', 'Rock', 'Fire', 'Water'],
        'Resistant To': ['Fire', 'Grass', 'Bug', 'Steel', 'Ice'],
        'Vulnerable To': ['Ground', 'Rock', 'Water']
    },
    'Water': {
        'Strong Against': ['Ground', 'Rock', 'Fire'],
        'Weak Against': ['Water', 'Grass', 'Dragon'],
        'Resistant To': ['Steel', 'Water', 'Fire', 'Ice'],
        'Vulnerable To': ['Electric', 'Grass']
    },
    'Grass': {
        'Strong Against': ['Ground', 'Rock', 'Water'],
        'Weak Against': ['Flying', 'Poison', 'Bug', 'Steel', 'Fire', 'Grass', 'Dragon'],
        'Resistant To': ['Ground', 'Water', 'Grass', 'Electric'],
        'Vulnerable To': ['Flying', 'Poison', 'Bug', 'Fire', 'Ice']
    },
    'Electric': {
        'Strong Against': ['Flying', 'Water'],
        'Weak Against': ['Ground', 'Grass', 'Electric', 'Dragon'],
        'Resistant To': ['Flying', 'Steel', 'Electric'],
        'Vulnerable To': ['Ground']
    },
    'Psychic': {
        'Strong Against': ['Fighting', 'Poison'],
        'Weak Against': ['Steel', 'Psychic', 'Dark'],
        'Resistant To': ['Fighting', 'Psychic'],
        'Vulnerable To': ['Bug', 'Ghost', 'Dark']
    },
    'Ice': {
        'Strong Against': ['Flying', 'Ground', 'Grass', 'Dragon'],
        'Weak Against': ['Steel', 'Fire', 'Water', 'Ice'],
        'Resistant To': ['Ice'],
        'Vulnerable To': ['Fighting', 'Rock', 'Steel', 'Fire']
    },
    'Dragon': {
        'Strong Against': ['Dragon'],
        'Weak Against': ['Steel', 'Fairy'],
        'Resistant To': ['Fire', 'Water', 'Grass', 'Electric'],
        'Vulnerable To': ['Ice', 'Dragon', 'Fairy']
    },
    'Fairy': {
        'Strong Against': ['Fighting', 'Dragon', 'Dark'],
        'Weak Against': ['Poison', 'Steel', 'Fire'],
        'Resistant To': ['Fighting', 'Bug', 'Dragon', 'Dark'],
        'Vulnerable To': ['Poison', 'Steel']
    },
    'Dark': {
        'Strong Against': ['Ghost', 'Psychic'],
        'Weak Against': ['Fighting', 'Dark', 'Fairy'],
        'Resistant To': ['Ghost', 'Psychic', 'Dark'],
        'Vulnerable To': ['Fighting', 'Bug', 'Fairy']
    },
}

reader = csv.DictReader(open('pokemon.csv', 'r'))
pokemon = []

for line in reader:
    pokemon.append(line)

pokemonNameList = []


for i in range(len(pokemon)):
    pokemonNameList.append(pokemon[i]['NAME'])

loop = 0
while loop == 0:
    pokeSearch = input('What Pokemon are you looking up? ').title()
    if pokeSearch not in pokemonNameList:
        print("Sorry, that pokemon can't be found, please check the spelling and try again!")
    else:
        loop = 1

for i in range(len(pokemon)):
    if pokeSearch not in pokemonNameList:
        print("Sorry, that pokemon can't be found, please check the spelling and try again!")
        break
    else:
        if pokemon[i]['NAME'] == pokeSearch:
            if pokemon[i]['TYPE2'] == '':
                type = [pokemon[i]['TYPE1']]
                print('Type:', type[0])
                print('Strong against:', typeChart[type[0]]['Strong Against'])
                print('Weak against:', typeChart[type[0]]['Weak Against'])
                print('Resistant to:', typeChart[type[0]]['Resistant To'])
                print('Vulnerable to:', typeChart[type[0]]['Vulnerable To'])
            else:
                type = [pokemon[i]['TYPE1'],pokemon[i]['TYPE2']]
                print('Type: ', type[0], 'and', type[1])
                print(type[0], 'is strong against:', typeChart[type[0]]['Strong Against'])
                print(type[0], 'is weak against:', typeChart[type[0]]['Weak Against'])
                print(type[0], 'is resistant to:', typeChart[type[0]]['Resistant To'])
                print(type[0], 'is vulnerable to:', typeChart[type[0]]['Vulnerable To'])
                print(type[1], 'is strong against:', typeChart[type[1]]['Strong Against'])
                print(type[1], 'is weak against:', typeChart[type[1]]['Weak Against'])
                print(type[1], 'is resistant to:', typeChart[type[1]]['Resistant To'])
                print(type[1], 'is vulnerable to:', typeChart[type[1]]['Vulnerable To'])
                break




