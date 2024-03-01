#include "IteratorMDO.h"
#include "MDO.h"

#define NIL -1

void IteratorMDO::deplasare()
{
	while ((curent < dict.m) && dict.td[curent]->c == NIL)
		curent++;
}

IteratorMDO::IteratorMDO(const MDO& d) : dict(d) {
	/* de adaugat */

	curent = 0;
	deplasare();
}

void IteratorMDO::prim() {
	/* de adaugat */

	curent = 0;

	deplasare();
	for (int i = curent; i < dict.td.size(); i++)
	{
		if (dict.td[i]->c != NIL && dict.rel(dict.td[i]->c, dict.td[curent]->c))
			curent = i;

	}
}

void IteratorMDO::urmator() {
	/* de adaugat */

	if (!valid())
	{
		throw std::exception("Iterator invalid");
	}
	int max = dict.td[curent]->c;
	int maxpoz = -1;
	for (int i = 0; i < dict.td.size(); i++)
	{
		if (i >= 0 && i != curent && dict.td[i]->c != NIL && dict.rel(dict.td[curent]->c, dict.td[i]->c))
		{
			max = dict.td[i]->c;
			maxpoz = i;
		}
	}
	if (maxpoz != -1)
		curent = maxpoz;
	else curent = dict.td.size();
}

bool IteratorMDO::valid() const {
	/* de adaugat */

	return !(curent == dict.m) && (curent >= 0);
}

TElem IteratorMDO::element() const {
	/* de adaugat */

	if (!valid())
	{
		throw std::exception("Iterator invalid");
	}
	int ok = 0;
	static pair <TCheie, TValoare> p(-1, -1);
	int elcurent = curent;

	for (auto it2 : dict.td[dict.td[elcurent]->c]->elem) {
		if (ok == 1)
			return p;
		if (p.first != dict.td[dict.td[elcurent]->c]->c)
		{
			p = pair <TCheie, TValoare>(dict.td[elcurent]->c, it2);
			return p;

		}
		else if (p.first == dict.td[dict.td[elcurent]->c]->c && p.second == it2)
		{
			ok = 1;
		}

	}
	return p;
}