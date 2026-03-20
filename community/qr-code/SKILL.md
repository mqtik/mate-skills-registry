---
name: qr-code
description: "Generate QR codes for URLs, text, WiFi, contacts"
argument-hint: "describe what you want the QR code to encode"
categories: media, productivity, design
version: 1.0.0
---

Help the user generate QR codes for various data types. For URLs, encode the full URL including protocol. For WiFi, generate the correct WPA format string: WIFI:T:WPA;S:networkname;P:password;; For contacts, generate a vCard 3.0 string with the relevant fields. For plain text, encode the text directly. Generate the correct qrencode or python-qrcode CLI command to produce the QR code file. Suggest appropriate error correction levels: L for clean digital displays, H for printed materials that may be damaged. Recommend a minimum size of 200x200 pixels for reliable scanning. For custom-styled QR codes (colored, with logo), note that this requires a library like qrcode with PIL. Always encode and decode test the output by describing how to verify it scans correctly.
