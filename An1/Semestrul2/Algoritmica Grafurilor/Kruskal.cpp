#include <iostream>
#include <fstream>

struct muchie
{
    int x, y, c;
} u[5000], sol[101];

std::ifstream f("in.txt");

void Kruskal()
{
    int n, m, L[101];
    f >> n >> m;
    int i, j;
    for (i = 1; i <= m; i++)
        f >> u[i].x >> u[i].y >> u[i].c;

    //sortare dupa cost
    for (i = 1; i < m; i++)
        for (j = i + 1; j < m; j++)
            if (u[i].c > u[j].c) {
                muchie aux = u[i]; 
                u[i] = u[j]; 
                u[j] = aux;
            }

    //initializare
    for (i = 1; i <= n; i++) 
        L[i] = i;

    int cost = 0, k = 0;
    i = 1;

    while (k < n - 1) {
        int arbx = L[u[i].x], arby = L[u[i].y];
        if (arbx != arby) {
            sol[++k] = u[i]; 
            cost += u[i].c;
            for (j = 1; j <= n; j++)
                if (L[j] == arby) 
                    L[j] = arbx;
        }
        i++;
    }

    std::cout << cost << '\n';
    for (i = 1; i <= k; i++) 
        std::cout << sol[i].x << " " << sol[i].y << '\n';
}

int main()
{
    Kruskal();

    f.close();

    return 0;
}