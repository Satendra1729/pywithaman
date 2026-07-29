import logging
import sys



def logging_setup():

    log_format = logging.Formatter(
     fmt="{asctime} - {levelname} - {message}",
    style="{"
    )

    file_handler = logging.FileHandler("app.log", mode="a")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(log_format)


    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(log_format)

    logging.basicConfig(
      level = logging.DEBUG,
      handlers = [file_handler,console_handler]
    )

if __name__ == "__main__" : 
    logging_setup()
    logging.info("This is info")
    logging.warning("This is warning")
    logging.debug("This is debug")
    logging.error("This is error")




