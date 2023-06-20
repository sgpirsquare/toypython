#1부터 시작하는 피보나치 수열 재귀함수

def fibonacci(n):
  if n <= 0:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n - 2)

a = input("Enter a natural number greater than or equal to 2: ")

for i in range(int(a)):
  print(fibonacci(i))
