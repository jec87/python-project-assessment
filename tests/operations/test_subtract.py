from calculator import subtract


def test_subtract():
    # Arrange
    a = 5
    b = 3
    expected = 2

    # Act
    result = subtract(a, b)

    # Assert
    assert result == expected
