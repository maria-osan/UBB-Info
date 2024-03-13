#include "service.h"
#include "repo.h"

#include <assert.h>
#include <algorithm>

//Sorteaza vectorul de device-uri dupa model
vector<Device> Service::sortModel()
{
	vector<Device> sorted = r.get_all();
	std::sort(sorted.begin(), sorted.end(), [](const Device& d1, const Device& d2) {
		return d1.get_model() < d2.get_model();
		});
	return sorted;
}

//Sorteaza vectorul de device-uri dupa an
vector<Device> Service::sortAn()
{
	vector<Device> sorted = r.get_all();
	std::sort(sorted.begin(), sorted.end(), [](const Device& d1, const Device& d2) {
		return d1.get_an() < d2.get_an();
		});
	return sorted;
}

//Test pentru adaugarea datelor din fisier
void test_add()
{
	RepoFile r{ "test.txt" };
	Service srv{ r };

	vector<Device> all = srv.get_all_dev();

	assert(all.size() == 5);

	Device d{ "12", "1h2", "ab", "d", "rosu", 2015, 20 };
	srv.add_dev(d);
	assert(all.size() == 6);

	assert(all[5].get_id() == "12");
	assert(all[5].get_serie() == "1h2");
	assert(all[5].get_model() == "ab");
	assert(all[5].get_tip() == "d");
	assert(all[5].get_culoare() == "rosu");
	assert(all[5].get_an() == 2015);
	assert(all[5].get_pret() == 20);
}

//Test pentru cautarea unui device
void test_search()
{
	RepoFile r{ "test.txt" };
	Service srv{ r };

	vector<Device> all = srv.get_all_dev();

	assert(all.size() == 5);

	auto d = srv.search("01");
	assert(d.get_model() == "ma");

	try {
		auto d1 = srv.search("52");
	}
	catch (RepoException&)
	{
		assert(true);
	}
}

//Test pentru functiile de sortare
void test_sort()
{
	RepoFile r{ "test.txt" };
	Service srv{ r };

	vector<Device> all = srv.get_all_dev();

	assert(all.size() == 5);

	vector<Device> sortModel = srv.sortModel();
	assert(sortModel[0].get_id() == "04");
	assert(sortModel[4].get_id() == "03");

	vector<Device> sortAn = srv.sortAn();
	assert(sortAn[0].get_id() == "05");
	assert(sortAn[4].get_id() == "04");
}

void test_all()
{
	test_add;
	test_search();
	test_sort();
}