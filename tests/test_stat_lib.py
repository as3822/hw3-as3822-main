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
geometric_mean: Callable[[List[float]], float]
running_mean: Callable[[List[float]], List[float]]


# Private type, to test if solutions handle input types abstractly (w/o 
# resorting to "ugly" tricks..)
class Counter:
  def __init__(self, i=0):
    self.i = i

  def __add__(self, other: "Counter") -> "Counter":
    assert isinstance(other, self.__class__)
    return self.__class__(self.i + other.i)

  # TODO __eq__ is only needed for test asserts, but.. no way someone can find a 
  #   way to exploit (at least without introspection?--and if they can do that...)
  def __eq__(self, other) -> bool:
    if isinstance(other, self.__class__):
      return self.i == other.i
    else:
      return False

  def __repr__(self):
    # return f"{self.__class__.__name__}({self.i})"
    return f"Counter({self.i})"


class GeometricMeanTests(HomeworkModuleTestCase):
  __scriptname__ = "stat_lib.py"
  __modulename__ = "stat_lib"
  __attrnames__ = [ "geometric_mean" ]

  @grade.score(2)
  def test_singletons(self):
    self.assertAlmostEquals(0.0, geometric_mean([0.0]), places=5)
    self.assertAlmostEquals(1.0, geometric_mean([1.0]), places=5)
    self.assertAlmostEquals(10.0, geometric_mean([10.0]), places=5)

  @grade.score(1)
  def test_pair(self):
    self.assertAlmostEquals(2.0, geometric_mean([2.0, 2.0]))
    self.assertAlmostEquals(1.4142135623730951, geometric_mean([1.0, 2.0]))
    self.assertAlmostEquals(1.4142135623730951, geometric_mean([2.0, 1.0]))

  @grade.score(4)
  def test_simple(self):
    self.assertAlmostEquals(3.6633153005840806, geometric_mean([3.5, 10.0, 1.5, 1.1, 8.7, 5.3, 2.9, 4.2]))
    # Also try a couple of permutations -- random (well, not really..), non-exhaustive)
    self.assertAlmostEquals(3.6633153005840806, geometric_mean([4.2, 2.9, 5.3, 8.7, 1.1, 1.5, 10.0, 3.5]))  # reversed
    self.assertAlmostEquals(3.6633153005840806, geometric_mean([10.0, 1.5, 1.1, 8.7, 5.3, 2.9, 4.2, 3.5]))  # rot by +1
    self.assertAlmostEquals(3.6633153005840806, geometric_mean([4.2, 3.5, 10.0, 1.5, 1.1, 8.7, 5.3, 2.9]))  # rot by -1
    self.assertAlmostEquals(3.6633153005840806, geometric_mean([1.1, 1.5, 10.0, 3.5, 4.2, 2.9, 5.3, 8.7]))  # mirror around midpoint

  @grade.score(2)
  def test_input_unmodified(self):
    with self.assertUnmodified([3.5, 10.0, 1.5, 1.1, 8.7, 5.3, 2.9, 4.2]) as data:
          self.assertAlmostEquals(3.6633153005840806, geometric_mean(data))

  @grade.score(1)
  def test_uses_product(self):
    import list_lib
    with self.assertAccesses(list_lib.product, module_names=['list_lib', 'stat_lib']):
      geometric_mean([1.0, 1.0])  # Don't care about return value here


class RunningMeanTests(HomeworkModuleTestCase):
  __scriptname__ = "stat_lib.py"
  __modulename__ = "stat_lib"
  __attrnames__ = [ "running_mean" ]

  @grade.score(3)
  def test_empty(self):
    with self.assertUnmodified([]) as arg:
      result = running_mean(arg)
      self.assertListEqual([], result)
      self.assertIsNot(arg, result, msg="Should *always* return *new* list")

  @grade.score(3)
  def test_singletons(self):
    arg, expected = [10], [10.0]
    with self.assertUnmodified(arg):
      result = running_mean(arg)
      self.assertListAlmostEqual(expected, result)
      self.assertIsInstance(result[0], float, msg="Returned list should always contain floats")
    arg, expected = [10.0], [10.0]
    with self.assertUnmodified(arg):
      result = running_mean(arg)
      self.assertListAlmostEqual(expected, result)
      self.assertIsNot(arg, result, msg="Should always return new list")

  @grade.score(9)
  def test_short(self):
    arg      = [1, 5, 10, 2, 1, -4]
    expected = [1/1, 6/2, 16/3, 18/4, 19/5, 15/6]
    with self.assertUnmodified(arg):
      self.assertListAlmostEqual(expected, running_mean(arg))

  def test_optional_uses_cumsum(self):
    import list_lib
    with self.assertAccesses(list_lib.cumsum, module_names=['list_lib', 'stat_lib']):
      running_mean([1, 1])  # Don't care about result here

