#pragma once

#include "repository.h"

typedef struct
{
	Lista_masini all_m;
}Service;

Service creeareService();

void distrugeService(Service* serv);

int s_add(Service* serv, Masina m);

int s_delete(Service* serv, char nr_inmatriculare[8]);

int s_update_model(Service* serv, char nr_inmatriculare[8], char model[20]);

int s_update_categorie(Service* serv, char nr_inmatriculare[8], char categorie[10]);


//Teste
void test_s_add();
void test_s_delete();
void test_s_update_model();
void test_s_update_categorie();