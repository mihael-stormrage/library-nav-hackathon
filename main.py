import sqlite3
import matplotlib.pyplot as plt

"""INITIALIZE DATABASE"""
def create_simple_db():
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    # Таблица помещений

    sql.execute('''CREATE TABLE IF NOT EXISTS rooms (
        ID_Room INT,
        Floor INT,
        Color TEXT
    )''')

    # Таблица точек: помещения и промежуточные точки в коридорах (для них ID_Room = 0)

    sql.execute('''CREATE TABLE IF NOT EXISTS points (
        ID_Point INT,
        ID_Room INT,
        Point_X INT,
        Point_Y INT
    )''')

    # Для начала просто загрузим данные

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

    sql.executemany('INSERT INTO rooms VALUES (?, ?, ?)', rooms)
    sql.executemany('INSERT INTO points VALUES (?, ?, ?, ?)', points)

    db.commit()
    db.close()

def get_points_for_room(room) -> list, list, int:
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    x_points = []
    y_points = []
    for value in sql.execute('SELECT Point_X FROM points WHERE ID_Room = {room}'):
        x_points.append(value)
    for value in sql.execute('SELECT Point_Y FROM points WHERE ID_Room = {room}'):
        y_points.append(value)
    for value in sql.execute('SELECT Floor FROM rooms WHERE ID_Room = {room}'):
        floor = value
    return x_points
    return y_points

def draw_path(floor,):
    img = plt.imread("Floor_{floor}.png")
    fig, ax = plt.subplots()
    x = range(300)
    ax.imshow(img, extent=[0, 400, 0, 300])
    ax.plot(x, x, '--', linewidth=5, color='firebrick')
    plt.axis('off')
    plt.savefig('foo2.png', bbox_inches='tight')

if __name__ == '__main__':
    create_simple_db()
    x_points, y_points, floor = get_points_for_room()
    draw_path(floor)
