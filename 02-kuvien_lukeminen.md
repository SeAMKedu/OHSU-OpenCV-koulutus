# Kuvien lukeminen

Jotta OpenCV:tä voi hyödyntää, täytyy olla jokin kuva, johon sen menetelmiä voi käyttää. Kuvana voidaan käyttää kuvatiedostoa, videotiedostoa, webkameran tai jonkin muun tietokoneeseen yhdistetyn kameran livekuvaa tai vaikkapa kännykkäkameran livekuvaa REST-rajapinnan kautta.

Aivan ensimmäiseksi OpenCV-moduuli täytyy ottaa käyttöön seuraavalla `import`-komennolla:

    import cv2

Tämän jälkeen OpenCV:n funktioita voi kutsua kirjoittamalla `cv2.funktion_nimi`

## Kuvatiedostot

Tietokoneelle tallennetut kuvatiedosto saadaan avattua komennolla `imread`. Ensimmäiseksi parametriksi annetaan kuvan polku. Se voi olla absoluuttinen (eli esim "C:\Users\kayttaja1\Pictures\Osat\osa1.jpg") tai suhteellinen: jos suoritettava Python-tiedosto on samassa kansiossa kuin kuva, riittää pelkkä kuvan nimi, jos taas Python-tiedosto on samassa kansiossa kuin kuvat sisältävä kansio, riittää "Osat/osa1.jpg". Toinen parametri kertoo yleensä, ladataanko kuva värillisenä vai harmaasävynä (vaihtoehtoja on useampiakin, mutta yleensä nämä kaksi riittävät). Oletuksena kuva avataan värillisenä eli siinä on kolme kerrosta. Jos kuva on harmaasävykuva, siinä on vain kolme identtistä kerrosta B-, G- ja R-kerroksina. Seuraavat komennot tekevät siis saman asian:

    kuva = cv2.imread("Osat/osa1.jpg")

    TAI

    kuva = cv2.imread("Osat/osa1.jpg", cv2.IMREAD_COLOR)

Jos kuva halutaan avata harmaasävynä, komento on taas

    kuva = cv2.imread("Osat/osa1.jpg", cv2.IMREAD_GRAYSCALE)

    TAI

    kuva = cv2.imread("Osat/osa1.jpg", 0)

Nyt muuttuja `kuva` sisältää kuvatiedoston informaation Numpy-taulukkona, kuten johdannossa selvitettiin. Jos kuvan avaaminen ei onnistunut (esim. kuvapolku annettiin väärin), muuttujan kuva arvoksi tulee `None`.

Jos kuva on jossain muussa kansiossa tietokoneella, ja sen absoluuttisen polun kopioi suoraan Windowsin resurssienhallinnasta, täytyy tiedostopolkua edeltävän lainausmerkin eteen laittaa r-kirjain ilmaisemaan, että käytetään ns. r-merkkijonoa (raw string). Pythonissa nimittäin kenoviiva \ tavallisen merkkijonon sisällä aloittaa erikoismerkin (esim. \n tarkoittaa rivinvaihtoa).

    kuva = cv2.imread(r"C:\Users\Juha\Documents\Kuvat\Osat\osa1.jpg")

Kuva näytetään komennolla `imshow`. Ensin annetaan nimi ikkunalle, jossa kuva näytetään, ja sitten kerrotaan näytettävä kuvataulukko. Avattu ikkuna katoaa saman tien. Jotta se näkyisi kauemman, pitää sen jälkeen antaa odotuskäsky `waitKey`, joka jää odottamaan näppäimen painallusta käyttäjältä. Käskyn parametrina kerrotaan, montako millisekuntia odotetaan. Nolla tarkoittaa, että odotetaan niin kauan, kunnes näppäimen painallus tulee.   

    cv2.imshow("Avattu kuva", kuva)
    cv2.waitKey(0)

Kuva voidaan tallentaa komennolla `imwrite`. Ensin annetaan polku ja tiedostonimi, johon kuva talletetaan, sitten talletettava kuvataulukko.

    cv2.imwrite("uusi_kuva.jpg", kuva)

## Videot ja webkamera

Videoita ja webkameraa varten on luokka `VideoCapture`, jonka metodien avulla videolta tai webkameralta saadaan luettua yksittäisiä ruutuja. Ensin luodaan video-olio tällä komennolla antamalla parametriksi videon polku: 
    
    cap = cv2.VideoCapture("video.mp4") 

Tämän jälkeen kuvia voidaan lukea olion `read`-metodilla while-silmukassa. Olion `isOpened`-metodi tarkoittaa tässä tapauksessa, että videota luetaan niin kauan kuin siitä löytyy uusia ruutuja. Nyt `waitKey`-funktiolla määritellään, että yksittäistä ruutua näytetään 40 ms. Ruutujen näyttäminen loppuu (while-silmukka katkeaa), jos käyttäjä painaa q-näppäintä ajon aikana.

    while cap.isOpened():
        ret, frame = cap.read() 
        if ret == False:
            break
        else:  
            cv2.imshow('Frame', frame) 
            
        # Näppäimen q painallus lopettaa 
            if cv2.waitKey(40) & 0xFF == ord('q'): 
                break

