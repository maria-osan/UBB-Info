#include "Colectie.h"
#include "IteratorColectie.h"
#include <iostream>

using namespace std;

bool rel(TElem e1, TElem e2) {
    //Θ(1)
    //return e1 <= e2;
    if (e1 <= e2)
        return true;
    return false;
}

Colectie::Colectie() {
    //Θ(1)
    this->cp = 70000;
    this->lg = 0;

    this->e = new TElem[cp];
    this->urm = new int[cp];
    this->prec = new int[cp];

    this->prim = 0;
    this->ultim = 0;
    this->primLiber = 0;

    initSpatiuLiber();
}

int Colectie::aloca() {
    //Θ(1)
    int i = primLiber;
    primLiber = urm[primLiber];
    prec[primLiber] = 0;
    return i;
}

void Colectie::dealoca(int i) {
    //Θ(1)
    prec[primLiber] = i;
    urm[i] = primLiber;
    primLiber = i;
    prec[primLiber] = 0;

    e[primLiber] = -1;
}

void Colectie::initSpatiuLiber() {
    for (int i = 0; i < cp - 1; i++) {
        urm[i] = i + 1;
    }
    urm[cp] = 0;
    primLiber = 1;
}

int Colectie::creeazaNod(TElem v) {
    //Θ(n)
    if (primLiber == 0) {
        redim();
    }
    int i = aloca();
    e[i] = v;
    urm[i] = 0;
    prec[i] = 0;
    return i;
}

void Colectie::redim() {
    //Θ(n)
    TElem* enou = new TElem[2 * cp];
    int* unou = new int[2 * cp];
    int* pnou = new int[2 * cp];

    for (int i = 0; i <= lg; i++) {
        enou[i] = e[i];
        unou[i] = urm[i];
        pnou[i] = prec[i];
    }

    cp *= 2;
    delete[] e;
    delete[] urm;
    delete[] prec;

    e = enou;
    urm = unou;
    prec = pnou;
    primLiber = lg + 1;
    for (int i = lg + 1; i < cp; i++) {
        urm[i] = i + 1;
        prec[i] = i - 1;
    }
    urm[cp] = 0;

    prec[cp] = cp - 1;
    prec[primLiber] = 0;
}

void Colectie::adauga(TElem elem) {
    //O(n)
    int nou = creeazaNod(elem);

    int crt = prim;
    while (crt != 0) {
        if (!rel(e[crt], elem)) {
            break;
        }
        crt = urm[crt];
    }
    //crt > elem
    if (crt == prim && crt == ultim && prim == 0) {
        //primul element din lista (crt==0)
        urm[nou] = 0;
        prec[nou] = 0;
        prim = nou;
        ultim = nou;
    }
    else if (crt == prim) {
        prec[prim] = nou;
        urm[nou] = prim;
        prim = nou;
        prec[prim] = 0;
    }
    else if (crt == 0) {
        //se adauga dupa ultim
        urm[ultim] = nou;
        prec[nou] = ultim;
        urm[nou] = 0;
        ultim = nou;
    }
    else {
        //daca e la mijloc
        urm[prec[crt]] = nou;
        prec[nou] = prec[crt];

        prec[crt] = nou;
        urm[nou] = crt;
    }

    lg++;
}


bool Colectie::sterge(TElem elem) {
    //O(n)
    if (vida()) {
        return false;
    }
    if (cauta(elem) == false) {
        return false;
    }

    //aflam pozitia elementului de sters
    int p = prim;
    while (p != 0) {
        if (e[p] == elem) {
            break;
        }
        p = urm[p];
    }

    if (e[p] != elem)
        return false;

    if (p == prim) {
        //sterg primul element
        prim = urm[p];
        prec[prim] = 0;
    }
    else if (p == ultim) {
        //sterg ultimul element
        ultim = prec[p];
        urm[ultim] = 0;
    }
    else {
        int q = prec[p];
        urm[q] = urm[p];
        prec[urm[p]] = q;
    }
    dealoca(p);
    lg--;
    return true;
}


bool Colectie::cauta(TElem elem) const {
    //O(n)
    int crt = prim;
    while (crt != 0) {
        if (e[crt] == elem) {
            return true;
        }
        if (!rel(e[crt], elem)) {
            break;
        }
        crt = urm[crt];
    }

    return false;
}


int Colectie::nrAparitii(TElem elem) const {
    //Θ(n)
    int n = 0;
    int crt = prim;
    while (crt != 0) {
        if (e[crt] == elem) {
            n++;
        }
        if (!rel(e[crt], elem)) {
            break;
        }
        crt = urm[crt];
    }
    return n;
}


int Colectie::dim() const {
    //Θ(1)
    return lg;
}


bool Colectie::vida() const {
    //Θ(1)
    return prim == 0;
}


IteratorColectie Colectie::iterator() const {
    //Θ(1)
    return IteratorColectie(*this);
}

int Colectie::transformăÎnMulțime()
{
    /*
    * Complexitate: 
    * Caz favorabil:O(n)
    * M<ediu: O(n^2)
    * Defavorabil: O(n^2)
    *
    * Pseudocod:
    * subalgoritm transformăÎnMulțime()
    *      prec: elementele din colecte
    *      post: returneaza numarul elementelor sterse
    * 
    *      i <- prim
    *      cate <- 0
    *      cat timp i != 0 executa
    *           nrAp <- nrAparitii(e[i])
    *           daca nrAp > 1 atunci
    *               sterge(e[i])
    *               cate <- cate+1
    *           sf_daca
    *           i <- urm[i]
    *      sf_cat timp
    *
    *      returneaza cate
    * sf_subalgoritm
    */
    int i = prim;
    int cate = 0;
    while (i != 0)
    {
        int nrAp = nrAparitii(e[i]);
        if (nrAp > 1)
        {
            sterge(e[i]);
            cate++;
        }
        i = urm[i];
    }
    return cate;
}

Colectie::~Colectie() {
    //Θ(n)

    /*delete[] e;
    delete[] urm;
    delete[] prec;*/
}