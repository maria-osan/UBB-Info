#include "IteratorDictionar.h"
#include "Dictionar.h"

using namespace std;

IteratorDictionar::IteratorDictionar(const Dictionar& d) : dict(d) {
	//seteaza iteratorul pe prima pozitie din vector
	curent = 0;
}


void IteratorDictionar::prim() {
	//seteaza iteratorul pe prima pozitie din vector
	curent = 0;
}


void IteratorDictionar::urmator() {
	curent++;
}


TElem IteratorDictionar::element() const {
	if (valid() == false)
		return pair <TCheie, TValoare>(-1, -1);
	return pair <TCheie, TValoare>(dict.e[curent].first, dict.e[curent].second);
}


bool IteratorDictionar::valid() const {
	//verifica daca iteratorul indica spre un element al vectorului
	if (curent < dict.dim())
		return true;
	return false;
}