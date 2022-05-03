import matplotlib.pyplot as plt

# greedy
gr = [67, 29, 20, 19, 18, 17, 16, 15, 14]

# process
gr_new = list(map(lambda x: x / gr[0], gr))

x_axis = list(range(len(gr)))

plt.figure(1)
plt.plot(x_axis, gr_new, 'mx-', label='Greedy', markersize=5)

# random
rand = [67, 65, 54, 54, 53, 53, 53, 53, 53, 52, 14]

# process
rand_new = list(map(lambda x: x / rand[0], rand))

k = 249
x_axis = list(range(0, k, 25))
x_axis.append(k)

plt.plot(x_axis, rand_new, 'cx-', label='Random', markersize=5)

# weighted
weighted = [67, 66, 64, 63, 63, 14, 14, 14, 14, 14, 14]

weighted_new = list(map(lambda x: x / weighted[0], weighted))

plt.plot(x_axis, weighted_new, 'gx-', label='Weighted', markersize=5)

# betweenness
betweenness = [67, 28, 14, 18, 21, 22, 22, 24, 24, 24, 24, 25, 25, 25, 25, 25, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28,
               28, 29, 29, 29, 30, 30]

betweenness_new = list(map(lambda x: x / betweenness[0], betweenness))
k = 768

x_axis = list(range(0, k, 25))
x_axis.append(k)

plt.plot(x_axis, betweenness_new, 'bx-', label='EdgeBetweennessDiff', markersize=5)

plt.legend()
plt.savefig('detLT_email.png')

# improved plot
# greedy
gr = [67, 29, 20, 19, 18, 17, 16, 15, 14]

# process
gr_new = list(map(lambda x: x / gr[0], gr))

x_axis = list(range(len(gr)))

plt.figure(2)

plt.plot(x_axis, gr_new, 'mx-', label='Greedy', markersize=5)

# random
rand = [67, 65, 54, 54, 53, 53, 53, 53, 53, 52, 14]

# process
rand_new = list(map(lambda x: x / rand[0], rand))

k = 249
x_axis = list(range(0, k, 25))
x_axis.append(k)

plt.plot(x_axis, rand_new, 'cx-', label='Random')

# weighted
weighted = [67, 66, 64, 63, 63, 14, 14, 14, 14, 14, 14]

weighted_new = list(map(lambda x: x / weighted[0], weighted))

plt.plot(x_axis, weighted_new, 'gx-', label='Weighted')

# betweenness
betweenness = [67, 28, 14, 18, 21, 22, 22, 24, 24, 24, 24, 25, 25, 25, 25, 25, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28,
               28, 29, 29, 29, 30, 30]
betweenness = betweenness[:len(x_axis)]

betweenness_new = list(map(lambda x: x / betweenness[0], betweenness))

x_axis[- 1] = x_axis[- 2] + 25

plt.plot(x_axis, betweenness_new, 'bx-', label='EdgeBetweennessDiff')

plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')
plt.legend()
plt.savefig('detLT_email_improved.png')
