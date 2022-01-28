from matplotlib import pyplot as plt


fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(8, 5)

ax = plt.axes(xlim=(0, 8), ylim=(0, 5))
# no axes numeration
ax.set_yticks([])
ax.set_xticks([])

one = plt.Rectangle((2, 3), 1, 1, fc='w', ec='black')
one_2 = plt.Rectangle((2, 4), 1, 1, fc='w', ec='black')
two = plt.Rectangle((0, 3), 2, 2, fc='w', ec='black')
three = plt.Rectangle((0, 0), 3, 3, fc='w', ec='black')
five = plt.Rectangle((3, 0), 5, 5, fc='w', ec='black')

shapes = [one, one_2, two, three, five]

for shape in shapes:
    plt.gca().add_patch(shape)


colors = {'r': [], 'g': [4], 'b': [3, 1], 'w': [2, 0]}


def update(colors):
    for color, indices in zip(colors.keys(), colors.values()):
        for i in indices:
            shapes[i].set_facecolor(color)


update(colors)


plt.show()
