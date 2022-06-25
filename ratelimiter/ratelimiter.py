from dataclasses import dataclass
from ratelimiter.event import Event
from ratelimiter.history import History

class RateLimiter:
  def __init__(
    self,
    time_window: float,
    limit: int,
  ):
    self.time_window = time_window
    self.limit = limit
    self.history = History()

  def rate_limit(self, evt: Event) -> int:
    count = self.history.getOpsCount(
      consumer=evt.consumer,
      after=evt.timestamp - self.time_window,
      length=self.time_window,
    )
    allowable_ops = min(evt.numberOfOperations, self.limit - count)
    allowable_ops = max(allowable_ops, 0)  # Just in case we have bad data, we should put the lower limit on 0

    self.history.addOps(consumer=evt.consumer, count=allowable_ops, timestamp=evt.timestamp)

    return allowable_ops
