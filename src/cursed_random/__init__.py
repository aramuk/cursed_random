import sys
import random as real_random

rand_mod = real_random.choice(sys.modules.keys())

print(rand_mod)