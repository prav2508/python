list = [12,11,74,55,89,22,78,45,12,36,94,41]
def finder(list):
     even=0
     odd = 0
     for i in list:
         if i%2 == 0:
            even+=1
         else:
             odd+=1
     return even,odd
ev,od = finder(list)
print("even:{} and odd:{}".format(ev, od))