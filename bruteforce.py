import itertools
import string
import time

password = "abc"  
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
    print("Contraseña encontrada:", found_password)
    print("Intentos realizados:", attempts)
    print("Tiempo de ejecución:", round(elapsed_time, 4), "segundos")
else:
    print("No se encontró la contraseña.")
