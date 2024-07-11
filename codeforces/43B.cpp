#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
	string s1, s2;
	getline(cin, s1);
	getline(cin, s2);

	map<char, int> cnt1, cnt2;
	for (auto ch : s1) {
		if (ch == ' ') continue;
		if (cnt1.find(ch) == cnt1.end()) cnt1[ch] = 0;
		++cnt1[ch];
	}
	for (auto ch : s2) {
		if (ch == ' ') continue;
		if (cnt2.find(ch) == cnt2.end()) cnt2[ch] = 0;
		++cnt2[ch];
	}
	bool flag = true;
	for (auto ch : cnt2) {
		if (cnt1.find(ch.first) == cnt1.end() || cnt1[ch.first] < cnt2[ch.first]) flag = false;
	}
	if (flag) cout << "YES\n";
	else cout << "NO\n";
}
