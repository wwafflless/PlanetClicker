import logging

# Logger = logging.getLogger("Logger")
# Logger.setLevel(logging.DEBUG)  # Set the threshold for this logger to DEBUG

# ConsoleHandler = logging.StreamHandler()
# ConsoleHandler.setLevel(logging.DEBUG)


class GameLogger(logging.Logger):
    def __init__(self) -> None:
        super().__init__("GameLogger")
        self.setLevel(logging.DEBUG)  # Set the threshold for this logger to DEBUG

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler = logging.FileHandler("error.log")
        file_handler.setFormatter(formatter)

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.addHandler(console_handler)
        self.addHandler(file_handler)
