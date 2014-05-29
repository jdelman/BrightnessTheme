BrightnessTheme
===============

Change your Sublime Text 3 theme based on the brightness of your Mac's monitor.
-------------------------------------------------------------------------------

First, download [brightness.c](http://dev.sabi.net/svn/dev/trunk/LocationDo/brightness.c).

Compile it using ```gcc -std=c99 -o brightness brightness.c -framework IOKit -framework ApplicationServices```. Then move it to your path: ```sudo mv brightness /usr/bin```.

You'll need to add three settings to your ```Preferences.sublime-settings``` file, like so:

```
	"dark_theme": "Packages/Color Scheme - Default/IDLE.tmTheme",
	"bright_theme": "Packages/RailsCasts Colour Scheme/RailsCastsColorScheme.tmTheme",
	"brightness_threshold": 0.375
```

- ```dark_theme``` is the theme Sublime will use when your screen is dark, below the threshold.
- ```bright_theme``` is the theme Sublime will use when your screen is bright, above the threshold.
- ```brightness_threshold``` is a number between 0 and 1. You can run ```brightness -l``` in Terminal to get your current brightness.

Finally, install in your Packages folder. The theme will automatically change upon window activation (like switching to a new tab.)

Tested on OS X 10.9 with Sublime Text 3.
