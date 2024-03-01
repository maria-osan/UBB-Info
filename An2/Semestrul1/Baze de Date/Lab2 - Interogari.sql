-- m-n
-- Extrage numele clienților care au făcut rezervări pentru pachete turistice cu prețuri mai mari decât o anumită valoare.
SELECT C.Nume, C.Prenume
FROM Clienti AS C
INNER JOIN Rezervari AS R ON C.IDClient = R.ClientID
INNER JOIN PacheteTuristice AS PT ON R.PachetID = PT.IDPachetTuristic
WHERE PT.Pret > 1500.00;

-- m-n
-- Extrage numele și prenumele clienților care au scris recenzii pentru anumite pachete turistice cu un anumit rating.
SELECT C.Nume, C.Prenume, RC.TextRecenzie, RC.Rating
FROM Clienti AS C
INNER JOIN RecenziiClienti AS RC ON C.IDClient = RC.ClientID
INNER JOIN PacheteTuristice AS PT ON RC.PachetID = PT.IDPachetTuristic
WHERE RC.Rating >=4;

-- Extrage numele clienților care au efectuat plăți pentru rezervările lor.
SELECT C.Nume, C.Prenume
FROM Clienti AS C
JOIN Rezervari AS R ON C.IDClient = R.ClientID
LEFT JOIN Plati AS P ON R.IDRezervare = P.RezervareID
WHERE P.IDPlata IN (1, 2, 3, 4, 5);

--  Extrage numele și prenumele clienților care au făcut rezervări pentru pachete turistice într-o anumită destinație.
SELECT C.Nume, C.Prenume
FROM Clienti AS C
JOIN Rezervari AS R ON C.IDClient = R.ClientID
JOIN PacheteTuristice AS PT ON R.PachetID = PT.IDPachetTuristic
JOIN Destinatii AS D ON PT.DestinatieID = D.IDDestinatie
WHERE D.NumeDestinatie = 'Atena';

-- Extrage informații despre plățile efectuate într-un anumit interval de timp.
SELECT C.Nume, C.Prenume
FROM Clienti AS C
JOIN Rezervari AS R ON C.IDClient = R.ClientID
JOIN Plati AS P ON R.IDRezervare = P.RezervareID
WHERE P.DataPlata BETWEEN '2023-02-05' AND '2023-06-05';

--Extrage numele pachetelor turistice și numărul total de plăți pentru fiecare pachet turistic.
SELECT PT.NumePachet, COUNT(P.IDPlata) AS NumarPlati
FROM PacheteTuristice AS PT
LEFT JOIN Rezervari AS R ON PT.IDPachetTuristic = R.PachetID
LEFT JOIN Plati AS P ON R.IDRezervare = P.RezervareID
GROUP BY PT.NumePachet

-- Extrage numele destinațiilor și numărul total de camere disponibile în fiecare destinație cu capacitatea mai mare ca o capacitate data.
SELECT D.NumeDestinatie, SUM(CH.Capacitate) AS NumarTotalCamere
FROM Destinatii AS D
LEFT JOIN PacheteTuristice AS PT ON D.IDDestinatie = PT.DestinatieID
LEFT JOIN Hoteluri AS H ON H.PachetID = PT.IDPachetTuristic
LEFT JOIN CamereHotel AS CH ON CH.HotelID = H.IDHotel
GROUP BY D.NumeDestinatie
HAVING SUM(CH.Capacitate) > 1;

-- Extrage numele clienților și suma totală a plăților efectuate de fiecare client care este mai mare decat o suma data.
SELECT C.Nume, C.Prenume, SUM(P.SumaPlata) AS SumaTotalaPlati
FROM Clienti AS C
JOIN Rezervari AS R ON C.IDClient = R.ClientID
JOIN Plati AS P ON R.IDRezervare = P.RezervareID
GROUP BY C.Nume, C.Prenume
HAVING SUM(P.SumaPlata) > 1000.00;

-- Extrage numele destinațiilor pentru care există cel puțin un pachet turistic și un hotel disponibil.
SELECT DISTINCT D.NumeDestinatie
FROM Destinatii AS D
LEFT JOIN PacheteTuristice AS PT ON D.IDDestinatie = PT.DestinatieID
LEFT JOIN Hoteluri AS H ON PT.IDPachetTuristic = H.PachetID;

-- Extrage numele pachetelor turistice și numărul total de recenzii cu rating-uri diferite pentru fiecare pachet turistic.
SELECT PT.NumePachet, COUNT(DISTINCT RC.Rating) AS NumarRatinguriDiferite
FROM PacheteTuristice AS PT
LEFT JOIN RecenziiClienti AS RC ON PT.IDPachetTuristic = RC.PachetID
GROUP BY PT.NumePachet;
