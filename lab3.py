import pandas as pd
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# Зчитування датасету
data = pd.read_csv('DS5.txt', sep=' ', header=None, names=['x', 'y'])

# Знаходження опуклої оболонки
hull = ConvexHull(data)

# Збереження опуклої оболонки у файл
# hull.vertices - масив індексів точок, які утворюють вершини опуклої оболонки. 
# Ці індекси вказують на позиції рядків у data (об'єкт класу DataFrame).
# data.iloc[hull.vertices] повертає новий DataFrame, що містить лише ті рядки з data, які відповідають вершинам опуклої оболонки.
hull_points = data.iloc[hull.vertices]
hull_points.to_csv('DS5_hull.txt', sep=' ', index=False, header=False)

# Створення фігури з розміром полотна 960x540 пікселів
fig = plt.figure(figsize=(960/100, 540/100))

# Встановлення осей графіка, щоб вони займали весь простір фігури
ax = fig.add_axes([0, 0, 1, 1])  # [лівий край, нижній край, ширина, висота]

# Розташування точок
ax.scatter(data['x'], data['y'])

# Відображення опуклої оболонки
# data.iloc[hull.vertices, 0] вибирає значення координати x для всіх точок, які утворюють вершини опуклої оболонки.
# data.iloc[hull.vertices, 1] вибирає значення координати y для цих же точок.
plt.plot(data.iloc[hull.vertices, 0], data.iloc[hull.vertices, 1], 'b-')

# Виведення результату у графічний файл
plt.savefig('output.png', dpi=100)

# Відображення полотна у вікні
plt.show()