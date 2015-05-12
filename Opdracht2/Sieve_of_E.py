import sys
import time
T1 = time.perf_counter()    
#N=100
N=int(sys.argv[1])
lijst=[]
primes=[]
for i in range(0, N):
    lijst.append(True)

lijst[0]=False
lijst[1]=False
for k in range(2,N):
    if lijst[k]==True:
#       print(k)
        primes.append(k)
        for i in range(2*k,N,k):
            lijst[i]=False

text=open(sys.argv[2],'w')

for i in primes[:-1]:
    text.write(str(i)+'\n')
text.write(str(primes[len(primes)-1]))

T2=time.perf_counter()
print('Found '+str(len(primes))+' Prime numbers smaller than '+str(N)+' in '+str(T2-T1)+' sec.')