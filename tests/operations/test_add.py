from calculator import add


def test_add():
    # Arrange
    a = 2
    b = 3
    expected = 5

    # Act
    result = add(a, b)

    # Assert
    assert result == expected
