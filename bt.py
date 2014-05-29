import re
import subprocess
import sublime, sublime_plugin

class BrightnessTheme(sublime_plugin.EventListener):
  def on_activated_async(self, view):
    settings = sublime.load_settings('Preferences.sublime-settings')
    
    # make sure to set dark_theme, bright_theme, and brightness_threshold in your User settings.
    dark = settings.get('dark_theme')
    bright = settings.get('bright_theme')
    threshold = settings.get('brightness_threshold')

    inp = str(subprocess.check_output(['brightness', '-l']))
    level = re.findall('brightness (\d\.\d+)', inp)
    theme = settings.get('color_scheme')
    if 'error' in inp or not level:
      pass
    else:
      level = float(level[0])
      if level > threshold and theme == dark:
        settings.set('color_scheme', bright)
      elif level <= threshold and theme == bright:
        settings.set('color_scheme', dark)
      else:
        pass