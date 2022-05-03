import matplotlib.pyplot as plt

# greedy
gr = [48907, 47596, 46426, 45508, 44733, 44099, 43502, 42944, 42390, 41863, 41357, 40879, 40411, 39947, 39483, 39033,
      38587, 38153, 37746, 37347, 36950, 36554, 36191, 35846, 35514, 35195, 34892, 34593, 34297, 34003, 33711, 33425,
      33139, 32862, 32585, 32310, 32044, 31779, 31516, 31254, 30994, 30734, 30480, 30232, 29984, 29737, 29497, 29262,
      29030, 28799, 28572, 28345, 28119, 27897, 27677, 27459, 27242, 27026, 26813, 26600, 26389, 26186, 25984, 25783,
      25585, 25391, 25198, 25008, 24819, 24631, 24443, 24264, 24089, 23915, 23741, 23568, 23396, 23225, 23054, 22884,
      22716, 22549, 22382, 22216, 22053, 21892, 21732, 21573, 21414, 21255, 21100, 20948, 20800, 20654, 20509, 20364,
      20221, 20079, 19937, 19795, 19654, 19514, 19374, 19236, 19103, 18970, 18838, 18707, 18576, 18445, 18314, 18185,
      18056, 17928, 17800, 17672, 17545, 17418, 17293, 17168, 17044, 16920, 16797, 16674, 16555, 16436, 16319, 16203,
      16087, 15972, 15857, 15743, 15629, 15516, 15404, 15292, 15180, 15068, 14957, 14847, 14738, 14630, 14522, 14415,
      14311, 14207, 14105, 14003, 13902, 13802, 13702, 13603, 13505, 13407, 13309, 13211, 13114, 13018, 12922, 12827,
      12732, 12638, 12544, 12451, 12358, 12266, 12174, 12082, 11990, 11898, 11807, 11716, 11626, 11536, 11447, 11358,
      11270, 11182, 11094, 11007, 10920, 10834, 10748, 10663, 10578, 10493, 10409, 10325, 10241, 10157, 10074, 9991,
      9909, 9827, 9747, 9667, 9588, 9509, 9430, 9352, 9274, 9197, 9122, 9047, 8974, 8901, 8828, 8756, 8684, 8612, 8540,
      8469, 8399, 8329, 8259, 8190, 8121, 8053, 7985, 7917, 7849, 7782, 7716, 7650, 7584, 7519, 7454, 7390, 7326, 7262,
      7199, 7137, 7075, 7014, 6954, 6894, 6834, 6774, 6714, 6655, 6596, 6537, 6478, 6421, 6364, 6307, 6251, 6195, 6139,
      6084, 6029, 5975, 5921, 5867, 5813, 5760, 5707, 5655, 5603, 5552, 5503, 5454, 5405, 5356, 5308, 5260, 5212, 5164,
      5117, 5070, 5023, 4976, 4930, 4884, 4838, 4793, 4748, 4704, 4660, 4617, 4574, 4531, 4489, 4447, 4405, 4363, 4321,
      4280, 4239, 4198, 4157, 4116, 4075, 4035, 3995, 3956, 3917, 3878, 3839, 3800, 3761, 3722, 3683, 3644, 3606, 3568,
      3530, 3493, 3456, 3420, 3384, 3348, 3312, 3276, 3240, 3205, 3170, 3135, 3100, 3066, 3032, 2998, 2964, 2930, 2896,
      2862, 2828, 2794, 2761, 2728, 2695, 2662, 2629, 2596, 2563, 2531, 2499, 2467, 2435, 2403, 2371, 2340, 2309, 2278,
      2247, 2216, 2185, 2154, 2123, 2092, 2061, 2031, 2001, 1972, 1943, 1915, 1887, 1859, 1832, 1805, 1778, 1751, 1725,
      1699, 1673, 1647, 1621, 1596, 1571, 1546, 1521, 1497, 1473, 1449, 1425, 1401, 1377, 1353, 1329, 1306, 1284, 1262,
      1240, 1218, 1197, 1176, 1155, 1134, 1113, 1093, 1073, 1053, 1033, 1014, 995, 976, 957, 938, 920, 902, 884, 867,
      850, 833, 816, 799, 782, 766, 750, 735, 720, 705, 690, 676, 662, 648, 634, 620, 606, 592, 578, 564, 550, 537, 524,
      511, 498, 486, 474, 462, 450, 438, 426, 414, 403, 392, 381, 370, 359, 348, 338, 328, 318, 309, 300, 291, 283, 275,
      267, 259, 251, 244, 237, 230, 223, 216, 209, 202, 195, 189, 183, 177, 172, 167, 162, 157, 153, 149, 145, 141, 137,
      133, 129, 125, 121, 117, 114, 111, 108, 105, 102, 99, 97, 95, 93, 91, 90, 89]
