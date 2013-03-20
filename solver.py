'''
a data scientist way to solve the 8809=6 problem

author: hongliang liu

problem: from Saam's email:

8809=6
7111=0
2172=0
6666=4
1111=0
3213=0
....

2581=?

answer: I know the answer since 1987 when I was 5, not to spoiler. But it becomes interesting to have a 
general solution: linear regression by frequency.

one can list the digits by its frequency, and this problem becomes a linear regression for a 10-dimension
(x0-x9) space, where:

8809=6 -> 100000021 = 6 by freq where 1,2,1 are p0,p8,p9 as parameters

thus, a linear regression can solve this problem easily.

explain the output:

the output should be:

(array([ 1.00000000e+00,   4.75790411e-24,   4.75709632e-24,
         4.75588463e-24,   1.00000000e+00,   4.75951970e-24,
         1.00000000e+00,   4.75790411e-24,   2.00000000e+00,
         1.00000000e+00]), 2)

it indicates the coeffciency for number 0 to 9 is:
1,0,0,0,1,0,1,0,2,1

which means, when number 0,4,6,9 appears, the weight is 1, and 8 gives weight two. However, '4' does not
exist in the content, so one should not count '4' in. (the reason was from the initial value of 1, which
was the default value if some patterns did not exist. )thus:

--- spoiler alert --

count by circles, 0,6,9 have 1 circle while 8 has two circles.

one can easily make another set of problems and solve by this linear regression
'''
import sys
import numpy
from numpy import array
from scipy.optimize import leastsq

#def __residual(params, y, zero, one, two, three, four, five, six, seven, eight, nine):
#    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9 = params
#    return p0*zero+p1*one+p2*two+p3*three+p4*four+p5*five+p6*six+p7*seven+p8*eight+p9*nine-y

def __residual(params, xdata, ydata):#guess the function is cosine dot
    return (ydata - numpy.dot(xdata, params))

f_in = open('input.txt','r')

#8809=6 -> 100000021 = 6 by freq where 1,2,1 are p0,p8,p9 as parameters
#by giving these parameters, one can fit a 10-dimension least square for y=\sum_{i from 0 to 9}x_i*p_i

parameter_matrix = numpy.zeros(shape=(10,20))
y_list = list()

#read in these 8809=6
current = 0
for l in f_in.readlines():
    p,y = l.strip().split('=')
    y_list.append(float(y))
    for t in p:
        x = int(t)
        parameter_matrix[x][current]+=1
    current+=1
    
f_in.close()

ydata=numpy.array(y_list)

print 'the freq matrix is '
for i in range(current):
    s = ','.join([str(parameter_matrix[j][i]) for j in range(10)])
    print s

xdata = numpy.transpose(parameter_matrix)

x0=numpy.array([1,1,1,1,1,1,1,1,1,1])#initial guess 

print 'fitting parameter is'
print leastsq(_r_func, x0, args=(xdata, ydata))
