stack = []
print('x= Exit, s= Show , [+-/=]')

while True:
    val = input(":")
    stack.append(val)
    if val == 's':
        print(stack)
        continue

    if val == 'x':
        break

    if val == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)

    if val == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a - b)

    if val == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(a / b)

    if val == '=':
        print(stack.pop())
        continue







