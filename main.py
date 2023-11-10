import time
import asyncio


async def brewCoffee():
  print("Brewing coffee...")
  await asyncio.sleep(5)
  print("Coffee is ready!")
  return "Coffee cup"


async def toastBagle():
  print("Toasting bagel...")
  await asyncio.sleep(2)
  print("Bagel is toasted")
  return "Toasted bagel"


async def main():
  startTime = time.time()
  batch = asyncio.gather(brewCoffee(), toastBagle())
  result_coffee, result_bagel = await batch
  print(f"Result of coffee: {result_coffee}")
  print(f"Result of bagel: {result_bagel}")

  print("Time taken: ", time.time() - startTime)


if __name__ == "__main__":
  asyncio.run(main())
