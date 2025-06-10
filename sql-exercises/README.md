# SQL Exercises - Core Features

## Exercise 1

    Write a SQL query to select the sex and body mass
    columns from the little_penguins in that order,
    sorted such that the largest body mass appears first.

    select
            sex,
            body_mass_g
    from little_penguins
    order by body_mass_g desc;

**Zrzut ekranu:**
![Exercise 1](./screenshots/Exercise1.png)

## Exercise 2

1.    Write a SQL query to select the islands and species from rows 50 to 60
    inclusive of the penguins table. Your result should have 11 rows.

    select
            island,
            species
    from penguins
    order by island, species
    limit 10 offset 50;


    Modify your query to select distinct combinations of island and species
    from the same rows and compare the result to what you got in part 1.

    select distinct
            island,
            species
    from penguins
    order by island, species;

**Zrzut ekranu:**
![Exercise 2](./screenshots/Exercise2.png)

## Exercise 3
    Write a query to select the body masses from penguins that are less
    than 3000.0 grams.

    select
            body_mass_g
    from penguins
    where body_mass_g < 3000


    Write another query to select the species and sex of penguins that
    weight less than 3000.0 grams. This shows that the columns displayed
    and those used in filtering are independent of each other.

    select
            species,
            sex
    from penguins
    where body_mass_g < 3000;

**Zrzut ekranu:**
![Exercise 3](./screenshots/Exercise3.png)


## Exercise 4
Exercise

    Use the not operator to select penguins that are not Gentoos.

    select
        species
    from penguins
    where species != 'Gentoos';

    SQL's or is an inclusive or: it succeeds if either or both conditions
    are true. SQL does not provide a specific operator for exclusive
    or, which is true if either but not both conditions are true, but the
    same effect can be achieved using and, or, and not. Write a query to
    select penguins that are female or on Torgersen Island but not both.

    select
        species,
        sex,
        island
    from penguins
    where (sex = 'FEMALE' and island != 'Torgersen') or (sex != 'FEMALE' and island = 'Torgersen');

**Zrzut ekranu:**
![Exercise 4](./screenshots/Exercise4.png)

## Exercise 5
**Treść zadania:**  
Write another query to select the species and sex of penguins that weight less than 3000.0 grams. This shows that the columns displayed and those used in filtering are independent of each other.

Napisz kolejne zapytanie, które wybiera gatunek (species) i płeć (sex) pingwinów ważących mniej niż 3000.0 gramów.
**Zapytanie SQL:**
```sql

SELECT species, sex
FROM penguins
WHERE body_mass_g < 3000.0;
```

**Zrzut ekranu:**
![Exercise 5](./screenshots/Exercise5.png)

## Exercise 6
**Treść zadania:**  
Use the not operator to select penguins that are not Gentoos.

Użyj operatora not, aby wybrać pingwiny inne niż Gentoo.
**Zapytanie SQL:**
```sql

SELECT * 
FROM penguins 
WHERE species != "Gentoo";
```

**Zrzut ekranu:**
![Exercise 6](./screenshots/Exercise6.png)

## Exercise 7
**Treść zadania:**  
SQL's or is an inclusive or: it succeeds if either or both conditions are true. SQL does not provide a specific operator for exclusive or, which is true if either but not both conditions are true, but the same effect can be achieved using and, or, and not. Write a query to select penguins that are female or on Torgersen Island but not both.

W SQL operator OR oznacza alternatywę łączną: zwraca wynik, jeśli jedno lub oba warunki są spełnione.
SQL nie ma operatora dla alternatywy rozłącznej (XOR), która jest prawdziwa, gdy tylko jeden z warunków jest spełniony (ale nie oba).
Można to jednak osiągnąć, używając AND, OR i NOT.
Napisz zapytanie, które wybierze pingwiny, które są samicami LUB znajdują się na wyspie Torgersen, ale NIE spełniają obu tych warunków jednocześnie.
**Zapytanie SQL:**
```sql

SELECT * 
FROM penguins 
WHERE (island="Torgersen" 
AND sex !="FEMALE") 
OR (island!="Torgersen" 
AND sex="FEMALE");
```

**Zrzut ekranu:**
![Exercise 7](./screenshots/Exercise7.png)

## Exercise 8
**Treść zadania:**  
Write a single query that calculates and returns:
A column called what_where that has the species and island of each penguin separated by a single space.
A column called bill_ratio that has the ratio of bill length to bill depth.

Napisz jedno zapytanie SQL, które oblicza i zwraca:
Kolumnę o nazwie what_where, która zawiera gatunek i wyspę każdego pingwina, oddzielone pojedynczą spacją.
Kolumnę o nazwie bill_ratio, która zawiera stosunek długości dzioba do jego głębokości.
**Zapytanie SQL:**
```sql

SELECT 
  species || ' ' || island AS what_where,
  bill_length_mm / bill_depth_mm AS bill_ratio
FROM penguins;
```

