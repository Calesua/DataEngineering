from dataclass import dataclass
from datetime import datetime

@dataclass
class TrafficEvent:
    """Class representing a traffic event."""

    location: str
    traffic_level: int
    timestamp: datetime

    def to_dict(self) -> dict:
        """Convert the TrafficEvent instance to a dictionary."""
        
        return {
            "location": self.location,
            "traffic_level": self.traffic_level,
            "timestamp": self.timestamp.isoformat(),
        }