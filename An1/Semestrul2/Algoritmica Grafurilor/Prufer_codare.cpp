#include <iostream>
#include <fstream>

std::ifstream inC("codare.txt");

int main()
{

    int v[105] = { 0 }, fr[105] = { 0 }, codare[105] = { 0 }, decodare[105] = { 0 };
    int n;
    inC >> n;
    for (int i = 0; i < n; i++)
    {
        inC >> v[i];
        if (v[i] != -1)
            fr[v[i]]++;
    }

    // codare
    int k = -1;
    for (int i = 1; i < n; i++)
    {
        int j = 0;
        while (fr[j])
            j++;
        codare[++k] = v[j];
        fr[j] = -1;
        fr[v[j]]--;
    }

    std::cout << n - 1 << "\n";
    for (int i = 0; i < n - 1; i++)
        std::cout << codare[i] << " ";
    std::cout << '\n';

    return 0;
}