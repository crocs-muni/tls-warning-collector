# TLS warning collector

## Prerequisities
1. Windows 10 (download link for VM: https://developer.microsoft.com/en-us/windows/downloads/virtual-machines)
2. Chocolatey

## Installation

1. Install `python3`. On the installation screen, check the option to automatically set path (to use pip).
2. Install the python library dependencies using `pip3`:
```sh
$ pip3 install -r requirements.txt
```
3. Download the browser driver -- follow the instructions in `README.md` in `drivers` folder.
4. When drivers are all set, add the drivers folder the the `PATH`.

## Configuration

You can change the configuration of the project in the `config.yaml` file. By commenting out the line with `#` you can choose which browsers and versions won't be in the dataset. (You can take a loot at the example test-versions).

## Run

After that, go to the project location via Administrator command line and run the `main.py` script with this command:
```sh
$ pyhton main.py
```

## Authors

The framework is developed at the [Centre for Research on Cryptography and Security (CRoCS)](https://crocs.fi.muni.cz), at the [Masaryk University](http://www.muni.cz/) in Brno, Czech Republic.
* **Martin Ukrop** 2018 - now (project lead, initial implementation)
* **Lydia Kraus** 2018 - now (project lead, researcher)
* **Filip Gontko** 2019 - now (main developer)
