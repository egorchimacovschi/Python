#performing multiple tasks at once

import threading
import time

def walk_dog(first):
    time.sleep(8)
    print("You finish walking the dog")


def take_out_thrash():
    time.sleep(2)
    print("Take out the thrash")

def get_mail():
    time.sleep(4)
    print("You get the email")


#all processes took at the same time
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2 = threading.Thread(target=take_out_thrash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

print("Not a single chore is complete")

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")