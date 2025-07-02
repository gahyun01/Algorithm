#include <stdio.h>

int main() {
  int A, C;
  int B[3];
  scanf("%d", &A);
  scanf("%d", &C);

  for (int i = 0; i < 3; i++) {
    B[i] = C % 10;
    C = C / 10;
  }

  printf("%d\n", A * B[0]);
  printf("%d\n", A * B[1]);
  printf("%d\n", A * B[2]);
  printf("%d\n", A * B[0] + A * B[1] * 10 + A * B[2] * 100);

  return 0;
}