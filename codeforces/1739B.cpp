#include <iostream>
#include <vector>

using namespace std;

int main() {
	int t, n;
	cin >> t;
	while (t--) {
		cin >> n;
		vector<int> d(n, 0);
		for (int i = 0; i < n; ++i) cin >> d[i];
		vector<int> a(n, 0);
		a[0] = d[0];
		bool flag = true;
		for (int i = 1; i < n; ++i) {
			int tmp1 = d[i] + a[i-1], tmp2 = (-d[i]) + a[i-1];
			if (tmp1 >= 0 && tmp2 >= 0 && tmp1 != tmp2) flag = false;
			if (tmp1 >= 0) a[i] = tmp1;
			else a[i] = tmp2;
		}
		if (!flag) {
			cout << "-1\n";
		} else {
			for (auto num : a) cout << num << ' ';
			cout << '\n';
		}
	}
}
