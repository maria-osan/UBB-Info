#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#include "repository.h"

void run()
{
    Repo r;
    Disciplina d = { "1234", "sdf", "2", "curs", "dfg" };
    r.store(d);
    r.modify(d, "sdg", '1');
    r.del(d);
}

int main()
{
    run();

    return  0;
}