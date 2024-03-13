#pragma once

#include "Disciplina.h"
#include "export.h"

#include <algorithm>  
#include <random>
#include <chrono>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

class study_contract
{
private:
	vector<Disciplina> list;

public:
	// empty the contract
	void empty_list() noexcept;

	// add a subject to the study contract
	void add(Disciplina d);

	// generate a random study contract
	// nr - given number of subjects
	void generate(int nr, vector<Disciplina> v);

	const vector<Disciplina>& get_list();

	int dim();

	// write in the file name_file the subject list
	// HTML format
	// throw RepoException if the file can't be open
	string export_html(string name_file);
};

void teste_cos();