# count votes for Romney across all states

f = open('2012_US_election_state.csv', 'r')

all_lines = f.readlines()
all_lines = all_lines[1:] #skip reading the first line 

names = [line.split(",")[5] for line in all_lines]

total=0
for name in names:
	total += int(name)

print 'vote of Romney:' + str(total) 