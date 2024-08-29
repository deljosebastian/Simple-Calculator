userinput = list(input("Enter the calculation as eg.25 + 45: ").split())

if len(userinput) != 3:
    print("Error: Invalid input please add the values as 'number format number'")
else:
    try:
        q1 = int(userinput[0])
        q2 = userinput[1]
        q3 = int(userinput[2])

        def calculator(q, a, r):
            if a == '+':
                return q + r
            elif a == '-':
                return q - r
            elif a == '*':
                return q * r
            elif a == '/':
                if r == 0:
                    return "Error: Division by zero is not possible"
                return q / r
            else:
                raise TypeError("Invalid operation")

        result = calculator(q1, q2, q3)
        print("Result", result)
    except ValueError:
        print("Error: Print valid numbers")
