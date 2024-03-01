1. Un client trimite unui server un sir de numere. Serverul va returna clientului suma numerelor primite.

#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>

int main() {
    int c;
    struct sockaddr_in server;
    uint16_t numere[100];
    int numar_numere;

    c = socket(AF_INET, SOCK_STREAM, 0);
    if (c < 0) {
        printf("Eroare la crearea socketului client\n");
        return 1;
    }

    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1235);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (connect(c, (struct sockaddr *) &server, sizeof(server)) < 0) {
        printf("Eroare la conectarea la server\n");
        return 1;
    }

    printf("Introduceti numarul de numere pe care doriti sa le trimiteti: ");
    scanf("%d", &numar_numere);

    numar_numere = htons(numar_numere);
    send(c, &numar_numere, sizeof(numar_numere), 0);

    for (int i = 0; i < ntohs(numar_numere); i++) {
        printf("Introduceti numarul %d: ", i + 1);
        scanf("%hu", &numere[i]);
        numere[i] = htons(numere[i]);
        send(c, &numere[i], sizeof(numere[i]), 0);
    }

    uint16_t suma;
    recv(c, &suma, sizeof(suma), 0);
    suma = ntohs(suma);
    printf("Suma numerelor este: %hu\n", suma);

    close(c);
}