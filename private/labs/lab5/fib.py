N = int(input("How many terms? "))

prev_term = 0
cur_term = 1

print(prev_term)
print(cur_term)
for n in range(N-2):
    next_term = prev_term + cur_term
    print(next_term)
    prev_term = cur_term
    cur_term = next_term
