#include "CP.h"

#include <exception>
#include <stdio.h>

using namespace std;


//constructor
//Complexitate: T(1)
Nod::Nod(Element e, PNod urm) {
	this->e = e;
	this->urm = urm;
}

//Complexitate: T(1)
Element Nod::element() {
	return e;
}

//Complexitate: T(1)
PNod Nod::urmator() {
	return urm;
}


//constructorul implicit
//complexitate: T(1)
CP::CP(Relatie r) {
	this->prim = nullptr;
	this->r = r;
}

//complexitate: O(n)
//adauga un element in CP
void CP::adauga(TElem e, TPrioritate p) {
	//creez un nod nou cu TElem e si TPrioritate p
	Element el;
	el.first = e;
	el.second = p;
	PNod nod = new Nod(el, nullptr);
	nod->e.first = e;
	nod->e.second = p;

	if (this->prim == nullptr || r(p, this->prim->e.second))
	{
		nod->urm = this->prim;
		this->prim = nod;
	}
	else
	{
		PNod temp = this->prim;
		while (temp->urm != nullptr && r(temp->urm->e.second, p))
			temp = temp->urm;
		nod->urm = temp->urm;
		temp->urm = nod;
	}
}

//acceseaza elementul cel mai prioritar in raport cu relatia de ordine
//arunca exceptie daca coada e vida
Element CP::element() const {
	if (this->prim == nullptr)
	{
		throw exception();
		return pair <TElem, TPrioritate>(-1, -1);      // copy constructor
	}
	return this->prim->e;
}

//complexitate: O(1)
//sterge elementul cel mai prioritar si il returneaza
//arunca exceptie daca CP e vida
Element CP::sterge() {
	if (this->prim == nullptr)
	{
		throw exception();
		return pair <TElem, TPrioritate>(-1, -1);
	}
	else
	{
		PNod temp = this->prim; 
		Element temp_el = this->prim->e;

		this->prim = this->prim->urm;

		delete temp;
		return temp_el;
	}
}

//verifica daca CP e vida
bool CP::vida() const {
	if (this->prim == nullptr)
		return true;
	else 
		return false;
}

// destructorul cozii
CP::~CP() {
	PNod urm;
	while (this->prim != nullptr)
	{
		urm = this->prim->urm;
		delete this->prim;
		this->prim = urm;
	}
};