# Scan Nearby Bluetooth LE Devices

> Ask Minis what's around you — it scans real nearby Bluetooth Low Energy devices via the native framework and returns a ranked signal-strength table, no separate BLE scanner app needed.

---

## 🎯 Pain Point

Diagnosing what Bluetooth devices are nearby (for troubleshooting HomeKit sensors, checking if AirPods are close by, spotting unknown/unnamed devices) normally requires a dedicated BLE scanner app — not something available inside a general-purpose assistant.

---

## 💡 What It Does

Minis calls the native Bluetooth CLI to run a timed BLE scan, returning every discoverable peripheral with its RSSI (signal strength), advertised services, and name (when broadcast). It renders the raw scan as a clean, sorted "Device / Signal" table and separately calls out how many unnamed/anonymous devices were also detected.

---

## 🛠 Skills Needed

None (built-in). Uses Minis' native `apple-bluetooth` CLI directly.

---

## 📋 How to Use

1. Ask Minis to scan for nearby Bluetooth devices.
2. Grant the native Bluetooth permission prompt the first time.
3. Review the ranked device/signal table.

---

## 💬 Example Prompt

```
Scan for nearby Bluetooth LE devices and tell me what's around, ranked by signal strength.
```

---

## 📤 Expected Output

> Found 28 BLE devices. Strongest named devices nearby:
>
> | Device | Signal |
> |---|---|
> | UltraTicci | −38 dBm |
> | M5 Pro | −52 dBm |
> | MBP | −54 dBm |
> | Aqara camera | −54 dBm |
> | ... | ... |
>
> Also detected 12 unnamed devices.

![Bluetooth LE scan: native permission prompt, raw scan output, and a ranked device/signal table](../../assets/screenshots/bluetooth-nearby-scan.jpg)

---

## ⚙️ Configuration / Requirements

- [ ] Grant the native Bluetooth permission prompt ("Allow Minis to find Bluetooth devices?")
- [ ] Bluetooth enabled on the device

---

## 💡 Tips & Variations

- Useful for quick troubleshooting: "is my Aqara sensor even broadcasting right now?"
- Ask Minis to repeat the scan periodically and diff the results to spot devices that come and go (e.g. someone else's phone passing by).

---

## 👤 Author

Sourced from: [Open Minis Is the iOS Agent I Wish Siri AI Could Be](https://www.macstories.net/reviews/open-minis-is-the-ios-agent-i-wish-siri-ai-could-be/) by Federico Viticci, MacStories (2026-07-20).

---

## 📅 Last Verified

2026-07
