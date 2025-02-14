#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    bool is_valid = true;
    
    for (int i = 0; i < n; i++) {
        int accountable_count = 0;
        for (int j = 0; j < m; j++) {
            char person;
            cin >> person;
            if (person == 'A') accountable_count++;
        }

        if (accountable_count != 1) {
            is_valid = false;
            break;
        }
    }

    cout << (is_valid ? "Yes" : "No") << '\n';

    return (0);
}
