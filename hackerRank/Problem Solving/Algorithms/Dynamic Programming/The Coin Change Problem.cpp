#include <bits/stdc++.h>
using namespace std;

long getWays(int n, vector<long>& c) {
    vector<long>dp(n + 1, 0);
    dp[0] = 1;
    for(auto i: c)
        for(int j = i; j <= n; j++)
            dp[j] += dp[j - i];
    return dp[n];
}
