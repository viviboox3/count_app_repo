from django.shortcuts import render
from metrix.counters import Counters
# Create your views here.
import random
import time
c = Counters("app1", "counter1")

d = Counters("app2", "counters2")

for i in range(10):
    time.sleep(3)
    #c = Counters("app1", "counter1")

    #d = Counters("app2", "counters2")

    c.increment_by(random.randint(1,10))
    d.increment()

