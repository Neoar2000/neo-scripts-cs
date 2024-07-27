import 'dart:io';

void main() {
  stdout.write("Ingrese el valor de a: ");
  int a = int.parse(stdin.readLineSync()!);

  stdout.write("Ingrese el valor de b: ");
  int b = int.parse(stdin.readLineSync()!);

  int suma = a + b;
  int resta = a - b;

  print("La suma de los valores es: $suma");
  print("La resta de los valores es: $resta");
}
