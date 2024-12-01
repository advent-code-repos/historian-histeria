from services.file_service import FileService
from services.location_service import LocationService


class HistorianHysteria:
    def __init__(self, logger):
        self.logger = logger
        self._file_service = FileService(logger)
        self._location_service = LocationService(logger)
        self._cached_pairs = None

    def read(self, path: str):
        self.logger.info(f"Read input starts with {path} path")
        self.logger.debug(f"Params path: {path}")
        try:
            locations = self._file_service.read(path)
            self._locations = locations
            self.logger.debug(f"Locations: {locations}")
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
        self.logger.info(f"Read input ends with {path} path")
        return locations

    def distance(self, locations):
        self.logger.info("Distance operation starts.")
        self.logger.debug(f"Params locations: {locations}")

        pairs = self._check_pairs(locations)
        self.logger.debug(f"Pairs: {pairs[0]} and {pairs[1]}")

        distance_value = self._location_service.distance(pairs)
        self.logger.debug(f"Return value distance_value: {distance_value}")

        self.logger.info("Distance operation ends.")
        return distance_value

    def distance_occurrence_based(self, locations):
        self.logger.info("Distance operation starts.")
        self.logger.debug(f"Params locations: {locations}")

        pairs = self._check_pairs(locations)
        self.logger.debug(f"Pairs: {pairs[0]} and {pairs[1]}")

        distance_value = self._location_service.distance_occurrence_based(
            pairs
        )
        self.logger.debug(f"Return value distance_value: {distance_value}")

        self.logger.info("Distance operation ends.")
        return distance_value

    def _check_pairs(self, locations):
        self.logger.debug(f"cached pairs: {self._cached_pairs}")
        if self._cached_pairs is not None:
            self.logger.debug("Returning cached pairs.")
            return self._cached_pairs
        else:
            self.logger.debug("Pair operation starts.")
            self._cached_pairs = self._location_service.pair(locations)
            return self._cached_pairs
