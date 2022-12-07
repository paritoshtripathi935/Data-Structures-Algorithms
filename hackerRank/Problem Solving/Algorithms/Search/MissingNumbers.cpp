
vector<int> missingNumbers(vector<int>& arr, vector<int>& brr) {
    vector<int> res(200001, 0), ans;
    for(auto i: brr)
        res[i]++;
    for(auto i: arr)
        res[i]--;
    for(int i = 0; i < 200001; i++)
        if (res[i] > 0) ans.push_back(i);
    return ans;
}
