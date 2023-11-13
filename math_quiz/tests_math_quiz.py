import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_generate_random_InRange(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = test_generate_random_InRange(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test the function multiple times to ensure randomness
        for _ in range(10):
            operator = generate_random_operator()

            # Check if the generated operator is one of the expected values
            self.assertIn(operator, ['+', '-', '*'])


    def test_math_quiz(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5.5, -8, '-', '5.5--8', -2.5),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                evaluate_expression
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
