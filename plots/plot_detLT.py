import matplotlib.pyplot as plt

# greedy
gr = [94, 85, 80, 79, 78, 77, 76, 75, 74, 73]

# process
gr_new = list(map(lambda x: x / gr[0], gr))

x_axis = list(range(len(gr)))

plt.figure(1)
plt.plot(x_axis, gr_new, 'mx-', label='Greedy', markersize=5)
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')


# random
rand = [94, 93, 92, 89, 88, 88, 82, 80, 79, 79, 72]

# process
rand_new = list(map(lambda x: x / rand[0], rand))

k = 494
x_axis = list(range(0, k, 50))
x_axis.append(k)


plt.plot(x_axis, rand_new, 'cx-', label='Random', markersize=5)
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')

# weighted
weighted = [94, 89, 82, 74, 73, 73, 73, 72, 72, 72, 72]

weighted_new = list(map(lambda x: x / weighted[0], weighted))

plt.plot(x_axis, weighted_new, 'gx-', label='Weighted', markersize=5)
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')

# distance
betweenness = [94, 89, 102]

betweenness_new = list(map(lambda x: x / betweenness[0], betweenness))
k = 70

x_axis = list(range(0, k, 50))
x_axis.append(k)

plt.plot(x_axis, betweenness_new, 'bx-', label='EdgeBetweennessDiff', markersize=5)
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')

plt.legend()
plt.savefig('detLT_wiki.png')

# greedy
gr = [94, 85, 80, 79, 78, 77, 76, 75, 74, 73]

# process
gr_new = list(map(lambda x: x / gr[0], gr))

x_axis = list(range(len(gr)))

plt.figure(2)
# greedy

plt.plot(x_axis, gr_new, 'mx-', label='Greedy', markersize=5)
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')


# random
rand = [94, 93, 92, 89, 88, 88, 82, 80, 79, 79, 72]

# process
rand_new = list(map(lambda x: x / rand[0], rand))

k = 494
x_axis = list(range(0, k, 50))
x_axis.append(k)


plt.plot(x_axis, rand_new, 'cx-', label='Random')
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')

# weighted
weighted = [94, 89, 82, 74, 73, 73, 73, 72, 72, 72, 72]

weighted_new = list(map(lambda x: x / weighted[0], weighted))

plt.plot(x_axis, weighted_new, 'gx-', label='Weighted')
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')

# betweenness
betweenness = [94, 89, 102]

betweenness = betweenness[:len(x_axis)]

betweenness_new = list(map(lambda x: x / betweenness[0], betweenness))

x_axis[- 1] = x_axis[- 2] + 50

plt.plot(x_axis, betweenness_new, 'bx-', label='EdgeBetweennessDiff')
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')

plt.legend()
plt.savefig('detLT_fb_improved.png')
