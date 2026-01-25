#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    int F, S, G, U, D;
    cin >> F >> S >> G >> U >> D;
    
    vector<int> cnt(F + 1, -1);
    deque<int> q;
    q.push_back(S);
    cnt[S] = 0;
    
    while(!q.empty()) {
        int x = q.front(); q.pop_front();
 
        for (int nx : {x + U, x - D}) {
            if (1 <= nx && nx <= F && cnt[nx] == -1) {
                cnt[nx] = cnt[x] + 1;
                q.push_back(nx);
            }
        }
    }
    if (cnt[G] == -1) {
            cout << "use the stairs";
        } else {
            cout << cnt[G];
    }
    return 0;
}