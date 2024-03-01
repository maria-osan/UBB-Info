#include "Dictionar.h"
#include "IteratorDictionar.h"

#include <iostream>

typedef std::pair<TCheie, TValoare> TElem;

void Dictionar::redim() {
	//alocam un spatiu de capacitate dubla
	TElem* eNou = new TElem[2 * cp];

	//copiem vechile valori in noua zona
	for (int i = 0; i < n; i++)
		eNou[i] = e[i];

	//dublam capacitatea
	cp = 2 * cp;

	//eliberam vechea zona
	delete[] e;

	//vectorul indica spre noua zona
	e = eNou;
}

Dictionar::Dictionar() {
	this->e = new TElem[this->cp];
	this->n = 0;
}

Dictionar::~Dictionar() {
	delete[] e;
}

TValoare Dictionar::adauga(TCheie c, TValoare v) {
	//daca s-a atins capacitatea maxima, redimensionam
	if (this->n == this->cp)
		redim();

	//verificam daca cheia exista deja in dictionar
	for (int i = 0; i < this->n; i++)
		if (c == this->e[i].first)
		{
			TValoare old = this->e[i].second;
			this->e[i].second = v;
			return old;
		}
	TElem d;
	d.first = c;
	d.second = v;
	this->e[this->n++] = d;
	return NULL_TVALOARE;
}


//cauta o cheie si returneaza valoarea asociata (daca dictionarul contine cheia) sau null
TValoare Dictionar::cauta(TCheie c) const {
	for (int i = 0; i < this->n; i++)
		if (c == this->e[i].first)
			return this->e[i].second;
	return NULL_TVALOARE;
}


TValoare Dictionar::sterge(TCheie c) {
	int poz = NULL_TVALOARE;
	for (int i = 0; i < this->n; i++)
		if (c == this->e[i].first)
			poz = i;
	if (poz == NULL_TVALOARE)
		return NULL_TVALOARE;
	else
	{
		TValoare val_sters = this->e[poz].second;
		for (int i = poz; i < this->n - 1; i++)
			this->e[i] = this->e[i + 1];
		n--;
		return val_sters;
	}
}

int Dictionar::actualizeazaValori(Dictionar& m) {
	int k = 0;
	for(int i=0;i<this->n;i++)
		if (m.e->first == this->e[i].first)
		{
			this->e[i].second = m.e->second;
			k++;
		}
	return k;
}

int Dictionar::dim() const {
	return this->n;
}

bool Dictionar::vid() const {
	if (dim() == 0)
		return true;
	return false;
}


IteratorDictionar Dictionar::iterator() const {
	return  IteratorDictionar(*this); //returnam un iterator pe vector
}