#include "Matrice.h"

#include <exception>

using namespace std;

//Complexitate: Theta(this->capacitate)
Matrice::Matrice(int m, int n) {
	/* de adaugat */
	if (m <= 0 || n <= 0)
		throw exception();

	this->capacitate = 50000;
	this->nrElemente = 0;
	this->nrLin = m;
	this->nrCol = n;
	this->radacina = -1;
	this->primLiber = 0;
	this->lista = new Nod[this->capacitate];

	this->lista[primLiber].stanga = 1;
	this->lista[primLiber].dreapta = -1;
	this->lista[primLiber].parinte = -1;
	this->lista[primLiber].info = NULL_TRIPLE;

	for (int i = 1; i < this->capacitate - 1; i++)
	{
		this->lista[i].stanga = i + 1;
		this->lista[i].dreapta = -1;
		this->lista[i].parinte = -1;
		this->lista[i].info = NULL_TRIPLE;
	}

	this->lista[this->capacitate - 1].stanga = -1;
	this->lista[this->capacitate - 1].dreapta = -1;
	this->lista[this->capacitate - 1].parinte = -1;
	this->lista[this->capacitate - 1].info = NULL_TRIPLE;
}


//Complexitate: Theta(1)
int Matrice::nrLinii() const {
	/* de adaugat */
	return this->nrLin;
}

//Complexitate: Theta(1)
int Matrice::nrColoane() const {
	/* de adaugat */
	return this->nrCol;
}

//Complexitate:
//CF: Theta(1) - daca elementul cautat este fix radacina
//CD: Theta(this->nrElemente) - daca elementul cautat nu este in arbore
//CM: O(this->nrElemente)
TElem Matrice::element(int i, int j) const {
	/* de adaugat */

	if (i < 0 || i >= this->nrLin)
		throw exception();
	if (j < 0 || j >= this->nrCol)
		throw exception();

	int nodCurent = this->radacina;

	while (nodCurent != -1)
	{
		if (get<0>(this->lista[nodCurent].info) == i && get<1>(this->lista[nodCurent].info) == j)
			return get<2>(this->lista[nodCurent].info);

		if (get<0>(this->lista[nodCurent].info) == i && get<1>(this->lista[nodCurent].info) < j)
			nodCurent = this->lista[nodCurent].dreapta;

		else if (get<0>(this->lista[nodCurent].info) < i)
			nodCurent = this->lista[nodCurent].dreapta;

		else if (get<0>(this->lista[nodCurent].info) == i && get<1>(this->lista[nodCurent].info) > j)
			nodCurent = this->lista[nodCurent].stanga;

		else if (get<0>(this->lista[nodCurent].info) > i)
			nodCurent = this->lista[nodCurent].stanga;
	}

	return NULL_TELEMENT;
}


