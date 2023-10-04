class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(image[sr][sc] == color)
            return image;
        return floodFillHelper(image, sr, sc, image[sr][sc], color, new boolean[image.length][image[0].length]);
        
    }

    public int[][] floodFillHelper(int[][] image, int sr, int sc, int color, int newColor, boolean[][] visited) {
        
        if(sr<0 || sc<0 || sr>=visited.length || sc>=visited[0].length || visited[sr][sc] || image[sr][sc]!=color)
            return image;
        image[sr][sc] = newColor;
        visited[sr][sc] = true;

        image = floodFillHelper(image, sr-1, sc, color, newColor, visited);
        image = floodFillHelper(image, sr+1, sc, color, newColor, visited);
        image = floodFillHelper(image, sr, sc-1, color, newColor, visited);
        image = floodFillHelper(image, sr, sc+1, color, newColor, visited);
        return image;
    }
}