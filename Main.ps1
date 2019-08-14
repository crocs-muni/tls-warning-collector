# SSL warnings automatic screening﻿

$Cases = @(
    @{ "filename" = "expired"         ; "url" = "https://expired.badssl.com/" }
#  , @{ "filename" = "wrong-host"      ; "url" = "https://wrong.host.badssl.com/" }
#  , @{ "filename" = "self-signed"     ; "url" = "https://self-signed.badssl.com/" }
#  , @{ "filename" = "untrusted-root"  ; "url" = "https://untrusted-root.badssl.com/" }
#  , @{ "filename" = "revoked"         ; "url" = "https://revoked.badssl.com/" }
#  , @{ "filename" = "ok-ev"           ; "url" = "https://extended-validation.badssl.com/" }
#  , @{ "filename" = "ok-ov"           ; "url" = "https://badssl.com/" }
#  , @{ "filename" = "http"            ; "url" = "http://http.badssl.com/" }
#  , @{ "filename" = "mixed-content"   ; "url" = "https://mixed.badssl.com/" }
)

$BrowserIDs = @(
#   "firefox"
#    ,
   "chromium"
#    ,
#    "chrome"
#    ,
#    "ie"
#   ,
#    "edge"
#   ,
#   "opera"
);

$Browsers = @{
    "firefox" = @{ "name" = "Mozilla Firefox" ; "package" = "firefox" ; "binary" = "firefox" ; "altbinary" = "firefox" ;
#       "versions" = @("64.0", "63.0", "62.0", "61.0", "60.0", "59.0", "58.0", "57.0", "56.0", "55.0", "54.0", "53.0", "52.0", "51.0", "50.0", "49.0", "48.0", "47.0", "46.0", "45.0", "44.0", "43.0", "42.0", "41.0", "40.0", "39.0", "38.0", "37.0", "36.0", "35.0", "33.1", "33.0", "32.0", "31.0", "30.0", "29.0", "28.0", "27.0", "26.0", "25.0", "24.0", "23.0", "22.0", "21.0", "19.0", "18.0", "15.0") ;
#       "versions" = @("62.0", "52.0", "45.0") ;
       "versions" = @("51.0", "50.0", "49.0", "48.0", "47.0", "46.0") ;
       "installFolders" = @(
            "C:\Program Files\Mozilla Firefox",
            "C:\Program Files (x86)\Mozilla Firefox",
            "C:\Program Files (x86)\Mozilla Maintenance Service",
            "C:\Users\username\AppData\Local\Mozilla"
       ) ;
       "profileFolders" = @(
            "C:\Users\username\AppData\Roaming\Mozilla"
       ) ;
    } ;
    "chromium" = @{ "name" = "Chromium" ; "package" = "chromium" ; "binary" = "chrome" ; 
       "altbinary" = "C:\users\username\appdata\local\Chromium\Application\chrome.exe" ;
#       "versions" = @("75.0.3770.142", "73.0.3683.75", "72.0.3626.121", "71.0.3578.98", "70.0.3538.110", "69.0.3497.100", "68.0.3440.106", "67.0.3396.99", "66.0.3359.181", "65.0.3325.181", "64.0.3282.186", "63.0.3239.132", "62.0.3202.94", "61.0.3163.0", "60.0.3112.0", "59.0.3071.0", "58.0.3029.0", "57.0.2987.0", "56.0.2924.0", "55.0.2882.0", "54.0.2840.0", "53.0.2784.0", "51.0.2683.0", "50.0.2661.0", "49.0.2598.0", "48.0.2564.0", "47.0.2526.0", "46.0.2490.0", "45.0.2454.0", "44.0.2403.0", "41.0.2255.0", "40.0.2211.0", "39.0.2171.0", "38.0.2125.0", "37.0.2061.0", "36.0.1978.0", "35.0.1916.0", "34.0.1848.0", "33.0.1732.0", "32.0.1701.0", "31.0.1650.4", "30.0.1599.14") ;
#       "versions" = @("66.0.3341.0-snapshots", "54.0.2840.0", "49.0.2598.0", "39.0.2171.0") ;
#       "versions" = @("34.0.1848.0") ;
#       "versions" = @("75.0.3770.142", "67.0.3396.99", "34.0.1848.0") ;
       "versions" = @("75.0.3770.142", "55.0.2882.0", "54.0.2840.0") ;
       "installFolders" = @(
            "C:\Program Files (x86)\Google",
            "C:\Program Files (x86)\Chromium",
            "C:\users\username\appdata\local\Chromium",
            "C:\users\username\appdata\local\Google"
       ) ;
       "profileFolders" = @(
            "(no chrome profile)"
       ) ;
    } ;
    "chrome" = @{ "name" = "Google Chrome" ; "package" = "googlechrome" ; "binary" = "chrome" ; 
       "altbinary" = "C:\users\username\appdata\local\Google\Chrome\Application\chrome.exe" ;
#       "arguments" = "--disable-background-mode --incognito --start-maximized --no-default-browser-check" ;
#       "versions" = @("75.0.3770.100", "74.0.3729.169", "73.0.3683.103", "72.0.3626.121", "71.0.3578.98", "70.0.3538.11000", "69.0.3497.10000", "68.0.3440.10600", "67.0.3396.9900", "66.0.3359.18100", "65.0.3325.18100", "64.0.3282.18600", "63.0.3239.132", "62.0.3202.94", "61.0.3163.100", "60.0.3112.113", "59.0.3071.115", "58.0.3029.110", "57.0.2987.13301", "56.0.2924.87001", "55.0.2883.87", "54.0.2840.99", "53.0.2785.143", "52.0.2743.116", "51.0.2704.106", "50.0.2661.102", "49.0.2623.112", "48.0.2564.116", "47.0.2526.111", "37.0.2062.94", "36.0.1985.143", "35.0.1916.153", "38.0.2125.0", "34.0.1847.11601", "33.0.1750.154", "32.0.1700.107", "31.0.1650.63", "30.0.1599.101", "29.0.1547.76", "28.0.1500.95", "27.0.1453.116", "26.0.1410.64", "10.0.0") ;
#       "versions" = @("75.0.3770.100", "67.0.3396.9900", "49.0.2623.112", "30.0.1599.101") ;
#       "versions" = @("75.0.3770.100", "67.0.3396.9900") ;
       "versions" = @("74.0.3729.169") ;
       "installFolders" = @(
            "C:\Program Files (x86)\Google",
            "C:\Program Files (x86)\Chrome",
            "C:\users\username\appdata\local\Chrome",
            "C:\users\username\appdata\local\Google"
       ) ;
       "profileFolders" = @(
            "(no chrome profile)"
       ) ;
    } ;
    "opera" = @{ "name" = "Opera" ; "package" = "opera" ; 
       "binary" = "opera" ; 
       "altbinary" = "C:\Users\username\AppData\Local\Programs\Opera\launcher.exe" ;
#       "arguments" = "--disable-background-mode --private --start-maximized --no-default-browser-check" ;
#       "versions" = @("58.0.3135.118", "57.0.3098.116", "56.0.3051.116", "55.0.2994.61", "54.0.2952.71", "53.0.2907.110", "52.0.2871.99", "51.0.2830.55", "50.0.2762.67", "49.0.2725.64", "48.0.2685.52", "47.0.2631.80", "46.0.2597.61", "45.0.2552.898", "44.0.2510.1457", "43.0.2442.991", "42.0.2393.94", "41.0.2353.69", "40.0.2308.90", "39.0.2256.48", "38.0.2220.41", "37.0.2178.54", "36.0.2130.65", "35.0.2066.92", "34.0.2036.50", "33.0.1990.58", "32.0.1948.69", "31.0.1889.99", "30.0.1835.88", "29.0.1795.60", "28.0.1750.51", "27.0.1689.76", "26.0.1656.60", "25.0.1614.71", "24.0.1558.64", "23.0.1522.77", "22.0.1471.70", "21.0.1432.68", "20.0.1387.91", "19.0.1326.63", "18.0.1284.68", "17.0.1241.53", "16.0.1196.80", "15.0.1147.141", "12.15") ;
       "versions" = @("56.0.3051.116", "46.0.2597.61", "38.0.2220.41") ;
#       "versions" = @("56.0.3051.116") ;
       "installFolders" = @(
            "C:\Users\username\AppData\Local\Programs\Opera",
            "C:\Users\username\AppData\Local\Opera Software"
       ) ;
       "profileFolders" = @(
            "C:\Users\username\AppData\Roaming\Opera Software"
       ) ;
    }
    "ie" = @{ "name" = "Internet Explorer" ; "package" = "ie11" ; 
       "binary" = "ie" ;
       "arguments" = "--start-maximized --no-default-browser-check --disable-update" ;
       "versions" = @("0.2") ;
       "installFolders" = @(
            "C:\Program Files\internet explorer"
       )
    }
    "edge" = @{ "name" = "Microsoft Edge" ; "package" = "edge" ;
     "binary" = "edge"; 
     "versions" = @("44")
    }
} ;

