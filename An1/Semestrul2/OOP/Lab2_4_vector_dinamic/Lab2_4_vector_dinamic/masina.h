#pragma once

typedef struct
{
	char* nr_inmatriculare;
	char* model;
	char* categorie;
}Masina;

Masina creeazaMasina(char* nr_inmatriculare, char* model, char* categorie);

void distrugeMasina(Masina* m);

Masina copieMasina(Masina* m);

char* get_nr_inmatriculare(Masina m);
char* get_model(Masina m);
char* get_categorie(Masina m);

void set_nr_inmatriculare(Masina* m, const char* nr_inmatriculare);
void set_model(Masina* m, const char* model);
void set_categorie(Masina* m, const char* categorie);

//int compara_masini(Masina* m1, Masina* m2);


//Teste
void test_creeazaMasina();
void test_set();