import random
import time
print("Get ready... When you see DRAW!, press Enter as fast as you can.")
wait = random.uniform(2, 5)
time.sleep(wait)
print("DRAW!")
start = time.time()
input()
end = time.time()
reaction = end - start
print("Your reaction time was", round(reaction, 3), "seconds.")
