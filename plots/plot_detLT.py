import matplotlib.pyplot as plt

# greedy
gr = [72, 60, 53, 49, 46, 44, 18, 17, 16, 15, 14, 13]

# process
gr_new = list(map(lambda x: x / gr[0], gr))

x_axis = list(range(len(gr)))

plt.figure(1)
plt.plot(x_axis, gr_new, 'mx-', label='Greedy', markersize=5)

# random
rand = [72, 72, 72, 68, 68, 68, 14, 13, 13, 13, 12]

# process
rand_new = list(map(lambda x: x / rand[0], rand))

k = 240
x_axis = list(range(0, k, 25))
x_axis.append(k)

plt.plot(x_axis, rand_new, 'cx-', label='Random', markersize=5)

# weighted
weighted = [72, 66, 66, 66, 65, 12, 12, 12, 12, 12, 12]

weighted_new = list(map(lambda x: x / weighted[0], weighted))

plt.plot(x_axis, weighted_new, 'gx-', label='Weighted', markersize=5)

# betweenness
betweenness = [72, 17, 19, 19, 20, 25, 28, 28, 30, 30, 30, 30, 30, 32, 32, 32, 32, 32, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36]

betweenness_new = list(map(lambda x: x / betweenness[0], betweenness))
k = 748

x_axis = list(range(0, k, 25))
x_axis.append(k)

plt.plot(x_axis, betweenness_new, 'bx-', label='EdgeBetweennessDiff', markersize=5)

plt.legend()
plt.savefig('detLT_email.png')

# improved plot
# greedy
gr = [72, 60, 53, 49, 46, 44, 18, 17, 16, 15, 14, 13]

# process
gr_new = list(map(lambda x: x / gr[0], gr))

x_axis = list(range(len(gr)))

plt.figure(2)

plt.plot(x_axis, gr_new, 'mx-', label='Greedy', markersize=5)

# random
rand = [72, 72, 72, 68, 68, 68, 14, 13, 13, 13, 12]

# process
rand_new = list(map(lambda x: x / rand[0], rand))

k = 240
x_axis = list(range(0, k, 25))
x_axis.append(k)

plt.plot(x_axis, rand_new, 'cx-', label='Random')

# weighted
weighted = [72, 66, 66, 66, 65, 12, 12, 12, 12, 12, 12]

weighted_new = list(map(lambda x: x / weighted[0], weighted))

plt.plot(x_axis, weighted_new, 'gx-', label='Weighted')

# betweenness
betweenness = [72, 17, 19, 19, 20, 25, 28, 28, 30, 30, 30, 30, 30, 32, 32, 32, 32, 32, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36]

betweenness = betweenness[:len(x_axis)]

betweenness_new = list(map(lambda x: x / betweenness[0], betweenness))

x_axis[- 1] = x_axis[- 2] + 25

plt.plot(x_axis, betweenness_new, 'bx-', label='EdgeBetweennessDiff')

plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')
plt.legend()
plt.savefig('detLT_email_improved.png')
