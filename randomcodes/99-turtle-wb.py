#
#-------------------------------------------------------------------
#
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

clear()
delay(10)

begin_fill()
while True:
    forward(400)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
#  - I still don't know what this code works. I need to check turtle 
# documenation and samples.
#
#-------------------------------------------------------------------
#
