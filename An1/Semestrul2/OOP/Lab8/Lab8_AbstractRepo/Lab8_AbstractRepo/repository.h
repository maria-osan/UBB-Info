#pragma once

#include "disciplina.h"

#include <vector>
#include <string>
#include <ostream>
#include <functional>
#include <map>

using std::vector;
using std::string;
using std::ostream;
using std::function;


class AbstractRepo {
	 virtual void met_1()=0;
	 //~AbstractRepo() = default;
};


class Repo :public AbstractRepo{
	vector<Disciplina> all;
	std::unique_ptr<AbstractRepo> rep;

	// private method that checks if d already exists in the repository
	bool exist(const Disciplina& d) const;

public:
	Repo() = default;

	// does not allow copying of objects
	Repo(const Repo& d) = delete;

	//~Repo() = default;

	void met_1()  {
			std::cout << "!\n";
	}

	// saving subject
	// throw an exception if there is another subject with the same id
	//void store(const Disciplina& d);
	void store(const Disciplina& d);

	// search
	// throw an exception is the subject does not exist
	const Disciplina& find(string id) const;

	// delete
	// throw an exception is the subject does not exist in the vector
	// void del(const Disciplina& d);
	void del(const Disciplina& d);

	// void modify(const Disciplina& d, const string& new_val, char opt);
	void modify(const Disciplina& d, const string& new_val, char opt);

	// return all the subjects saved
	const vector<Disciplina>& get_all() const noexcept;

	std::map<string, int> raport();
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
