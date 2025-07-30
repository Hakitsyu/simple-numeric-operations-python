import unittest
from simple_numeric_operations_python.operations import Number, Sum, Subtract, Multiply, Divide

class TestOperationResults(unittest.TestCase):

    def test_example_1(self):
        """Valida o resultado de: ((10 + 20) * (5 - 3)) / ((6 + 2) * (4 / 2))"""
        expression = Divide(
            Multiply(Sum(Number(10), Number(20)), Subtract(Number(5), Number(3))),
            Multiply(Sum(Number(6), Number(2)), Divide(Number(4), Number(2)))
        )
        
        print(f"\nCenário 1: {expression}")
        self.assertAlmostEqual(expression.execute(), 3.75)

    def test_example_2(self):
        """Valida o resultado de: (50 - ((10 * 3) + (8 / 2))) + (20 * (4 + 1))"""
        expression = Sum(
            Subtract(Number(50), Sum(Multiply(Number(10), Number(3)), Divide(Number(8), Number(2)))),
            Multiply(Number(20), Sum(Number(4), Number(1)))
        )
        
        print(f"Cenário 2: {expression}")
        self.assertAlmostEqual(expression.execute(), 116.0)

    def test_example_3(self):
        """Valida o resultado de: ((15 + 5) - (20 / (4 + 1))) * ((10 * 2) + (30 / 6))"""
        expression = Multiply(
            Subtract(Sum(Number(15), Number(5)), Divide(Number(20), Sum(Number(4), Number(1)))),
            Sum(Multiply(Number(10), Number(2)), Divide(Number(30), Number(6)))
        )

        print(f"Cenário 3: {expression}")
        self.assertAlmostEqual(expression.execute(), 400.0)

    def test_example_4(self):
        """Valida o resultado de: (((30 / 3) + (5 * 2)) - (12 / (4 - 1))) * (25 - (10 + 5))"""
        expression = Multiply(
            Subtract(Sum(Divide(Number(30), Number(3)), Multiply(Number(5), Number(2))), Divide(Number(12), Subtract(Number(4), Number(1)))),
            Subtract(Number(25), Sum(Number(10), Number(5)))
        )

        print(f"Cenário 4: {expression}")
        self.assertAlmostEqual(expression.execute(), 160.0)

    def test_example_5(self):
        """Valida o resultado de: ((100 / (5 + 5)) * ((30 - 10) + (40 / 2))) - (50 * ((6 + 4) / 2))"""
        expression = Subtract(
            Multiply(
                Divide(Number(100), Sum(Number(5), Number(5))),
                Sum(Subtract(Number(30), Number(10)), Divide(Number(40), Number(2)))
            ),
            Multiply(Number(50), Divide(Sum(Number(6), Number(4)), Number(2)))
        )
        
        print(f"Cenário 5: {expression}")
        self.assertAlmostEqual(expression.execute(), 150.0)

if __name__ == '__main__':
    unittest.main()