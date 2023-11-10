### Experiments with asyncio in Python

The puropose of this project is to demonstrate how asyncio can be used to provide for concurreny in Python.

To ilustrate the "paralelism" of the tasks, a spinner will run while the tasks are being carried out. When both taks are finished, the spinner is stoped(canceled actually).

The spinners can be created by a series of printable things (strings or chars or emojis) that will be repeteadly printed on top of the previous using the ```end="\r"``` parameter of the ```print```function. This is the famous ```carriage return``` character that makes the printing cursor (the cursor that points to where the next char will be printed) to the begining of the line. By default, Python ```print``` ends the print sequence with a ```\\n``` char that causes the print cursor to jump to the begining of the next line (hence the ```\\n```). With this technique it's possible to create many animations. 

## Challenge proposed - Level easy

Create new kind of animations by creating different sequences of stuff to be printed over the previous. Follow the examples on the code and create a new one.

## Challenge proposed - Level medium

Create a new spinner that shows how much % of the tasks are done.

