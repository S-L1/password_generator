# Password Generator

*- English Version Below -*

### Beschreibung

Dieses Repository enthält den Code für einen Passwort-Generator mit UI. Wenn `PwdGenerator.py` gestartet wird, öffnet sich ein Fenster, in dem einige Parameter für das zu generierende Passwort festgelegt werden können. </br></br>

![Linux-Screenshot](/assets/screenshot.png "Linux Screenshot")

</br>Das Passwort, welches generiert wird, hat mindestens 12 und bis zu 50 Zeichen. Standardmäßig sind die Optionen Großbuchstaben (*"upper case letters"*), Zahlen (*"numbers"*) und Sonderzeichen (*"special characters"*) aktiviert (sicherste Einstellungsmöglichkeit), können aber auch deaktiviert werden, um beispielsweise ein Passwort ohne Sonderzeichen oder Großbuchstaben zu erstellen. Wenn alle drei Optionen deaktiviert sind, wird das Passwort nur aus Kleinbuchstaben erstellt (**am wenigsten sichere Einstellung**). </br></br>
Zusätzlich zu Python, werden auch die Python-Bibliotheken `math`, `PyQt6`, `random` und `string` benötigt, wobei insbesondere die letzten beiden meist bereits mit der Standardinstallation von Python mitkommen.

**Wichtig:** Der Passwort-Generator generiert lediglich das Passwort, speichert es aber nirgends! Sobald das Ergebnisfenster geschlossen wurde, kann das gleiche Passwort nicht noch einmal aufgerufen, sondern nur ein neues erstellt werden.

Diese Arbeit unterliegt den Bestimmungen einer MIT-Lizenz.<br/>
© 2023 Sandra Liedtke.


## English Version

### Description

This repository contains the code for a password generator. When `PwdGenerator.py` is being started, a window opens where some parameters for the password to be generated can be specified. </br></br>

![Linux-Screenshot](/assets/screenshot.png "Linux Screenshot")

</br>The generated password has at least 12 and up to 50 characters. By default, the options *"upper case letters"*, *"numbers"* and *"special characters"* are activated (most secure setup), but may be deactivated to be able to generate a password without upper case letters, numbers or special characters. If all three options are deactivated, the password is created only from lower case letters (**least secure option**). </br></br>
In addition to Python, also the Python libraries `math`, `PyQt6`, `random` and `string` are needed, whereby especially the last two usually come already with the standard installation of Python.

**Important:** The Password Generator only generates the password, but does not save it anywhere! Once the result window is closed, the same password cannot be recalled again, but only a new password may be generated.

This work is licensed under an MIT License.<br/>
© 2023 Sandra Liedtke.
