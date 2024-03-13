#pragma once
#pragma once

#include "disciplina.h"
#include "vector_dinamic_template.h"

#include <vector>
#include <string>
#include <ostream>
#include <functional>

using std::vector;
using std::string;
using std::ostream;
using std::function;

class Repo {
	vector_dinamic_t<Disciplina> all;

	// private method that checks if d already exists in the repository
	bool exist(const Disciplina& d) const;

public:
	Repo() = default;

	// does not allow copying of objects
	Repo(const Repo& d) = delete;

	// saving subject
	// throw an exception if there is another subject with the same id
	template <typename Disciplina>
	void store(const Disciplina& d);

	// search
	// throw an exception is the subject does not exist
	template <typename Disciplina>
	const Disciplina& find(string id) const;

	// delete
	// throw an exception is the subject does not exist in the vector
	template <typename Disciplina>
	void del(const Disciplina& d);

	template <typename Disciplina>
	void modify(const Disciplina& d, const string& new_val, char opt);

	// return all the subjects saved
	const vector_dinamic_t<Disciplina>& get_all() const noexcept;
};

// used to signal exceptional situations that may appear in the repo
class RepoException {
	string msg;

public:
	RepoException(string m) : msg{ m } {}

	// friend function (I want to use private member msg)
	friend ostream& operator<<(ostream& out, const RepoException& exp);
};

ostream& operator<<(ostream& out, const RepoException& exp);


// ---TESTS---
void tests_repo();