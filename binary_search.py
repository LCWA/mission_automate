import random

from sets import Set

MAX_RANGE = 300

commits = {}
commit_ids = []

def execute_tests(commit_id):
    global time_elapsed 
    time_elapsed = time_elapsed + 10
    good = not commits[commit_id]
    if good:
        good_string = 'good' 
    else:
        good_string = 'bad'
    # print('Executing on ', good_string, ' commit ', commit_id,\
    #     ' Time elapsed: ', time_elapsed)
    return good

def execute_and_memoize(commit_id):
    if not commit_id in memoized:
        memoized[commit_id] = execute_tests(commit_id)
    return memoized[commit_id]

def bin_search(commits_ids, start, end):
    if start + 1 == end:
        if execute_tests(commit_ids[start]):
            return end
        else:
            return start
    elif start == end:
        return start
    else:
        length = (end - start)
        half = start + length / 2
        if execute_tests(commit_ids[half]):
            return bin_search(commits_ids, half + 1, end)
        else:
            return bin_search(commits_ids, start, half)

def find_bad_commit(commit_ids):
    key = bin_search(commit_ids, 0, len(commit_ids) - 1)
    return commit_ids[key]

def generate():
    global commit_ids
    temp_ids = Set()
    while(len(temp_ids) < MAX_RANGE):
        temp_ids.add(random.randint(1, 1000))
    # for i in range(MAX_RANGE):
    #     commit_ids.append(random.randint(1, 1000))
    commit_ids = list(temp_ids)
    commit_ids.sort()
    for c in commit_ids:
        commits[c] = False
    # bad_commit = False
    # for c in commit_ids:
    #     if bad_commit:
    #         commits[c] = False
    #     else:
    #         max = 150
    #         r = random.randint(1, 150)
    #         if r == 150:
    #             commits[c] = False
    #             bad_commit = False
    #         else:
    #             commits[c] = True
    # if not bad_commit:
    #     commits[c] = False

def print_commits():
    for c in commit_ids:
        if commits[c]:
            print("Commit id: " + str(c) + " is " + str(commits[c]))
            return c
    print(c, commits[c])

generate()
print(commit_ids)
min_time = 3000
max_time = 0
min_pos = 0
max_pos = 0
total_time = 0
for c in range(299, -1, -1):
    time_elapsed = 0
    memoized = {}
    commits[commit_ids[c]] = True
    c = print_commits()
    bad_commit = find_bad_commit(commit_ids)
    print('Found bad commit ', bad_commit, ' in ', time_elapsed, 'minutes')
    if c != bad_commit:
        print('Error', c, bad_commit)
        exit(2)
    if time_elapsed < min_time:
        min_time = time_elapsed
        min_pos = bad_commit
    if time_elapsed > max_time:
        max_time = time_elapsed
        max_pos = bad_commit
    total_time += time_elapsed

print('Total time ', total_time, ' Average time ', total_time / 300)
print('Min time ', min_time, ' at commit ', min_pos)
print('Max time ', max_time, ' at commit ', max_pos)