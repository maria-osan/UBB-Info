#include "repo.h"

#include <fstream>

using std::ifstream;
using std::ofstream;

//Functia citeste datele din fisier si arunca exceptie daca fisierul nu se poate deschide
void RepoFile::load_from_file()
{
	ifstream fin{ file_name };

	if (!fin.is_open())
		throw RepoException("Fisierul nu s-a putut deschide " + file_name);

	while (!fin.eof())
	{
		string id, serie, model, tip, culoare;
		int an, pret;

		fin >> id>> serie >> model >> tip >> culoare >> an >> pret;

		Device d{ id, serie, model, tip, culoare, an, pret };
		all.push_back(d);
	}

	fin.close();
}

//Functia salveaza datele in fisier
void RepoFile::save_to_file(const vector<Device>& all)
{
	ofstream fout(file_name);

	if (!fout.is_open())
		throw RepoException("Fisierul nu s-a putut deschide " + file_name);

	int n = all.size();
	for (const auto& d : all)
	{
		if (n == 0)
			fout << d.get_id() << " " << d.get_serie() << " " << d.get_model() << " " << d.get_tip() << " " << d.get_culoare() << " " << d.get_an() << " " << d.get_pret();
		else
		{
			fout << d.get_id() <<  " " << d.get_serie() << " " << d.get_model() << " " << d.get_tip() << " " << d.get_culoare() << " " << d.get_an() << " " << d.get_pret() << "\n";
		}
		n--;
	}
}

//Adauga un device in vector
void RepoFile::add(const Device& d)
{
	all.push_back(d);
	save_to_file(all);
}

//Cauta un device in vector si arunca exceptie daca nu il gaseste
const Device& RepoFile::find(const string& id)
{
	for (const auto& d : all)
	{
		if(d.get_id() == id)
			return d;
	}
	throw RepoException("Device-ul cu acest id nu se afla in lista");
}