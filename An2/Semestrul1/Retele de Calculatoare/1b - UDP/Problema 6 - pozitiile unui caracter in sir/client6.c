6. Un client trimite unui server un sir de caractere si un caracter. Serverul va returna clientului toate pozitiile pe care caracterul primit se regaseste in sir.

#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>

int main() {
  int c;
  struct sockaddr_in server;
  int nr_poz, poz[100];
  char sir[100], chr;

  c = socket(AF_INET, SOCK_DGRAM, 0);
  if (c < 0) {
    printf("Eroare la crearea socketului client\n");
    return 1;
  }

  memset(&server, 0, sizeof(server));
  server.sin_port = htons(1234);
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = inet_addr("127.0.0.1");


  int l = sizeof(server);
  //while(1) {
          printf("Introduceti un sir de caractere: ");
          fgets(sir, sizeof(sir), stdin);
          printf("Introduceti caracterul cautat: ");
          scanf("%c", &chr);

          sendto(c, &sir, sizeof(sir), 0, (struct sockaddr *) &server, sizeof(server));
          sendto(c, &chr, sizeof(chr), 0, (struct sockaddr *) &server, sizeof(server));

          recvfrom(c, &nr_poz, sizeof(nr_poz), 0, (struct sockaddr *) &server, &l);
          for(int i=0; i<nr_poz; i++)
                  recvfrom(c, &poz[i], sizeof(poz[i]), 0, (struct sockaddr *) &server, &l);

          printf("Caracterul %c apare in sir pe pozitiile: \n", chr);
          for(int i=0; i<nr_poz; i++)
                  printf("%d ", poz[i]);
          printf("\n");
  //}

  close(c);
}