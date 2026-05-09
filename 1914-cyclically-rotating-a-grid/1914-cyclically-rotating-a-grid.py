class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # m, n = len(grid), len(grid[0])

        # layers = min(m, n) // 2

        # for layer in range(layers):
        #     vals = []

        #     top = layer
        #     left = layer
        #     bottom = m - layer - 1
        #     right = n - layer - 1

        #     for j in range(left, right + 1):
        #         vals.append(grid[top][j])

        #     for i in range(top + 1, bottom):
        #         vals.append(grid[i][right])

        #     for j in range(right, left - 1, -1):
        #         vals.append(grid[bottom][j])

        #     for i in range(bottom - 1, top, -1):
        #         vals.append(grid[i][left])

        #     sz = len(vals)
        #     idx = k % sz

        #     for j in range(left, right + 1):
        #         grid[top][j] = vals[idx]
        #         idx += 1

        #         if idx == sz:
        #             idx = 0

        #     for i in range(top + 1, bottom):
        #         grid[i][right] = vals[idx]
        #         idx += 1
                
        #         if idx == sz:
        #             idx = 0

        #     for j in range(right, left - 1, -1):
        #         grid[bottom][j] = vals[idx]
        #         idx += 1

        #         if idx == sz:
        #             idx = 0

        #     for i in range(bottom - 1, top, -1):
        #         grid[i][left] = vals[idx]
        #         idx += 1

        #         if idx == sz:
        #             idx = 0

        # return grid


        T, L = 0, 0
        B, R = len(grid) - 1, len(grid[0]) - 1

        while T < B and L < R:
            ln, wid = B - T, R - L
            perimeter = 2 * (ln + wid)
            r = k % perimeter

            while r:
                tmp = grid[T][L]

                for i in range(L, R):
                    grid[T][i] = grid[T][i + 1]

                for i in range(T, B):
                    grid[i][R] = grid[i + 1][R]

                for i in range(R, L, -1):
                    grid[B][i] = grid[B][i - 1]

                for i in range(B, T, -1):
                    grid[i][L] = grid[i - 1][L]

                grid[T + 1][L] = tmp
                r -= 1

            T += 1
            L += 1
            B -= 1
            R -= 1

        return grid
