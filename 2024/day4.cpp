#include <bits/stdc++.h>

using namespace std;

void setup() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("tests/day4.txt", "r", stdin);
}

bool valid(int x, int y, int n, int m) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

int countXMAS(const vector<string>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    string target = "XMAS";
    int targetLength = target.size();
    int count = 0;

    vector<pair<int, int>> dirs = {
        {1, 1}, {1, -1}, {-1, -1}, {-1, 1}
    };

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (const auto& dir : dirs) {
                int dx = dir.first, dy = dir.second;
                int x = i, y = j;
                bool found = true;

                for (int k = 0; k < targetLength; ++k) {
                    if (!valid(x, y, n, m) || grid[x][y] != target[k]) {
                        found = false;
                        break;
                    }
                    x += dx;
                    y += dy;
                }

                if (found) count++;
            }
        }
    }

    return count;
}

int countXMAS2(const vector<string>& grid) {
    int n = grid.size();
    int m = grid[0].size();
    int count = 0;

    vector<pair<int, int>> topLeft = {{-1, -1}, {1, 1}};
    vector<pair<int, int>> bottomLeft = {{1, -1}, {-1, 1}};
    string patterns[2] = {"MAS", "SAM"}; 

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] != 'A') continue;

            for (const auto& pattern : patterns) {
                bool isXMAS = true;
                
                for (int k = 0; k < 3; ++k) {
                    int x = i + k * topLeft[0].first, y = j + k * topLeft[0].second;
                    if (!valid(x, y, n, m) || grid[x][y] != pattern[k]) {
                        isXMAS = false;
                        break;
                    }
                }

                if (!isXMAS) continue;

                for (int k = 0; k < 3; ++k) {
                    int x = i + k * bottomLeft[0].first, y = j + k * bottomLeft[0].second;
                    if (!valid(x, y, n, m) || grid[x][y] != pattern[k]) {
                        isXMAS = false;
                        break;
                    }
                }

                if (isXMAS) count++;
            }
        }
    }

    return count;
}

void problem1() {
    vector<string> grid;
    string line;

    while (cin >> line) {
        grid.push_back(line);
    }

    cout << "Total occurrences of XMAS: " << countXMAS(grid) le<< "\n";
}

void problem2() {
    vector<string> grid;
    string line;

    while (cin >> line) {
        grid.push_back(line);
    }

    cout << "Total X-MAS occurrences: " << countXMAS2(grid) << "\n";
}

int main() {
    setup();
    problem1();
    setup();
    problem2();
    return 0;
}
