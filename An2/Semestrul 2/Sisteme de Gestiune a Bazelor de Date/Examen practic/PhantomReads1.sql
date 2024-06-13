USE S13

BEGIN TRAN
WAITFOR DELAY '00:00:10'
INSERT INTO TipuriTablouri (Tip, Descriere, MrMediuTablouri)
VALUES ('tablouri cu peisaje', 'rasarit de soare pe plaja', 50)
COMMIT TRAN