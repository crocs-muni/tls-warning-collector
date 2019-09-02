# TLS warning collector

## Installation
* Firstly, download and install python3, and on the installation screen check the option to automatically set path (to use pip).<br />
```sh
$ pip3 install -r requirements.txt
```

* Secondly, go to the folder where you downloaded the project and follow the instructions in the README.md in 'drivers' folder.
* When drivers are all set, add the drivers folder the the PATH.
* You can change the configuration of the project in 'config.yaml' file. By commenting out the line with '#' you can choose which browsers and versions won't be in the dataset. (You can take a loot at the example test-versions).

* After that, go to the folder location via command line and run the script with this command.

```sh
$ pyhton main.py
```

## Authors
The framework is developed at the [Centre for Research on Cryptography and Security (CRoCS)](https://crocs.fi.muni.cz), at the [Masaryk University](http://www.muni.cz/) in Brno, Czech Republic.
* **Martin Ukrop** 2018 - now (project lead, initial implementation)
* **Lydia Kraus** 2018 - now (project lead, researcher)
* **Filip Gontko** 2019 - now (main developer)
