
for i in range(1, 100):
    if i % 15 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# генератор
my_gen = ("FizzBuzz" if i % 15 == 0
          else "Fizz" if i % 3 == 0
          else "Buzz" if i % 5 == 0
          else i
          for i in range(1, 100) )
print(*my_gen)
