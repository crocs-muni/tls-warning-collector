# TLS warning collector

## Prerequisities
1. Windows 10 (download link for VM: https://developer.microsoft.com/en-us/windows/downloads/virtual-machines)
2. Chocolatey (link: https://chocolatey.org/docs/installation)

## Installation

1. Install `python3`. On the installation screen, check the option to automatically set path (to use pip).
2. Download the browser driver -- follow the instructions in `README.md` in `drivers` folder.
3. Install the python library dependencies and check if "drivers" are in PATH via command:
```sh
$ python requirements.py
```

## Configuration

You can change the configuration of the project in the `config.yaml` file. By commenting out the line with `#` you can choose which browsers and versions won't be in the dataset. (You can take a look at the example `test-versions`).

## Run

After that, go to the project location via Administrator command line and run the `main.py` script with this command:
```sh
$ pyhton main.py
```
Note: There may be a firewall settings popup during the first run as python wants to access the Internet. In older Firefox versions there can be a restart computer popup which you can postpone (Windows 7) or you have to restart the computer (Windows 10).

## Wiki

For more information, please visit the wiki page: https://github.com/crocs-muni/tls-warning-collector/wiki

## Authors

The framework is developed at the [Centre for Research on Cryptography and Security (CRoCS)](https://crocs.fi.muni.cz), at the [Masaryk University](http://www.muni.cz/) in Brno, Czech Republic.
* **Martin Ukrop** 2018 - now (project lead, initial implementation)
* **Lydia Kraus** 2018 - now (project lead, researcher)
* **Filip Gontko** 2019 - now (main developer)
