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

## Instance variables and methods

- Contain data that is unique to each instance

## Class Methods
- Update data for class to collect data across instances

```
Employee.num_of_emps += 1
```
```
#Prints out instance attributes
print(emp_1.__dict__)
#Prints out class values and aspects of class
print(Employee.__dict__)
```