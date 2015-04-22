import pygtk
import gtk
import appindicator
import urllib2
import json
import os
import gobject
import socket

class IpIndicator:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    flags_dir = os.path.join(script_dir, "flags")
    initialIcon = "applications-internet"

    ipMenuItem = gtk.MenuItem()
    countryMenuItem = gtk.ImageMenuItem(gtk.STOCK_NEW, '')
    infoSeparatorMenuItem = gtk.SeparatorMenuItem()

    def __init__(self):
        self.ind = appindicator.Indicator ("example-simple-client", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon ("indicator-messages-new")
        self.ind.set_icon(self.initialIcon)

        self.menu = gtk.Menu()

        refresh = gtk.MenuItem("Refresh")
        refresh.show()
        refresh.connect("activate", self.refreshInfo)
        self.menu.append(refresh)

        separator = gtk.SeparatorMenuItem()
        separator.show()
        self.menu.append(separator)

        self.menu.append(self.countryMenuItem)
        self.menu.append(self.ipMenuItem)
        self.menu.append(self.infoSeparatorMenuItem)

        image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        image.connect("activate", self.quit)
        image.show()
        self.menu.append(image)
                    
        self.menu.show()

        self.ind.set_menu(self.menu)

        self.refreshInfo()
        gobject.timeout_add(1000, self.refreshInfo)

    def quit(self, widget, data=None):
        gtk.main_quit()

    def refreshInfo(self, widget=None): 
        info = self.getIpInfo()
        if "country_code" in info.keys():
            flagIcon = info["country_code"].lower() + ".png"
            flagIconPath = os.path.join(self.flags_dir, flagIcon)
            self.ind.set_icon(flagIconPath)

            self.ipMenuItem.set_label("IP:"+info["ip"])
            self.ipMenuItem.show()

            img = gtk.Image()
            img.set_from_file(flagIconPath)
            self.countryMenuItem.set_image(img)
            self.countryMenuItem.set_label(info["country"])
            self.countryMenuItem.show()

            self.infoSeparatorMenuItem.show()
        else:
            self.ind.set_icon(self.initialIcon)
            self.ipMenuItem.hide()
            self.countryMenuItem.hide()
            self.infoSeparatorMenuItem.hide()
        return True

    def getIpInfo(self):
        info = {}
        try:
            infoJson = urllib2.urlopen('http://www.telize.com/geoip', None, 1)
            info = json.load(infoJson)
        except urllib2.URLError as e:
            pass
        except socket.timeout as e:
            pass
        return info


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    indicator = IpIndicator()
    main()
