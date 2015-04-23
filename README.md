# ip-indicator
IP indicator app for GTK

Useful in case when often switching VPNs. It shows flag of country of your public IP. After opening menu additionally IP is visible.
It refreshes every second and fetches data from http://www.telize.com/. 

Flag icons used from http://www.famfamfam.com/lab/icons/flags/.

Tested on Xubuntu 15.04.

![screenshot](http://i.imgur.com/MiNWv84.png)

# How to run
    $ python ipIndicator.py
    
Keep running after closing terminal

    $ python ipIndicator.py
    Ctrl+z
    $ bg
    $ disown
    $ exit
