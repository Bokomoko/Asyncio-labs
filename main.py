import time


def brewCoffee():
  print("Brewing coffee...")
  time.sleep(5)
  print("Coffee is ready!")
  return "Coffee cup"


def toastBagle():
  print("Toasting bagel...")
  time.sleep(2)
  print("Bagel is toasted")
  return "Toasted bagel"


def main():
  startTime = time.time()
  result_coffee = brewCoffee()
  result_bagel = toastBagle()
  print(f"Result of coffee: {result_coffee}")
  print(f"Result of bagel: {result_bagel}")

  print("Time taken: ", time.time() - startTime)


if __name__ == "__main__":
  main()
