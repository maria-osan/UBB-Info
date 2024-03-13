#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#include "console.h"
#include "repository.h"
#include "service.h"
#include "validator.h"
#include "study_contract.h"


// add some subjects
void add_some(Service& srv)
{
    srv.add("5006", "POO", "1", "seminar", "Czibula Istvan");
    srv.add("5005", "POO", "2", "curs", "Czibula Istvan");
    srv.add("5022", "SDA", "1", "laborator", "Maier Mariana");
    srv.add("0014", "Geometrie", "2", "curs", "Blaga Paul");
}


void test_all()
{
    tests_repo();
    tests_service();
    test_validator();
    teste_cos();
}

void run()
{
    //Repo r;
    RepoFile r{ "discipline.txt" };
    ValidateDisciplina val;
    Service srv{ r,val };
    //add_some(srv);
    study_contract list{ list };
    Console ui{ srv };
    ui.start();
}

int main()
{
    test_all();

    run();

    _CrtDumpMemoryLeaks();

    return  0;
}