//Complexitate:
//CF: Theta(1)
//CD: Theta(this->nrElemente)
//CM: O(this->nrElemente)
TElem Matrice::modifica(int i, int j, TElem e) {
	/* de adaugat */

	if (i < 0 || i >= this->nrLin)
		throw exception();
	if (j < 0 || j >= this->nrCol)
		throw exception();

	Triplet triplet = Triplet(i, j, e);
	if (e != 0) //trebuie sa modificam valoarea sau sa inseram o noua valoare
	{
		int nodCurent = this->radacina;
		int nodPrecedent = 0;

		//Cazul in care trebuie sa modificam valoarea din triplet
		while (nodCurent != -1)
		{
			if (get<0>(this->lista[nodCurent].info) == i && get<1>(this->lista[nodCurent].info) == j)
			{
				TElem valVeche = get<2>(this->lista[nodCurent].info);
				this->lista[nodCurent].info = triplet;
				return valVeche;
			}

			if (get<0>(this->lista[nodCurent].info) == i && get<1>(this->lista[nodCurent].info) < j)
			{
				nodPrecedent = nodCurent;
				nodCurent = this->lista[nodCurent].dreapta;
			}
			else if (get<0>(this->lista[nodCurent].info) < i)
			{
				nodPrecedent = nodCurent;
				nodCurent = this->lista[nodCurent].dreapta;
			}
			else if (get<0>(this->lista[nodCurent].info) == i && get<1>(this->lista[nodCurent].info) > j)
			{
				nodPrecedent = nodCurent;
				nodCurent = this->lista[nodCurent].stanga;
			}
			else if (get<0>(this->lista[nodCurent].info) > i)
			{
				nodPrecedent = nodCurent;
				nodCurent = this->lista[nodCurent].stanga;
			}
		}

		//Cazul in care trebuie sa adaugam un nou element
		
		//Caz 1: Arborele binar este gol, deci primul nod adaugat devine radacina
		if (this->radacina == -1)
		{
			int poz = this->allocate();
			this->lista[poz].info = triplet;
			this->radacina = poz;
			this->nrElemente++;
			return 0;
		}

		//Caz 2: In acest caz am gasit nodul pentru care adaugam un nou "copil"
		int poz = this->allocate();
		
		if ((get<0>(this->lista[nodPrecedent].info) == i && get<1>(this->lista[nodPrecedent].info) < j) || get<0>(this->lista[nodPrecedent].info) < i)
		{
			//Adaugam noul nod in partea dreapta
			this->lista[nodPrecedent].dreapta = poz;
			this->lista[poz].info = triplet;
			this->lista[poz].parinte = nodPrecedent;
			this->nrElemente++;
			return 0;
		}
		else {
			//Adaugam nodul in partea stanga
			this->lista[nodPrecedent].stanga = poz;
			this->lista[poz].info = triplet;
			this->lista[poz].parinte = nodPrecedent;
			this->nrElemente++;
			return 0;
		}
	}

	else if (e == 0) //treuie sa stergem nodul
	{
		int currentNodeToBeRemoved = 0;
		int currentNode = this->radacina;
		bool stop = false;

		while (currentNode != -1 and !stop) {
			if (get<0>(this->lista[currentNode].info) == i and get<1>(this->lista[currentNode].info) == j)
			{
				currentNodeToBeRemoved = currentNode;
				stop = true;
			}
			else if (get<0>(this->lista[currentNode].info) == i and get<1>(this->lista[currentNode].info) < j) {
				currentNode = this->lista[currentNode].dreapta;
			}
			else if (get<0>(this->lista[currentNode].info) < i) {
				currentNode = this->lista[currentNode].dreapta;
			}
			else if (get<0>(this->lista[currentNode].info) == i and get<1>(this->lista[currentNode].info) > j) {
				currentNode = this->lista[currentNode].stanga;
			}
			else if (get<0>(this->lista[currentNode].info) > i) {
				currentNode = this->lista[currentNode].stanga;
			}
		}
		
		if (currentNode == -1)
			return 0;

		///Cazul 1: avem doar o un nod care este radacina
		if (currentNodeToBeRemoved == this->radacina) {
			this->radacina = -1;
			TElem oldValue = get<2>(this->lista[currentNodeToBeRemoved].info);
			this->nrElemente--;
			return oldValue;
		}
		else
		{
			int parent = this->lista[currentNodeToBeRemoved].parinte;

			if (this->lista[parent].stanga == currentNodeToBeRemoved) {
				this->lista[parent].stanga = -1;
			}

			else if (this->lista[parent].dreapta == currentNodeToBeRemoved) {
				this->lista[parent].dreapta = -1;
			}
				
			TElem oldValue = get<2>(this->lista[currentNodeToBeRemoved].info);
			this->nrElemente--;
			return oldValue;
		}
	}
}

//Complexitate: Theta(1)
int Matrice::allocate()
{
	int newElement = this->primLiber;
	if (newElement != -1)
	{
		this->primLiber = this->lista[this->primLiber].stanga;
		this->lista[newElement].stanga = -1;
		this->lista[newElement].dreapta = -1;
		this->lista[newElement].parinte = -1;
	}

	return newElement;
}

//Complexitate: Theta(1)
void Matrice::deallocate(int poz)
{
	this->lista[poz].stanga = this->primLiber;
	get<2>(this->lista[poz].info) = NULL_TELEMENT;
	this->lista[poz].dreapta = -1;
	this->lista[poz].parinte = -1;
	this->primLiber = poz;
}