from unittest import TestCase
from ratelimiter.event import Event

from ratelimiter.ratelimiter import RateLimiter

example_events = [
  Event(
    1559318000,
    10,
    "Vlad",
  ),
  Event(
    1559318030,
    10,
    "Vlad",
  ),
  Event(
    1559318040,
    20,
    "Vlad",
  ),
  Event(
    1559318040,
    20,
    "Vlad_the_alchemist",
  ),
  Event(
    1559318070,
    20,
    "Vlad",
  ),
]

class RateLimiterTest(TestCase):
  def test(self):
    rateLimiter = RateLimiter(
      time_window = 60.0,
      limit = 30,
    )
    actual = list(map(rateLimiter.rate_limit, example_events))
    expected = [10, 10, 10, 20, 10]
    self.assertEqual(actual, expected)