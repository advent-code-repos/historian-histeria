from services.file_service import FileService
from services.location_service import LocationService


class HistorianHysteria:
    def __init__(self, logger):
        self.logger = logger
        self._file_service = FileService(logger)
        self._location_service = LocationService(logger)

    def read(self, path: str):
        self.logger.info(f"Read input starts with {path} path")
        self.logger.debug(f"Params path: {path}")
        try:
            locations = self._file_service.read(path)
            self.logger.debug(f"Locations: {locations}")
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
        self.logger.info(f"Read input ends with {path} path")
        return locations

    def distance(self, locations):
        self.logger.info("Distance operation starts.")
        self.logger.debug(f"Params locations: {locations}")

        distance_value = self._location_service.distance(locations)
        self.logger.debug(f"Return value distance_value: {distance_value}")

        self.logger.info("Distance operation ends.")
        return distance_value

    def distance_occurrence_based(self, locations):
        self.logger.info("Distance operation starts.")
        self.logger.debug(f"Params locations: {locations}")

        distance_value = self._location_service.distance_occurrence_based(
            locations
        )
        self.logger.debug(f"Return value distance_value: {distance_value}")

        self.logger.info("Distance operation ends.")
        return distance_value
