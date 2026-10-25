# SEA Haze — Privacy Policy

**English** · [华文](PRIVACY.zh-Hans.md) · [Bahasa Melayu](PRIVACY.ms.md) · [தமிழ்](PRIVACY.ta.md)

Effective date: 25 October 2026

This policy explains how the SEA Haze app ("the App") for iPhone, iPad, Mac, Apple Watch and Apple Vision Pro, including its widgets, handles your information.

## In short

- The App **does not collect, store or share any personal information or usage data**.
- There is **no account, no sign-in, no advertising, no tracking and no analytics**.
- Your settings and location stay **on your device**.

## 1. Information kept on your device

The App stores the following only on your device. It is never sent to the developer:

- Your settings (for example language, map layers, alert threshold).
- Optional API keys you enter (OpenAQ, NASA FIRMS).
- Recently downloaded air quality, weather and fire data, kept so the App can open quickly (shown only while under 30 minutes old).
- If you allow location access: your approximate last location, used to choose the nearest station. It is shared with the App's widgets on the same device through an App Group, and nowhere else.

Deleting the App removes all of this. You can also clear downloaded data in **Settings → Storage & Cache**.

## 2. Location

Location access is optional ("While Using the App"). It is used **only on your device** to pick the air quality station nearest to you, in the App and its widgets. Your location is **never sent** to the developer or to any data provider. You can turn it off in Settings → Location, or in your device's system settings. Without it, the App shows Singapore Central by default.

## 3. Data providers the App connects to

To show live data, the App downloads public data directly from these services:

| Service | What the App downloads |
|---|---|
| data.gov.sg (National Environment Agency, Singapore) | PM2.5, PM10 and PSI readings |
| Malaysia Department of Environment (APIMS) | Air Pollutant Index readings |
| Open-Meteo (including Copernicus CAMS data) | Wind, cloud, rain and modelled air quality |
| Sensor.Community | Community air quality sensor readings |
| OpenAQ (only if you enter your own API key) | Air quality station readings |
| NASA FIRMS | Satellite fire hotspots |
| RainViewer | Rain radar images |
| GDACS | Tropical cyclone advisories |
| Amazon Web Services (open elevation tiles) | Terrain heights for the Vision Pro 3D view |
| Apple Maps | Map images |

These requests contain fixed regional areas or coordinates, **not your location**. Like any website, these services may receive standard technical information such as your IP address, under their own privacy policies. Your optional API keys are sent only to the service they belong to.

## 4. Artificial intelligence

The optional **Situation Summary** uses only Apple's **on-device** Foundation Model (Apple Intelligence), where available on your device. The summary is written entirely on your device from readings already shown in the App. **Nothing is sent to the developer or to any AI server** for this feature. AI-generated text may contain mistakes.

## 5. Notifications

Air quality alerts are created **locally on your device**. No push notification server is used.

## 6. Children

The App does not collect personal information from anyone, including children.

## 7. Future changes

A future version may collect **anonymous** usage data (for example, which features are used) to improve the App. Such data will not identify you and will not be sold or used for advertising. This policy and the App Store privacy details will be updated **before** any such collection begins. Other changes to this policy will also be published here with a new effective date.

## 8. Contact

For questions about this policy, please open an issue in this repository: [Issues](../../issues).

---

Translations are provided for convenience. If there is any difference between a translation and this English version, the English version prevails.
