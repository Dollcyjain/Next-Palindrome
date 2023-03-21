test_cases = []
inputs = int(input("Enter the number of test cases you want to test: "))
for i in range(inputs):
    item = int(input(f"Enter the test case no. {i+1}: "))
    test_cases.append(item)
for item in test_cases:
    i = item
    while True:
        if str(i)[::-1] == str(i) and i >= item:
            print(f"The next palindrome of {item} is {i}")
            break
        else:
            i += 1
