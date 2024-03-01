#include "IteratorMDO.h"
#include "MDO.h"

#include <iostream>
#include <vector>
#include <exception>

#define NIL -1

using namespace std;

int hashCode(TCheie e)
{
	//pt moment numarul este intreg
	return abs(e);
}

int MDO::d(TCheie e, int i) const
{
	return (hashCode(e) % m + i * (1 + hashCode(e) % mm)) % m;
}

Nod::Nod(TCheie cc, TValoare vv) :c(cc)
{
	if (cc != -1)
		elem.push_back(vv);
}

MDO::MDO(Relatie r) :m(517), mm(516), rel(r) {
	/* de adaugat */
	for (int i = 0; i < m; i++)
	{
		Nod* n = new Nod(-1, 0);
		td.push_back(n);
	}
}


void MDO::adauga(TCheie c, TValoare v) {
	/* de adaugat */

	int i = 0; //numarul de verificare
	bool gasit = false;

	do {
		int j = d(c, i);
		if (td[j]->c == NIL) {
			td[j]->c = c;
			td[c]->elem.push_back(v);
			gasit = true;
		}
		else if (td[j]->c == c)
		{
			td[c]->elem.push_back(v);
			gasit = true;
		}
		else {
			i++;
		}
	} while (i < m && !gasit);
}

vector<TValoare> MDO::cauta(TCheie c) const {
	/* de adaugat */

	int i = 0; //numarul de verificare
	do {
		int j = d(c, i);
		if (td[j]->c == c) {
			return td[j]->elem;

		}
		else i++;
	} while (i < m);
	return vector<TValoare>();
}

bool MDO::sterge(TCheie c, TValoare v) {
	/* de adaugat */

	vector<TValoare> valori = cauta(c);
	if (valori.size() > 1)
	{
		int i = 0; //numarul de verificare
		do {
			int j = d(c, i);
			if (td[j]->c == c) {

				auto it = find(td[j]->elem.begin(), td[j]->elem.end(), v);
				if (it != td[j]->elem.end())
					td[j]->elem.erase(it);
				else
					return false;
				break;

			}
			else i++;
		} while (i < m);
		return true;
	}
	else if (valori.size() == 1)
	{

		int pozitia_cheii = 0;
		bool gasit = false;
		int i = 0; //numarul de verificare
		do {
			int j = d(c, i);
			if (td[j]->c == c) {
				pozitia_cheii = j;
				auto it = find(td[j]->elem.begin(), td[j]->elem.end(), v);
				if (it == td[j]->elem.end())
					return false;
				else td[j]->elem.erase(it);

				gasit = true;
			}
			else i++;
		} while (i < m && !gasit);

		i = pozitia_cheii; //numarul de verificare
		int p = 0;
		int ok = 1;
		do {
			ok = 1;
			int j = d(c, i + 1);
			if (td[j]->c == NIL) {
				p = (td[j]->c) % m;
				if (i < j)
				{
					if (0 <= p && p <= i)
					{
						td[i]->c = td[j]->c;
						i = j;
						ok = 0;

					}
					else if (i < p && p <= j)
					{
						ok = 0;
					}
					else if (j < p && p <= m - 1)
					{

						td[i]->c = td[j]->c;
						i = j;
						ok = 0;
					}
				}
				else if (i > j)
				{
					if (0 <= p && p <= j)
					{
						ok = 0;

					}
					else if (j < p && p <= i)
					{

						td[i]->c = td[j]->c;
						i = j;
						ok = 0;
					}
					else if (i < p && p <= m - 1)
					{

						ok = 0;
					}
				}

			}
			else i++;
		} while (i < m && p != -1);
		delete td[pozitia_cheii];
		Nod* n = new Nod(-1, 0);
		td[pozitia_cheii] = n;
		return true;
	}
	return false;
}

int MDO::dim() const {
	/* de adaugat */

	int dim = 0;
	for (auto it : td)
	{
		dim += it->elem.size();
	}
	return dim;
}

bool MDO::vid() const {
	/* de adaugat */

	int dim = 0;
	for (auto it : td)
	{
		if (it->elem.size() != 0)
			return false;
	}
	return true;
}

IteratorMDO MDO::iterator() const {
	return IteratorMDO(*this);
}

MDO::~MDO() {
	/* de adaugat */

	for (int i = 0; i < td.size(); i++)
	{
		td[i]->~Nod();
	}
	td.~vector();
}

//Complexitate:
//CF: O(m)
//CM: O(m*val.size())
//CD: O(m*val.size())
vector<TValoare> MDO::stergeValoriPentruCheie(TCheie cheie)
{
	/*
	Subalgoritm stergeValoriPentruCheie(TCheie c)
		pre: TCheie c
		post: vectorul de valori sterse
		v <- cauta(cheie)
		pentru i <- 0, v.size() executa:
			sterge(c, v[i])
		stergeValoriPentruCheie <- v;
	*/
	vector<TValoare> val = cauta(cheie);
	for(int i=0; i<val.size(); i++)
		sterge(cheie, val[i]);
	return val;
}