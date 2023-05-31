#3
import random
import logging

logging.basicConfig(filename='info.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
def generate_numbers(file_path, n):
    try:
        with open(file_path, "w") as file:
            for i in range(n):
                random_number = random.randint(1, 200)
                file.write(str(random_number) + '\n')
                logging.info(f"Рандомне число: {random_number}")
    except Exception as e:
        logging.error(f"Error: {e}")
file_path = "numbers.txt"
num_numbers = 4
generate_numbers(file_path, num_numbers)