from IPython import embed

TXT_FILE = open("jobs.txt", "r")
INPUT_STRING = TXT_FILE.read()
ROWS = INPUT_STRING.splitlines()
JOBS = [[int(x) for x in row.split(" ")] for row in ROWS]

JOBS_SCORES = [[job[0], job[1], job[0] - job[1]] for job in JOBS]
SORTED_JOBS_SCORES = sorted(JOBS_SCORES, key=lambda x: -x[2])

total, time, tot_j, tot_t = (0, 0, 0, 0)
for job in SORTED_JOBS_SCORES:
    time += job[1]
    total += time * job[0]
    tot_j += job[0]
    tot_t += job[1]

# print(time)

JOBS_SCORES_2 = [[job[0], job[1], job[0] * 1.0 / job[1]] for job in JOBS]
SORTED_JOBS_SCORES_2 = sorted(JOBS_SCORES_2, key=lambda x: x[2])

total_2 = 0
time_2 = 0
tot_j2 = 0
tot_t2 = 0
for job in SORTED_JOBS_SCORES_2:
    time_2 += job[1]
    total_2 += time_2 * job[0]
    tot_j2 += job[0]
    tot_t2 += job[1]
# print(total_2)
print(tot_j2)
print(tot_j)
print(tot_t2)
print(tot_j2)
embed()
