# 1
def digitize(m):
   return[int(x) for x in str(m)[::-1]]


#print(digitize(120))

# 2
def past(h, m, s):
      return h*60000*60+m*60000+s*1000 
   
#print(past(0,1,1))

#3
def number(bus_stops):
    people = 0
    for x in bus_stops:
        people=people+x[0]-x[1]
    return people

def number1(bus_stops):
    return sum([on - off for on, off in bus_stops])
#print(number1([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))


#4
def positive_sum(arr):
    filt = filter((lambda x: x>0), arr)
    return sum(filt)

#print(positive_sum([]))

#5
def invert(lst):
    return [0-x for x in lst]

print(invert([1,2,-3]))