#include < stdio.h >
#include < stdlib.h >
using namespace std;

int main() {
  int n, x, p, q, i, j, count;
  int *arr;
  scanf(" % d ", &n);
  arr = (int *)malloc(n * sizeof(int));
  for (i = 0; i < n; i++)
    scanf(" % d ", &arr[i]);
  scanf(" % d ", &x);
  while (x--) {
    scanf(" % d % d ", &p, &q);
    count = 0;
    for (i = p - 1; i < q; i++) {
      for (j = i + 1; j < q; j++) {
        if (arr[i] > arr[j])
          count++;
      }
    }
    printf(" % d  ", count);
  }
  return 0;
}