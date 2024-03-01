6. Un client trimite unui server un sir de caractere si un caracter. Serverul va returna clientului toate pozitiile pe care caracterul primit se regaseste in sir.

#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>

void deservire_client(int c) {
        char sir[100];
        char caracter;
        int pozitii[100];
        int numar_pozitii = 0;

        // Deservirea clientului
        recv(c, sir, sizeof(sir), MSG_WAITALL);
        recv(c, &caracter, sizeof(caracter), MSG_WAITALL);

        // Găsirea pozițiilor caracterului în șir
        for (int i = 0; sir[i] != '\0'; i++) {
            if (sir[i] == caracter) {
                pozitii[numar_pozitii] = i;
                numar_pozitii++;
            }
        }

        // Trimiterea pozițiilor către client
        send(c, &numar_pozitii, sizeof(numar_pozitii), 0);
        send(c, pozitii, sizeof(int) * numar_pozitii, 0);

        close(c);
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
    server.sin_port = htons(1234);
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
        c = accept(s, (struct sockaddr *) &client, &l);
        printf("S-a conectat un client.\n");

        if(fork() == 0) {
                deservire_client(c);
                return 0;
        }
    }
}