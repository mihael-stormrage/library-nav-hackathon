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

def get_points_for_room() -> list, list:
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    for value in sql.execute('SELECT * FROM ')


def draw_path():

    """DRAWING THE PATH"""
    img = plt.imread("Floor_1.png")
    fig, ax = plt.subplots()
    x = range(300)
    ax.imshow(img, extent=[0, 400, 0, 300])
    ax.plot(x, x, '--', linewidth=5, color='firebrick')
    plt.axis('off')
    plt.savefig('foo2.png', bbox_inches='tight')

if __name__ == '__main__':
    create_simple_db()
    x_points, y_points  = get_points_for_room()
