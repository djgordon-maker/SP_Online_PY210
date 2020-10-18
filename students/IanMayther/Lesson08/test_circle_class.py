"""
test code for circle_class.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes it easier to test everything in a module.
from circle_class import *

########
# Step 1
########

def test_circle1():
    with pytest.raises(AttributeError):
        c = Circle()

def test_circle2():
    c = Circle(4)

    assert c.radius == 4