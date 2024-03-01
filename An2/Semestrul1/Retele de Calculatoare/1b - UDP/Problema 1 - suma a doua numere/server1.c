1. Un client trimite unui server un sir de numere. Serverul va returna clientului suma numerelor primite.

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

          int nr1, nr2;
          recvfrom(s, &nr1, sizeof(nr1), 0, (struct sockaddr *) &client, &l);
          recvfrom(s, &nr2, sizeof(nr2), 0, (struct sockaddr *) &client, &l);

          nr1= ntohs(nr1);
          nr2 = ntohs(nr2);
          printf("S-a conectat un client\n");

          int sum = nr1 + nr2;
          sum = htons(sum);
          sendto(s, &sum, sizeof(sum), 0, (struct sockaddr *) &client, l);
  }

  close(s);
}