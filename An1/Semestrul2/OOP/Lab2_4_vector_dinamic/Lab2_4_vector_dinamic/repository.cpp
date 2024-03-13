#define _CRE_SECURE_NO_WARNINGS
#include "masina.h"
#include "repository.h"

#include <iostream>
#include <string.h>
#include <assert.h>

Repo makeRepo()
{
	/*
	* Creaza o lista de participanti
	* returneaza repo
	*/
	Repo lista_m;
	lista_m.dim = 0;
	lista_m.capacitate = 100;

	return lista_m;
}

Masina get_masina(Repo lista_m, int poz)
{
	/*
	* lista_m - lista de masini
	* poz - pozitia in lista
	* returneaza masina de la pozitia poz din lista
	*/
	return lista_m.m[poz];
}

int incrementare_dimensiune(Repo* lista_m)
{
	/*
	* Incrementeaza dimensiunea listei
	* lista_m - lista de masini
	* returneaza dimensiunea (int)
	*/
	lista_m->dim++;
	return lista_m->dim;
}

int decrementare_dimensiune(Repo* lista_m)
{
	/*
	* Decrementeaza dimensiunea listei
	* lista_m - lista de masini
	* returneaza dimensiunea (int)
	*/
	lista_m->dim--;
	return lista_m->dim;
}

int get_dimensiune(Repo lista_m)
{
	/*
	* lista_m - lista de masini
	* returneaza dimensiunea listei
	*/
	return lista_m.dim;
}

int get_capacitate(Repo lista_m)
{
	/*
	* lista_m - lista de masini
	* returneaza capacitatea listei
	*/
	return lista_m.capacitate;
}

int r_add(Repo* lista_m, Masina masina)
{
	/*
	* Se adauga paramentrul masina in lista.
	* lista_m - lista de masini
	* masina -> tip Masina
	* return: returneaza 1 daca masina s-a adaugat in lista, 0 in caz contrar
	*/
	if (get_dimensiune(*lista_m) < get_capacitate(*lista_m) - 1)
	{
		incrementare_dimensiune(lista_m);
		lista_m->m[lista_m->dim] = masina;
		return 1;
	}
	return 0;

}
int r_search(Repo lista_m, char nr_inmatriculare[8])
{
	/*
	* Se cauta masina cu numarul de inmatriculare dat.
	* lista_m - lista de masini
	* nr_inmatriculare -> numarul de inmatriculare dat (string)
	* return: returneaza pozitia sa sau -1, in caz contrar (nu exista masina cu acel numar de inmatriculare in lista)
	*/
	for (int i = 1; i <= get_dimensiune(lista_m); i++)
		if (strcmp(get_nr_inmatriculare(&lista_m.m[i]), nr_inmatriculare) == 0)
			return i;
	return -1;
}

int r_delete(Repo* lista_m, char nr_inmatriculare[8])
{
	/*
	* Sterge un parametru de tip Masina din lista
	* lista_m - lista de masini
	* nr_inmatriculare -> numarul de inmatriculare dat (string)
	* return: returneaza 1 daca parametrul m s-a sters cu succes din lista, 0 in caz contrar
	*/
	//return delete_masina(&(*memory).v, m);
	int poz = r_search(*lista_m, nr_inmatriculare);
	if (poz != -1)
	{
		for (int i = poz; i < get_dimensiune(*lista_m); i++)
			lista_m->m[i] = lista_m->m[i + 1];
		decrementare_dimensiune(lista_m);
		return 1;
	}
	return 0;
}

int r_update_model(Repo* lista_m, char nr_inmatriculare[8], char model[20])
{
	/*
	* Actualizeaza modelul parametrului masina
	* lista_m - lista de masini
	* nr_inmatriculare -> numarul de inmatriculare dat (string)
	* model - modelul masinii (string)
	* return: 1 daca actualizarea s-a putut realiza, 0 in caz contrar
	*/
	int poz = r_search(*lista_m, nr_inmatriculare);
	if (poz != -1)
	{
		set_model(&lista_m->m[poz], model);
		return 1;
	}
	return 0;
}

