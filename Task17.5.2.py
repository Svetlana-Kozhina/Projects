# Алгоритм Дейкстры - позволяет найти кратчайший путь от одной вершины к другой.

G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}

D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от неё до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
        D[v] = min(D[v], D[min_k] + G[min_k][v]) # минимум
    U[min_k] = True # просмотренную вершину помечаем

print(D) #в результате - кратчайшее расстояние от "Адмиралтейской" до стации, которая задает ключ

