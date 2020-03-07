from setuptools import setup

APP = ["nightscout_menubar_mac/nightscout_menubar_mac.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "nightscout.icns",
    "plist": {"CFBundleShortVersionString": "0.2.0", "LSUIElement": True,},
    "packages": ["rumps", "requests"],
}

setup(
    app=APP,
    name="nightscout_menubar_mac",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=["rumps", "requests"],
)
