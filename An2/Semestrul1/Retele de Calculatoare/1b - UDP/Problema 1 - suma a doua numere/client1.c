1. Un client trimite unui server un sir de numere. Serverul va returna clientului suma numerelor primite.

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
  int nr1, nr2, sum;

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

  printf("Introduceti 2 numere: ");
  scanf("%d %d", &nr1, &nr2);
  nr1 = htons(nr1);
  nr2 = htons(nr2);

  sendto(c, &nr1, sizeof(nr1), 0, (struct sockaddr *) &server, sizeof(server));
  sendto(c, &nr2, sizeof(nr2), 0, (struct sockaddr *) &server, sizeof(server));

  recvfrom(c, &sum, sizeof(sum), 0, (struct sockaddr *) &server, &l);

  sum = ntohs(sum);
  printf("Suma este: %d\n", sum);

  close(c);
}