#include <iostream>
#include <fstream>

int n, m, p, a[100][100], L[500];

void Euler(int k)
{
    for (int i = 0; i <= n; i++)
        if (a[k][i])
        {
            a[k][i] = a[i][k] = 0;
            Euler(i);
        }
    L[++p] = k;
}

int main()
{
    std::ifstream f("in.txt");

    int i, j;
    f >> n >> m;
    for (int k = 1; k <= m; k++)
    {
        f >> i >> j;
        a[i][j] = a[j][i] = 1;
    }
    
    Euler(1);

    std::cout << p << "\n";
    for (i = 1; i <= p; i++)
        std::cout << L[i] << " ";

    f.close();

    return 0;
}