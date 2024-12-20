class LocationService:
    def __init__(self, logger):
        self.logger = logger

    def pair(self, locations):
        self.logger.info("Pair operation starts")
        self.logger.debug(f"Params locations: {locations}")

        if not locations:
            self.logger.error("No locations data found, exiting.")
            return

        left_list, right_list = map(lambda x: sorted(x), locations)
        self.logger.debug(
            f"Sorted left list: {left_list} "
            f"Sorted right list: {right_list}"
        )
        return left_list, right_list

    def distance(self, pairs):
        self.logger.info("Distance operation starts")
        left_list = pairs[0]
        right_list = pairs[1]
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

    def distance_occurrence_based(self, pairs):
        self.logger.info("Distance occurrence based operation starts")
        left_list = pairs[0]
        right_list = pairs[1]
        self.logger.debug(
            f"Sorted left list: {left_list} "
            f"Sorted right list: {right_list}"
        )

        distance_value = sum(
            left * right_list.count(left) for left in left_list
        )

        self.logger.debug(f"Distance value: {distance_value}")

        self.logger.info("Pair operation ends")
        return distance_value
