# M12P4 Module 12 Patrick Chang 11/25/2026

#define functions
def display_players(names, averages):
  for i in range(10):
    print(names[i], averages[i])


def search_player(names, averages, target):
  found = False
  for i in range(10):
    if names[i].lower() == target.lower():
      print(names[i], averages[i])
      found = True
  if not found:
    print("Player not found.")


#define variables
def main():
  names = []
  averages = []

  f = open("players.txt", "r")
  line = f.readline()

  while line != "":
    names.append(line.strip())
    avg = float(f.readline().strip())
    averages.append(avg)
    line = f.readline()

  f.close()

  #outputs
  print("Player List:")
  display_players(names, averages)

  #prompt loop
  search_name = input("\nEnter a last name to search (or 'quit' to stop): ")
  while search_name.lower() != "quit":
    search_player(names, averages, search_name)
    search_name = input("\nEnter a last name to search (or 'quit' to stop): ")


main()