vector<int> icecreamParlor(int m, vector<int>& arr) {
    unordered_map<int, int> mp;
    for(int i = 0; i < arr.size(); i++){
        if (mp.find(m - arr[i]) != mp.end())
            return {mp[m - arr[i]], i + 1};
        mp[arr[i]] = i + 1;
    }
    return {};
}
