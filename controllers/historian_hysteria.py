from services.file_service import FileService


class HistorianHysteria:
    def __init__(self, logger):
        self.logger = logger
        self._file_service = FileService(logger)

    def read(self, path: str):
        self.logger.info(f"Read input at {path} path")
        try:
            locations = self._file_service.read(path)
            self.logger.debug(f"Locations: {locations}")
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
        return locations
