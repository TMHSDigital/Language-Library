#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int num1 = 5;
    int num2 = 10;
    int sum = add(num1, num2);
    printf("Sum of %d and %d is %d\n", num1, num2, sum);
    return 0;
}
