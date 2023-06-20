def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n - 2)

a = input("2 이상 자연수를 입력하세요: ")

for i in range(int(a)):
  print(fibonacci(i))
