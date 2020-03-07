import datetime
import json
import traceback
import webbrowser

import requests
import rumps


class NightscoutMenuBarApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Nightscout menu bar",
            "interval": 180,
            "ns_url": "https://endafarrell-nightscout.herokuapp.com",
        }
        self.app = rumps.App(self.config["app_name"])
        self.timer = rumps.Timer(self.on_update, self.config["interval"])
        self.timer.start()
        self.url_button = rumps.MenuItem(
            title=self.config["ns_url"], callback=self.url_callback
        )
        self.app.menu = [self.url_button]

    def on_update(self, sender):
        title = self.get_title()
        self.app.title = title

    def get_title(self):
        try:
            resp = requests.get(f"{self.config['ns_url']}/pebble")
            j = resp.json()
            bg = j["bgs"][0]
            sgv = bg["sgv"]
            direction = bg["direction"]
            direction = {
                "DoubleUp": "⇈",
                "SingleUp": "↑",
                "FortyFiveUp": "↗",
                "Flat": "→",
                "FortyFiveDown": "↘",
                "SingleDown": "↓",
                "DoubleDown": "⇊",
            }.get(direction, direction)
            time_delta = j["status"][0]["now"] - bg["datetime"]

            seconds = int(time_delta / 1000.0)
            mins = int(seconds / 60.0)

            age = {
                0: "\N{CIRCLED IDEOGRAPH ONE}",
                1: "\N{CIRCLED DIGIT ONE}",
                2: "\N{CIRCLED DIGIT TWO}",
                3: "\N{CIRCLED DIGIT THREE}",
                4: "\N{CIRCLED DIGIT FOUR}",
                5: "\N{CIRCLED DIGIT FIVE}",
                6: "\N{CIRCLED DIGIT SIX}",
                7: "\N{CIRCLED DIGIT SEVEN}",
                8: "\N{CIRCLED DIGIT EIGHT}",
                9: "\N{CIRCLED DIGIT NINE}",
            }.get(mins, mins)
            if age != mins:
                title = f"{age} {sgv}{direction}"
            else:
                if mins < 20:
                    title = f"{age}:{sgv}{direction}"
                else:
                    title = f"{mins} ago"
        except BaseException:
            title = "☠ error"
        print(f"{__file__} {datetime.datetime.utcnow()} {title}")
        return title

    def run(self):
        self.app.run()

    def url_callback(self, sender):
        webbrowser.open_new_tab(self.config["ns_url"])


if __name__ == "__main__":
    app = NightscoutMenuBarApp()
    app.run()