int r_update_categorie(Repo* lista_m, char nr_inmatriculare[8], char categorie[10])
{
	/*
	* Actualizeaza categoria parametrului masina
	* lista_m - lista de masini
	* nr_inmatriculare -> numarul de inmatriculare dat (string)
	* categorie - categoria masinii (string)
	* return: 1 daca actualizarea s-a putut realiza, 0 in caz contrar
	*/
	int poz = r_search(*lista_m, nr_inmatriculare);
	if (poz != -1)
	{
		set_categorie(&lista_m->m[poz], categorie);
		return 1;
	}
	return 0;
}


//teste
void test_makeRepo()
{
	/*Test pentru functia makeRepo*/
	Repo l = makeRepo();
	assert(get_dimensiune(l) == 0);
	assert(get_capacitate(l) == 100);
	assert(incrementare_dimensiune(&l) == 1);
	assert(decrementare_dimensiune(&l) == 0);
}

void test_get_masina()
{
	/*Rest pentru functia get_masina*/
	Repo l = makeRepo();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m1 = creazaMasina(nr_inmatriculare, model, categorie);

	l.m[1] = m1;

	assert(strcmp(get_masina(l, 1).nr_inmatriculare, nr_inmatriculare) == 0);
	assert(strcmp(get_masina(l, 1).model, model) == 0);
	assert(strcmp(get_masina(l, 1).categorie, categorie) == 0);
}

void test_r_add()
{
	/*Test pentru functia r_add*/
	Repo l = makeRepo();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m1 = creazaMasina(nr_inmatriculare, model, categorie);

	assert(r_add(&l, m1) == 1);

	for (int i = 1; i <= get_dimensiune(l); i++)
		r_add(&l, m1);
	assert(r_add(&l, m1) == 0);
}

void test_r_search()
{
	/*Test pentru functia r_search*/
	Repo l = makeRepo();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m1 = creazaMasina(nr_inmatriculare, model, categorie);

	char nr_inmatriculare1[8];
	strcpy_s(nr_inmatriculare1, "CJ23ACB");
	strcpy_s(model, "Ford Focus");
	Masina m2 = creazaMasina(nr_inmatriculare1, model, categorie);

	r_add(&l, m1);
	r_add(&l, m2);

	assert(r_search(l, nr_inmatriculare) == 1);
	assert(r_search(l, nr_inmatriculare1) == 2);
	strcpy_s(nr_inmatriculare, "CJ23AAA");
	assert(r_search(l, nr_inmatriculare) == -1);
}

void test_r_delete()
{
	/*Test pentru functia r_delete*/
	Repo l = makeRepo();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m1 = creazaMasina(nr_inmatriculare, model, categorie);

	char nr_inmatriculare1[8];
	strcpy_s(nr_inmatriculare1, "CJ23ACB");
	strcpy_s(model, "Ford Focus");
	Masina m2 = creazaMasina(nr_inmatriculare1, model, categorie);

	assert(r_add(&l, m1) == 1);
	assert(get_dimensiune(l) == 1);

	assert(r_add(&l, m2) == 1);
	assert(get_dimensiune(l) == 2);

	assert(r_delete(&l, nr_inmatriculare) == 1);
	assert(get_dimensiune(l) == 1);

	assert(r_delete(&l, nr_inmatriculare1) == 1);
	assert(get_dimensiune(l) == 0);

	assert(r_delete(&l, nr_inmatriculare) == 0);
}

void test_r_update()
{
	/*Teste pentru functiile de actualizare (r_update_model, r_update_categorie)*/
	Repo l = makeRepo();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m1 = creazaMasina(nr_inmatriculare, model, categorie);

	char nr_inmatriculare1[8];
	strcpy_s(nr_inmatriculare1, "CJ23ACB");
	strcpy_s(model, "Ford Focus");
	Masina m2 = creazaMasina(nr_inmatriculare1, model, categorie);

	assert(r_add(&l, m1) == 1);

	strcpy_s(model, "SEAT Ibiza");
	r_update_model(&l, nr_inmatriculare, model);
	assert(strcmp(get_model(&l.m[1]), model) == 0);

	strcpy_s(categorie, "mica");
	r_update_categorie(&l, nr_inmatriculare, categorie);
	assert(strcmp(get_categorie(&l.m[1]), categorie) == 0);

	assert(r_update_model(&l, nr_inmatriculare1, model) == 0);
	assert(r_update_categorie(&l, nr_inmatriculare1, categorie) == 0);
}