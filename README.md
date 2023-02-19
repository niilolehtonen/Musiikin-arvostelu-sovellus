# Musiikin-arvostelu-sovellus(Tietokantasovellus-Harjoitustyö)

Sovellus mahdollistaa musiikin arvostelun internet-selaimessa.

Linkki sovellukseen: https://tsoha-reviewmusic.fly.dev/

## Sovelluksen vaatimusmäärittely:
* Käyttäjä voi luoda uuden tunnuksen sekä kirjautua sisään ja ulos.
* Käyttäjä voi tarkastella muiden käyttäjien antamia arvosteluja kappaleista sekä albumikokonaisuuksista. Käyttäjä voi myös tarkastella yksittäisen artistin sivua, jossa näkyy kaikki kyseisen artistin teosten arvostelut.
* Arvostelusivulla näytetään kaikkien arvostelujen keskiarvo, yksittäiset arvostelut sekä tietoja teoksesta(nimi,genre,julkaisuvuosi).
* Käyttäjä voi etsiä teosta hakusanalla.
* Käyttäjä voi suodattaa teoksia genrejen mukaan.
* Käyttäjä voi luoda uuden arvioitavan teoksen ja antaa sille arvostelun(tähdet ja kommentti), jos sille ei ole vielä luotu yhtäkään arvostelua. Vaihtoehtoisesti käyttäjä voi myös antaa olemassaolevalle teokselle uuden arvostelun.
* Ylläpitäjä voi tarvittaessa lisätä ja poistaa teoksia tai yksittäisiä arvosteluita.


## Välipalautus 2(Notes):
* Sovelluksen käyttöliittymä on hyvässä vaiheessa: Etusivu(sis. kirjautumisen),Rekisteröitymissivu,Valikko
* SQL Skeeman pohja on määritelty
* Kirjautumistoiminto toteutettu, vaikka ei vielä täysin toimivasti
* Valitettavasti en ole saanut yhdistettyä tietokantaan, joten sisäänkirjautuminen ei käytännössä vielä toimi.En tiedä syytä, aion huomenna 6.2 osallistua ohjaukseen ja kysyä neuvoa asiaan. Saattaa johtua siitä, että käytän MacBookia fuksiläppärin sijasta. (Postgres.app kuitenkin asennettu ja näyttäisi toimivan)
* Ensimmäinen committini GitHubiin oli aivan liian suuri, committasin kerralla monen päivän koodaustyön. Jatkossa pyrin tekemään committeja mahdollisimman usein.

## Välipalautus 3(Notes):

* Sovelluksen toiminta tällä hetkellä:
  - Käyttäjä voi luoda käyttäjätunnuksen, kirjautua sisään sekä kirjautua ulos
  - Käyttäjä voi lisätä 'releases' sivulle julkaisun tai tarkastella muita julkaisuja
  - Julkaisun lisäämisen yhteydessä jokaiselle julkaisulle luodaan oma dynaaminen 'reviews' välilehti. 'Reviews' välilehdellä useat käyttäjät voivat käydä arvostelemassa julkaisun sekä tarkastella muiden arvosteluja. Arvostelujen keskiarvo näkyy 'releases' välilehdellä jokaisen julkaisun kohdalla.
  - Jos käyttäjä ei ole sisäänkirjautuneena, käyttäjän on mahdollista tarkastella sivustolle lisättyjä julkaisuja ja arvosteluja, mutta ei pysty lisäämään omia julkaisuja tai arvosteluja.
  
* Sovelluksen edistyminen viimeisen kahden viikon aikana:
  - Käyttöliittymä luotu toimivammaksi 'layout.html'-tiedostolla, jota laajennetaan Jinja-kirjaston avulla.
  - Toteutettu 'releases' sivulle lista julkaisuista jotka haetaan tietokannasta, sekä 'add release' toiminnallisuus. Toteutettu dynaamiset 'reviews' välilehdet, joihin lista arvosteluista sekä 'add review' toiminnalisuus.
  - SQL-skeemaa muutettu rakenteeseen 'users, artists, releases, reviews'
  - Sovellus tuotannossa fly.io:n serverillä

* Paranneltavaa:
  - 'Artists' välilehden tulee näyttää lukumäärä artistin julkaisuista sekä kaikkien julkaisujen keskiarvo. (Tällä hetkellä sivu näyttää ainoastaan tyhjän listan)
  - Toiminnalisuuden varmistaminen ja virheiden minimointi
  - Tietoturvan parantaminen (CSRF-token yms.)
  - Jos aikaa jää tarpeeksi, luodaan hakutoiminto 'releases' sivulle sekä admin käyttäjätyyppi, jonka on mahdollista poistaa julkasuja tai arvosteluja.
 
* __Yhteenveto: Sovellus on hyvässä vaiheessa, mutta vaatii vielä hienosäätöä.__

## Sovelluksen käynnistysohjeet lokaalisti:

- Lataa sovelluksen lähdekoodi GitHubista, asenna PostgreSQL sekä luo virtuaaliympäristö:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

- Tämän jälkeen viedään SQL-skeema tietokantaan:

```bash
psql < schema.sql
```

- Luo .env tiedosto ja määrittele 'database_url' osoite sekä luo henkilökohtainen salainen avain:

```bash
DATABASE_URL=postgresql://
SECRET_KEY=yoursecretkeyhere
```

- Sovellus aukeaa nyt suorittamalla komennon:

```bash
flask run
```
