# M12P3 Module 12 Patrick Chang

#define functions
def display_names(names, scores):
  for i in range(10):
    print(names[i], scores[i])


def display_reverse(names, scores):
  for i in range(9, -1, -1):
    print(names[i], scores[i])


def display_high_low(names, scores):
  high_var = 0
  high_index = 0
  low_var = 999
  low_index = 0

  for i in range(10):
    if scores[i] > high_var:
      high_var = scores[i]
      high_index = i
    if scores[i] < low_var:
      low_var = scores[i]
      low_index = i

  print("\nHighest score:", names[high_index], high_var)
  print("Lowest score:", names[low_index], low_var)


#define variables
def main():
  names = []
  scores = []

  f = open("scores.txt", "r")
  line = f.readline()

  while line != "":
    names.append(line.strip())
    score = int(f.readline().strip())
    scores.append(score)
    line = f.readline()

  f.close()

  #outputs
  print("Names and scores in order:")
  display_names(names, scores)

  print("\nNames and scores in reverse:")
  display_reverse(names, scores)

  display_high_low(names, scores)


main()