#define _CRT_SECURE_NO_WARNINGS
#include "masina.h"
#include "repository.h"
#include "service.h"
#include "validare.h"
#include "consola.h"

#include <iostream>
#include <string.h>

using namespace std;

Consola creazaConsola()
{
	/*
	* Creaza consola
	* returneaza consola
	*/
	Consola cons;
	cons.srv = creeareService();
	return cons;
}

Service get_service(Consola cons)
{
	/*
	* cons - consola (tip Consola)
	* returneaza service-ul consolei
	*/
	return cons.srv;
}

void meniu()
{
	/*
	* Meniul principal al aplicatiei
	*/
	std::cout << "-----------------------------------\n";
	std::cout << "-       Inchiriere masini         -\n";
	std::cout << "-----------------------------------\n";
	std::cout << "- Alegeti o comanda din meniu:    -\n";
	std::cout << "-----------------------------------\n";
	std::cout << "- 1. Adaugare masina              -\n";
	std::cout << "- 2. Actualizare masina           -\n";
	std::cout << "- 3. Inchiriere masina            -\n";
	std::cout << "- t. Tipareste toate masinile     -\n";
	std::cout << "- x. Iesire                       -\n";
	std::cout << "-----------------------------------\n";
}

void update_meniu()
{
	/*Meniul pentru comanda 2: actualizare produs*/
	std::cout << "-------------------------------------\n";
	std::cout << "-     Actualizari disponibile:      -\n";
	std::cout << "-------------------------------------\n";
	std::cout << "- 1. Model                          -\n";
	std::cout << "- 2. Categorie                      -\n";
	std::cout << "- x. Intoarcere la meniul principal -\n";
	std::cout << "-------------------------------------\n";
	std::cout << "- Alegeti optiunea: ";
}

void successful_operation()
{
	std::cout << "\nOpetatie realizata cu succes. \n\n";
}

void unsuccessful_operation()
{
	std::cout << "\nOpetatia nu s-a realizat cu succes. \n\n";
}

void afisare_toate_masinile(Service srv)
{
	/*
	* Tipareste toate masinile
	* srv - service-ul
	*/
	Repo rep = get_repo(srv);
	if (get_dimensiune(&rep.l) == 0)
		std::cout << "Nu exista masini in lista!\n";
	else {
		for (int i = 1; i <= get_dimensiune(&rep.l); i++)
		{
			Masina m = get_masina(&rep.l, i);
			std::cout << get_nr_inmatriculare(m) << ": Modelul - " << get_model(m) << ", Categoria - " << get_categorie(m) << "\n";
		}
	}
	std::cout << "\n";
}

void citire_nr_inmatriculare(char nr_inmatriculare[8])
{
	/*
	* Functia citeste numarul de inmatriculare valid al unei masini
	* nr_inmatriculare - string
	*/
	do {
		std::cout << "Numarul de inmatriculare: ";
		std::cin >> nr_inmatriculare;
	} while (validare_nr_inmatriculare(nr_inmatriculare) == 0);
}

void citire_model(char model[20])
{
	/*
	* Functia citeste modelul unei masini
	* model - string
	*/
	std::cout << "Modelul: ";
	std::cin.get();
	std::cin.getline(model, 20);
}

void citire_categorie(char categorie[10])
{
	/*
	* Functia citeste categoria valida a unei masini
	* categorie - string
	*/
	do {
		std::cout << "Categoria: ";
		std::cin >> categorie;
	} while (validare_categorie(categorie) == 0);
}

void citire(Masina* m)
{
	char nr_inmatriculare[8], model[20], categorie[10];
	citire_nr_inmatriculare(nr_inmatriculare);
	citire_model(model);
	citire_categorie(categorie); //Dc se afis de 3 ori ??
	*m = creeazaMasina(nr_inmatriculare, model, categorie);
}

void start()
{
	/*Interfata cu utilizatorul*/
	Consola cons = creazaConsola();
	Service serv = get_service(cons);
	Masina m;
	char nr_inmatriculare[8], model[20], categorie[10], opt, cmd;
	int ok = 1;

	while (ok)
	{
		meniu();
		std::cout << "Comanda: ";
		std::cin >> cmd;
		std::cout << "\n";

		if (cmd == '1')
		{
			citire(&m);
			std::cout << "\n";
			if (s_add(&serv, m) == 1)
				successful_operation();
			else
			{
				std::cout << "Masina cu acest numar de inmatriculare exista deja!\n";
				unsuccessful_operation();
			}
			std::cout << "\n";

		}
		else if (cmd == '2')
		{
			int k = 1;
			while (k)
			{
				update_meniu();
				std::cin >> opt;
				std::cout << "\n";
				if (opt == '1')
				{
					citire_nr_inmatriculare(nr_inmatriculare);
					citire_model(model);
					if (s_update_model(&serv, nr_inmatriculare, model))
						successful_operation();
					else unsuccessful_operation();
					std::cout << "\n";
				}
				else if (opt == '2')
				{
					citire_nr_inmatriculare(nr_inmatriculare);
					citire_categorie(categorie);
					if (s_update_categorie(&serv, nr_inmatriculare, categorie))
						successful_operation();
					else unsuccessful_operation();
					std::cout << "\n";
				}
				else if (opt == 'x')
				{
					std::cout << "___________________________________\n\n";
					k = 0;
				}
				else std::cout << "Optiune inexistenta! \n";
			}
		}
		else if (cmd == '3')
		{
			citire(&m);
			if (s_delete(&serv, m) == 1)
				successful_operation();
			else unsuccessful_operation();
		}
		else if (cmd == 't')
		{
			afisare_toate_masinile(serv);
		}
		else if (cmd == 'x')
		{
			std::cout << "\nAplicatia a fost inchisa cu succes! \n";
			std::cout << "___________________________________\n";
			ok = 0;
		}
		else {
			std::cout << "\nComanda invalida! \n\n";
		}
	}
}