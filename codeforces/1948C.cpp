#include <iostream>
#include <vector>
#include <string>
#include <deque>


using namespace std;



int main() {
	int t, n;
	cin >> t;
	while (t--) {
		cin >> n;
		vector<string> grid(2);
		cin >> grid[0];
		cin >> grid[1];
		bool flag = true;
		for (int i = 1; i < n; i += 2) {
			if ((grid[0][i] == '<' && grid[1][i-1] == '<') || (grid[0][i] == '<' && grid[1][i+1] == '<')) {
				flag = false;
			}
		}
		if (flag) cout << "YES\n";
		else cout << "NO\n";
	}
	return 0;
}
