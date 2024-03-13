#define _CRT_SECURE_NO_WARNINGS
#include <string.h>
#include <assert.h>
#include <iostream>

using namespace std;

int validare_nr_inmatriculare(char nr_inmatriculare[8])
{
	/*
	* Functia verifica daca sirul dat ca parametru este un numar de inmatriculare valid
	* nr_inmatriculare - string
	* return: 1 daca sirul e valid si 0 in caz contrar
	*/
	if (nr_inmatriculare[0] != 'C' || nr_inmatriculare[1] != 'J')
		return 0;
	if ((nr_inmatriculare[2] < '0' || nr_inmatriculare[2] > '9') || (nr_inmatriculare[3] < '0' || nr_inmatriculare[3] > '9'))
		return 0;
	if ((nr_inmatriculare[4] < 'A' || nr_inmatriculare[4] > 'Z') || (nr_inmatriculare[5] < 'A' || nr_inmatriculare[5] > 'Z') || (nr_inmatriculare[6] < 'A' || nr_inmatriculare[6] > 'Z'))
		return 0;
	return 1;
}

int validare_categorie(char categorie[10])
{
	/*
	* Functia verifica daca sirul dat ca parametru este o categorie valida de masini
	* categorie - string
	* return: 1 daca sirul e valid si 0 in caz contrar
	*/
	int ok = 0;
	char categori[6][10];
	strcpy_s(categori[0], "mini");
	strcpy_s(categori[1], "mica");
	strcpy_s(categori[2], "compacta");
	strcpy_s(categori[3], "mare");
	strcpy_s(categori[4], "sport");
	strcpy_s(categori[5], "suv");
	for (int i = 0; i < strlen(categorie); i++)
		categorie[i] = tolower(categorie[i]);
	for (int i = 0; i < 6; i++)
	{
		if (strcmp(categorie, categori[i]) == 0)
			ok = 1;
	}
	if (ok)
		return 1;
	return 0;
}

//teste
void test_validare_nr_inmatriculare()
{
	/*Test pentru functia de validare_nr_inmatriculare*/
	char str[8];

	strcpy_s(str, "CJ23ACB");
	assert(validare_nr_inmatriculare(str) == 1);

	strcpy_s(str, "CL23ACB");
	assert(validare_nr_inmatriculare(str) == 0);

	strcpy_s(str, "CJ230CB");
	assert(validare_nr_inmatriculare(str) == 0);

	strcpy_s(str, "CJ23aCB");
	assert(validare_nr_inmatriculare(str) == 0);

	strcpy_s(str, "CJ2ZACB");
	assert(validare_nr_inmatriculare(str) == 0);
}

void test_validare_categorie()
{
	/*Test pentru functia de validare_categorie*/
	char str[10];

	strcpy_s(str, "cOmPacTA");
	assert(validare_categorie(str) == 1);

	strcpy_s(str, "SuV");
	assert(validare_categorie(str) == 1);

	strcpy_s(str, "Audi");
	assert(validare_categorie(str) == 0);
}