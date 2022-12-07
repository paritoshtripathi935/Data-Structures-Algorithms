#include <bits/stdc++.h>
using namespace std;


int hackerlandRadioTransmitters(vector<int>& x, int k) {
    sort(x.begin(), x.end());
    int res = 0, i = 0;
    while (i < x.size()){
        res++;
        int range = x[i] + k;
        while (i < x.size() && x[i] <= range) i++;
        range = x[--i] + k;
        while (i < x.size() && x[i] <= range) i++;
    }
    return res;
}


int main(){
    vector<int>arr{1, 2, 3, 4, 5};
    cout << hackerlandRadioTransmitters(arr, 1);
    return 0;
}
