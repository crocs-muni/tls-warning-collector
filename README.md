# tls-warning-collector

## Installation
Firstly, set the right execution policy.
Run below line as Administrator via cmd.
```sh
$ powershell Set-ExecutionPolicy RemoteSigned
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
$ powershell .\Main.ps1
```
