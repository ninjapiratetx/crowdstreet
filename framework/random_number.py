
# generate random integer values
import random
import time

FIRST_NUMBER=1
MAX_RNNDOM = 100000

def generate_random_number():
	random.seed(time.time())
	for _ in range(MAX_RNNDOM):
		value = random.randint(FIRST_NUMBER,MAX_RNNDOM )
		return value