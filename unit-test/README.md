# Unit Test

- naming convention is usually test_{modules}.py
- class must inherit from `unittest.TestCase`
- methods must start with `test_{function}(self)`
- [Test docs](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)
- classes should use two instances which you should do `setUp` and `TearDown` methods
- Always setup and teardown after each test as you don't know when each test would happen
- `setupClass` and `tearDownClass` class methods will run at the beginning and end
- use patch

```python
import unittest 
import module
```

- run module using either of the following

```python
if __name__ == '__main__':
    unittest.main()
```
then run `python test_{module}.py`

or

run `python -m unittest test_calc.py`


-- dots represent tests that passed, and F represent the test that failed

```bash
..F.
======================================================================
FAIL: test_multiply (__main__.TestCalc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_calc.py", line 20, in test_multiply
    self.assertEqual(calc.multiply(10,5),50)
AssertionError: 100000 != 50

----------------------------------------------------------------------
Ran 4 tests in 0.000s

FAILED (failures=1)
```


