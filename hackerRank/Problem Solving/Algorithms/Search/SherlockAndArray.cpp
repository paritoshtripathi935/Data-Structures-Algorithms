string balancedSums(vector<int>& arr) {
    vector<int> left, right(arr.size(), 0);
    left.push_back(arr[0]), right[arr.size() - 1] = arr[arr.size() - 1];
    for(int i = 1; i < arr.size(); i++)
        left.push_back(left[i - 1] + arr[i]);
    for(int j = arr.size() - 2; j >= 0; j--)
        right[j] = right[j + 1] + arr[j];

    for(int i = 0; i < arr.size(); i++){
        if ((i == 0 && right[i + 1] == 0) ||
        (i == arr.size() - 1 && left[i - 1] == 0))
            return "YES";
        if (left[i - 1] == right[i + 1])
            return "YES";
    }

    return "NO";
}
