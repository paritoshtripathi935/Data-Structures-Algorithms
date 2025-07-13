#include <array>
#include <iostream>
#include <vector>

// Explain how to implment two stacks in an array in such a way that neither
// stack overflows unless the total number of elements in both stacks together
// is equal to the size of the array.
int n = 5;
std::vector<int> arr(n);
int top1 = -1;
int top2 = n;

int push1(int x) {
  if (top1 + 1 == top2) {
    std::cout << "overflow" << std::endl;
    return 0;
  }
  top1 += 1;
  arr[top1] = x;
  return top1;
}

int push2(int x) {
  if (top1 + 1 == top2) {
    std::cout << "overflow" << std::endl;
    return 0;
  }
  top2 -= 1;
  arr[top2] = x;
  return top2;
}

int pop1(int top1) {
  if (top1 == -1) {
    std::cout << "underflow" << std::endl;
  }
  int x = arr[top1];
  top1 -= 1;
  return x;
}

int pop2(int top2) {
  if (top2 == n) {
    std::cout << "underflow" << std::endl;
  }
  int x = arr[top2];
  top2 += 1;
  return x;
}

int main() {
  push1(1);
  push2(2);
  // Print the vector
  std::cout << "arr = { ";
  for (const auto &elem : arr) {
    std::cout << elem << " ";
  }
  std::cout << "}" << std::endl;

  // print the tops
  std::cout << "s1_top = " << top1 << std::endl;
  std::cout << "s2_top = " << top2 << std::endl;

  push1(3);
  push2(4);

  // Print the vector
  std::cout << "arr = { ";
  for (const auto &elem : arr) {
    std::cout << elem << " ";
  }
  std::cout << "}" << std::endl;

  // print the tops
  std::cout << "s1_top = " << top1 << std::endl;
  std::cout << "s2_top = " << top2 << std::endl;

  push1(5);
  push2(6);

  std::cout << "arr = { ";
  for (const auto &elem : arr) {
    std::cout << elem << " ";
  }
  std::cout << "}" << std::endl;

  // print the tops
  std::cout << "s1_top = " << top1 << std::endl;
  std::cout << "s2_top = " << top2 << std::endl;

  return 0;
}