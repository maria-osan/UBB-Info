6. Un client trimite unui server un sir de caractere si un caracter. Serverul va returna clientului toate pozitiile pe care caracterul primit se regaseste in sir.

#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>

int main() {
  int s;
  struct sockaddr_in server, client;
  int c, l, i;

  s = socket(AF_INET, SOCK_DGRAM, 0);
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

  l = sizeof(client);
  memset(&client, 0, sizeof(client));

  while(1) {
          printf("Waiting for clients...\n");
          l = sizeof(client);

          char sir[100], chr;
          recvfrom(s, &sir, sizeof(sir), 0, (struct sockaddr *) &client, &l);
          recvfrom(s, &chr, sizeof(chr), 0, (struct sockaddr *) &client, &l);

          printf("S-a conectat un client\n");

          int poz[100], nr_poz = 0;
          for(int i=0; sir[i] != '\0'; i++)
                  if(sir[i] == chr)
                          poz[nr_poz++] = i;

          sendto(s, &nr_poz, sizeof(nr_poz), 0, (struct sockaddr *) &client, l);
          for(int i=0; i<nr_poz; i++)
                  sendto(s, &poz[i], sizeof(poz[i]), 0,  (struct sockaddr *) &client, l);
  }

  close(s);
}