from prettytable import PrettyTable
import prettytable

table = PrettyTable()

pokemon_names = ["Pikachu", "Squirtle", "Charmander"]
pokemon_types = ["Electric", "Water", "Fire"]

table.add_column("Pokemon Name", pokemon_names)
table.add_column("Type", pokemon_types)
table.align = 'l'

print(table.get_string(sortby = "Type", reversedsort = True))
