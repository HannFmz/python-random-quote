def main():
  print("Keep it logically awesome.main()")

  f = open("quotes")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__main__":
  main()