# process
gr_new = list(map(lambda x: x / gr[0], gr))

x_axis = list(range(len(gr)))

plt.figure(1)
plt.plot(x_axis, gr_new, 'mx-', label='Greedy', markersize=3)

# random
rand = [48655, 44216, 38882, 35781, 30894, 26364, 21224, 15983, 9983, 4285, 164]

# process
rand_new = list(map(lambda x: x / rand[0], rand))

k = 494
x_axis = list(range(0, k, 50))
x_axis.append(k)

plt.plot(x_axis, rand_new, 'cx-', label='Random', markersize=5)

# weighted
weighted = [48714, 33639, 26556, 19982, 14789, 10291, 7584, 4598, 1992, 565, 115]

weighted_new = list(map(lambda x: x / weighted[0], weighted))

plt.plot(x_axis, weighted_new, 'gx-', label='Weighted', markersize=5)

# distance
distance = [48250, 37499, 33745, 31251, 29400, 24865, 16752, 12559, 7697, 5196, 3239, 2730, 2750, 2753, 1450, 1483,
            1504, 1515, 1517, 1524, 1586, 1614, 1501, 1515, 1517, 1523, 1527, 1535, 1550, 682, 708, 720, 747, 754, 800,
            828, 860, 884, 925, 940, 949, 951, 951, 927, 934, 942, 962, 966, 983, 992, 1010, 1019, 1027, 1037, 1048,
            1052, 1059, 1074, 1141, 1149, 1179, 1166, 1221, 1238]

distance_new = list(map(lambda x: x / distance[0], distance))
k = 3111

x_axis = list(range(0, k, 50))
x_axis.append(k)

plt.plot(x_axis, distance_new, 'bx-', label='DistanceDiff', markersize=5)

plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')
plt.legend()
plt.savefig('LT_wiki.png')

# improved plot

