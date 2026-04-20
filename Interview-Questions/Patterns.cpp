#include <bits/stdc++.h>
using namespace std;
void print_pattern_1(int input) {
    for (int i = 0; i < input; i++) {
        for (int j = 0; j < input; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testcases;
    cin >> testcases;
    for (int i=0;i<testcases;i++) {
        int input;
        cin >> input;
        print_pattern_1(input);
    }
    return 0;
}