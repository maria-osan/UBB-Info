// Lab2_pb2.cpp : This file contains the 'main' function. Program execution begins and ends there.
// 2. Sa se determine închiderea transitivã a unui graf orientat. (Închiderea tranzitivã poate fi reprezentatã ca matricea care descrie, 
// pentru fiecare vârf în parte, care sunt vârfurile accesibile din acest vârf. Matricea inchiderii tranzitive aratã unde se poate ajunge din 
// fiecare vârf.) ex. figura inchidere_tranzitiva.png - pentru graful de sus se construieste matricea de jos care arata inchiderea tranzitiva.

#include <iostream>
#include <fstream>

std::ifstream f("graf.txt");

void citire(int adiac[][31], int &n)
{
	int x, y;
	f >> n;
	while (f >> x >> y)
		adiac[x][y] = 1;
	f.close();
}

void afisareMatrice(int matrice[][31], int n)
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			std::cout<<matrice[i][j]<<" ";
		std::cout<<"\n";
	}
}

void initializare(int matr_tranz[][31], int adiac[][31], int n)
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			matr_tranz[i][j] = adiac[i][j];
		matr_tranz[i][i] = 1;
	}
}

void inchidere(int matr_tranz[][31], int adiac[][31], int n)
{
	int i, j, k;
	initializare(matr_tranz, adiac, n);
	for (k = 1; k <= n; k++)
		for (i = 1; i <= n; i++)
			for (j = 1; j <= n; j++)
				if (matr_tranz[i][j] == 0)
					matr_tranz[i][j] = matr_tranz[i][k] * matr_tranz[k][j];
}

int main()
{
	int n, adiac[31][31] = { 0 }, matr_tranz[31][31] = { 0 };
	citire(adiac, n);
	//std::cout << "Matricea de adiacenta:\n";
	//afisareMatrice(adiac, n);

	inchidere(matr_tranz, adiac, n);
	std::cout << "Inchiderea tranzitiva a grafului:\n";
	afisareMatrice(matr_tranz, n);
	return 0;
}
