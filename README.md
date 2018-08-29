# SheddingWallpapers

<img align="right" width="250" height="250" src="/Icons/full_size.png">

SheddingWallpapers is an open-source python script that allows you to automatically transform and apply the stunning Google Calendar wallpapers every month!

### Prerequisites

In order to use SheddingWallpapers you will need:
* [Pillow](https://pypi.org/project/Pillow/2.1.0/) 
* [screeninfo](https://pypi.org/project/screeninfo/)
* [tqdm](https://pypi.org/project/tqdm/)

### Compatibility

This script has been tested to work on Mac, Windows, and Linux. Linux compatability is limited to the following desktop environments:
* gnome
* gnome2
* unity
* cinnamon
* kde
* mate
* xfce
* lxde
* fluxbox
* blackbox
* openbox
* icewm
* jwm
* afterstep
* trinity
* pantheon
* i3
* lxqt
* awesome
* razor-qt
* windowmaker


### Installing through Github

In order to manually download the extension through github:

```
1. Download the project by clicking the "clone or download" button at the top of this page
2. Once downloaded, unzip the folder
3. If you have not done so, install the relevant prerequisites, which are listed above
4. Navigate to the directory in which you have un-zipped the project 
5. Simply type "python SheddingWallpapers.py". 

```

### Optional Parameters

- " -d " or " --alternate_dir " allows you to load wallpapers\* from an alternate directory
- " -r " or " --rebuild " will re-transform, and apply, the default wallpapers included in this project
- " -a " or " --auto_start "\*\* will add the script automatically start on boot on desktop environments which support the [Desktop Application Autostart Specification](https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html) 

\* Note that the wallpapers included in the alternate directory must be named using the same convention as the ones included in this project. The wallpapers must be each named after the particular month you wish to see them in (ex/ 'January' for the wallpaper which will display in January

\*\* Note that to run this parameter correctly, SheddingWallpapers needs to be ran with the " sudo " command

## Contributing

Please contact me through<a href="mailto:george.ridgway@protonmail.com"> my email</a>, or submit a pull request 

## The Wallpapers

Please note that I take no credit for creating the wallpapers themselves, you can find the wallpapers individually [here](https://www.droid-life.com/2014/10/23/download-seasonal-backgrounds-from-new-google-calendar-app/)

## Authors

* **George Ridgway** - *Main Developer* - [Github](https://github.com/ridgeontheway)

## License

This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The [Desktop.py](Desktop.py) module was taken from the [WeatherDesk project](https://gitlab.com/bharadwaj-raju/WeatherDesk) 
