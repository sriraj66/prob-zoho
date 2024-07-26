import java.util.*;

public class MazeSolver {

    public static void main(String[] args) {
        int n = 4;
        int[][] m = {{1,0,0,0},{1,1,0,1},{1,1,0,0},{0,1,1,0}};

        List<String> paths = new ArrayList<>();
        boolean[][] visited = new boolean[n][n];

        if (findPath(m, 0, 0, n, visited, paths)) {
            System.out.println("Path found:");
            for (String path : paths) {
                System.out.println(path);
            }
        } else {
            System.out.println("No path found");
        }
    }

    public static boolean findPath(int[][] maze, int row, int col, int n, boolean[][] visited, List<String> paths) {
        // Base case: reached the bottom-right corner
        if (row == n-1 && col == n-1) {
            paths.add("(" + row + "," + col + ")");
            return true;
        }

        // Check if current cell is valid
        if (row < 0 || row >= n || col < 0 || col >= n || maze[row][col] == 0 || visited[row][col]) {
            return false;
        }

        // Mark current cell as visited
        visited[row][col] = true;

        // Explore in all 4 directions: right, down, left, up (in this order)
        if (findPath(maze, row, col + 1, n, visited, paths) || // right
            findPath(maze, row + 1, col, n, visited, paths) || // down
            findPath(maze, row, col - 1, n, visited, paths) || // left
            findPath(maze, row - 1, col, n, visited, paths)) { // up
            paths.add("(" + row + "," + col + ")");
            return true;
        }

        // Backtrack: mark current cell as unvisited
        visited[row][col] = false;
        return false;
    }
}
