USE S13

SELECT Denumire, TipMuzeu, NrExponate FROM Muzee
ORDER BY NrExponate;

CREATE INDEX IndexMuzee ON Muzee(Denumire, TipMuzeu, NrExponate);
DROP INDEX IndexMuzee ON Muzee;