def main():
  print("Keep it logically awesome.")

if __name__== "__main__":
  main()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)

  print(quotes[0])
  
  last =13 
  rnd = random.randint(0, last)

  print(quotes[rnd])
  
