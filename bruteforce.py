import itertools
import string
import time

password = "abc123"  
alphabet = string.ascii_lowercase  

def brute_force(password, alphabet):
    start_time = time.time()
    attempts = 0

    for length in range(1, len(password) + 1):
        for guess in itertools.product(alphabet, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)

            if guess_password == password:
                end_time = time.time()
                return guess_password, attempts, end_time - start_time

    return None, attempts, time.time() - start_time

found_password, attempts, elapsed_time = brute_force(password, alphabet)

if found_password:
    print("Password found:", found_password)
    print("Attempts:", attempts)
    print("Execution time:", round(elapsed_time, 4), "seconds")
else:
    print("Password not found.")

