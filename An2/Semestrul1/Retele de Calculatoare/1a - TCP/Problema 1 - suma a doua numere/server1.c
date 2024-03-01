1. Un client trimite unui server un sir de numere. Serverul va returna clientului suma numerelor primite.

#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <stdlib.h>

void deservire_client(int c) {
        uint16_t numere[100];
        int numar_numere = 0;

        // Deservirea clientului
        int numere_primiti;
        recv(c, &numere_primiti, sizeof(numere_primiti), MSG_WAITALL);
        numere_primiti = ntohs(numere_primiti);


        // Primeste numerele
        for (int i = 0; i < numere_primiti; i++) {
            uint16_t numar;
            recv(c, &numar, sizeof(numar), MSG_WAITALL);
            numar = ntohs(numar);
            numere[i] = numar;
            numar_numere++;
        }

        // Calculează suma numerelor
        uint16_t suma = 0;
        for (int i = 0; i < numar_numere; i++) {
            suma += numere[i];
        }
        suma = htons(suma);

        // Trimite suma înapoi la client
        send(c, &suma, sizeof(suma), 0);

        close(c);
        exit(0);
}

int main() {
    int s;
    struct sockaddr_in server, client;
    int c, l;

    s = socket(AF_INET, SOCK_STREAM, 0);
    if (s < 0) {
        printf("Eroare la crearea socketului server\n");
        return 1;
    }

    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1235);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;

    if (bind(s, (struct sockaddr *) &server, sizeof(server)) < 0) {
        printf("Eroare la bind\n");
        return 1;
    }

    listen(s, 5);

    l = sizeof(client);
    memset(&client, 0, sizeof(client));

    while (1) {
        //uint16_t numere[100];
        //int numar_numere = 0;

        c = accept(s, (struct sockaddr *) &client, &l);
        printf("S-a conectat un client.\n");

        if(fork() == 0) {
                deservire_client(c);
                return 0;
        }
        /*// Deservirea clientului
        int numere_primiti;
        recv(c, &numere_primiti, sizeof(numere_primiti), MSG_WAITALL);
        numere_primiti = ntohs(numere_primiti);


        // Primeste numerele
        for (int i = 0; i < numere_primiti; i++) {
            uint16_t numar;
            recv(c, &numar, sizeof(numar), MSG_WAITALL);
            numar = ntohs(numar);
            numere[i] = numar;
            numar_numere++;
        }

        // Calculează suma numerelor
        uint16_t suma = 0;
        for (int i = 0; i < numar_numere; i++) {
            suma += numere[i];
        }
        suma = htons(suma);

        // Trimite suma înapoi la client
        send(c, &suma, sizeof(suma), 0);

        //printf("Suma numerelor primite: %u\n", ntohs(suma));

        close(c);*/
    }
}