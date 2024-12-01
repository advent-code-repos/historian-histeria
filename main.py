from configs.logger import logger
from controllers.factories import create_historian_hysteria

INPUT_PATH = "input.example"


def main():
    logger.info("[AD24 - day 1] Historian Histeria starts")

    historian_hysteria = create_historian_hysteria(logger)
    logger.debug(
        "Historian hysteria controller successfully created "
        f"{historian_hysteria}"
    )

    locations = historian_hysteria.read(INPUT_PATH)
    logger.debug(f"Locations: {locations}")

    left_list, right_list = map(list, locations)
    logger.debug(f"Left list: {left_list}")
    logger.debug(f"Right list: {right_list}")


if __name__ == "__main__":
    main()
