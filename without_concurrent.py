import time
data = [243242354,543543565,654654767,654645665,654654645] 
def process_data(data):
    # Perform some computation or task on the data
    # ...
    result=0
    for i in range(0,data):
         # Store the result
         result=result+i
    return result
start=time.time()
for i in data:
     print(process_data(i))

print(time.time()-start)     