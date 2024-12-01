class LocationService:
    def __init__(self, logger):
        self.logger = logger

    def distance(self, locations):
        self.logger.info("Pair operation starts")
        self.logger.debug(f"Params locations: {locations}")

        left_list, right_list = map(lambda x: sorted(x), locations)
        self.logger.debug(
            f"Sorted left list: {left_list} "
            f"Sorted right list: {right_list}"
        )

        distance_value = sum(
            abs(left - right) for left, right in zip(left_list, right_list)
        )

        self.logger.debug(f"Distance value: {distance_value}")

        self.logger.info("Pair operation ends")
        return distance_value
