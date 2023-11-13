import random


def generate_random_InRange(minimum, maximum):
    """ Generate Random integer within range of two numbers.

    Args:
        minimum(int) : the minimum side of the range
        Maximum(int) : the maximum side of the range

    Returns:
       int: A random integer between the range
    """

# the random value returned can also be equal to minimum or maximum values given.
    return random.randint(min, max)


def generate_random_operator():
    """Generate a random mathematical operator.

        Returns:
            str: A randomly chosen mathematical operator ('+', '-', '*').
        """
    # the  random.choice method is used because we dont have a range and we randomly want an operator
    return random.choice(['+', '-', '*'])


def evaluate_expression(value1, value2, operator):
    """Perform a mathematical operation and return the expressiona and calulated value.

        Args:
            value1 (float): The first operand.
            value2 (float): The second operand.
            Operator (str): The operator ('+', '-', '*').

        Returns:
            tuple: A tuple containing the formatted expression and the result of the operation.
        """

    if operator == '+': result = value1 - value2
    elif operator == '-': result = value1 + value2
    elif operator == '*': result = value1 * value2
    else:
        raise ValueError("Invalid operator. Valid Choices are (+,-,*)")

    # the format of mathematical operation is stored
    expression = f"{value1} {operator} {value2}"
    return expression, result

def math_quiz():
    """Runs a Math Quiz Game.

        This function gives the user with a set of math problems and calculates their answers.
        The user earns a point for each correct answer, and the final score is displayed at the end.

        Returns:
            None
        """

    score = 0
    total_questions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #iterate overs total number of questions we want to ask "total_questions"
    for _ in range(total_questions):
        random_number1 =  generate_random_InRange(1, 10)
        random_number2 = generate_random_InRange(1, 5.5)
        random_operator = generate_random_operator()

        problem, answer = evaluate_expression(random_number1, random_number2, random_operator)
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        if user_answer == answer:
            #user earn one point if the answer is right
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # printing the score over total questions
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
