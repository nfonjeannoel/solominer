# import random
#
# def get_random_nonce_1():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)
#
# def get_random_nonce_2():
#     return hex(random.randint(0, 2**32-1))[2:].upper().zfill(8)
#
# def get_random_nonce_3():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)
#
# def get_random_nonce_4():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)
#
# def get_random_nonce_5():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)
#
# def get_random_nonce_6():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)
#
# def get_random_nonce_7():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)
#
# def get_random_nonce_8():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)
#
# def get_random_nonce_9():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)
#
# def get_random_nonce_10():
#     return hex(random.randint(0, 2**32-1))[2:].zfill(8)

import random
import os
import hashlib
import time
import uuid
from datetime import datetime

# Function 1: Using random.getrandbits
def get_random_nonce_1():
    return '{:08x}'.format(random.getrandbits(32))

# Function 2: Using os.urandom and converting to an integer
def get_random_nonce_2():
    return '{:08x}'.format(int.from_bytes(os.urandom(4), 'big'))

# Function 3: Using time-based approach
def get_random_nonce_3():
    return hex(int(time.time() * 1000000) % (2**32))[2:].zfill(8)

# Function 4: Using hash of current time
def get_random_nonce_4():
    return hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]

# Function 5: Using random.SystemRandom for cryptographic security
def get_random_nonce_5():
    return '{:08x}'.format(random.SystemRandom().getrandbits(32))

# Function 6: Using datetime now
def get_random_nonce_6():
    return hex(int(datetime.now().timestamp() * 1000000) % (2**32))[2:].zfill(8)

# Function 7: Using a combination of time and os.urandom
def get_random_nonce_7():
    return hashlib.md5(os.urandom(4) + str(time.time()).encode()).hexdigest()[:8]

# Function 8: Using random.sample
def get_random_nonce_8():
    return ''.join(random.sample('0123456789abcdef', 8))

# Function 9: Using a counter and os.urandom
counter = 0
def get_random_nonce_9():
    global counter
    counter += 1
    return hashlib.sha256(os.urandom(4) + counter.to_bytes(4, 'big')).hexdigest()[:8]

# Function 10: Using UUID4
def get_random_nonce_10():
    return uuid.uuid4().hex[:8]

def get_random_nonce():
    rands = []
