#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t, n;
	string s;
	cin >> t;
	vector<long long> answers;
	while (t--) {
		cin >> n;
		long long ans = 0;
		map<int, vector<int> > mp1;
		map<int, vector<int> > mp2;
		while (n--) {
			cin >> s;
			// check first index
			if (mp1.find(s[0]) != mp1.end()) {
				for (int i = 0; i < 26; ++i) {
					// skip its second
					if (i == s[1] - 'a') continue;
					ans += mp1[s[0]][i];
				}
			}
			// check second ind
			if (mp2.find(s[1]) != mp2.end()) {
				for (int i = 0; i < 26; ++i) {
					if (i == s[0] - 'a') continue;
					ans += mp2[s[1]][i];
				}
			}
			// add to map
			if (mp1.find(s[0]) == mp1.end()) mp1[s[0]] = vector<int>(26, 0);
			if (mp2.find(s[1]) == mp2.end()) mp2[s[1]] = vector<int>(26, 0);
			++mp1[s[0]][s[1]-'a'];
			++mp2[s[1]][s[0]-'a'];
		}

		answers.push_back(ans);
	}
	for (auto a : answers) cout << a << '\n';
}
