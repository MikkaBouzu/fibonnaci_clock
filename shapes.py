from matplotlib import pyplot as plt


fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(8, 5)

ax = plt.axes(xlim=(0, 8), ylim=(0, 5))

one = plt.Rectangle((2, 3), 1, 1, fc='g')
one_2 = plt.Rectangle((2, 4), 1, 1, fc='r')
two = plt.Rectangle((0, 3), 2, 2, fc='b')
three = plt.Rectangle((0, 0), 3, 3, fc='r')
five = plt.Rectangle((3, 0), 5, 5, fc='b')


for shape in [one, one_2, two, three, five]:
    plt.gca().add_patch(shape)

# plt.axis('scaled')

plt.show()
