#greedy scheduling

import numpy as np


def schedule(m, jobs):
    machines = np.zeros(m)
    for i in jobs:
        min_idx = np.argmin(machines)
        machines[min_idx] += int(i.strip())
    return int(np.max(machines))


for file_idx in range (1, 4):
    with open(f'inputJobs{file_idx}.txt') as f:
        lines = f.readlines()
        m = int(lines[0][0])
        print(schedule(m, lines[1::]))