**Zrzut ekranu:**
![Exercise 8](./screenshots/Exercise 8.png)

## Exercise 9
**Treść zadania:**  
Use SQLite's .nullvalue command to change the printed representation of null to the string null and then re-run the previous query. When will displaying null as null be easier to understand? When might it be misleading?


**Zapytanie SQL:**
```sql

.nullvalue null
SELECT species || ' ' || 
island ,bill_length_mm / bill_depth_mm as bill_ratio 
FROM penguins;
```

**Zrzut ekranu:**
![Exercise 9](./screenshots/Exercise 9.png)

## exercise-10
**Treść zadania:**  
Write a query to find penguins whose body mass is known but whose sex is not.

Napisz zapytanie SQL, które wybiera pingwiny, których masa ciała jest znana, ale płeć jest nieznana (czyli sex IS NULL):

**Zapytanie SQL:**
```sql

SELECT *
FROM penguins
WHERE body_mass_g IS NOT NULL
  AND sex IS NULL;
```

**Zrzut ekranu:**
![exercise-10](./screenshots/exercise-10.png)

## exercise-11
**Treść zadania:**  
Write another query to find penguins whose sex is known but whose body mass is not.

Napisz kolejne zapytanie, aby znaleźć pingwiny, których płeć jest znana, ale masa ciała nie jest znana.

**Zapytanie SQL:**
```sql

SELECT *
FROM penguins
WHERE body_mass_g IS NULL
  AND sex IS NOT NULL;
```

**Zrzut ekranu:**
![exercise-11](./screenshots/exercise-11.png)



## exercise-12
**Treść zadania:**  
What is the average body mass of penguins that weight more than 3000.0 grams?

Jaka jest średnia masa ciała pingwinów ważących ponad 3000,0 gramów?
**Zapytanie SQL:**
```sql

SELECT AVG(body_mass_g) 
as average_body_mass
FROM 
(SELECT body_mass_g FROM penguins 
WHERE body_mass_g > 3000);
```

**Zrzut ekranu:**
![exercise-12](./screenshots/exercise-12.png)

## exercise-13
**Treść zadania:**  
How many different body masses are in the penguins dataset?

Ile różnych mas ciała znajduje się w zbiorze danych dotyczącym pingwinów?
**Zapytanie SQL:**
```sql

SELECT COUNT(DISTINCT body_mass_g) AS unique_body_masses
FROM penguins;
```

**Zrzut ekranu:**
![exercise-13](./screenshots/exercise-13.png)

## exercise-14
**Treść zadania:**  
Write a query that shows each distinct body mass in the penguin dataset and the number of penguins that weigh that much.

Napisz zapytanie, które wyświetli każdą odrębną masę ciała w zbiorze danych dotyczących pingwinów i liczbę pingwinów, które ważą tyle samo
**Zapytanie SQL:**
```sql

SELECT body_mass_g, COUNT(*) AS count
FROM penguins
WHERE body_mass_g IS NOT NULL
GROUP BY body_mass_g
ORDER BY body_mass_g;
```

**Zrzut ekranu:**
![exercise-14](./screenshots/exercise-14.png)

## exercise-15
**Treść zadania:**  
Write a query that uses filter to calculate the average body masses of heavy penguins (those over 4500 grams) and light penguins (those under 3500 grams) simultaneously. Is it possible to do this using where instead of filter?

Napisz zapytanie, które używa filtra do obliczenia średniej masy ciała ciężkich pingwinów (tych powyżej 4500 gramów) i lekkich pingwinów (tych poniżej 3500 gramów) jednocześnie. Czy można to zrobić używając where zamiast filtra?
**Zapytanie SQL:**
```sql

SELECT 
  AVG(CASE WHEN body_mass_g > 4500 THEN body_mass_g ELSE NULL END) AS avg_heavy,
  AVG(CASE WHEN body_mass_g < 3500 THEN body_mass_g ELSE NULL END) AS avg_light
FROM penguins;
```

**Zrzut ekranu:**
![exercise-15](./screenshots/exercise-15.png)


## exercise-16
**Treść zadania:**  
Using an in-memory database, define a table called notes with two text columns author and note and then add three or four rows. Use a query to check that the notes have been stored and that you can (for example) select by author name.

Używając bazy danych w pamięci, zdefiniuj tabelę o nazwie notatki z dwiema kolumnami tekstowymi autor i notatka, a następnie dodaj trzy lub cztery wiersze. Użyj zapytania, aby sprawdzić, czy notatki zostały zapisane i czy możesz (na przykład) wybrać według nazwiska autora.
**Zapytanie SQL:**
```sql


CREATE TABLE notes (
  author TEXT,
  note TEXT
);

INSERT INTO notes (author, note)
VALUES 
  ('Ala', 'Kup mleko'),
  ('Ola', 'Notatka'),
  ('Jan', '<3');

SELECT * FROM notes;

```

