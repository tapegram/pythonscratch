from dataclasses import dataclass


@dataclass
class Record:
  timestamp: int
  count: int

class History:
  def __init__(self):
    self.state = dict()

  def getOpsCount(self, consumer: str, after: int, length: int) -> int:
    """
    consumer: name/key of the consumer
    after: unix timestamp to use as predicate to determine which ops to count (inclusive)
    length: number of seconds to include ops after the `after` param (also inclusive)
    """
    records = filter(
      lambda r: r.timestamp >= after and r.timestamp <= (after + length),
      self.state.get(consumer, [])
    )
    return sum([record.count for record in records])

  def addOps(self, count: int, consumer: str, timestamp: int):
    """
    count: number of opps to add
    consumer: name of the consumer to save as a key
    timestamp: unixtimestamp associated with the ops
    """
    prev = self.state.get(consumer, [])
    self.state[consumer] = prev + [Record(timestamp, count)]
