#define _CRT_SECURE_NO_WARNINGS
#include "masina.h"
#include "service.h"

#include <iostream>
#include <string.h>
#include <assert.h>

Service creeareService()
{
	/*
	* Creaza service-ul
	* returneaza service-ul
	*/
	Service serv;
	serv.all_m = creeazaLista();
	return serv;
}

void distrugeService(Service* serv)
{
	distruge(&serv->all_m);
}

int s_add(Service* serv, Masina m)
{
	/*
	* Adauga o masina in lista
	* m - tip Masina
	* return: 1 daca masina s-a adaugat in lista, 0 in caz contrar
	*/
	return r_add(&serv->repo_list, m);
}

int s_delete(Service* serv, char nr_inmatriculare[8])
{
	/*
	* Sterge un parametru de tip Masina din lista de vectori
	* nr_inmatriculare - numarul de inmatriculare al masinii (string)
	* return: returneaza 1 daca parametrul m s-a sters cu succes din lista, 0 in caz contrar
	*/
	return r_delete(&serv->repo_list, nr_inmatriculare);
}

int s_update_model(Service* serv, char nr_inmatriculare[8], char model[20])
{
	/*
	* Actualizeaza modelul parametrului masina
	* nr_inmatriculare - numarul de inmatriculare al masinii (string)
	* model - string
	* return: 1 daca actualizarea s-a putut realiza, 0 in caz contrar
	*/
	return r_update_model(&serv->repo_list, nr_inmatriculare, model);
}

int s_update_categorie(Service* serv, char nr_inmatriculare[8], char categorie[10])
{
	/*
	* Actualizeaza categoria parametrului masina
	* nr_inmatriculare - numarul de inmatriculare al masinii (string)
	* categorie - string
	* return: 1 daca actualizarea s-a putut realiza, 0 in caz contrar
	*/
	return r_update_categorie(&serv->repo_list, nr_inmatriculare, categorie);
}


//teste
void test_s_add()
{
	/*Test pentru functa de adaugare*/
	Service serv = creareService();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);

	assert(s_add(&serv, m) == 1);
}

void test_s_delete()
{
	/*Test pentru functia de stergere*/
	Service serv = creareService();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);

	assert(get_dimensiune(get_repo(serv)) == 0);
	assert(s_delete(&serv, nr_inmatriculare) == 0);
	assert(get_dimensiune(get_repo(serv)) == 0);

	assert(s_add(&serv, m) == 1);
	assert(get_dimensiune(get_repo(serv)) == 1);

	assert(s_delete(&serv, nr_inmatriculare) == 1);
	assert(get_dimensiune(get_repo(serv)) == 0);
}

void test_s_update_model()
{
	/*Test pentru functia s_update_model*/
	Service serv = creareService();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);

	assert(s_add(&serv, m) == 1);

	strcpy_s(model, "BMW Seria 1");
	assert(s_update_model(&serv, nr_inmatriculare, model) == 1);
	assert(strcmp(get_model(&serv.repo_list.m[1]), model) == 0);
}

void test_s_update_categorie()
{
	/*Test pentru functia s_update_categorie*/
	Service serv = creareService();
	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);

	assert(s_add(&serv, m) == 1);

	strcpy_s(categorie, "suv");
	assert(s_update_categorie(&serv, nr_inmatriculare, categorie) == 1);
	assert(strcmp(get_categorie(&serv.repo_list.m[1]), categorie) == 0);
}