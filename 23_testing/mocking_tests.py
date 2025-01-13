import unittest
from unittest.mock import Mock, patch, MagicMock

class Calculator:
    def __init__(self, database):
        self.database = database
    
    def add(self, a, b):
        result = a + b
        self.database.save_operation("add", a, b, result)
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.database.save_operation("divide", a, b, result)
        return result

class TestCalculatorWithMocks(unittest.TestCase):
    
    def setUp(self):
        self.mock_database = Mock()
        self.calculator = Calculator(self.mock_database)
    
    def test_add_calls_database(self):
        result = self.calculator.add(5, 3)
        self.assertEqual(result, 8)
        self.mock_database.save_operation.assert_called_once_with("add", 5, 3, 8)
    
    def test_divide_success(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)
        self.mock_database.save_operation.assert_called_once_with("divide", 10, 2, 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)
        self.mock_database.save_operation.assert_not_called()
    
    @patch('time.time')
    def test_with_time_patch(self, mock_time):
        mock_time.return_value = 1640995200
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)
        mock_time.assert_called()

class TestMockExamples(unittest.TestCase):
    
    def test_mock_return_value(self):
        mock = Mock(return_value=42)
        result = mock()
        self.assertEqual(result, 42)
    
    def test_mock_side_effect(self):
        mock = Mock(side_effect=[1, 2, 3])
        self.assertEqual(mock(), 1)
        self.assertEqual(mock(), 2)
        self.assertEqual(mock(), 3)
    
    def test_magic_mock(self):
        mock = MagicMock()
        mock.method.return_value = "mocked"
        result = mock.method()
        self.assertEqual(result, "mocked")

if __name__ == "__main__":
    unittest.main()
