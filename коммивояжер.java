import java.util.ArrayList;

public class TravelingSalesman {
    private int n; // число городов
    private int[][] graph; // матрица расстояний
    private boolean[] visited;
    private ArrayList<Integer> path = new ArrayList<>();
    private int minCost = Integer.MAX_VALUE;
    private ArrayList<Integer> bestPath = new ArrayList<>();

    public TravelingSalesman(int[][] graph) {
        this.n = graph.length;
        this.graph = graph;
        this.visited = new boolean[n];
    }

    public void findOptimalTour() {
        path.add(0); // начинаем с города 0
        visited[0] = true;
        backtrack(0, 1, 0);
        System.out.println("Минимальный маршрут: " + bestPath);
        System.out.println("Общая длина: " + minCost);
    }

    private void backtrack(int currentCity, int count, int costSoFar) {
        if (count == n) {
            // возвращаемся в стартовый город
            int totalCost = costSoFar + graph[currentCity][0];
            if (totalCost < minCost) {
                minCost = totalCost;
                bestPath = new ArrayList<>(path);
                bestPath.add(0); // возвращаемся в старт
            }
            return;
        }
        for (int nextCity = 1; nextCity < n; nextCity++) {
            if (!visited[nextCity]) {
                int newCost = costSoFar + graph[currentCity][nextCity];
                if (newCost < minCost) { // оптимизационная проверка (отбрасываем путь с большим весом)
                    visited[nextCity] = true;
                    path.add(nextCity);
                    backtrack(nextCity, count + 1, newCost);
                    visited[nextCity] = false;
                    path.remove(path.size() - 1);
                }
            }
        }
    }

    public static void main(String[] args) {
        int[][] distances = {
            {0, 10, 15, 20},
            {10, 0, 35, 25},
            {15, 35, 0, 30},
            {20, 25, 30, 0}
        };
        TravelingSalesman tsp = new TravelingSalesman(distances);
        tsp.findOptimalTour();
    }
}
