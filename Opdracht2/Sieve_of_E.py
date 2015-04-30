import sys
# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv)) 

N=20
lijst=[]
for i in range(0, N):
    lijst.append(True)

lijst[0]=False
lijst[1]=False
for k in range(2,N):
    if lijst[k]==True:
        print(k)
        for i in range(2*k,N,k):
            lijst[i]=False

print(lijst)


def som(a,b):
    c=a+b
    return str(c)+" is de som"
    
print(som(4,8)+"!")
