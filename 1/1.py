# Multiples of 3 and 5
# Find sum of all multiples of 3 or 5 below 1000

def multiples_sum():
  sum = 0
  for i in range(0, 1000, 3):
    sum += i
  for i in range(0, 1000, 5):
    if i % 3 != 0:  # skip multiples of 3
      sum += i
  return sum

print(multiples_sum())
