#define _CRT_SECURE_NO_WARNINGS
#include "masina.h"

#include <string.h>
#include <assert.h>
#include <stdlib.h>

Masina creeazaMasina(char* nr_inmatriculare, char* model, char* categorie)
{
	/*
	* Creeaza o noua masina.
	* nr_inmatriculare - string (numarul de inmatriculare al masinii)
	* model - string (modelul masinii)
	* categorie - string (categoria din care face parte masina)
	* Se returneaza tipul Masina.
	*/
	Masina m;

	size_t nrC = strlen(nr_inmatriculare) + 1;
	m.nr_inmatriculare = (char*)malloc(sizeof(char) * nrC);
	strcpy_s(m.nr_inmatriculare, nrC, nr_inmatriculare);

	nrC = strlen(model) + 1;
	m.model = (char*)malloc(sizeof(char) * nrC);
	strcpy_s(m.model, nrC, model);

	nrC = strlen(categorie) + 1;
	m.categorie = (char*)malloc(sizeof(char) * nrC);
	strcpy_s(m.categorie, nrC, categorie);

	return m;
}

void distrugeMasina(Masina* m)
{
	/*Dealoca memoria ocupata de masina*/
	free(m->nr_inmatriculare);
	free(m->model);
	free(m->categorie);
	m->nr_inmatriculare = NULL;
	m->model = NULL;
	m->categorie = NULL;
}

Masina copieMasina(Masina* m)
{
	/*
	* Se creeaza o copie a masinii (deep copy)
	*/
	return creeazaMasina(m->nr_inmatriculare, m->model, m->categorie);
}

//Getters
char* get_nr_inmatriculare(Masina m)
{
	/*
	* Getter pentru numarul de inmatriculare al masinii
	* m - tip Masina
	* returneaza numarul de inmatriculare al masinii
	*/
	return m.nr_inmatriculare;
}

char* get_model(Masina m)
{
	/*
	* Getter pentru modelul masinii
	* m - tip Masina
	* returneaza modelul masinii
	*/
	return m.model;
}

char* get_categorie(Masina m)
{
	/*
	* Getter pentru categoria masinii
	* m - tip Masina
	* returneaza categoria masinii
	*/
	return m.categorie;
}


//Setters
void set_nr_inmatriculare(Masina* m, const char* nr_inmatriculare)
{
	/*
	* Setter pentru numarul de inmatriculare al masinii
	* m - tip Masina
	* nr_inmatriculare - string (noul numar de inmatriculare al masinii)
	* returneaza numarul de inmatriculare al masinii
	*/
	free(m->nr_inmatriculare);
	m->nr_inmatriculare = (char*)malloc(sizeof(char) * (strlen(nr_inmatriculare) + 1));
	strcpy_s(m->nr_inmatriculare, strlen(nr_inmatriculare) + 1, nr_inmatriculare);
}

void set_model(Masina* m, const char* model)
{
	/*
	* Setter pentru modelul masinii
	* m - tip Masina
	* model - string (noul model al masinii)
	* returneaza modelul masinii
	*/
	free(m->model);
	m->model = (char*)malloc(sizeof(char) * (strlen(model) + 1));
	strcpy_s(m->model, strlen(model) + 1, model);
}

void set_categorie(Masina* m, const char* categorie)
{
	/*
	* Setter pentru categoria masinii
	* m - tip Masina
	* categorie - string (noua categorie a masinii)
	* returneaza categoria masinii
	*/
	free(m->categorie);
	m->categorie = (char*)malloc(sizeof(char) * (strlen(categorie) + 1));
	strcpy_s(m->categorie, strlen(categorie) + 1, categorie);
}

/*int compara_masini(Masina* m1, Masina* m2)
{
	* Functia compara 2 parametrii de tip Masina
	* Comparatia se face dupa numarul de inmatriculare al masinilor
	* m1 - primul parametru de tip Masina
	* m2 - al doilea parametru de tip Masina
	* return: 1 (masini distincte), 0 (masini identice)
	if (strcmp(get_nr_inmatriculare(m1), get_nr_inmatriculare(m2)) == 0)
		return 1;
	return 0;
}*/

//Teste
void test_creeazaMasina()
{
	/*Test pentru functia creazaMasina si pentru getters*/
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);

	assert(strcmp(get_nr_inmatriculare(m), nr_inmatriculare) == 0);
	assert(strcmp(get_model(m), model) == 0);
	assert(strcmp(get_categorie(m), categorie) == 0);

	distrugeMasina(&m);
	assert(m.nr_inmatriculare == NULL);
	assert(m.model == NULL);
	assert(m.categorie == NULL);
}

void test_set()
{
	//Test pentru setters
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);

	strcpy_s(nr_inmatriculare, "CJ73TOM");
	set_nr_inmatriculare(&m, nr_inmatriculare);
	assert(strcmp(get_nr_inmatriculare(m), nr_inmatriculare) == 0);

	strcpy_s(model, "SEAT Ibiza");
	set_model(&m, model);
	assert(strcmp(get_model(m), model) == 0);

	strcpy_s(categorie, "mica");
	set_categorie(&m, categorie);
	assert(strcmp(get_categorie(m), categorie) == 0);

	distrugeMasina(&m);
}