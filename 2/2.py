# Even Fibonacci numbers
# Find the sum of even valued fibonacci numbers that do not exceed 4 million

def even_fib_sum():
  fibs = [1, 2]
  sum = 2
  while True:
    new_fib = fibs[-2] + fibs[-1]
    if new_fib > 4000000:
      return sum
    fibs.append(new_fib)
    if new_fib % 2 == 0:
      sum += new_fib

print(even_fib_sum())
