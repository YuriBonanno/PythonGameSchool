import datetime
from datetime import *

def update():
    print("update")
    pass

def render():
    print("render")
    pass

previous = datetime.now().microsecond
lag = 0.0
aSecond = 0
while True:
    current = datetime.now().microsecond
    elapsed = current - previous
    previous = current
    lag = lag + elapsed
    print(elapsed)
    while lag >= (1/60)*datetime.second:
        update()
        lag - (1/60)*datetime.second

    if aSecond == 60:
        print("een seconde is voorbij bitches")
        aSecond = 0

    render()
    aSecond = aSecond + 1
