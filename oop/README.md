# python-review

## Simple class with no attribute or methods
```
Class Employee:
  pass
```

## Identifies the constructor
```
  def __init__(self, args...):
```
- self identifies the instance of the object
- self is the same as the instance of the object

```
Employee.fullname(emp_1)
```
# Instances of employee
```
emp_1 = Employee()
emp_2 = Employee()
```

## Instance variables

- Contain data that is unique to each instance

## Class variables
- Update data for class to collect data across instances

```python
Employee.num_of_emps += 1
```
```python
#Prints out instance attributes
print(emp_1.__dict__)
#Prints out class values and aspects of class
print(Employee.__dict__)
```

## Class Methods
- takes class or `cls` as first argument instead of `self`
- use decorator `@classmethod`
- calling class method `Employee.set_raise_amt(1.06)`
  - can also use instance to update class method `emp_1.set_raise_amt(1.06)`
- Use class method to create alternative constructors
  ```python
    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        #creates instance
        return cls(first,last,pay)
  ```
## Static Method
  - Does not pass instance or that class but have logical connection with the class
  - if you don't access the instance or class, it will need to be a static method

```python
    @staticmethod
    def is_workday(day):
        if day.weekday(5) == 5 or day.weekday() == 6:
            return False
        return True

    print(Employee.is_workday(my_date))
    print(new_emp_2.is_workday(my_date))
```