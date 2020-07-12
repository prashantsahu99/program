# Problem Statement: Vaibhav has just completed his first year of Job. He is really 
# happy about it but at the same time he needs to pay taxes to government on what he 
# has earned in his last one year. Vaibhav found that all of his friends were facing the 
# same difficulty in calculating the tax. 
# He felt the need of a program where he can enter all of his friend’s name along with 
# their income one by one and the program will calculate the tax and print the liable 
# taxes of all of his friends. 
# Let’s help Vaibhav write the program for the same.
print ("\nTax Calculator App")
print ("-----WELCOME------\n") 
nm=[]
l=[]
t=[]
print ("Enter total person count:")
n=int(input ())
for i in range(1,n+1):
    print("\nEnter name "+str(i)+":")
    s=input ()
    print ("Enter "+s+"'""s Annual Income:")
    sl=int(input ())
    nm.append(s)
    l.append(sl)
   

    
def calculateTax(p):
    q=0
    if p>=300000:
        q=p*0.2
    elif p >=100000:
        q=p*0.1   
    else:
        q=0
    return q
for i in l:
    z=0
    z=calculateTax(i) 
    t.append(z)    
print("\nNames with liable taxes")
print ("------------------------")
for i in range(0,len(nm)):
    print (nm[i] +" : "+str(round(t[i])))           
    


    
    
