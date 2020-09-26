import matplotlib.pyplot as plt
img = plt.imread('Floor_1.png')
fig, ax = plt.subplots()

rooms = [
    (203, 2, 'red'),
    (301, 3, 'green'),
    (102, 1, 'yellow')
]

points = [
    (1, 0, 1050, 650),
    (2, 0, 1050, 550),
    (3, 102, 450, 550)
]

ax.imshow(img)
ax.plot([points[0][2], points[1][2],points[2][2]], [points[0][3], points[1][3],points[2][3]], '--', linewidth=5, color='yellow')
plt.axis('off')
plt.savefig('foo2.png')

