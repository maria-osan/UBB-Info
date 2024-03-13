#include "service.h"

#include <assert.h>
#include <iostream>
#include <sstream>
#include <functional>
//#include <algorithm>

using std::ostream;
using std::stringstream;


// add a new sunject
// throw exception if: it can't be saved, it's invalid
void Service::add(const string& id, const string& name, const string& nr_hours, const string& type, const string& teacher)
{
	Disciplina d{ id, name, nr_hours, type, teacher };
	val.validate(d);
	r.store(d);
}

// delete a subject
// throw an exception is the subject does not exist in the vector
void Service::del(const Disciplina& d)
{
	r.del(d);
}

// search for a subject
// throw an exception is the subject doesn't exist
const Disciplina& Service::find(string id) const
{
	return r.find<Disciplina>(id);
}

void Service::modify(const Disciplina& d, const string& new_val, char opt)
{
	r.modify(d, new_val, opt);
}

template <typename Disciplina>
vector_dinamic_t<Disciplina> Service::filter(function<bool(const Disciplina&)> fct)
{
	vector_dinamic_t<Disciplina> rez;
	vector_dinamic_t<Disciplina> all{ r.get_all() };

	/*for (const auto& d : r.get_all())
		if (fct(d))
			rez.add(d);*/

	for (int i = 0; i < all.size(); i++)
		if (fct(all.get_elem(i)))
			rez.add(all.get_elem(i));

	return rez;
}

// filter after number of hours per week
template <typename Disciplina>
vector_dinamic_t<Disciplina> Service::filter_equal_hours(const string& nr_hours)
{
	return filter<Disciplina>([nr_hours](const Disciplina& d) {
		return d.get_nr_hours() == nr_hours;
		});
}

// filter after teacher
template <typename Disciplina>
vector_dinamic_t<Disciplina> Service::filter_same_teacher(const string& teacher)
{
	return filter<Disciplina>([teacher](const Disciplina& d) {
		return d.get_teacher() == teacher;
		});
}

vector_dinamic_t<Disciplina> Service::general_sort(bool(*cmp_f)(const Disciplina&, const Disciplina&))
{
	vector_dinamic_t<Disciplina> v{ r.get_all() }; // a copy is made
	for (int i = 0; i < v.size(); i++)
		for (int j = 0; j < v.size(); j++)
			if (!cmp_f(v.get_elem(i), v.get_elem(j)))
			{
				// switch the subjects
				Disciplina aux = v.get_elem(i);
				v.get_elem(i) = v.get_elem(j);
				v.get_elem(j) = aux;
			}
	return v;
}

// sort by subject name
vector_dinamic_t<Disciplina> Service::sort_name()
{
	// auto coppy_all = r.get_all();
	// std::sort(coppy_all.begin(), coppy_all.end(), cmp_name);
	// return coppy_all;
	return general_sort(cmp_name);
}

// sort by number of hours per week and id
vector_dinamic_t<Disciplina> Service::sort_hours()
{
	return general_sort([](const Disciplina& d1, const Disciplina& d2) {
		if (d1.get_nr_hours() == d2.get_nr_hours()) {
			return d1.get_id() > d2.get_id();
		}
		return d1.get_nr_hours() > d2.get_nr_hours();
		});
}

// sort by teacher and type
vector_dinamic_t<Disciplina> Service::sort_teacher_type() {
	return general_sort([](const Disciplina& d1, const Disciplina& d2) {
		if (d1.get_teacher() == d2.get_teacher()) {
			return d1.get_type() > d2.get_type();
		}
		return d1.get_teacher() > d2.get_teacher();
		});
}

// ---TESTS---

void test_add_serv()
{
	// Test for functoin: add
	Repo r;
	ValidateDisciplina val;
	Service srv{ r,val };
	assert(srv.get_all().size() == 0);

	srv.add("5006", "POO", "1", "seminar", "Czibula Istvan");
	assert(srv.get_all().size() == 1);

	// I try to add something invalid
	try {
		srv.add("5006", "POO", "-1", "semi", "");
	}
	catch (ValidateException&) {
		assert(true);
	}

	// I try to add something that already exist
	try {
		srv.add("5006", "POO", "1", "semi", "Czibula Istvan");
	}
	catch (const RepoException&) {
		assert(true);
	}
}

