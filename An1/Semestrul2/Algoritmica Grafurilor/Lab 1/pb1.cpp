// 1. Fie un fisier ce contine un graf neorientat reprezentat sub forma: prima linie contine numarul nodurilor iar urmatoarele randuri muchiile grafului. 
// Sa se scrie un program in C/C++ care sa citeasca fisierul si sa reprezinte/stocheze un graf folosind matricea de adiacenta, lista de adiacenta si 
// matricea de incidenta. Sa se converteasca un graf dintr-o forma de reprezentare in alta.

// Fisier->matrice de adiacenta->lista adiacenta->matrice de incidenta->lista adiacenta->matrice de adiacenta->lista.

#include <iostream>
#include <fstream>

using namespace std;

ifstream f("in.txt");


// citim datele din fiosier si le stocam in matricea de adiacenta
void citire_fisier(int n, int matr_adiac[][30], int &m)
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

// transformare din matrice de adiacenta in lista de adiacenta 
void lista_adiacenta(int n, int matr_adiac[][30], int lista_adiac[][30])
{
    for (int i = 1; i <= n; i++)
    {
        int k = 0;
        for (int j = 1; j <= n; j++)
            if (matr_adiac[i][j] == 1)
            {
                k++;
                lista_adiac[i][k] = j;
            }
        lista_adiac[i][0] = k;
    }
}

void afisare_lista_adiacenta(int n, int lista_adiac[][30])
{
    for (int i = 1; i <= n; i++)
    {
        cout << i << ": ";
        for (int j = 1; j <= lista_adiac[i][0]; j++)
            cout << lista_adiac[i][j] << " ";
        cout << endl;
    }
}

// transformare din lista de adiacenta in matrice de incidenta
void matrice_incidenta(int n, int m, int lista_adiac[][30], int matr_inc[][30])
{
    int k = 1;
    for (int i = 1; i <= n; i++)
    {
        int j = 1;
        while(lista_adiac[i][j])
        {
            if (lista_adiac[i][j] > i)
                matr_inc[i][k] = matr_inc[lista_adiac[i][j]][k++] = 1; // ??!!!???!
            j++;
        }
    }
}

// transformare din matrice de incidenta inapoi in lista de adiacenta
void inapoi_lista_adiacenta(int n, int m, int lista_adiac[][30], int matr_inc[][30])
{
    for (int j = 1; j <= m; j++)
    {
        int x = 0, y = 0;
        for (int i = 1; i <= n; i++)
            if (matr_inc[i][j]) 
            {
                x = y;
                y = i;
            }
        int k = 1;
        while (lista_adiac[x][k])
            k++;
        lista_adiac[x][k] = y;
        lista_adiac[x][0] = k;
        k = 1;
        while (lista_adiac[y][k])
            k++;
        lista_adiac[y][k] = x;
        lista_adiac[y][0] = k;
    }
}

// transformare din lista de adiacenta inapoi in matrice de adiacenta
void matrice_adiacenta(int n, int lista_adiac[][30], int matr_adiac[][30])
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= lista_adiac[i][0]; j++)
        {
            matr_adiac[i][lista_adiac[i][j]] = 1;
        }
    }
}

// se initializeaza matricea cu 0
void initialoizare(int n, int matr[][30])
{
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= n; j++)
            matr[i][j] = 0;
}

// se afiseaza matricea pe ecran
void afisare_matrice(int n, int matr[][30])
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            cout << matr[i][j] << " ";
        cout << endl;
    }
}

int main()
{
    int n, m, matr_adiac[30][30], lista_adiac[30][30], matr_inc[30][30];
    f >> n; // numarul de noduri
    // matricea de adiacenta
    cout << "Matricea de adiacenta: \n";
    initialoizare(n,matr_adiac);
    citire_fisier(n, matr_adiac, m);
    afisare_matrice(n, matr_adiac);

    // lista de adiacenta
    cout << "\nLista de adiacenta: \n";
    initialoizare(n,lista_adiac);
    lista_adiacenta(n, matr_adiac, lista_adiac);
    afisare_lista_adiacenta(n, lista_adiac);

    // matricea de incidenta
    cout << "\nMatricea de incidenta: \n";
    initialoizare(m,matr_inc);
    matrice_incidenta(n, m, lista_adiac, matr_inc);
    afisare_matrice(n, matr_inc);

    // lista de adiacenta
    cout << "\nLista de adiacenta: \n";
    initialoizare(n, lista_adiac);
    inapoi_lista_adiacenta(n, m, lista_adiac, matr_inc);
    afisare_lista_adiacenta(n, lista_adiac);

    // matricea de adiacenta
    cout << "\nMatricea de adiacenta: \n";
    initialoizare(n, matr_adiac);
    matrice_adiacenta(n, lista_adiac, matr_adiac);
    afisare_matrice(n, matr_adiac);

    f.close();

    return 0;
}
