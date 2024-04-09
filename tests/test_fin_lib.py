# (c) 2022- Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from .hwtest.unittest import HomeworkModuleTestCase
from .hwtest import autograde as grade

from typing import Callable, List, Protocol

class Summable(Protocol):
  def __add__(self, other: "Summable") -> "Summable": ...


# Note: we use float in type annotations, even though that doesn't *fully*
#  capture requirements (ok, since we have these just to sush Pylance/Pylint...)
daily_rates: Callable[[List[float]], List[float]]
daily_prices: Callable[[float, List[float]], List[float]]


class DailyRatesTests(HomeworkModuleTestCase):
  __scriptname__ = "fin_lib.py"
  __modulename__ = "fin_lib"
  __attrnames__ = [ "daily_rates" ]

  @grade.score(4)
  def test_simple(self):
    with self.assertUnmodified([100.0, 80.0, 100.0, 110.0]) as arg:
      self.assertListAlmostEqual([-0.2, 0.25, 0.10], daily_rates(arg))

  @grade.score(2)
  def test_empty(self):
    with self.assertUnmodified([]) as arg:
      self.assertListEqual([], daily_rates(arg))
      self.assertIsNot

  @grade.score(2)
  def test_empty_not_alias(self):
    with self.assertUnmodified([]) as empty:
      result = daily_rates(empty)
      self.assertIsNot(empty, result, msg="Must always return a new list")

  @grade.score(2)
  def test_singleton(self):
    with self.assertUnmodified([100.0]) as arg:
      self.assertListEqual([], daily_rates(arg))

  @grade.score(2)
  def test_pairs(self):
    with self.assertUnmodified([100.0, 20.0]) as arg:
      self.assertListAlmostEqual([-0.8], daily_rates(arg))
    with self.assertUnmodified([100.0, 180.0]) as arg:
      self.assertListAlmostEqual([0.8], daily_rates(arg))
    with self.assertUnmodified([200.0, 360.0]) as arg:
      self.assertListAlmostEqual([0.8], daily_rates(arg))

  @grade.score(3)
  def test_constant(self):
    with self.assertUnmodified([100.0] * 10) as arg:
      self.assertListAlmostEqual([0.0] * 9, daily_rates(arg))
    with self.assertUnmodified([-100.0] * 100) as arg:
      self.assertListAlmostEqual([0.0] * 99, daily_rates(arg))


class DailyPricesTests(HomeworkModuleTestCase):
  __scriptname__ = "fin_lib.py"
  __modulename__ = "fin_lib"
  __attrnames__ = [ "daily_prices" ]

  @grade.score(6)
  def test_simple(self):
    with self.assertUnmodified([-0.2, 0.25, 0.10]) as rates:
      self.assertListAlmostEqual([100.0, 80.0, 100.0, 110.0], daily_prices(100.0, rates))
    with self.assertUnmodified([-0.2, 0.25, 0.10]) as rates:
      self.assertListAlmostEqual([150.0, 120.0, 150.0, 165.0], daily_prices(150.0, rates))

  @grade.score(4)
  def test_empty_rates(self):
    with self.assertUnmodified([]) as rates:
      self.assertListAlmostEqual([100.0], daily_prices(100.0, rates))
    with self.assertUnmodified([]) as rates:
      self.assertListAlmostEqual([-200.0], daily_prices(-200.0, rates))

  @grade.score(5)
  def test_exponential(self):
    with self.assertUnmodified([0.0] * 50) as rates:
      self.assertListAlmostEqual([100.0] * 51, daily_prices(100.0, rates))
    with self.assertUnmodified([0.1] * 50) as rates:
      self.assertListAlmostEqual(
        [100.0*(1.1**e) for e in range(51)],
        daily_prices(100.0, rates)
      )
