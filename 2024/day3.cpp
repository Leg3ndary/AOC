#include <bits/stdc++.h>

using namespace std;

void setup() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("tests/day3.txt", "r", stdin);
    cin.clear();
    fseek(stdin, 0, SEEK_SET);
}

void problem1() {
    string input;
    string temp;
    while (getline(cin, temp)) {
        input += temp;
    }
    regex pattern(R"(mul\((\d{1,3}),(\d{1,3})\))");
    smatch match;
    long long sum = 0;

    auto it = input.cbegin();
    while (regex_search(it, input.cend(), match, pattern)) {
        int x = stoi(match[1].str());
        int y = stoi(match[2].str());
        sum += x * y;
        it = match.suffix().first;
    }

    cout << "Sum of all results: " << sum << "\n";
}

void problem2() {
    string input;
    string temp;

    while (getline(cin, temp)) {
        input += temp;
    }

    regex combinedPattern(R"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))");
    smatch match;
    long long sum = 0;
    bool enabled = true;

    auto it = input.cbegin();
    while (regex_search(it, input.cend(), match, combinedPattern)) {
        string matched = match.str();

        if (matched.find("mul") == 0) {
            if (enabled) {
                int x = stoi(match[1].str());
                int y = stoi(match[2].str());
                sum += x * y;
            }
        } else if (matched == "do()") {
            enabled = true;
        } else if (matched == "don't()") {
            enabled = false;
        }

        it = match.suffix().first;
    }

    cout << "Sum of all results: " << sum << "\n";
}

int main() {
    setup();
    problem1();
    setup();
    problem2();
    return 0;
}