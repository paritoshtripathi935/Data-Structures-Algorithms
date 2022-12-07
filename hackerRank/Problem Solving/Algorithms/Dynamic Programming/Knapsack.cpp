
int recursive(int k, vector<int>& arr){
    int res = 0;
    if (k == 0)
        return 0;
    for(int i = 0; i < arr.size(); i++){
        if (k >= arr[i])
            res = max(res, arr[i] + recursive(k - arr[i], arr));
    }
    return res;
}

int unboundedKnapsack(int k, vector<int>& arr) {
    vector<int> dp(k + 1, 0);
    for (int i: arr)
        for (int j = i; j <= k; j++)
            dp[j] = max(dp[j], i + dp[j - i]);
    return dp[k];
}

// Corrected input format

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));
    while(t--){
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        int n = stoi(first_multiple_input[0]);
        int k = stoi(first_multiple_input[1]);

        string arr_temp_temp;
        getline(cin, arr_temp_temp);
        vector<string> arr_temp = split(rtrim(arr_temp_temp));
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            int arr_item = stoi(arr_temp[i]);

            arr[i] = arr_item;
        }
        int result = unboundedKnapsack(k, arr);
        fout << result << "\n";
    }
    fout.close();
    return 0;
}
