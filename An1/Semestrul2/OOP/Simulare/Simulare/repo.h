#pragma once

#include "device.h"


#include <vector>

using std::vector;

class RepoFile {
private:
	vector<Device> all; //vectorul de device-uri

	string file_name; //numele fisierului
	void load_from_file(); //functia de citire din fisier
	void save_to_file(const vector<Device>& all);

public:
	RepoFile(string f_name) :file_name{ f_name } {
		load_from_file();
	}

	//Getter pentru lista de deviceuri
	const vector<Device>& get_all() const
	{
		return all;
	}

	//Functie de adaugare
	void add(const Device& d);

	//Functie de cautare a unui device
	const Device& find(const string& id);
};

class RepoException {
	string msg;

public:
	RepoException(string m) :msg{ m } {}

	//Getter pentru erori
	const string& get_msg() const
	{
		return msg;
	}
};