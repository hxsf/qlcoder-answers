#include <cstdio>
#include <cstring>
#include <map>
using namespace std;

long long twist(long long u, long long v) {
	return (((u & 0x80000000L) | (v & 0x7fffffffL)) >> 1) ^ ((v & 1) == 1 ? 0x9908b0dfL : 0);
}
long long state[624];
int left = 1;

void next_state() {
	int p = 0;
	left = 624;
	for (int j = 228; --j > 0; p++)
		state[p] = state[p + 397] ^ twist(state[p], state[p + 1]);

	for (int j = 397; --j > 0; p++)
		state[p] = state[p - 227] ^ twist(state[p], state[p + 1]);

	state[p] = state[p - 227] ^ twist(state[p], state[0]);
}

long long next() {
	if (--left == 0)
		next_state();
	return state[624 - left];
}

int main() {
	for (int j = 1; j < 624; j++) {
		state[j] = (1812433253L * (state[j - 1] ^ (state[j - 1] >> 30)) + j);
		state[j] &= 0xffffffffL;
	}

	map<long long, unsigned char> map1;

	for (long long i = 0; i < 5000000000L; i++) {
		long long t = next();
		map1[t]++;
		// printf("%lld\n", next());
	}
	long long max = 0;
	unsigned char max_value = 0;
	for (map<long long, unsigned char>::iterator it = map1.begin(); it != map1.end(); ++it) {
		if (it->second > max_value) {
			max = it->first;
			max_value = it->second;
		}
	}
	printf("max is %lld\n, count = %d", max, max_value);
	return 0;
}
