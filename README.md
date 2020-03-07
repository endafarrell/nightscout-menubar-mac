# nightscout-menubar-mac

* I (for years now) always use conda, even when it can be overkill.
* My own nightscout url is hardcoded - but it's such simple code, you'll 
  fix your own.

## Minimal instructions to get running:

    conda env create --file conda-env.yaml
    conda activate nightscout-menubar-mac
    rm -rf  build dist
    python setup.py py2app
    open dist/nightscout_menubar_mac.app

* You should copy the ~21MB dist/nightscout_menubar_mac.app somewhere in your
  ~/Applications and from there add it to your Startup Items.
* If something goes wrong, try `open dist/nightscout_menubar_mac.app/Contents/MacOS/nightscout_menubar_mac`
  which gives a Terminal window which may be enlightening.

