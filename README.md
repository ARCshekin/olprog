# olprog

Хочется сохранить всё то, что я учу по спортивному программированию. Может быть однажды это будет полезно кому-нибудь)
Да и к тому же на питоне очень сложно найти какие-либо материалы, вся спорт. прога идёт на плюсах. Иногда Си или Джава.
Реализации всех алгоритмов присутствуют, алгоритмы по графам в папке "graphs" и так далее.

## Графы

### Термины
Не буду касаться совсем банальщины типо "взвешенный", "ориентированный" или "ребро"/"узел"

- <b>Остовное дерево</b> - подграф для данного графа, который является деревом. Простыми словами мы убираем все циклы из графа.
- <b>Минимальное остовное дерево</b> - остовное дерево, в котором сумма весов всех рёбер минимальна
- <b>Гамильтонов цикл</b> - цикл, который обходит каждый узел в графе
- <b>Релаксация ребра</b> - перерассчёт стоимости досягания до ребра. Например попасть в ребро n = cost[n] мы можем попасть из ребра a в ребро b за w[a][b]. Тогда релаксация ребра i: cost[i] = min(cost[i], cost[j] + w[j][i]).

### Алгоритмы:

#### Алгоритм Дейкстры. 
- Нужен чтобы рассчитать кратчайшее расстояние от A до B
- Первый раз выбираем ребро A, в следующие разы - ребро с минимальным весом, которое до этого не использовали
- Для выбранного ребра релаксируем все рёбра, в которые можно попасть напрямую из A.
- Повторяем так пока не будет выбрано ребро B.
- Если все рёбра с небесконечным расстоянием уже выбирали, а до B так и не дошли - значит оно недосягаемо из A
- Ассимптотика O(n<sup>2</sup>)

/graphs/dijkstra.py

### Алгоритм Форда-Беллмана
- Поиск минимального расстояния от A до каждой точки.
- Создаём массив dp размерами n*n. dp[0][A] = 0, все остальные элементы бесконечно большие
- Алгоритм задействует n-1 итерацию (номер итерации будем обозначать k, k∈[1, n)), каждый раз мы просто релаксируем каждую вершину по всем входящим в неё рёбрам.
- В начале каждой итерации для всех i dp[k][i] = dp[k][i-1]. 
- Релаксация ребра i с помощью ребра j будет выглядеть как dp[k][i] = min(dp[k][i], dp[k][j] + w[j][i]).
- Дополнение алгоритма. Если после n-1 итераций провести ещё одну и хоть один вес изменится - будет означать, что на графе присутствует цикл отрицательного веса.
- Ассимптотика O(n<sup>3</sup>)

/graphs/ford-bellman.py

### Алгоритм Краскала
- Составление остовного дерева наименьшего веса
- Сортируем все рёбра по весу, начинаем с минимального.
- Пока все узлы не будут соединены, проходимся по всем рёбрам (в отсортированном порядке).
- За основу сразу берём ребро с минимальным весом, соотвественно в наше будущее остовное дерево входит пока только две вершины
- Если ребро соединено одним из концов с уже добавленным узлом, а вторым — нет, то добавляем это ребро. И начинаем смотреть снова все рёбра с первого, иначе идём к следующему в списке
- Если мы дошли до последнего ребра и оно нас не удовлетворило — значит рёбер недостаточно для решения задачи.
- Ассимптотика O(M<i>log</i>M + n<sup>2</sup>)

/graphs/kruskal.py

### Алгоритм Флойда
- Кратчайшее расстояние от a до b
- По сути задача на двумерную динамику. Сначала мы используем рёбра с номерами меньше 0, потом меньше 1, 2 ... n.
- Т. е. изначально мы просто смотрим на наличие ребра между a и b, потом рассматриваем каждый раз на один узел больше и пытаемся с помощью него оптимизировать маршрут.
- 
