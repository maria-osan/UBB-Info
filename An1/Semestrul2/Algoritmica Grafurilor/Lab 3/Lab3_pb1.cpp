#include <iostream>
#include <cstring>
#include <fstream>
#include <vector>
#include <queue>
#include <list>
#include <string>

using namespace std;

const int VMAX = INT_MAX;
const int INF = INT_MAX;

class Graph 
{
	// fisierul de intrare
	string infile; 

	// fisierul de iesire
	string outfile; 

	// V - numarul de varfuri
	// E - numarul de arce
	// S - varful de start
	int V, E, S; 

	// adiac - lista de perechi de varfuri adiacente
	list<pair<int, int>>* adiac;

public:
	Graph(string in, string out);

	// algoritm Dijkstra
	void dijkstra();

	// stergem lista de adiacenta
	~Graph();
};

Graph::Graph(string in, string out) 
{
	// fisierul de intrare
	this->infile = in;

	// fisierul de iesire
	this->outfile = out;

	// citire date din fisier:
	ifstream fin(this->infile);
	if (!fin) 
	{
		cout << "Fisierul de intrare nu a putut fi deschis!\n";
		exit(-1);
	}

	// citim numaul de varfuri (V), numarul de arce (E) si varful de start (S)
	int V, E, S;
	fin >> V >> E >> S;
	this->V = V;
	this->E = E;
	this->S = S;

	// lista de perechi de varfuri adiacente
	this->adiac = new list<pair<int, int>>[V];

	// citim varfurile adiacente (u, v) si ponderea muchiei dintre ele (w)
	for (int u, v, w; fin >> u >> v >> w; adiac[u].push_back({ v, w }));
	fin.close();
}

struct comparare
{
	bool operator()(const pair<int, int>& l, const pair<int, int>& r)
	{
		return l.first > r.first;
	}
};

void Graph::dijkstra() 
{
	priority_queue<pair<int, int>, vector<pair<int, int>>, comparare> coada;

	// drumul de cost minim, initializam cu infinit (o valoare foarte mare)
	vector<int> dist(V, INF);

	// punem varful de start in coada
	coada.push({ 0, this->S });
	dist[this->S] = 0;

	// algoritm de drum minim in graf: Dijkstra
	while (!coada.empty()) 
	{
		int u = coada.top().second;
		coada.pop();

		for (auto i : adiac[u]) 
		{
			int v = i.first;
			int w = i.second;
			if (dist[v] > dist[u] + w) 
			{
				dist[v] = dist[u] + w;
				coada.push({ dist[v], v });
			}
		}
	}

	// afisam drumul de cost minim in fisierul de iesire
	ofstream fout(this->outfile);
	for (int i = 0; i < V; ++i) 
	{
		if (dist[i] == INF) 
		{
			fout << "INF ";
		}
		else 
		{
			fout << dist[i] << " ";
		}
	}
	fout << "\n";
	fout.close();
}

Graph::~Graph() 
{
	delete[] adiac;
}


int main(int argc, char** argv) 
{
	if (argc != 3) 
	{
		cout << "Numar invalid de argumente!\n";
		cout << "Utilizare: ./p1.exe fisier1 fisier2\n";
		exit(-1);
	}

	Graph G(argv[1], argv[2]);
	G.dijkstra();

	return 0;
}