void test_search_serv()
{
	// Test for functoin: find
	Repo r;
	ValidateDisciplina val;
	Service srv{ r,val };
	srv.add("5006", "POO", "1", "seminar", "Czibula Istvan");
	srv.add("5022", "SDA", "1", "laborator", "Maier Mariana");

	auto d = srv.find("5006");
	assert(d.get_id() == "5006");
	assert(d.get_name() == "POO");
	assert(d.get_nr_hours() == "1");
	assert(d.get_type() == "seminar");
	assert(d.get_teacher() == "Czibula Istvan");

	// throw exception if it doesn't exist
	try {
		srv.find("5026");
	}
	catch (RepoException&) {
		assert(true);
	}
}

void test_delete_serv()
{
	// Test for function: del
	Repo r;
	ValidateDisciplina val;
	Service srv{ r,val };
	srv.add("5006", "POO", "1", "seminar", "Czibula Istvan");
	srv.add("5022", "SDA", "1", "laborator", "Maier Mariana");

	Disciplina d = srv.find("5022");
	srv.del(d);
	assert(r.get_all().size() == 1);

	r.del(r.find<Disciplina>("5006"));
	assert(srv.get_all().size() == 0);

	// I can't delete a subject that doesn't exist in the vector
	try {
		srv.del(Disciplina{ "5006", "POO", "1", "seminar", "Czibula Istvan" });
	}
	catch (const RepoException& e) {
		stringstream os;
		os << e;
		assert(os.str().find("exista") >= 0);
	}
}

void test_modify_serv()
{
	// Test for function: modify
	Repo r;
	ValidateDisciplina val;
	Service srv{ r,val };
	Disciplina d = { "5006", "POO", "1", "seminar", "Czibula Istvan" };
	srv.add("5006", "POO", "1", "seminar", "Czibula Istvan");
	Disciplina d2 = { "5022", "SDA", "1", "laborator", "Maier Mariana" };
	srv.add("5022", "SDA", "1", "laborator", "Maier Mariana");

	const string& name = "FP";
	srv.modify(d, name, '1');
	assert(r.get_all().get_elem(0).get_name() == "FP");

	const string& nr_hours = "2";
	srv.modify(d, nr_hours, '2');
	assert(r.get_all().get_elem(0).get_nr_hours() == "2");

	const string& type = "curs";
	srv.modify(d2, type, '3');
	assert(r.get_all().get_elem(1).get_type() == "curs");

	const string& teacher = "Czibula Istvan";
	srv.modify(d2, teacher, '4');
	assert(r.get_all().get_elem(1).get_teacher() == "Czibula Istvan");
}

void test_filter() {
	// Test for functions: filter_equal_hours, filter_same_teacher
	Repo r;
	ValidateDisciplina val;
	Service srv{ r,val };
	srv.add("5006", "POO", "1", "seminar", "Czibula Istvan");
	srv.add("5022", "SDA", "1", "laborator", "Maier Mariana");
	srv.add("0014", "Geometrie", "2", "curs", "Blaga Paul");

	assert(srv.filter_equal_hours<Disciplina>("1").size() == 2);
	assert(srv.filter_equal_hours<Disciplina>("2").size() == 1);
	assert(srv.filter_same_teacher<Disciplina>("Czibula Istvan").size() == 1);
	assert(srv.filter_same_teacher<Disciplina>("Maier Mariana").size() == 1);
	assert(srv.filter_same_teacher<Disciplina>("Blaga Paul").size() == 1);
}

void test_sort() {
	// Test for sort functions
	Repo r;
	ValidateDisciplina val;
	Service srv{ r,val };
	srv.add("5006", "POO", "1", "seminar", "Czibula Istvan");
	srv.add("5022", "SDA", "1", "laborator", "Maier Mariana");
	srv.add("0014", "Geometrie", "2", "curs", "Blaga Paul");
	srv.add("0015", "Geometrie", "2", "seminar", "Blaga Paul");

	auto first_d = srv.sort_name().get_elem(0);
	assert(first_d.get_name() == "Geometrie");

	first_d = srv.sort_hours().get_elem(0);
	assert(first_d.get_nr_hours() == "1");
	assert(first_d.get_id() == "5006");

	first_d = srv.sort_teacher_type().get_elem(0);
	assert(first_d.get_teacher() == "Blaga Paul");
	assert(first_d.get_type() == "curs");

}

void tests_service()
{
	test_add_serv();
	test_search_serv();
	test_delete_serv();
	test_modify_serv();
	test_filter();
	test_sort();
}