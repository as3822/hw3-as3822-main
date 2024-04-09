# (c) 2022- Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from .hwtest.unittest import HomeworkModuleTestCase
from .hwtest import autograde as grade

from typing import Any, Callable, List, Protocol
from functools import total_ordering


class Summable(Protocol):
  def __add__(self, other: "Summable") -> "Summable": ...


# Note: we use float in type annotations, even though that doesn't *fully*
#  capture requirements (ok, since we have these just to sush Pylance/Pylint...)
product: Callable[[List[float]], float]
cumsum: Callable[[List[Summable]], List[Summable]]
is_increasing: Callable[[List[Any]], bool]

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


# Private class to tests that solutions to order-related functions do
# not use unecessary operations...
@total_ordering
class Comparable:
  def __init__(self, val):
    self.val = val

  def __eq__(self, other):
    assert isinstance(other, self.__class__)
    return self.val == other.val

  def __ne__(self, other):
    assert isinstance(other, self.__class__)
    return self.val != other.val

  def __lt__(self, other):
    assert isinstance(other, self.__class__)
    return self.val < other.val

  def __repr__(self):
    # return f"{self.__class__.__name__}({self.val})"
    return f"Val({self.val})"


class ProductTests(HomeworkModuleTestCase):
  __scriptname__ = "list_lib.py"
  __modulename__ = "list_lib"
  __attrnames__ = [ "product" ]

  @grade.score(2)
  def test_empty(self):
    with self.assertUnmodified([]) as arg:
      self.assertEqual(1, product(arg))

  @grade.score(3)
  def test_type(self):
    with self.assertUnmodified([1]) as arg:
      result = product(arg)
      self.assertIsInstance(result, int)
      self.assertEqual(1, product(arg))
    with self.assertUnmodified([1.0]) as arg:
      result = product(arg)
      self.assertIsInstance(result, float)
      self.assertAlmostEqual(1.0, product(arg))

  @grade.score(10)
  def test_simple(self):
    with self.assertUnmodified([2, -3, 4]) as arg:
      self.assertEqual(-24, product(arg))
    with self.assertUnmodified([2, -3, 0]) as arg:
      self.assertEqual(0, product(arg))
    with self.assertUnmodified([2, -3, 4, -0.2]) as arg:
      self.assertAlmostEqual(4.8, product(arg))


class CumSumTests(HomeworkModuleTestCase):
  __scriptname__ = "list_lib.py"
  __modulename__ = "list_lib"
  __attrnames__ = [ "cumsum" ]

  @grade.score(2)
  def test_empty(self):
    with self.assertUnmodified([]) as arg:
      result = cumsum(arg)
      self.assertListEqual([], result)
      self.assertIsNot(arg, result, msg="Should return empty list on empty input")

  @grade.score(2)
  def test_empty_not_alias(self):
    with self.assertUnmodified([]) as arg:
      result = cumsum(arg)
      self.assertIsNot(arg, result, msg="Should *always* return *new* list")

  @grade.score(3)
  def test_singletons(self):
    arg, expected = [10], [10]
    with self.assertUnmodified(arg):
      self.assertListEqual(expected, cumsum(arg))
    arg, expected = [10.0], [10.0]
    with self.assertUnmodified(arg):
      result = cumsum(arg)
      self.assertListEqual(expected, result)
      self.assertIsNot(arg, result, msg="Should always return new list")

  @grade.score(4)
  def test_short(self):
    arg, expected = [1, 5, 10, 2, 1, 5], [1, 6, 16, 18, 19, 24]
    with self.assertUnmodified(arg):
      self.assertListEqual(expected, cumsum(arg))

  @grade.score(4)
  def test_short_negative(self):
    arg, expected = [0, -1, -5, 8, -5, 12, 3], [0, -1, -6, 2, -3, 9, 12]
    with self.assertUnmodified(arg):
      self.assertListEqual(expected, cumsum(arg))

  def test_optional_strings(self):
    arg, expected = ["Hi ", "", "there", " human", "!"], \
                    ["Hi ", "Hi ", "Hi there", "Hi there human", "Hi there human!"]
    with self.assertUnmodified(arg):
      self.assertListEqual(expected, cumsum(arg))

  def test_optional_user_defined_element_type(self):
    arg, expected = [Counter(1), Counter(2), Counter(-1)], \
                    [Counter(1), Counter(3), Counter(2)]
    with self.assertUnmodified(arg):
      self.assertListEqual(expected, cumsum(arg))


class IsAscendingTests(HomeworkModuleTestCase):
  __scriptname__ = "list_lib.py"
  __modulename__ = "list_lib"
  __attrnames__ = [ "is_increasing" ]

  @grade.score(2)
  def test_empty(self):
    arg = []
    with self.assertUnmodified(arg):
      self.assertTrue(is_increasing(arg))

  @grade.score(2)
  def test_constant(self):
    arg = [1]
    with self.assertUnmodified(arg):
      self.assertTrue(is_increasing(arg))
    arg = [1,1]
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    arg = [1] * 100
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))

  # For informative purposes mostly (if this fails, other tests are very unlikely to pass)
  @grade.score(1)
  def test_pairs(self):
    # Constant pair tested above
    arg = [1, 2]
    with self.assertUnmodified(arg):
      self.assertTrue(is_increasing(arg))
    arg = [2, 1]
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))

  @grade.score(1)
  def test_repeated(self):
    arg = sum(([i]*5 for i in range(1, 101, 1)), start=[])
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    arg = sum(([i]*5 for i in range(100, -1, -1)), start=[])
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))

  @grade.score(4)
  def test_edges(self):
    # Only last pair ascending
    arg = list(range(100,-1,-1)) + [1]
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    # First pair ascending (only)
    arg = [99] + list(range(100, -1, -1))
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    # Last pair descending (only)
    arg = list(range(0, 101, 1)) + [99]
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    # Plain range (asceding)
    arg = list(range(0, 101, 1))
    with self.assertUnmodified(arg):
      self.assertTrue(is_increasing(arg))

  @grade.score(3)
  def test_string_simple(self):
    arg = ['a', 'a', 'a']
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    arg = ['a', 'b', 'a']
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    arg = ['b', 'a', 'b']
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    arg = ['a', 'b', 'c']
    with self.assertUnmodified(arg):
      self.assertTrue(is_increasing(arg))

  @grade.score(2)
  def test_user_defined_simple(self):
    arg = [Comparable('a'), Comparable('a'), Comparable('a')]
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    arg = [Comparable('a'), Comparable('b'), Comparable('a')]
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    arg = [Comparable('b'), Comparable('a'), Comparable('b')]
    with self.assertUnmodified(arg):
      self.assertFalse(is_increasing(arg))
    arg = [Comparable('a'), Comparable('b'), Comparable('c')]
    with self.assertUnmodified(arg):
      self.assertTrue(is_increasing(arg))
