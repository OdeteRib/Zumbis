#include <stdio.h>

int main() {
  int i, n;

  printf("Digite o valor de n: ");
  scanf("%d",&n);

  i = 1;
  while ((i*(i+1)*(i+2)) < n)
    i = i + 1;

  if (i*(i+1)*(i+2) == n)
    printf("%d e' o produto %d*%d*%d\n", n, i, i+1, i+2);
  else
    printf("%d nao e' triangular\n", n);

  return 0;
}
