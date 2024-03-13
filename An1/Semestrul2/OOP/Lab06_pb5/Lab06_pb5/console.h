#pragma once

#include "service.h"
#include "disciplina.h"

class Console {
	Service& srv;

	// Read data from the keyboard and add the new subject
	// throw exception if: it cannot be saved, it's not valid
	void add_UI();

	// Delete a subject from the vector of subjects
	// throw exception if the subject doesn't exist in the vector
	void delete_UI();

	// Search a subject in the vector
	// throw exception if the subject doesn't exist in the vector
	void search_UI();

	// print a list of subjects on the console
	// void print(const vector<Disciplina>& d_lst);
	template <typename Disciplina>
	void print(const vector_dinamic_t<Disciplina>& d_lst);

public:
	Console(Service& srv) noexcept : srv{ srv }{}

	// does not allow copying objects
	Console(const Console& ot) = delete;

	void start();
};