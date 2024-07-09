#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

int main() {
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	int n, m;
	cin >> n;
	vector<long long> heroes(n, 0);
	for (int i = 0; i < n; ++i) cin >> heroes[i];
	sort(heroes.begin(), heroes.end());
	cin >> m;
	vector<long long> answers;
	long long total = 0;
	total = accumulate(heroes.begin(), heroes.end(), 0ll);
	while (m--) {
		long long x, y;
		cin >> x >> y;
		int i = lower_bound(heroes.begin(), heroes.end(), x) - heroes.begin();
		long long ans = numeric_limits<long long>::max();
		if (i > 0) ans = min(ans, (x - heroes[i - 1]) + max(0LL, y - total + heroes[i - 1]));
		if (i < n) ans = min(ans, max(0LL, y - total + heroes[i]));
		answers.push_back(ans);
	}
	for (auto a : answers) cout << a << '\n';
}