function Main {
  foreach ($BrowserID in $BrowserIDs) {
    $Browser = $($Browsers.$BrowserID);
    foreach ($Version in $Browser.versions) {
      Write-Host "`n######## Processing $($Browser.name) (v$($Version))`n"
      if ($Browser -ne "edge") {
        Install-BrowserVersion -Browser $Browser -Version $Version
      }
      Get-SSLScreenshots -Browser $Browser -Version $Version
      Uninstall-Browser -Browser $Browser
    }
  }
}

function Remove-Item-Test-Log([String] $Item) {
  if (Test-Path $Item) { 
    Write-Host "# Removing item: $($Item)"
    Remove-Item –Path $Item –Recurse 
  } else {
    Write-Host "# Item does not exist, not removing: $($Item)"
  }
}

function New-Diretory-Test-Log([String] $Item) {
  if (Test-Path $Item) { 
    Write-Host "# Directory exists, not creating: $($Item)"
  } else {
    Write-Host "# Creating directory: $($Item)"
    New-Item -Path $Item -ItemType directory
  }
}

function Install-BrowserVersion($Browser, [String] $Version) {
  choco install $($Browser.package) --force --version=$Version --yes --nocolor --limit-output --no-progress --ignore-checksums --log-file=$ChocoLog
#  if ($Browser.package -like "*chrome*") {
#    rename-item -path "C:\Program Files (x86)\Google\Update\GoogleUpdate.exe" -newname GoogleUpdate.exe.bak
#  } 
}

function Uninstall-Browser($Browser) {
  choco uninstall $($Browser.package) --allversions --yes --nocolor --limit-output --log-file=$ChocoLog
  foreach ($Folder in $($Browser.installFolders)) {
      Remove-Item-Test-Log -Item $Folder
  }
}

function Get-SSLScreenshots($Browser, [String] $Version) {
  # Loop through all cases
  foreach ($Case in $Cases) {
      Write-Host "`n#### Processing case $($Case.filename) ($($Case.url))`n"
      python main.py $Browser.binary $Version $Case.filename $Case.url $Browser.package
  }
}

Main;