// Lab2_pb1.cpp : This file contains the 'main' function. Program execution begins and ends there.
// 1. Implementați algoritmul lui Moore pentru un graf orientat neponderat (algoritm bazat pe Breath-first search, vezi cursul 2). 
// Datele sunt citete din fisierul graf.txt. Primul rând din graf.txt conține numărul vârfurilor, iar următoarele rânduri conțin muchiile grafului.
// Programul trebuie să afiseze lanțul cel mai scurt dintr-un vârf (vârful sursa poate fi citit de la tastatura).

#include <iostream>
#include <fstream>
#include<string>
#include<queue>

using namespace std;

std::ifstream f("graf.txt");

#define MAXIM 999999

typedef struct {
	int parinte, distanta;
}varf;

void init(int matrice[][31], int &n) {
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			matrice[i][j] = 0;
}

void citire(int adiac[][31], int &n) {
	int extr1, extr2;
	f >> n;
	init(adiac, n);
	while (f >> extr1 >> extr2) 
	{
		adiac[extr1][extr2] = 1;
	}
	f.close();
}

void afisare_matrice(int adiac[][31], int n)
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
			std::cout << adiac[i][j] << " ";
		cout << "\n";
	}
}

void Moore(int adiac[][31], int n, varf varfuri[], int start) {
	varf vf;
	int i, u, v;
	queue<int> q;
	//initializare lista de varfuri
	for (i = 1; i <= n; i++) {
		vf.distanta = MAXIM;
		vf.parinte = -1;
		varfuri[i] = vf;
	}

	varfuri[start].distanta = 0;
	
	q.push(start);
	while (!q.empty()) 
	{
		u = q.front(); //luam primul element din coada
		q.pop();
		for (v = 1; v <= n; v++)
			if (adiac[u][v] == 1) //verificam daca este muchie
				if (varfuri[v].distanta == MAXIM) 
				{
					varfuri[v].distanta = varfuri[u].distanta + 1;
					varfuri[v].parinte = u;
					q.push(v);
				}
	}
}

void afisare(varf varfuri[], int n) 
{
	int i, p, d;
	for (i = 1; i <= n; i++) {
		if (varfuri[i].parinte != -1) {
			p = i;
			d = varfuri[i].distanta;
			while (d >= 0) {
				cout << p << " ";
				p = varfuri[p].parinte;
				d--;
			}
			cout << endl;
		}
	}
}

int main()
{
	int adiac[31][31], n, start;
	varf varfuri[31];

	std::cout << "Dati varful de start: ";
	std::cin >> start;

	citire(adiac, n);
	//afisare_matrice(adiac, n);
	Moore(adiac, n, varfuri, start);
	afisare(varfuri, n);

	return 0;
}

