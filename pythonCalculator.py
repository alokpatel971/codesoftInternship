def calculate(num1, num2, operation):
  

  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    if num2 == 0:
      return "Cannot divide by zero."
    else:
      return num1 / num2
  else:
    return "Invalid operation."

def main():
  

  while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, or divide): ")

    result = calculate(num1, num2, operation)
    print("Result:", result)

    choice = input("Do you want to perform another calculation? (yes/no): ")
    if choice.lower() != "yes":
      break

if __name__ == "__main__":
  main()