**Zrzut ekranu:**
![exercise-16](./screenshots/exercise-16.png)

## exercise-17
**Treść zadania:**  
What happens if you try to delete rows that don't exist (e.g., all entries in work that refer to juna)?

Co się stanie, jeśli spróbujesz usunąć wiersze, które nie istnieją (np. wszystkie wpisy w pracy odnoszące się do juna)?


**Zapytanie SQL:**
```sql

DELETE FROM notes WHERE author = 'juna';

```

**Zrzut ekranu:**
![exercise-17](./screenshots/exercise-17.png)

## exercise-18
**Treść zadania:**  
Re-create the notes table in an in-memory database and then use SQLite's .output and .dump commands to save the database to a file called notes.sql. Inspect the contents of this file: how has your data been stored?


Utwórz ponownie tabelę notatek w bazie danych w pamięci, a następnie użyj poleceń .output i .dump SQLite, aby zapisać bazę danych w pliku o nazwie notes.sql. Sprawdź zawartość tego pliku: w jaki sposób Twoje dane zostały zapisane?
**Zapytanie SQL:**
```sql

sqlite> .output notes.sql
sqlite> .dump
sqlite> .output stdout

```

**Zrzut ekranu:**
![exercise-18](./screenshots/exercise-18.png)

## exercise-19
**Treść zadania:**  
Start a fresh SQLite session and load notes.sql using the .read command. Inspect the database using .schema and select *: is everything as you expected?

Rozpocznij nową sesję SQLite i załaduj notes.sql za pomocą polecenia .read. Przejrzyj bazę danych za pomocą .schema i wybierz *: czy wszystko jest takie, jak oczekiwałeś?
**Zapytanie SQL:**
```sql

sqlite> .read notes.sql
sqlite> SELECT * FROM notes

```

**Zrzut ekranu:**
![exercise-19](./screenshots/exercise-19.png)

## exercise-20
**Treść zadania:**  
Re-create the notes table in an in-memory database once again and use SQLite's .backup command to save it to a file called notes.db. Inspect this file using od -c notes.db or a text editor that can handle binary data: how has your data been stored?

Utwórz ponownie tabelę notatek w bazie danych w pamięci i użyj polecenia .backup programu SQLite, aby zapisać ją w pliku o nazwie notes.db. Sprawdź ten plik za pomocą polecenia od -c notes.db lub edytora tekstu obsługującego dane binarne: w jaki sposób Twoje dane zostały zapisane?
**Zapytanie SQL:**
```sql

sqlite> .backup notes.db

```

**Zrzut ekranu:**
![exercise-20](./screenshots/exercise-20.png)

## exercise-21
**Treść zadania:**  
Start a fresh SQLite session and load notes.db using the .restore command. Inspect the database using .schema and select *: is everything as you expected?

Rozpocznij nową sesję SQLite i załaduj notes.db za pomocą polecenia .restore. Przejrzyj bazę danych za pomocą .schema i wybierz *: czy wszystko jest takie, jak oczekiwałeś?
**Zapytanie SQL:**
```sql

.restore notes.db

```

**Zrzut ekranu:**
![exercise-21](./screenshots/exercise-21.png)

## exercise-22
**Treść zadania:**  
Re-run the query shown above using where job = name instead of the full table.name notation. Is the shortened form easier or harder to read and more or less likely to cause errors?

Uruchom ponownie zapytanie pokazane powyżej, używając where job = name zamiast pełnej notacji table.name. Czy skrócona forma jest łatwiejsza czy trudniejsza do odczytania i bardziej lub mniej prawdopodobne, że spowoduje błędy?

**Zapytanie SQL:**
```sql

select *
from work, job
where work.job = job.name

```

**Zrzut ekranu:**
![exercise-22](./screenshots/exercise-22.png)

## exercise-23
**Treść zadania:**  
Find the least time each person spent on any job. Your output should show that mik and po each spent 0.5 hours on some job. Can you find a way to show the name of the job as well using the SQL you have seen so far?

Znajdź najkrótszy czas, jaki każda osoba spędziła na dowolnym zadaniu. Twój wynik powinien pokazywać, że mik i po spędzili po 0,5 godziny na jakimś zadaniu. Czy możesz znaleźć sposób, aby pokazać nazwę zadania, używając do tej pory SQL, który widziałeś?

**Zapytanie SQL:**
```sql

select work.person, MIN(job.billable), job.name
from work join job on work.job = job.name
group by work.person

```

**Zrzut ekranu:**
![exercise-23](./screenshots/exercise-23.png)