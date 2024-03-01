6. Un client trimite unui server un sir de caractere si un caracter. Serverul va returna clientului toate pozitiile pe care caracterul primit se regaseste in sir.

#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>

int main() {
    int c;
    struct sockaddr_in server;
    char sir[100];
    char caracter;
    int pozitii[100];
    int numar_pozitii;

    c = socket(AF_INET, SOCK_STREAM, 0);
    if (c < 0) {
        printf("Eroare la crearea socketului client\n");
        return 1;
    }

    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1234);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (connect(c, (struct sockaddr *) &server, sizeof(server)) < 0) {
        printf("Eroare la conectarea la server\n");
        return 1;
    }

    printf("Introduceti un sir: ");
    fgets(sir, sizeof(sir), stdin);
    //scanf("%s", sir);

    printf("Introduceti un caracter: ");
    scanf(" %c", &caracter);

    send(c, sir, sizeof(sir), 0);
    send(c, &caracter, sizeof(caracter), 0);

    recv(c, &numar_pozitii, sizeof(numar_pozitii), 0);
    recv(c, pozitii, sizeof(int) * numar_pozitii, 0);

    printf("Pozitiile caracterului '%c' in sir: ", caracter);
    for (int i = 0; i < numar_pozitii; i++) {
        printf("%d ", pozitii[i]);
    }
    printf("\n");

    close(c);
}