import concurrent.futures
import time
# Define the function to be executed in parallel
def process_data(data):
    # Perform some computation or task on the data
    # ...
    result=0
    for i in range(0,data):
         # Store the result
         result=result+i
    return result

# Prepare the data
data = [243242354,543543565,654654767,654645665,654654645]  # Your input data
start = time.time()
# Create a ThreadPoolExecutor or ProcessPoolExecutor
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Submit the function for each data item
    futures = [executor.submit(process_data, item) for item in data]

    # Retrieve the results as they become available
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)
        # Process the result as needed
        # ...
print(time.time()-start)        