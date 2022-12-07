#include <iostream>
#include <vector>
using namespace std;

int main() {
  // list
  vector<int> vector1 = {1, 2, 3, 4, 5};
  vector<int> vector2{1, 2, 3, 4, 5};
  vector<int> vector3(5, 12);

  for (const int &i : vector1) {
    cout << i << " " << endl;
  }
  
}