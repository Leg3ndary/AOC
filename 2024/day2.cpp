#include <bits/stdc++.h>

using namespace std;

void setup() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("tests/day2.txt", "r", stdin);
    cin.clear();
    fseek(stdin, 0, SEEK_SET);
}

void problem1() {
    vector<string> lines;
    string temp;
    while (getline(cin, temp)) {
        lines.push_back(temp);
    }
    int safe = 0;

    for (const string line : lines) {
        vector<int> data;
        stringstream ss(line);
        int temp;
        while (ss >> temp) {
            data.push_back(temp);
        }

        if (is_sorted(data.begin(), data.end()) || is_sorted(data.begin(), data.end(), greater<int>())) {
            bool valid = true;
            for (size_t i = 0; i < data.size() - 1 && valid; ++i) {
                int diff = abs(data[i] - data[i + 1]);
                if (!(diff > 0 && diff < 4)) {
                    valid = false;
                }
            }
            if (valid) {
                safe++;
            }
        }
    }
    cout << safe << endl;
}

void problem2() {
    vector<string> lines;
    string temp;
    while (getline(cin, temp)) {
        lines.push_back(temp);
    }
    int safe = 0;

    for (const string &line : lines) {
        vector<int> data;
        stringstream ss(line);
        int temp;
        while (ss >> temp) {
            data.push_back(temp);
        }

        auto is_safe = [](const vector<int> &vec) -> bool {
            if (is_sorted(vec.begin(), vec.end()) || is_sorted(vec.begin(), vec.end(), greater<int>())) {
                for (size_t i = 0; i < vec.size() - 1; ++i) {
                    int diff = abs(vec[i] - vec[i + 1]);
                    if (!(diff > 0 && diff < 4)) {
                        return false;
                    }
                }
                return true;
            }
            return false;
        };

        if (is_safe(data)) {
            safe++;
            continue;
        }
        bool made_safe = false;
        for (size_t i = 0; i < data.size(); ++i) {
            vector<int> modified_data = data;
            modified_data.erase(modified_data.begin() + i);
            if (is_safe(modified_data)) {
                made_safe = true;
                break;
            }
        }

        if (made_safe) {
            safe++;
        }
    }

    cout << safe << endl;
}


int main() {
    setup();
    problem1();
    setup();
    problem2();
    return 0;
}