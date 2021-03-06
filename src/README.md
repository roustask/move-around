## Clone project
```bash
git clone https://github.com/Elite-Build-Team/move-around.git
```

## Install prerequisites

You should have `python3` and `pip` and `virtualenv3` installed and available in your PATH (replace with `python` and `virtualenv` accordingly if python version 3 is your default version). Then execute the following:

```bash
cd move-around/src
virtualenv3 .
source bin/activate
pip3 install -r requirements.txt
```

## Run
```bash
python3 ui.py
```
* Στο Report Issue, ο χρήστης καλείται να επιλέξει τοποθεσία στον χάρτη με δεξί κλικ και να πατήσει υποβολή. 
* Ύστερα, πρέπει να επιλέξει φωτογραφία από τη συλλογή του και να δώσει μια περιγραφή.
* Μετά απο την αναφορά του προβλήματος, το νέο εμπόδιο θα εμφανίζεται στον χάρτη πρόσβασης, όπου ο χρήστης μπορεί να επιλέξει φίλτρο και να το δει.

## Demo
![](screenshots/move-around-demo.gif)

## Screenshots

### Κύρια οθόνη
![](screenshots/main-screen.png)

### Χάρτης Πρόσβασης
#### Οθόνη 1
![](screenshots/access-map-screen.png)

#### Οθόνη 2
![](screenshots/do-you-want-to-report-issue.png)

### Αναφορά προβλήματος
#### Οθόνη 1
![](screenshots/choose-location-screen.png)

#### Οθόνη 2
![](screenshots/choose-photograph-screen.png)

#### Οθόνη 3
![](screenshots/issue-description-screen.png)