# greedy
gr = [48907, 47596, 46426, 45508, 44733, 44099, 43502, 42944, 42390, 41863, 41357, 40879, 40411, 39947, 39483, 39033,
      38587, 38153, 37746, 37347, 36950, 36554, 36191, 35846, 35514, 35195, 34892, 34593, 34297, 34003, 33711, 33425,
      33139, 32862, 32585, 32310, 32044, 31779, 31516, 31254, 30994, 30734, 30480, 30232, 29984, 29737, 29497, 29262,
      29030, 28799, 28572, 28345, 28119, 27897, 27677, 27459, 27242, 27026, 26813, 26600, 26389, 26186, 25984, 25783,
      25585, 25391, 25198, 25008, 24819, 24631, 24443, 24264, 24089, 23915, 23741, 23568, 23396, 23225, 23054, 22884,
      22716, 22549, 22382, 22216, 22053, 21892, 21732, 21573, 21414, 21255, 21100, 20948, 20800, 20654, 20509, 20364,
      20221, 20079, 19937, 19795, 19654, 19514, 19374, 19236, 19103, 18970, 18838, 18707, 18576, 18445, 18314, 18185,
      18056, 17928, 17800, 17672, 17545, 17418, 17293, 17168, 17044, 16920, 16797, 16674, 16555, 16436, 16319, 16203,
      16087, 15972, 15857, 15743, 15629, 15516, 15404, 15292, 15180, 15068, 14957, 14847, 14738, 14630, 14522, 14415,
      14311, 14207, 14105, 14003, 13902, 13802, 13702, 13603, 13505, 13407, 13309, 13211, 13114, 13018, 12922, 12827,
      12732, 12638, 12544, 12451, 12358, 12266, 12174, 12082, 11990, 11898, 11807, 11716, 11626, 11536, 11447, 11358,
      11270, 11182, 11094, 11007, 10920, 10834, 10748, 10663, 10578, 10493, 10409, 10325, 10241, 10157, 10074, 9991,
      9909, 9827, 9747, 9667, 9588, 9509, 9430, 9352, 9274, 9197, 9122, 9047, 8974, 8901, 8828, 8756, 8684, 8612, 8540,
      8469, 8399, 8329, 8259, 8190, 8121, 8053, 7985, 7917, 7849, 7782, 7716, 7650, 7584, 7519, 7454, 7390, 7326, 7262,
      7199, 7137, 7075, 7014, 6954, 6894, 6834, 6774, 6714, 6655, 6596, 6537, 6478, 6421, 6364, 6307, 6251, 6195, 6139,
      6084, 6029, 5975, 5921, 5867, 5813, 5760, 5707, 5655, 5603, 5552, 5503, 5454, 5405, 5356, 5308, 5260, 5212, 5164,
      5117, 5070, 5023, 4976, 4930, 4884, 4838, 4793, 4748, 4704, 4660, 4617, 4574, 4531, 4489, 4447, 4405, 4363, 4321,
      4280, 4239, 4198, 4157, 4116, 4075, 4035, 3995, 3956, 3917, 3878, 3839, 3800, 3761, 3722, 3683, 3644, 3606, 3568,
      3530, 3493, 3456, 3420, 3384, 3348, 3312, 3276, 3240, 3205, 3170, 3135, 3100, 3066, 3032, 2998, 2964, 2930, 2896,
      2862, 2828, 2794, 2761, 2728, 2695, 2662, 2629, 2596, 2563, 2531, 2499, 2467, 2435, 2403, 2371, 2340, 2309, 2278,
      2247, 2216, 2185, 2154, 2123, 2092, 2061, 2031, 2001, 1972, 1943, 1915, 1887, 1859, 1832, 1805, 1778, 1751, 1725,
      1699, 1673, 1647, 1621, 1596, 1571, 1546, 1521, 1497, 1473, 1449, 1425, 1401, 1377, 1353, 1329, 1306, 1284, 1262,
      1240, 1218, 1197, 1176, 1155, 1134, 1113, 1093, 1073, 1053, 1033, 1014, 995, 976, 957, 938, 920, 902, 884, 867,
      850, 833, 816, 799, 782, 766, 750, 735, 720, 705, 690, 676, 662, 648, 634, 620, 606, 592, 578, 564, 550, 537, 524,
      511, 498, 486, 474, 462, 450, 438, 426, 414, 403, 392, 381, 370, 359, 348, 338, 328, 318, 309, 300, 291, 283, 275,
      267, 259, 251, 244, 237, 230, 223, 216, 209, 202, 195, 189, 183, 177, 172, 167, 162, 157, 153, 149, 145, 141, 137,
      133, 129, 125, 121, 117, 114, 111, 108, 105, 102, 99, 97, 95, 93, 91, 90, 89]

# process
gr_new = list(map(lambda x: x / gr[0], gr))

x_axis = list(range(len(gr)))

plt.figure(2)

plt.plot(x_axis, gr_new, 'mx-', label='Greedy', markersize=5)

# random
rand = [48655, 44216, 38882, 35781, 30894, 26364, 21224, 15983, 9983, 4285, 164]

# process
rand_new = list(map(lambda x: x / rand[0], rand))

k = 494
x_axis = list(range(0, k, 50))
x_axis.append(k)

plt.plot(x_axis, rand_new, 'cx-', label='Random')

# weighted
weighted = [48714, 33639, 26556, 19982, 14789, 10291, 7584, 4598, 1992, 565, 115]

weighted_new = list(map(lambda x: x / weighted[0], weighted))

plt.plot(x_axis, weighted_new, 'gx-', label='Weighted')
plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')

# distance
distance = [48250, 37499, 33745, 31251, 29400, 24865, 16752, 12559, 7697, 5196, 3239, 2730, 2750, 2753, 1450, 1483,
            1504, 1515, 1517, 1524, 1586, 1614, 1501, 1515, 1517, 1523, 1527, 1535, 1550, 682, 708, 720, 747, 754, 800,
            828, 860, 884, 925, 940, 949, 951, 951, 927, 934, 942, 962, 966, 983, 992, 1010, 1019, 1027, 1037, 1048,
            1052, 1059, 1074, 1141, 1149, 1179, 1166, 1221, 1238]

distance = distance[:len(x_axis)]

distance_new = list(map(lambda x: x / distance[0], distance))

x_axis[- 1] = x_axis[- 2] + 50

plt.plot(x_axis, distance_new, 'bx-', label='DistanceDiff')

plt.ylabel('Susceptibility Ratio')
plt.xlabel('# removed edges')
plt.legend()
plt.savefig('LT_wiki_improved.png')
