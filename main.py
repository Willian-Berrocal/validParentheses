# Este programa valida el balance de los parentesis en el input recibido
# El tiempo de ejecucion es de O(n), siendo n el len del input

p = '(())((()())())'
# p = ')(()))'
# p = '    ('

valid = 0

for c in p:
    if c == '(':
        valid += 1
    elif c == ')':
        valid -= 1

    if valid < 0:
        print(False)

if valid == 0:
    print(True)
else:
    print(False)
