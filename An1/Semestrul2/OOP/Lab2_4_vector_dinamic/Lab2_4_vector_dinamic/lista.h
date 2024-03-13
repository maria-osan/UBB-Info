#pragma once
#include "masina.h"

typedef struct 
{
	Masina* elem;
	int dim; //dimensiunea
	int capacitate; //capacitatea
}Lista_masini;

Lista_masini creeazaLista();

void distruge(Lista_masini* l);

Masina get_masina(Lista_masini* l, int poz);

int get_dimensiune(Lista_masini* l);
int get_capacitate(Lista_masini* l);

void add(Lista_masini* l, Masina m);

int search(Lista_masini* l, Masina masina);

void delete_masina(Lista_masini* l, Masina m);

Lista_masini copiere_lista(Lista_masini* l);

///Teste
void test_creeazaLista();
void test_add();
void test_copiere_lista();
//void test_realocare();