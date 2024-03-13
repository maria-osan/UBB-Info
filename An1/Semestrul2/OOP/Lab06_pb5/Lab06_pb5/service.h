#pragma once

#include "disciplina.h"
#include "repository.h"
#include "validator.h"
#include "vector_dinamic_template.h"

#include <string>
#include <vector>
#include <functional>

using std::vector;

class Service {
	Repo& r;
	ValidateDisciplina& val;

	// General filtering function
	// cmp_f - function that compares 2 subjects, checks if the criteria occurs
	//       - it can be any function (outside the class) that respects the signature (returns bool and has 2 subject parameters)
	//       - it can be a lambda function (which does not capture anything in the capture list)
	// return only the subjects that pass the filter (fct(d) == true)
	template <typename Disciplina>
	vector_dinamic_t<Disciplina> filter(function<bool(const Disciplina&)> fct);

	// General sorting function
	// cmp_f - function that compares 2 subjects, checks if the criteria occurs
	//       - it can be any function (outside the class) that respects the signature (returns bool and has 2 subject parameters)
	//       - it can be a lambda function (which does not capture anything in the capture list)
	// returns a list sorted by the criteria given as a parameter
	vector_dinamic_t<Disciplina> general_sort(bool (*cmp_f)(const Disciplina&, const Disciplina&));

public:
	Service(Repo& rep, ValidateDisciplina& v) noexcept : r{ rep }, val{ v } {}

	// does not allow copying of Service objects
	Service(const Service& ot) = delete;

	// return all the subjects in the added order
	const vector_dinamic_t<Disciplina>& get_all() noexcept {
		return r.get_all();
	}

	// add a new subject
	// throw exception if: it can't be saved, it's invalid
	void add(const string& id, const string& name, const string& nr_hours, const string& type, const string& teacher);

	// delete a subject
	// throw an exception is the subject does not exist in the vector
	void del(const Disciplina& d);

	// search for a subject
	// throw an exception is the subject doesn't exist
	const Disciplina& find(string id) const;

	void modify(const Disciplina& d, const string& new_val, char opt);

	// sort by subject name
	vector_dinamic_t<Disciplina> sort_name();

	// sort by number of hours per week and id
	vector_dinamic_t<Disciplina> sort_hours();

	// sort by teacher and type
	vector_dinamic_t<Disciplina> sort_teacher_type();

	// return only the subjects that has the number of hours per week equal with a given one
	template <typename Disciplina>
	vector_dinamic_t<Disciplina> filter_equal_hours(const string& nr_hours);

	// return only the subjects that has the same teacher as a given one
	template <typename Disciplina>
	vector_dinamic_t<Disciplina> filter_same_teacher(const string& teacher);
};

void tests_service();