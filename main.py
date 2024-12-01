from configs.logger import logger
from controllers.factories import create_historian_hysteria

INPUT_PATH = "inputs/input.first"


def main():
    logger.info("[AD24 - day 1] Historian Histeria starts")

    historian_hysteria = create_historian_hysteria(logger)
    logger.debug(
        "Historian hysteria controller successfully created "
        f"{historian_hysteria}"
    )

    locations = historian_hysteria.read(INPUT_PATH)
    logger.debug(f"Locations: {locations}")

    distance_value = historian_hysteria.distance(locations)
    logger.info(f"Distance value: {distance_value}")


if __name__ == "__main__":
    main()
