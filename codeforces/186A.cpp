#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	string s1, s2;
	cin >> s1;
	cin >> s2;
	size_t n = s1.length(), m = s2.length();

	if (s1 == s2) {
		cout << "YES\n";
		return 0;
	} else if (n != m) {
		cout << "NO\n";
		return 0;
	}

	vector<int> ind;
	for (int i = 0; i < n; ++i) {
		if (s1[i] != s2[i]) {
			ind.push_back(i);
		}
	}
	if (ind.size() == 2 && s1[ind[0]] == s2[ind[1]] && s1[ind[1]] == s2[ind[0]]) cout << "YES\n";
	else cout << "NO\n";
}
