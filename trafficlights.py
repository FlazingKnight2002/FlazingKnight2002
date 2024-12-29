import time
from itertools import cycle
lights = [
    ('Green' , 2),
    ('Yellow' , 0.5),
    ('Red' , 3)
] 
i = 1
while True:
    c,s =  lights[i]
    print(c)
    time.sleep(s)
    if i == len(lights) - 1:
        i = 0
    else: 
        i += 1