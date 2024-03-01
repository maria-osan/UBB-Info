#pragma once
#include <iostream>

typedef int TElem;

typedef bool(*Relatie)(TElem, TElem);

//in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class IteratorColectie;

class Colectie {

    friend class IteratorColectie;

private:
    /* aici e reprezentarea */

    TElem* e; //vectorul de elemente
    int* urm; //vectorul de legaturi inainte
    int* prec; //vectorul de legaturi inapoi

    int cp; //capacitatea vectorilor
    int lg; //lungimea reala a vectorilor

    int prim; //primul element
    int ultim; //ultimul element
    int primLiber; //primul element in lista de el libere

    //aloca spatiu liber de indice i
    int aloca();

    //dealoca spatiu de indice i
    void dealoca(int i);

    //initializeaza spatiul liber
    void initSpatiuLiber();

    int creeazaNod(TElem v);

    //redimensioneaza vectorii
    void redim();

public:
    //constructorul implicit
    Colectie();

    //adauga un element in colectie
    void adauga(TElem elem);

    //sterge o aparitie a unui element din colectie
    //returneaza adevarat daca s-a putut sterge
    bool sterge(TElem elem);

    //verifica daca un element se afla in colectie
    bool cauta(TElem elem) const;

    //returneaza numar de aparitii ale unui element in colectie
    int nrAparitii(TElem elem) const;


    //intoarce numarul de elemente din colectie;
    int dim() const;

    //verifica daca colectia e vida;
    bool vida() const;

    //returneaza un iterator pe colectie
    IteratorColectie iterator() const;

    // păstrează doar o apariție a tuturor elementelor din colecție 
    // returnează numărul de elemente eliminate 
    int transformăÎnMulțime();

    // destructorul colectiei
    ~Colectie();


};