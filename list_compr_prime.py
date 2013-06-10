## this shows dict compression ##  
## num : Boolean
## num contains the numeric value and boolen holds either True/False according to if the number is true of False

def isPrime(a):
	if a <=1 :
		return False
	for  i in range (2,a):
		if ( a % i == 0):
			return False
		
	return True

num_list=[a for a in range(1,100)]
prime_dict={a:isPrime(a) for a in num_list}

print prime_dict

for k in prime_dict:
        if prime_dict.get(k):
                print k
        

## other example to put the prime numbers in a separate list ###

prime_list = [a for a in num_list if isPrime(a)]

print (' the prime list ')
print prime_list
