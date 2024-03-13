#pragma once

#include <string>

using std::string;

class Device {
private:
	string id;
	string serie; //seria device-ului
	string model; //modelul device-ului
	string tip; //tipul device-ului
	string culoare; //culoarea device-ului
	int an; //anul in care a fost lansat device-ul
	int pret; //pretul pe piata al device-ului

public:
	Device(string id, string s, string m, string t, string c, int a, int p) :id{ id }, serie { s }, model{ m }, tip{ t }, culoare{ c }, an{ a }, pret{ p } {}

	//Getter pentru id
	const string& get_id() const
	{
		return id;
	}

	//Getter pentru serie
	const string& get_serie() const
	{
		return serie;
	}

	//Getter pentru model
	const string& get_model() const
	{
		return model;
	}

	//Getter pentru tip
	const string& get_tip() const
	{
		return tip;
	}

	//Getter pentru culoare
	const string& get_culoare() const
	{
		return culoare;
	}

	//Getter pentru an
	int get_an() const
	{
		return an;
	}

	//Getter pentru pret
	int get_pret() const
	{
		return pret;
	}
};