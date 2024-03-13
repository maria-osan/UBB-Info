#pragma once

#include "repo.h"

class Service {
private:
	RepoFile r{ "device.txt" };

public:
	Service(RepoFile r) :r{ r } {}

	//Getter pentru vectorul de device-uri
	const vector<Device>& get_all_dev() const
	{
		return r.get_all();
	}

	//Adauga un device in vector
	void add_dev(const Device& d)
	{
		r.add(d);
	}

	//Cauta un device in vector si arunca exceptie daca nu il gaseste
	const Device& search(const string& model)
	{
		return r.find(model);
	}

	//Functii pentru sortari
	vector<Device> sortModel();
	vector<Device> sortAn();
};

// --- Teste ---
void test_all();