## sample pogram to swap teh key and value using 
## dict comprehension 

first_dict={'1':"one",'2':"two",'3':"three",'4':"four",'5':"five"}
swap_dict={first_dict.get(a):a for a in first_dict}
print first_dict
print swap_dict

