import asyncio
import time


async def brewCoffee():
  print("Brewing coffee...")
  await asyncio.sleep(5)
  print("Coffee is ready!")
  return "Coffee cup"


async def toastBagel():
  print("Toasting bagel...")
  await asyncio.sleep(2)
  print("Bagel is toasted")
  return "Toasted bagel"


async def main():
  startTime = time.time()
  coffee_task = asyncio.create_task(brewCoffee())
  bagel_task = asyncio.create_task(toastBagel())

  result_coffee = await coffee_task
  result_bagel = await bagel_task

  print(f"Result of coffee: {result_coffee}")
  print(f"Result of bagel: {result_bagel}")

  print("Time taken: ", time.time() - startTime)


if __name__ == "__main__":
  asyncio.run(main())
