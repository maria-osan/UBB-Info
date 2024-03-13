#include "lista.h"

#include <string.h>
#include <assert.h>
#include <stdlib.h>

Lista_masini creeazaLista()
{
	/*Creeaza o lista goala*/
	Lista_masini list;
	list.dim = 0;
	list.capacitate = 100;
	list.elem = (Masina*)malloc(sizeof(Masina) * list.capacitate);
	return list;
}

void distruge(Lista_masini* l)
{
	/*Distruge lista*/
	//dealocare masini
	for (int i = 0; i < l->dim; i++)
		distrugeMasina(&l->elem[i]);
	free(l->elem);
	l->elem = NULL;
	l->dim = 0;
}

Masina get_masina(Lista_masini* l, int poz)
{
	/*
	* Getter pentru un element din lista
	* poz - int (pozitia elementului)
	* returneaza elementul de pe pozitia data
	*/
	return l->elem[poz];
}

int get_dimensiune(Lista_masini* l)
{
	/*
	* returneaza dimensiunea listei (numarul de elemente din lista)
	*/
	return l->dim;
}

int get_capacitate(Lista_masini* l)
{
	/*
	* returneaza capacitatea listei
	*/
	return l->capacitate;
}

void verificare_capacitate(Lista_masini* l)
{
	/*Se aloca mai multa memorie daca este necesar*/
	if (l->dim < l->capacitate)
		return; //mai este loc
	
	//alocare memorie
	int capacitateNoua = l->capacitate + 100;
	Masina* mNoi = (Masina*)malloc(sizeof(Masina) * capacitateNoua);
	
	//copiere elemente
	for (int i = 0; i < l->dim; i++)
		mNoi[i] = l->elem[i];
	
	//dealocarea vectorului vechi
	free(l->elem);

	l->elem = mNoi;
	l->capacitate = capacitateNoua;
}

void add(Lista_masini* l, Masina m)
{
	/*
	* Se adauga un element nou in lista
	* Elementul este adaugat la finalul listei
	*/
	verificare_capacitate(l);
	l->elem[l->dim] = m;
	l->dim++;
}

int search(Lista_masini* l, Masina masina)
{
	/*
	* Cauta o masina in lista
	* returneaza pozitia, daca masina se afla in lista si -1 in caz contrar
	*/
	Masina m;
	for (int i = 0; i < get_dimensiune(l); i++)
	{
		m = get_masina(l, i);
		if (strcmp(get_nr_inmatriculare(m), get_nr_inmatriculare(masina)) == 0)
			return i;
	}
	return -1;
}

void delete_masina(Lista_masini* l, Masina m)
{
	/*
	* Se sterge un element din lista
	*/
	int poz = search(l, m);
	if (poz != -1)
	{
		for (int i = poz; i < get_dimensiune(l) - 1; i++)
			l->elem[i] = l->elem[i + 1];
		l->dim--;
	}
}

Lista_masini copiere_lista(Lista_masini* l)
{
	/*
	* Se face o copie a listei
	* returneaza copia (care contine aceleasi elemente ca si lista l)
	*/
	Lista_masini cop = creeazaLista();
	for (int i = 0; i < get_dimensiune(l); i++)
	{
		Masina m = get_masina(l, i);
		add(&cop, copieMasina(&m));
	}
	return cop;
}


//Teste
void test_creeazaLista()
{
	/*Test pentru crearea unei liste*/
	Lista_masini l = creeazaLista();
	assert(get_dimensiune(&l) == 0);
	assert(get_capacitate(&l) == 100);
	distruge(&l);
}

void test_add()
{
	/*Test pentru functia de adaugare*/
	Lista_masini l = creeazaLista();

	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);

	add(&l, m);
	assert(get_dimensiune(&l) == 1);
	Masina m2 = get_masina(&l, 0);

	assert(strcmp(m2.nr_inmatriculare, nr_inmatriculare) == 0);
	assert(strcmp(m2.model, model) == 0);
	assert(strcmp(m2.categorie, categorie) == 0);

	distruge(&l);
	assert(get_dimensiune(&l) == 0);
}

void test_copiere_lista()
{
	/*Test pentru functia de copiere*/
	Lista_masini l = creeazaLista();

	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);
	add(&l, m);

	Lista_masini l2 = copiere_lista(&l);
	assert(get_dimensiune(&l2) == 1);
	Masina	m2 = get_masina(&l2, 0);

	assert(strcmp(m2.nr_inmatriculare, nr_inmatriculare) == 0);
	assert(strcmp(m2.model, model) == 0);
	assert(strcmp(m2.categorie, categorie) == 0);

	distruge(&l);
	distruge(&l2);
}

/*void test_realocare()
{
	//Test pentru functia verificare_capacitate
	Lista_masini l = creeazaLista();

	char nr_inmatriculare[8], model[20], categorie[10];
	strcpy_s(nr_inmatriculare, "CJ37MTO");
	strcpy_s(model, "Volkswagen golf 5");
	strcpy_s(categorie, "compacta");
	Masina m = creeazaMasina(nr_inmatriculare, model, categorie);

	for (int i = 0; i < 150; i++)
		add(&l, m);
	assert(get_dimensiune(&l) == 150);
	distruge(&l);
	assert(get_dimensiune(&l) == 0);
	assert(l.elem == NULL);
}*/