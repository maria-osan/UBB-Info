#pragma once

#include <tuple>

typedef int TElem;
typedef std::tuple<int, int, TElem> Triplet;

#define NULL_TELEMENT 0
#define NULL_TRIPLE Triplet{-1, -1, NULL_TELEMENT}

struct Nod {
	Triplet info;
	int stanga;
	int dreapta;
	int parinte;
};

class Matrice {
	friend class IteratorMatrice;

private:
	/* aici e reprezentarea */
	Nod* lista;
	int radacina;
	int primLiber;
	int nrCol;
	int nrLin;
	int capacitate;
	int nrElemente;

	int allocate();
	void deallocate(int poz);

public:

	//constructor
	//se arunca exceptie daca nrLinii<=0 sau nrColoane<=0
	Matrice(int nrLinii, int nrColoane);


	//destructor
	~Matrice() {};

	//returnare element de pe o linie si o coloana
	//se arunca exceptie daca (i,j) nu e pozitie valida in Matrice
	//indicii se considera incepand de la 0
	TElem element(int i, int j) const;


	// returnare numar linii
	int nrLinii() const;

	// returnare numar coloane
	int nrColoane() const;


	// modificare element de pe o linie si o coloana si returnarea vechii valori
	// se arunca exceptie daca (i,j) nu e o pozitie valida in Matrice
	TElem modifica(int i, int j, TElem e);
};