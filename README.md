# TLS warning collector
TLS warning collector is a tool to support the creation of an open dataset of TLS warnings and indicators in web browsers. It automatically downloads, installs and uninstalls browsers, and collects browser screenshots for comparison and analysis of TLS warnings.

## Prerequisities
1. Windows 10 (download link for VM: https://developer.microsoft.com/en-us/windows/downloads/virtual-machines)
2. Chocolatey (link: https://chocolatey.org/docs/installation)
3. Python 3 (link: https://www.python.org/downloads/windows/)
4. Git (link: https://git-scm.com/download/win)

## Installation

1. Install `python3`. On the installation screen, check the option to automatically set path (to use pip).
2. Clone the repository to your computer via `git clone https://github.com/crocs-muni/tls-warning-collector.git`
3. Download the browser driver -- follow the instructions in `README.md` in `drivers` folder.

## Configuration

You can change the configuration of the project in the `config.yaml` file. By commenting out the line with `#` you can choose which browsers and cases won't be in the dataset. 
If you don't want to run all of the browser versions then you can use "one-version", but you have to change the `main.py` file (`all_versions = cfg.get('browsers')[browserID].get('versions')` --> `all_versions = cfg.get('browsers')[browserID].get('one-version')`).
* Which "one-version" you want to run is easy to change -- just pick some of the supported versions and place it in the "[]" brackets. E.g. `one-version: [72.0.3626.121]`
* ### Architecture x86
  For Chromium running on x86 OS you have to change the file location of the Application from `...\Program Files (x86)\` to `...\Program Files\` only (function - `set_chromium_capabilities` in `browsers.py`). !!!

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
