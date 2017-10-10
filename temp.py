import os
from pyspectator import Cpu
from time import sleep
cpu = Cpu(monitoring_latency=1)
while true:
    print(cpu.temperature)
    sleep(1)