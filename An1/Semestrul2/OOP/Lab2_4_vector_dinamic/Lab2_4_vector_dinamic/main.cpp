// Lab02_4.cpp : 
// 4. Inchiriere masini:
// Creati o aplicatie pentru o firma de inchirieri auto.Fiecare masina are un numar de inmatriculare, model si categorie(mini, sport, suv, etc).
// Aplicatia permite :
// a) adaugare de masini
// b) actualizare masina existenta
// c) inchiriere masina / returnare masina
// d) Vizualizare masini dupa un criteru dat(categorie, model)
// e) Permite sortarea masinilor dupa : model sau categorie(crescator / descrescator)

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#include "masina.h"
#include "lista.h"
#include "repository.h"
#include "consola.h"
#include "validare.h"

void teste()
{
	//teste pentru masina
	test_creeazaMasina();
	test_set();

	//teste pentru validare
	test_validare_nr_inmatriculare();
	test_validare_categorie();

	//teste pentru lista
	test_creeazaLista();
	test_add();
	test_copiere_lista();
	//test_realocare();

	//teste pentru repo
	//test_makeRepo();
	//test_r_add();
	//test_r_search();
	//test_r_delete();
	//test_r_update();

	//teste pentru service
	//test_s_add();
	//test_s_delete();
	//test_s_update_model();
	//test_s_update_categorie();
}

int main()
{
	teste();
	start();
	_CrtDumpMemoryLeaks();//print memory leak
	return 0;
}