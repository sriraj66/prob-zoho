import java.util.*;

public class MazeSolverDIR {

    public static void main(String[] args) {
        int n = 4;
        int[][] maze = {
            {1, 0, 0, 0},
            {1, 1, 0, 1},
            {1, 1, 0, 0},
            {0, 1, 1, 1}
        };

        List<String> paths = new ArrayList<>();
        boolean[][] visited = new boolean[n][n];
        String path = "";

        if (findPath(maze, 0, 0, n, visited, path, paths)) {
            System.out.println("Path found:");
            for (String p : paths) {
                System.out.println(p);
            }
        } else {
            System.out.println("No path found");
        }
    }

    public static boolean findPath(int[][] maze, int row, int col, int n, boolean[][] visited, String path, List<String> paths) {
        // Base case: reached the bottom-right corner
        if (row == n - 1 && col == n - 1) {
            paths.add(path);
            return true;
        }

        // Check if current cell is valid
        if (row < 0 || row >= n || col < 0 || col >= n || maze[row][col] == 0 || visited[row][col]) {
            return false;
        }

        // Mark current cell as visited
        visited[row][col] = true;

        // Explore in all 4 directions: right, down, left, up (in this order)
        if (findPath(maze, row, col + 1, n, visited, path + "R", paths) || // right
            findPath(maze, row + 1, col, n, visited, path + "D", paths) || // down
            findPath(maze, row, col - 1, n, visited, path + "L", paths) || // left
            findPath(maze, row - 1, col, n, visited, path + "U", paths)) { // up
            return true;
        }

        // Backtrack: mark current cell as unvisited
        visited[row][col] = false;
        return false;
    }
}