Webkameraa käytetään aivan vastaavasti, paitsi nyt video-oliota luotaessa annetaan parametriksi kameran numero videotiedoston sijaan. Jos tietokoneeseen on liitetty vain yksi webkamera, sen numero on 0. Toisen kameran numero on 1 jne.

    cap = cv2.VideoCapture(0) 

## Muut kamerat

Erilaisia konenäössä käytettyjä kameroita liitetään tietokoneeseen yleensä Ethernetin, USB-liitännän tai erityisen liitäntästandardin kuten CameraLink kautta. Kameravalmistajat tarjoavat yleensä kameransa mukana ohjelmointirajapinnan, jonka avulla tietokoneeseen liitettyä kameraa voi komentaa ohjelmallisesti. Basler-merkkisten kameroiden ohjelmointirajapinta on [Pylon](https://www.baslerweb.com/en/software/pylon/), ja siihen on saatavissa [pypylon](https://pypi.org/project/pypylon/1.5.4/)-niminen Python-kääreluokka (wrapper). Kääreluokan avulla ohjelmointirajapinnan funktioita voidaan käyttää Python-kielellä. AVT:n valmistamien kameroiden ohjelmointirajapinta on taas [Vimba](https://www.alliedvision.com/en/products/software/) ja sen Python-kääreluokka [Pymba](https://pypi.org/project/pymba/). 

Ensin tietokoneelle pitää siis asentaa kameravalmistajan tarjoama ohjelmointirajapinta ja sen jälkeen tälle tarjottu kääreluokka. Käyttö on samantyylistä kuin webkameran tapauksessa: ensin pitää luoda kameraolio, jonka metodeilla saadaan säädettyä kameran parametreja, käynnistettyä kuvaamisen ja luettua kuvia kameralta. Pypylonin ja Pymban sivuilla on esimerkkiskriptit niiden käyttämisestä.

Kameravalmistajien omien ohjelmointirajapintojen lisäksi on olemassa geneerinen kameroiden ohjelmointirajapinta GenICam. Sen pitäisi toimia useimpien valmistajien kameroiden kanssa. Pythonilla GenICam-rajapinnan käyttäminen onnistuu moduulin [Harvester](https://github.com/genicam/harvesters) avulla. Lisäksi Harvester tarvitsee kameran kanssa kommunikointiin ns. GenTL-tuottajan. Helpointa on käyttää kameravalmistajan tarjoamaa tuottajaa. Niistä lisää [täällä](https://pypi.org/project/harvesters-util/#gentl-producers). Nyt siis tarvitaan jonkin kameravalmistajan GenTL-tuottaja (osa niistä toimii muidenkin valmistajien kameroissa) ja Harvester-moduuli.

## Kännykkäkameran käyttö livekamerana

Kännykkäkameraa voi käyttää livekamerana hyödyntämällä sovellusta, joka lähettää kuvia verkon yli hyödyntäen REST-rajapintaa. Tällöin puhelimen ja tietokoneen täytyy olla samassa verkossa. Googlen Play-kaupassa on saatavilla esimerkiksi [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en) -niminen sovellus.

Tällaista sovellusta käyttäessä pitää ensin ohjelmassa määritellä kameran url puhelimen ip-osoitteen avulla. Sitten hyödynnetään Pythonin requests-kirjastoa (asennus komennolla `pip install requests`) yhteydenottoon kyseiseen urliin. Kuva luetaan tavumuodossa, ja se pitää dekoodata OpenCV:n `decode`-komennolla. Alla esimerkki:

    import numpy as np
    import requests

    url = "http://192.168.___.___:8080//shot.jpg"

    while True:
        kuva_resp = requests.get(url)
        kuva_bytearr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        kuva = cv2.imdecode(img_arr, -1)

## Tehtäviä

1. Selvitä, miten voit lukea for-silmukassa kansiollisen kuvia. Käytä siis esim. logiikkaa `for tiedostonimi in kansion_nimi: imread(tiedostonimi)`. Voit käyttää ainakin funktiota [listdir](https://www.tutorialspoint.com/python/os_listdir.htm) tai funktiota [glob](https://docs.python.org/3/library/glob.html).
2. Tee ohjelma, joka lukee videotiedostoa, ja tallettaa joka 100:n kuvan kansioon omana jpg-tiedostonaan.
3. Tee ohjelma, joka lukee kuvia tietokoneen webkamerasta ja tallettaa kuvan kahden sekunnin välein.
4. Kokeile kännykkäkamerasi käyttöä livekameralla viimeisen ohjeen mukaisesti. 

### Kurssin rakenne
**[Johdanto](01-johdanto.md) | Kuvien lukeminen | [Laskutoimitukset](03-laskutoimitukset.md) | [Harmaasävykuva](04-harmaasavykuva.md) | [Värit](05-varit.md) | [Esi- ja jälkikäsittely](06-esi_ja_jalkikasittely.md) | [Hough-muunnokset](07-hough.md)**