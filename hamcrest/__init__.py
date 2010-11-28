"""Hamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations where
matchers are invaluable, such as UI validation, or data filtering, but it is in
the area of writing flexible tests that matchers are most commonly used. This
tutorial shows you how to use Hamcrest for unit testing.

When writing tests it is sometimes difficult to get the balance right between
overspecifying the test (and making it brittle to changes), and not specifying
enough (making the test less valuable since it continues to pass even when the
thing being tested is broken). Having a tool that allows you to pick out
precisely the aspect under test and describe the values it should have, to a
controlled level of precision, helps greatly in writing tests that are "just
right." Such tests fail when the behavior of the aspect under test deviates
from the expected behavior, yet continue to pass when minor, unrelated changes
to the behaviour are made.

MY FIRST HAMCREST TEST

We'll start by writing a very simple PyUnit test, but instead of using PyUnit's
assertEqual function, we'll use Hamcrest's assert_that construct and the
standard set of matchers:

from hamcrest import *
import unittest

class BiscuitTest(unittest.TestCase):
    def testEquals(self):
        theBiscuit = Biscuit('Ginger')
        myBiscuit = Biscuit('Ginger')
        assert_that(theBiscuit, equal_to(myBiscuit))

if __name__ == '__main__':
    unittest.main()

The assert_that function is a stylized sentence for making a test assertion. In
this example, the subject of the assertion is the object theBiscuit, which is
the first method parameter. The second method parameter is a matcher for
Biscuit objects, here a matcher that checks one object is equal to another
using the Python == operator. The test passes since the Biscuit class defines
an eq method.

If you have more than one assertion in your test you can include an identifier
for the tested value in the assertion:

assert_that(theBiscuit.getChocolateChipCount(), equal_to(10), 'chocolate chips')
assert_that(theBiscuit.getHazelnutCount(), equal_to(3), 'hazelnuts')

As a convenience, assert_that can also be used to verify a boolean condition:

assert_that(theBiscuit.isCooked(), 'cooked')

This is equivalent to the assert_ method of unittest.TestCase, but because it's
a standalone function, it offers greater flexibility in test writing.

FOR MORE INFORMATION

Further information is available from
    http://code.google.com/p/hamcrest/wiki/TutorialPython

"""

__author__ = "Jon Reid"
__copyright__ = "Copyright 2010 www.hamcrest.org"
__license__ = "BSD, see License.txt"
__version__ = "1.0"

from core.matcher_assert import assert_that
from core import *
from library import *
