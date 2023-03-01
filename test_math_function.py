import math_function
import pytest
import sys



#@pytest.mark.number   # executed by marks cmd-> pytest -v -m number
# cmd-> pytest -v -x -> the tests stops to execute when ther is one failed
#cmd test execution = pytest test_math_function.py

##@pytest.mark.skip(reason = "do not run")
#@pytest.mark.skipif(sys.version_info < 3, 3)
def test_add():
    assert  math_function.add(7,3) == 10  #ywe expectin the result 10
    assert math_function.add((7)) == 9
    assert math_function.add((5)) == 7

#@pytest.mark.number
def test_product():
    assert math_function.product(5,5) == 25
    assert math_function.product(5) == 10
    assert math_function.product(7) == 14


#@pytest.mark.strings
def test_add_strings():
    result = math_function.add('Hello', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result

#@pytest.mark.strings
def test_product_strings():
    assert math_function.product('Hello ', 3) == 'Hello Hello Hello'
    result = math_function.product('Hello ')
    assert result == 'Hello Hello'
    assert type(result) is str
    assert 'Hello' in result








