#pragma once
#include "service.h"

typedef struct
{
	Service srv;
}Consola;

Consola creazaConsola();

Service get_service(Consola cons);

void start();