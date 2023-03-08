import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)



def test_string_only(order, first_entry):
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]

