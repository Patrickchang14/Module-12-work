# M12P2 Module 12 Patrick Chang 11/24/2026

#define variables
def display_names(names, scores):
  for i in range(10):
    print(names[i], scores[i])


def display_reverse(names, scores):
  for i in range(9, -1, -1):
    print(names[i], scores[i])


#names and scores
def main():
  names = [
      "Pinky",
      "Browny",
      "Yellowy",
      "Orangey",
      "Bluey",
      "Purpley",
      "Redy",
      "Greeny",
      "Blacky",
      "Whitey",
  ]
  scores =[10,20,30,40,50,60,70,80,90,100]

#output in order
  print("Names and scores in order:")
  display_names(names, scores)

#output in reverse
  print("\nNames and scores in reverse:")
  display_reverse(names, scores)


main()