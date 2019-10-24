a, b, c=5, 3.2, "\"Hello\""

print (a)
print (b)
print (c)

print ("%s\t %s\t %s" % (a,b,c))

print ('I love {} and {}' . format ('bread','butter'))

print ('I love {0} and {1}' . format ('bread','butter'))

print ('I love {1} and {0}' . format ('bread','butter'))

age=23 
y=10
message = "Happy " +str(age) + "rd Birthday !"
print(message)

x = "Happy {}rd Birthday!".format(y) 
print(x)
print("Happy {}th Birthday!".format(y))