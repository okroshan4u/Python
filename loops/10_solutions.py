# Eponential backoff 
    #Implement an exponential backoff strategy that doubles the wait the time between retries, starting from 1 second , but stops after 5 retries

import time

attempts = 0
max_retries = 5

wait_time = 1

while(attempts  < max_retries):
    print("Attempts", attempts + 1, "- wait time ", wait_time )   
    time.sleep(wait_time)
    wait_time *=2 
    attempts += 1