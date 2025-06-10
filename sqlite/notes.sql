PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE notes (
    author text,
    note text
);
INSERT INTO notes VALUES('Jozef','Narod wspanialy, tylko ludzie kurwy');
INSERT INTO notes VALUES('Jozef','Kto nie byl za mlodu socjalista ten na starosc bedzie skurwysynem');
INSERT INTO notes VALUES('Jozef','Zdanie jest jak dupa, kazdy ma swoja');
COMMIT;
