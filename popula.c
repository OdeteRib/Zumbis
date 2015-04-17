// Supondo que a população de um país A seja da ordem de 90.000 habitantes com uma
// taxa anual de crescimento de 3% e que a população de um país B seja, aproximadamente,
// de 200.000 habitantes com uma taxa anual de crescimento de 1,5%, fazer um programa
// que calcule e escreva o número de anos necessários para que a população do país A
// ultrapasse ou se iguale à população do país B, mantidas essas taxas de crescimento.

#include <stdio.h>

void main() {
  float popA, popB,taxaA,taxaB;
  int anos = 0;
  
  printf ("Digite o valor da população de A: ");
  scanf ("%d", &popA);
  printf ("Digite o valor da taxa de cresimento da população de A: ");
  scanf ("%d", &taxaA);
  
  printf ("Digite o valor da população de B: ");
  scanf ("%d", &popB);
  printf ("Digite o valor da taxa de cresimento da população de B: ");
  scanf ("%d", &taxaB);
  
  
  
  while (popA < popB) {
    popA = popA * taxaA;
    popB = popB * taxaB;
    anos = anos + 1;
  }
 
  printf("Populacao Pais A- %7.0f habitantes.\n", popA);
  printf("Populacao Pais B- %7.0f habitantes.\n", popB);
  printf("\n");
  printf("Pais A ultrapassa Pais B em %d anos.", anos);
}
