#include <bits/stdc++.h>

using namespace std;

void setup() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("tests/day1.txt", "r", stdin);
    cin.clear();
    fseek(stdin, 0, SEEK_SET);
}

void problem1() {
    vector<int> la;
    vector<int> lb;

    int a, b;
    while (cin >> a >> b) {
        la.push_back(a);
        lb.push_back(b);
    }

    sort(la.begin(), la.end());
    sort(lb.begin(), lb.end());

    int answer = 0;
    for (size_t i = 0; i < la.size(); ++i) {
        answer += abs(la[i] - lb[i]);
    }
    cout << answer << endl;
}

void problem2() {
    unordered_map<int, int> la;
    unordered_map<int, int> lb;
    int a, b;

    while (cin >> a >> b) {
        la[a]++;
        lb[b]++;
    }

    int answer = 0;
    
    for (auto it = la.begin(); it != la.end(); ++it) {
        if (lb.find(it->first) != lb.end()) {
            answer += it->first * lb[it->first];
        }
    }

    cout << answer << endl;
}

int main() {
    setup();
    problem1();
    setup();
    problem2();
    return 0;
}