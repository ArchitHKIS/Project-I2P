import time

lapping = int(raw_input("How many laps do you want to do?"))

for i in range (lapping):
    start = time.time()

    lapper = lapping - (lapping - 1)

    print  "You are on lap number %s" % lapper
    stop = (raw_input("Press 'e' to stop")
    end = time.time()
    elapsed = end - start
    print "Lap time: %s" % (elapsed)