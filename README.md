# TLS warning collector

## Installation
Firstly, set the right execution policy.
Run below lines as Administrator via cmd.
```sh
$ powershell
$ Set-ExecutionPolicy RemoteSigned
```
If still not working, go to file properties and Allow it to run by checking the checkbox.

Download and install python3 and on the installation screen check the option to automatically set path (to use pip).<br />
Run these commands as Administator via cmd
```sh
$ pip3 install pillow
$ pip3 install selenium
```

Go to the folder where you downloaded the whole project and run (in cmd or Powershell ISE)
```sh
$ powershell 
$ .\Main.ps1
```

## Authors
The framework is developed at the [Centre for Research on Cryptography and Security (CRoCS)](https://crocs.fi.muni.cz), at the [Masaryk University](http://www.muni.cz/) in Brno, Czech Republic.
* **Martin Ukrop** 2018 - now (project lead, initial implementation)
* **Lydia Kraus** 2018 - now (project lead, researcher)
* **Filip Gontko** 2019 - now (main developer)
