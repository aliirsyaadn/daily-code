def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        three = (i % 3 == 0)
        five = (i % 5 == 0)
        if three and five:
        	print("FizzBuzz")
	elif three:
		print("Fizz")
	elif five:
		print("Buzz")
	else:
		print(i)
            
fizzBuzz(10)
