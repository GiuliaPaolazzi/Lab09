from dataclasses import dataclass
@dataclass
class Airports:
    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: float
    LONGITUDE: float
    TIMEZONE_OFFSET: float

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"{self.AIRPORT} ({self.IATA_CODE})"

