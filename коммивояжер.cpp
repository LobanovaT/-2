#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    // Матрица расстояний между городами
    vector<vector<int>> graph = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    int n = graph.size();
    vector<int> vertices;
    for (int i = 1; i < n; ++i) {
        vertices.push_back(i);
    }

    int minCost = INT_MAX;
    vector<int> bestPath;

    do {
        int currentCost = 0;
        int k = 0; // стартуем из города 0
        // считаем сумму пути по текущему перму
        for (int i = 0; i < n - 1; ++i) {
            currentCost += graph[k][vertices[i]];
            k = vertices[i];
        }
        // возвращаемся в первый город
        currentCost += graph[k][0];

        if (currentCost < minCost) {
            minCost = currentCost;
            bestPath = vertices;
            bestPath.insert(bestPath.begin(), 0);
            bestPath.push_back(0);
        }

    } while (next_permutation(vertices.begin(), vertices.end()));

    // вывод результата
    cout << "Минимальный путь: ";
    for (int city : bestPath) {
        cout << city << " ";
    }
    cout << "\nОбщая длина: " << minCost << endl;

    return 0;
}
