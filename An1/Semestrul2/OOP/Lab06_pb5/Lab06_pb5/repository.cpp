#include "repository.h"

#include <assert.h>
#include <iostream>
#include <sstream>
#include <vector>

using std::ostream;
using std::stringstream;
using std::vector;


// Add 
template <typename Disciplina>
void Repo::store(const Disciplina& d)
{
	if (exist(d))
	{
		throw RepoException("Exista deja disciplina: " + d.get_name() + " cu id-ul: " + d.get_id());
	}
	all.add(d);
}

bool Repo::exist(const Disciplina& d) const
{
	try
	{
		find<Disciplina>(d.get_id());
		return true;
	}
	catch (RepoException&)
	{
		return false;}
}

// Search
// throw exception if the subject doesn't exist
template <typename Disciplina>
const Disciplina& Repo::find(string id) const
{
	//vector_dinamic_t<Disciplina> v{ all };

	for (int i = 0; i < all.size(); i++)
		if (all.get_elem(i).get_id() == id)
			return all.get_elem(i);

	/*for (const auto& d : all)
	{
		if (d.get_id() == id)
			return d;
	}*/

	// if it doesn't exist throw an exception
	throw RepoException("Nu exista disciplina cu id-ul: " + id);}

// Delete
// throw an exception is the subject doesn't exist
template <typename Disciplina>
void Repo::del(const Disciplina& d)
{
	if (!exist(d))
	{
		throw RepoException("Nu exista disciplina cu id-ul: " + d.get_id());
	}

	int i = 0;
	for (const auto& dis : all)
	{
		if (d.get_id() == dis.get_id())
		{
			// all.erase(all.begin() + i);
			/*for (int j = 1; j < all.size() - 1; j++)
				all.get_elem(j) = all.get_elem(++j);*/
			all.del(i, dis);
		}
		i += 1;
	}
}

template <typename Disciplina>
void Repo::modify(const Disciplina& d, const string& new_val, char opt)
{
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
const vector_dinamic_t<Disciplina>& Repo::get_all() const noexcept
{
	return all;
}


ostream& operator<<(ostream& out, const RepoException& exp)
{
	out << exp.msg;
	return out;
}


// ---TESTS---

void test_add()
{
	// Test for functoin: store
	Repo r;
	r.store(Disciplina{ "5006", "POO", "1", "seminar", "Czibula Istvan" });
	assert(r.get_all().size() == 1);
	assert(r.find<Disciplina>("5006").get_name() == "POO");

	r.store(Disciplina{ "5022", "SDA", "1", "laborator", "Maier Mariana" });
	assert(r.get_all().size() == 2);

	// I can't add 2 with the same id
	try {
		r.store(Disciplina{ "5006", "POO", "1", "seminar", "Czibula Istvan" });
	}
	catch (const RepoException&) {
		assert(true);
	}

	// search for a sunject that doesn't exist
	try {
		r.find<Disciplina>("5026");
	}
	catch (const RepoException& e) {
		stringstream os;
		os << e;
		assert(os.str().find("exista") >= 0);
	}
}

void test_search()
{
	// Test for functoin: find
	Repo r;
	Disciplina d1 = { "5006", "POO", "1", "seminar", "Czibula Istvan" };
	r.store(d1);
	Disciplina d2 = { "5022", "SDA", "1", "laborator", "Maier Mariana" };
	r.store(d2);

	auto d = r.find<Disciplina>("5006");
	assert(d.get_id() == "5006");
	assert(d.get_name() == "POO");
	assert(d.get_nr_hours() == "1");
	assert(d.get_type() == "seminar");
	assert(d.get_teacher() == "Czibula Istvan");

	// throw exception if it doesn't exist
	try {
		r.find<Disciplina>("5026");
	}
	catch (RepoException&) {
		assert(true);
	}
}

void test_delete()
{
	// Test for function: del
	Repo r;
	Disciplina d1 = { "5006", "POO", "1", "seminar", "Czibula Istvan" };
	r.store(d1);
	Disciplina d2 = { "5022", "SDA", "1", "laborator", "Maier Mariana" };
	r.store(d2);
	assert(r.get_all().size() == 2);

	Disciplina d = r.find<Disciplina>("5006");
	r.del(d);
	assert(r.get_all().size() == 1);

	r.del(r.find<Disciplina>("5022"));
	assert(r.get_all().size() == 0);

	// I can't delete a subject that doesn't exist in the vector
	try {
		r.del(Disciplina{ "5006", "POO", "1", "seminar", "Czibula Istvan" });
	}
	catch (const RepoException& e) {
		stringstream os;
		os << e;
		assert(os.str().find("exista") >= 0);
	}
}

void test_modify()
{
	// Test for function: modify
	Repo r;
	Disciplina d = { "5006", "POO", "1", "seminar", "Czibula Istvan" };
	r.store(d);
	Disciplina d2 = { "5022", "SDA", "1", "laborator", "Maier Mariana" };
	r.store(d2);

	const string& name = "FP";
	r.modify(d, name, '1');
	assert(r.get_all().get_elem(0).get_name() == "FP");

	const string& nr_hours = "2";
	r.modify(d, nr_hours, '2');
	assert(r.get_all().get_elem(0).get_nr_hours() == "2");

	const string& type = "curs";
	r.modify(d2, type, '3');
	assert(r.get_all().get_elem(1).get_type() == "curs");

	const string& teacher = "Czibula Istvan";
	r.modify(d2, teacher, '4');
	assert(r.get_all().get_elem(1).get_teacher() == "Czibula Istvan");
}

void tests_repo()
{
	test_add();
	test_search();
	test_delete();
	test_modify();
}