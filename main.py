def digit_sum(n):
  if n < 10:
    return n
  return digit_sum(n // 10) + digit_sum(n % 10)
def run():
  n = int(input("Enter an int: "))
  print(f"sum of digits of {n} is {digit_sum(n)}.")

if __name__ == "__main__":
	run()
	
  
#  result = n%10  result += n  result += n  result += n