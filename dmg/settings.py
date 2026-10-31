# dmgbuild settings for the SEA Haze disk image (see make_dmg.sh).
# dmgbuild writes the window layout itself; create-dmg's Finder scripting no longer
# sets backgrounds or icon positions on current macOS.
import os.path

app = defines.get("app", "dist-macos-archive/SEAHaze.app")  # noqa: F821
here = os.path.abspath("dmg")  # run from the repository root (make_dmg.sh does)

format = "UDZO"
filesystem = "HFS+"
files = [app]
symlinks = {"Applications": "/Applications"}
icon = os.path.join(app, "Contents/Resources/AppIcon.icns")
hide_extensions = ["SEAHaze.app"]

# Window and icons match make_background.py (640x428 content, icons centred at y 185). The window
# origin is the bottom-left corner in screen points; its height includes the 32 pt title bar.
background = os.path.join(here, "background.tiff")
window_rect = ((200, 360), (640, 460))
show_status_bar = False
show_tab_view = False
show_toolbar = False
show_pathbar = False
show_sidebar = False
default_view = "icon-view"
icon_size = 128
text_size = 13
icon_locations = {
    "SEAHaze.app": (170, 185),
    "Applications": (470, 185),
}
