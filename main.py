import asyncio
import itertools
import time

isBagelReady = False
spinners = [
    r'\|/-', r'.oO*Oo.', r'😀😃😄😁😆🥹😅😂🙂', r'😛😝😜🤪🤪😜😝😛',
    [".", "..", "...", "....", "    "], [">", " >", "  >", "   >", "    "],
    ["8=o", "8==o", "8===o", "8====o", "8=====o", "8======o", "        "]
]
# the following for will loop infinetely thru the sequences
mySpinner = spinners[1]


async def brewCoffee():
  print("Brewing coffee...")
  await asyncio.sleep(2)
  print("Coffee is ready!")
  return "Coffee cup"


async def toastBagel():
  global isBagelReady
  print("Toasting bagel...")
  await asyncio.sleep(7)
  isBagelReady = True
  print("Bagel is toasted")
  return "Toasted bagel"


async def showRotatingSequence(spinStyle, speed: float = 0.1):
  for char in itertools.cycle(spinStyle):
    status = char
    print(status, end='\r', flush=True)
    try:
      await asyncio.sleep(speed)  # sleep for 100ms
    except asyncio.CancelledError:  # if a cancel is receive ...
      break  # jump out of the loop
  # clean the output line
  print("", flush=True)
  return None


async def main():
  startTime = time.time()
  # start the spinner
  # chose the style of the spinner from 0 to 3 (0 is default)
  spinner = asyncio.create_task(showRotatingSequence(mySpinner))
  coffee_task = asyncio.create_task(brewCoffee())
  bagel_task = asyncio.create_task(toastBagel())
  result_coffee = await coffee_task
  # if the coffee get's ready before the bagel, cancel the bagel
  result_bagel = await bagel_task
  # all results came back so we stop/cancel the spinner
  spinner.cancel()
  print(f"Result of coffee: {result_coffee}")
  print(f"Result of bagel: {result_bagel}")

  print("Time taken: ", time.time() - startTime)


if __name__ == "__main__":
  asyncio.run(main())
