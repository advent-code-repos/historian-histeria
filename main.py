from configs.logger import logger
from controllers.factories import create_historian_hysteria

INPUT_PATH = "inputs/input"


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
    logger.debug(f"Distance value: {distance_value}")

    locations = historian_hysteria.read(INPUT_PATH)
    logger.debug(f"Locations: {locations}")

    distance_occurrence_value = historian_hysteria.distance_occurrence_based(
        locations
    )
    logger.debug(
        f"Distance occurrence based value: {distance_occurrence_value}"
    )

    logger.info(
        "========================= SOLUTIONs =========================="
    )
    logger.info(f"Distance value: {distance_value}")
    logger.info(
        f"Distance occurrence based value: {distance_occurrence_value}"
    )
    logger.info(
        "=============================================================="
    )


if __name__ == "__main__":
    main()
