#include "repository.h"

#include <assert.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using std::ostream;
using std::stringstream;
using std::vector;


// Add 
void Repo::store(const Disciplina& d)
{
	met_1();
	if (exist(d))
	{
		throw RepoException("Exista deja disciplina: " + d.get_name() + " cu id-ul: " + d.get_id());
	}
	all.push_back(d);
}

bool Repo::exist(const Disciplina& d) const
{
	//try
	//{
	//	find(d.get_id());
	//	return true;
	//}
	//catch (RepoException&)
	//{
	//	return false;
	//}

	auto rez = std::find_if(all.begin(), all.end(), [d](const Disciplina& dis) {
		return d.get_id() == dis.get_id();
		});

	if (rez != all.end())
		return true;
	else return false;
}

// Search
// throw exception if the subject doesn't exist
const Disciplina& Repo::find(string id) const
{
	for (const auto& d : all)
	{
		if (d.get_id() == id)
			return d;
	}
	// if it doesn't exist throw an exception
	throw RepoException("Nu exista disciplina cu id-ul: " + id);
}

// Delete
// throw an exception is the subject doesn't exist
void Repo::del(const Disciplina& d)
{
	met_1();
	if (!exist(d))
	{
		throw RepoException("Nu exista disciplina cu id-ul: " + d.get_id());
	}
	int i = 0;
	for (const auto& dis : all)
	{
		if (d.get_id() == dis.get_id())
			all.erase(all.begin() + i);
		i++;
	}
}

void Repo::modify(const Disciplina& d, const string& new_val, char opt)
{
	met_1();
	for (auto& dis : all)
	{
		if (d.get_id() == dis.get_id())
		{
			if (opt == '1')
				dis.set_name(new_val);
			else if (opt == '2')
				dis.set_nr_hours(new_val);
			else if (opt == '3')
				dis.set_type(new_val);
			else dis.set_teacher(new_val);
		}
	}
}

// return all of the saved subjects
const vector<Disciplina>& Repo::get_all() const noexcept
{
	return all;
}

std::map<string, int> Repo::raport()
{
	std::map<string, int> map;
	for (int i = 0; i < all.size(); i++)
	{
		Disciplina d = all[i];
		auto it = map.find(d.get_type());
		if (it != map.end())
			it->second++;
		else
			map.insert(std::pair<string, int>(d.get_type(), 1));
	}
	return map;
}


ostream& operator<<(ostream& out, const RepoException& exp)
{
	out << exp.msg;
	return out;
}