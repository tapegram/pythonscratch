from dataclasses import dataclass


@dataclass
class Event:
  timestamp: int #  UnixTimestamp (seconds)
  numberOfOperations: int
  consumer: str