#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    
    cin >> n;
    int input;
    
    vector<int> arr;
    
    while(cin >> input)
        arr.push_back(input);
    
    for (auto ir = arr.crbegin(); ir != arr.crend(); ++ir)
        cout << *ir << " ";
}
