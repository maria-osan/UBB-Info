#pragma once
#include "masina.h"
#include "lista.h"

typedef struct
{
	Lista_masini l;
}Repo;

Repo makeRepo();


int r_add(Repo r, Masina m);

int r_search(Repo r, char nr_inmatriculare[8]);

int r_delete(Repo r, Masina m);

int r_update_model(Repo r, char nr_inmatriculare[8], char model[20]);

int r_update_categorie(Repo r, char nr_inmatriculare[8], char categorie[10]);


//Teste
void test_makeRepo();
void test_r_add();
void test_r_search();
void test_r_delete();
void test_r_update();