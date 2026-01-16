#include <iostream>
#include <string>

using namespace std;

int n, isPossible;
string a, b;

int main() {
    cin >> n;
    while(n--) {
        int cnt_a[26] = {};
        int cnt_b[26] = {};

        cin >> a >> b;
        if (a.length() != b.length()) {
            cout << "Impossible" << "\n";
            continue;
        }
        for (int i = 0; i < a.length(); i++) {
            cnt_a[a[i] - 'a']++;
            cnt_b[b[i] - 'a']++;
        }
        isPossible = true;
        for (int i = 0; i < 26; i++) {
            if (cnt_a[i] != cnt_b[i]) {
                isPossible = false;
                break;
            }
        }
        if (isPossible) {
            cout << "Possible" << "\n";
        } else {
            cout << "Impossible" << "\n";
        }
    }
    return (0);
}