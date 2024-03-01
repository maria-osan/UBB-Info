// 2. Fie un graf reprezentat sub o anumita forma (graful este citit dintr-un fisier). Sa se rezolve:
// a. sa se determine nodurile izolate dintr - un graf.
// b. sa se determine daca graful este regular.
// c. pentru un graf reprezentat cu matricea de adiacenta sa se determine matricea distantelor.
// d. pentru un graf reprezentat cu o matrice de adiacenta sa se determine daca este conex.

#include <iostream>
#include <fstream>
#include <iomanip>

// #define inf INT_MAX

using namespace std;

ifstream f("in3.txt");


// citim datele din fiosier si le stocam in matricea de adiacenta
void citire_fisier(int n, int matr_adiac[][30], int& m)
{
    m = 0; // numarul de muchii
    int x, y;
    while (f >> x >> y)
    {
        matr_adiac[x][y] = 1;
        matr_adiac[y][x] = 1;
        m++;
    }
}

// se initializeaza matricea cu 0
void initialoizare(int n, int matr[][30])
{
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= n; j++)
            matr[i][j] = 0;
}

void initialoizare_matr_dist(int n, int matr_adiac[][30], int matr[][30])
{
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= n; j++)
            if (i == j)
                matr[i][j] = 0;
            else if(matr_adiac[i][j] == 1)
                matr[i][j] = 1;
            else
                matr[i][j] = INT_MAX;
}

void afisare_matrice(int n, int matr[][30])
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            cout << matr[i][j] << " ";
        cout << endl;
    }
}

void afisare_matr_dist(int n, int matr[][30])
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            if (matr[i][j] == INT_MAX)
                cout << setw(3) << "inf" << " ";
            else
                cout << setw(3) << matr[i][j] << " ";
        cout << endl;
    }
}

// determinam numarul nodurilor izolate din graf
void noduri_izolate(int n, int matr_adiac[][30], int nod_izolat[], int &k)
{
    k = 0;
    for (int i = 1; i <= n; i++)
    {
        int contor = 0;
        for (int j = 1; j <= n; j++)
            if (matr_adiac[i][j] != 0)
                contor++;
        if (contor == 0)
            nod_izolat[++k] = i;
    }
}

// determinam daca graful e regular (toate vârfurile au acelaºi grad)
void graf_regular(int n, int matr_adiac[][30], int grad_noduri[])
{   
    for (int i = 1; i <= n; i++)
    {
        int cate = 0;
        for (int j = 1; j <= n; j++)
            if (matr_adiac[i][j] == 1)
                cate++;
        grad_noduri[i] = cate;
    }
}

// determinam matricea distantelor
void matricea_distantelor(int n, int matr_dist[][30], int matr_adiac[][30])
{
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (matr_dist[i][k] != INT_MAX && matr_dist[k][j] != INT_MAX)
                    if (matr_dist[i][j] > matr_dist[i][k] + matr_dist[k][j])
                        matr_dist[i][j] = matr_dist[i][k] + matr_dist[k][j];
}

// algoritmul de PARCURGERE IN ADANCIME
void DFS(int x, int vizitat[], int matr_adiac[][30], int n)
{
    vizitat[x] = 1;
    for (int i = 1; i <= n; i++)
        if (matr_adiac[x][i] == 1 && vizitat[i] == 0)
            DFS(i, vizitat, matr_adiac, n);
}

// verificam daca un graf este conex cu ajutorul DFS (parcurgerea in adancime)
int Conex(int vizitat[], int matr_adiac[][30], int n)
{
    DFS(1, vizitat, matr_adiac, n);
    for (int i = 1; i <= n; i++)
        if (vizitat[i] == 0)
            return 0;
    return 1;
}

int main()
{
    int n, m, matr_adiac[30][30], k, nod_izolat[30], grad_noduri[100], matr_dist[30][30], vizitat[30] = { 0 };
    f >> n; // numarul de noduri
    // matricea de adiacenta
    cout << "Matricea de adiacenta: \n";
    initialoizare(n, matr_adiac);
    citire_fisier(n, matr_adiac, m);
    afisare_matrice(n, matr_adiac);

    // nodurile izolate
    noduri_izolate(n, matr_adiac, nod_izolat, k);
    if (k == 0)
        cout << "\nNu exista noduri izolate in graf!";
    else {
        cout << "\nNodurile izolate din graf sunt: \n";
        for (int i = 1; i <= k; i++)
            cout << nod_izolat[i] << " ";
    }

    // graf regular
    if (k)
        cout << "\n\nGraful nu este regular!\n";
    else
    {
        graf_regular(n, matr_adiac, grad_noduri);
        int ok = 1;
        for (int i = 1; i < n; i++)
            if (grad_noduri[i] != grad_noduri[i + 1])
                ok = 0;
        if (ok)
            cout << "\n\nGraful este regular!\n";
        else
            cout << "\n\nGraful nu este regular!\n";
    }

    // matricea distantelor
    cout << "\nMatricea distantelor: \n";
    initialoizare_matr_dist(n, matr_adiac, matr_dist);
    matricea_distantelor(n, matr_dist, matr_adiac);
    afisare_matr_dist(n, matr_dist);

    // graf conex
    if (Conex(vizitat, matr_adiac, n))
        cout << "\nGraful este conex!\n";
    else cout << "\nGraful nu este conex!\n";

    f.close();

    return 0;
}