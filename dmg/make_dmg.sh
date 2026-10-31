#!/bin/zsh
# Builds dist-macos/SEAHaze-<version>.dmg from the exported, notarized app, then notarizes and staples it.
# Needs dmgbuild (pip install dmgbuild) and a notarytool profile named "notary"
# (xcrun notarytool store-credentials "notary").
#   dmg/make_dmg.sh [path/to/SEAHaze.app]
set -euo pipefail
cd "${0:A:h}/.."

APP=${1:-dist-macos-archive/SEAHaze.app}
VERSION=$(/usr/libexec/PlistBuddy -c 'Print :CFBundleShortVersionString' "$APP/Contents/Info.plist")
DMG=dist-macos/SEAHaze-$VERSION.dmg
DMGBUILD=${DMGBUILD:-dmgbuild}

python3 dmg/make_background.py
tiffutil -cathidpicheck dmg/background.png dmg/background@2x.png -out dmg/background.tiff

mkdir -p dist-macos
rm -f "$DMG"
"$DMGBUILD" -s dmg/settings.py -D app="$APP" "SEA Haze" "$DMG"
# Sign the image too when a local Developer ID certificate exists (Xcode's cloud signing keeps none on the Mac;
# an unsigned image holding the notarized app can still be notarized and stapled)
if security find-identity -v -p codesigning | grep -q "Developer ID Application"; then
    codesign --sign "Developer ID Application" --timestamp "$DMG"
fi

if [[ ${SKIP_NOTARIZE:-0} != 1 ]]; then
    xcrun notarytool submit "$DMG" --keychain-profile notary --wait
    xcrun stapler staple "$DMG"
    xcrun stapler validate "$DMG"
fi
echo "$DMG"
