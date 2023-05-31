#2
import logging
def write_file(fill_path , data):
    try:
        with open(fill_path , 'w') as file:
            logger = logging.getLogger("File")
            logger.setLevel(logging.INFO)
            logger.addHandler(logging.StreamHandler())
            file.write(data)
            logger.info("Файл успішно записаний")
    except Exception as a:
        logger.error(f"У вашому файлі '{fill_path}' сталася помилка -> {a}")
logging.basicConfig(level=logging.INFO)
write_file("output.txt" , input("Введіть що потрібно вписати файл: "))