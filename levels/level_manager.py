# levels/level_manager.py

LEVELS = {
    1: {
        "title": "The Missing Link",
        "buggy_code": (
            "def greet(name):\n"
            "    print(\"Hello, \" + name\n\n"
            "greet(\"Coder\")"
        ),
        "expected_output": "Hello, Coder",
        "hint": (
            "Python requires balanced parentheses. "
            "Count the '(' and ')' in your print statement."
        ),
        "penalty": 15,
        "difficulty": "Easy"
    },

    2: {
        "title": "Range Rover",
        "buggy_code": (
            "# Goal: Print numbers 1 to 5\n"
            "for i in range(1, 5):\n"
            "    print(i)"
        ),
        "expected_output": "1\n2\n3\n4\n5",
        "hint": (
            "In Python, range(start, stop) stops BEFORE the 'stop' value."
        ),
        "penalty": 10,
        "difficulty": "Easy"
    },

    3: {
        "title": "The Pricing Bug",
        "buggy_code": (
            "# Goal: Give a 10% discount ONLY if the bill is more than 150\n"
            "def calculate_bill(price):\n"
            "    if price > 100:\n"
            "        return price * 0.9\n"
            "    else:\n"
            "        return price\n\n"
            "print(calculate_bill(150))"
        ),
        "expected_output": "150",
        "hint": "Check the 'if' condition. It gives a discount for prices LESS than 100.",
        "penalty": 10,
        "difficulty": "Easy-Medium"
    },

    4: {
        "title": "The String Stumbler",
        "buggy_code": (
            "# Goal: Take two numbers and print their sum multiplied by 2\n"
            "def calculate_double_sum(a, b):\n"
            "    result = a + b\n"
            "    return result * 2\n\n"
            "val1 = \"10\"\n"
            "val2 = \"20\"\n"
            "print(calculate_double_sum(val1, val2))"
        ),
        "expected_output": "60",
        "hint": "Adding strings results in concatenation. Convert inputs to integers first.",
        "penalty": 15,
        "difficulty": "Easy-Medium"
    },

    5: {
        "title": "Broken Username Logic",
        "buggy_code": (
            "# Goal: A valid username must:\n"
            "# 1. Be at least 5 characters long\n"
            "# 2. Contain at least one number\n"
            "def is_valid_user(name):\n"
            "    if len(name) < 3:\n"
            "        return False\n"
            "    for char in name:\n"
            "        if char.isdigit():\n"
            "            return False\n"
            "    return True\n\n"
            "print(is_valid_user(\"Dev123\"))"
        ),
        "expected_output": "True",
        "hint": "Return True when a digit is found. Return False only after the loop ends.",
        "penalty": 20,
        "difficulty": "Medium"
    },

    6: {
        "title": "The Inventory Glitch",
        "buggy_code": (
            "# Goal: Get the price of an item from the inventory.\n"
            "# If the item doesn't exist, return 'Not Found'.\n"
            "def get_price(item_name):\n"
            "    inventory = {'apple': 50, 'banana': 30, 'orange': 40}\n"
            "    \n"
            "    # Bug: This will crash if the item is not in the dictionary\n"
            "    price = inventory[item_name]\n"
            "    return price\n\n"
            "print(get_price('apple'))\n"
            "print(get_price('grapes'))"
        ),
        "expected_output": "50\nNot Found",
        "hint": "Using inventory[item] on a missing key raises a KeyError. Use the .get() method or an 'if item in inventory' check to handle missing items safely.",
        "penalty": 15,
        "difficulty": "Medium"
    },

    7: {
        "title": "The Fibonacci Timeout",
        "buggy_code": (
            "def fib(n):\n"
            "    if n <= 1:\n"
            "        return n\n"
            "\n"
            "    a, b = 1,2\n"
            "    for _ in range(1, n + 1):\n"
            "        a, b = b\n"
            "\n"
            "    return b\n\n"
            "print(fib(35))"
        ),
        "expected_output": "9227465",
        "hint": "Use memoization or an iterative approach to avoid repeated calculations.",
        "penalty": 25,
        "difficulty": "Hard"
    },

    8: {
        "title": "The Final Boss: Matrix Transpose",
        "buggy_code": (
            "# Goal: Transpose a 2x3 matrix into a 3x2 matrix\n"
            "def transpose(matrix):\n"
            "    rows = len(matrix)\n"
            "    cols = len(matrix[0])\n"
            "    result = [[0 for _ in range(rows)] for _ in range(cols)]\n"
            "    for i in range(rows):\n"
            "        for j in range(cols):\n"
            "            result[i][j] = matrix[j][i]\n"
            "    return result\n\n"
            "print(transpose([[1, 2, 3], [4, 5, 6]]))"
        ),
        "expected_output": "[[1, 4], [2, 5], [3, 6]]",
        "hint": "Swap row/column indices correctly when assigning values.",
        "penalty": 30,
        "difficulty": "Hard"
    }
}
