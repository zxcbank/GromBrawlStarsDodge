import spike
import random
import Constants
lt = 350
def generator(all_strikes):
    all_strikes.add(spike.Spike(0, random.randint(0, Constants.HEIGHT), 1 + 3 * random.random(), 0, random.randint(50, lt), True))  #
    all_strikes.add(spike.Spike(random.randint(0, Constants.WIDTH), 0, 0, 1 + 3 * random.random(), random.randint(50, lt), True))
    all_strikes.add(spike.Spike(random.randint(0, Constants.WIDTH), 0, 1 + 3 * random.random(), 1 + 3 * random.random(), random.randint(50, lt), True))

def breakout(x, y, x1, y1):
    if (x1 + 35 >= x >= x1) and (y1 + 35 >= y >= y1):
        return True
    return False

def clamp(cx):
    if 255 * abs(cx) > 255:
        return 255
    return int(255 * abs(cx))