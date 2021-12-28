#include <iostream>
using namespace std;


const int MAX_CHAR = 26;

bool checkString(string s) {
    
     int count[MAX_CHAR] = {0};

    // Length of the string
    int n = s.length();
    if (n == 1)
        return true;

    // traverse till the middle element
    // is reached
    for (int i=0,j=n-1; i<j; i++,j--)
    {
        // First half
        count[s[i]-'a']++;

        // Second half
        count[s[j]-'a']--;
    }

    // Checking if values are different
    // set flag to 1
    for (int i = 0; i<MAX_CHAR; i++)
        if (count[i] != 0)
            return false;

    return true;
}

int main() {
	// your code goes here
	    // String to be checked
    int n;
    
    cin >> n;
    
    string arr[n];
    
    for(int i=0; i<n; i++){
        std::cin >> arr[i];
    }
    
    for(int k=0; k<n; k++){
        
        if (checkString(arr[k]))
        cout << "YES"<<endl;
        else
        cout << "NO"<<endl;
    }
    return 0;
}
