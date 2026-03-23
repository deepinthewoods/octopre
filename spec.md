# PCB Design Specification

## 8-Channel Audio DSP System

**Revision 0.1 · Draft for PCB Designer**

---

## 1. System Overview

This document specifies a two-board audio DSP system comprising a Digital Board and an Analog Board, connected via a 2.54mm pitch header. The system captures up to 8 stereo input channels (including optional electret microphone inputs), performs per-channel and global DSP across five ESP32-S3 processors, and outputs processed audio via headphone and line outputs.

The system is powered by a 2S LiPo battery with onboard USB-C charging and programming. All external connections are 2.54mm through-hole pads suitable for soldering DuPont headers or direct wire attachment.

---

## 2. Board Specifications

### 2.1 Common to Both Boards

| Parameter | Specification |
|---|---|
| Board dimensions | 70 × 55 mm |
| Layer count | 6-layer, double-sided |
| Stackup | Signal / GND / Signal / Power / GND / Signal (designer to confirm with JLCPCB) |
| PCB thickness | 1.6 mm |
| Minimum trace width | 0.1 mm (signal), 0.3 mm (power) |
| Surface finish | HASL or ENIG (designer preference) |
| Solder mask | Both sides |
| Board interconnect | 2.54mm pitch through-hole header, both boards, mating pair |
| Manufacturing | JLCPCB Standard PCBA |

### 2.2 Board Interconnect Header

The two boards connect face-to-face (sandwich configuration) via a 2×20 (40-pin) 2.54mm pitch header. Pin assignment to be finalised during schematic capture. Signals crossing the connector include:

- I2S TDM bus: BCLK, LRCLK, DATA (×4 slaves), MCLK
- ES8388 headphone output L/R (analog, differential if possible)
- ES8388 line output L/R (analog)
- I2C bus for ES8388 control
- 3.3V power (digital)
- 3.3V analog power (AVDD, low-noise LDO output)
- 1.8V analog power (DVDD, if required by ES8388 config)
- GND (multiple pins — minimum 6 GND pins on connector)

> **NOTE:** Analog signals crossing the connector should be routed on dedicated pins at one end of the header, away from digital signals. Designer to add series resistors (33Ω) on all digital lines at the connector.

---

## 3. Digital Board

### 3.1 ESP32-S3 Modules

Five ESP32-S3 modules are used. One master with PCB antenna, four slaves with U.FL connector (unpopulated — antenna disabled in firmware).

| Designator | Part | JLCPCB # | Flash | PSRAM | Antenna | Role |
|---|---|---|---|---|---|---|
| U1 | ESP32-S3-WROOM-1-N16R8 | C2913202 | 16 MB | 8 MB | PCB (on-board) | Master — WiFi/BT active |
| U2–U5 | ESP32-S3-WROOM-1U-N16R8 | C3013946 | 16 MB | 8 MB | U.FL (unpopulated) | Slaves — WiFi/BT disabled in firmware |

> **NOTE:** Master module (U1) antenna must protrude beyond the board edge. Maintain 3.7mm copper keepout around all antenna sides including inner layers. Slave U.FL pads should be present on PCB but connector not populated.

### 3.2 ES8388 Audio Codecs

Five ES8388 stereo audio codecs, one per ESP32-S3. Each codec handles one stereo input channel pair and one stereo output. The master codec (U6) drives the headphone and line outputs.

| Designator | Part | Package | Role |
|---|---|---|---|
| U6 | ES8388 | QFN-28 (4×4mm) | Master codec — headphone out + line out |
| U7–U10 | ES8388 | QFN-28 (4×4mm) | Slave codecs — audio input capture only |

> **NOTE:** ES8388 requires a low-noise analog supply (AVDD). Route AVDD from a dedicated LDO with LC filtering. Keep ES8388 analog ground pour separate from digital ground, joining at a single star point near the power supply.

**ES8388 I2S connections per unit:**

- MCLK: shared from master ESP32-S3 (U1) — star route to all codecs
- BCLK / LRCLK: shared TDM clock bus from master ESP32-S3
- SDIN (ADC input): individual per codec
- SDOUT (DAC output): individual — master codec only used for output
- I2C (SDA/SCL): shared I2C bus, each ES8388 has unique address via ADDR pin

### 3.3 TDM Bus

The four slave ESP32-S3 modules (U2–U5) output audio via I2S TDM to the master (U1). Each slave occupies two TDM slots (stereo). Clock master is U1.

| Signal | Direction | Note |
|---|---|---|
| BCLK | U1 → U2–U5 | Shared clock — series 33Ω at source |
| LRCLK | U1 → U2–U5 | Shared frame sync — series 33Ω at source |
| DATA (×4) | U2–U5 → U1 | One data line per slave |
| MCLK | U1 → U2–U5 + all ES8388s | 256× or 512× Fs — star topology |

> **NOTE:** Keep TDM data lines short and matched in length. At 44.1kHz × 32bit × 8slot = ~11.3MHz BCLK, trace impedance and crosstalk matter. Route with ground stitching vias alongside signal traces.

### 3.4 UART Programming Mux

A 4-channel UART multiplexer allows the master ESP32 to bridge USB-CDC UART to any slave for firmware flashing. GPIO-controlled mux IC (e.g. 74HC4052 or equivalent dual 4:1 mux) routes TX/RX. GPIO0 and EN (reset) lines from master to each slave are required for bootloader entry.

| Signal | From | To | Note |
|---|---|---|---|
| USB_TX / USB_RX | USB-C (CH340/CP2102 or native USB) | Master U1 | Primary programming port |
| UART_TX / UART_RX | Master U1 | Mux input | Bridged via firmware |
| MUX_A / MUX_B | Master U1 GPIO | Mux select pins | 2 GPIOs select 1-of-4 slave |
| GPIO0 (×4) | Master U1 GPIO | Each slave GPIO0 | Bootloader entry |
| EN / RST (×4) | Master U1 GPIO | Each slave EN pin | Reset control |

### 3.5 Power System

#### 3.5.1 Battery & Charger

| Parameter | Specification |
|---|---|
| Battery | 2S LiPo (7.4V nominal, 8.4V max) |
| Battery connector | JST-PH 2.0mm 2-pin (designer to confirm with client) |
| Charger IC | BQ25798RQMR (Texas Instruments) |
| Charge input | USB-C — same port as programming |
| Charge topology | Buck-boost, supports USB-C PD negotiation for >8.4V input |
| Max charge current | To be set by designer per battery capacity (suggest 1C) |
| BQ25798RQMR interface | I2C — connect to master ESP32-S3 I2C bus |
| Cell balancing | External 2S BMS balancing board or integrated BQ25798RQMR monitoring |

> **NOTE:** BQ25798RQMR integrates USB-C PD negotiation — no companion PD controller required. Supports 2S LiPo charging (up to 4S) with I2C configuration. Minimal firmware required; TI reference drivers available for ESP32. Include reverse polarity protection on battery input.

#### 3.5.2 Power Rails

| Rail | Voltage | Source | Consumers | Notes |
|---|---|---|---|---|
| VBAT | 7.4–8.4V | 2S LiPo | Buck converters input | Fused, reverse polarity protected |
| 3V3_DIG | 3.3V | Buck converter (e.g. TPS62xxx) | All 5 ESP32-S3 modules, ES8388 DVDD, logic ICs | 2A+ capable, good transient response |
| 3V3_ANA | 3.3V | Low-noise LDO from VBAT | ES8388 AVDD, op-amp supplies (analog board) | Separate LDO — e.g. LP5907 or TLV70233. LC filter on output |
| 1V8 | 1.8V | LDO from 3V3_DIG or direct | ES8388 DVDD if 1.8V mode selected | Check ES8388 config — may not be required |
| 5V_USB | 5V | USB-C VBUS | BQ25798RQMR input | Protected with TVS diode |

### 3.6 USB-C Interface

| Parameter | Specification |
|---|---|
| Connector | USB-C, through-hole or SMD — 2.54mm hole pads if through-hole |
| Function | Programming (USB-CDC or UART bridge) + 2S LiPo charging |
| USB bridge | Use ESP32-S3 native USB-CDC (no external IC required) on master U1 |
| ESD protection | TVS diode array on VBUS and data lines (e.g. USBLC6-2SC6) |
| CC resistors | 5.1kΩ on CC1 and CC2 for USB-C sink identification |

### 3.7 Digital Board I/O — 2.54mm Through-Hole Pads

| Pad/Header | Signals | Count | Notes |
|---|---|---|---|
| USB-C connector | VBUS, D+, D−, CC1, CC2, GND | — | Panel-edge preferred |
| Battery connector | VBAT+, GND | 2 pins | JST-PH or through-hole pads |
| Board interconnect | See Section 2.2 | 40 pins (2×20) | 2.54mm pitch header |
| Debug/JTAG header | TDI, TDO, TCK, TMS, GND, 3V3 | 6 pins | Master ESP32-S3 only |
| Status LEDs | Charge status, power good, user LED | 3× | On-board, not on header |

---

## 4. Analog Board

### 4.1 Input Preamp — 8 Channels

Eight identical input preamp channels, each accepting unbalanced line-level or instrument-level signal via 2.54mm through-hole pads. Two channels (CH1 and CH2) additionally support electret condenser microphone input via a switchable bias circuit.

| Parameter | Specification |
|---|---|
| Topology | Non-inverting op-amp stage per channel |
| Op-amp | OPA2134U (dual, SOIC-8 SMD) — one per 2 channels. Note: OPA2134PA is DIP — specify OPA2134U for SMT |
| Input impedance | ≥100kΩ (suitable for both line and electret mic source) |
| Gain | Variable 0 to +30dB via Nidec ST-4EA 10kΩ SMD trim pot per channel — top-adjust, 4×4mm SMT footprint, reflow solderable |
| Input coupling | AC coupled — 10µF film or electrolytic input cap per channel |
| Input protection | Schottky clamp diodes to 3V3_ANA and GND |
| Output | DC coupled to ES8388 analog input on digital board via interconnect header |
| Supply | 3V3_ANA from digital board via header |

### 4.2 Electret Microphone Bias (CH1 & CH2)

Channels 1 and 2 support optional electret condenser microphone input. A bias resistor network provides the required DC bias voltage. The mic input and line input share the same 2.54mm pads — the user selects the source by populating the appropriate input.

| Parameter | Specification |
|---|---|
| Mic type | 3.5mm electret condenser (standard PC/headset type) |
| Bias voltage | ~3V derived from 3V3_ANA via 2.2kΩ bias resistor |
| AC coupling | 1µF series cap between bias node and preamp input |
| Input pads | Shared 2.54mm through-hole pads with line input (CH1 and CH2 only) |
| Designators | MIC_IN_1, MIC_IN_2 — labelled on silkscreen |

### 4.3 Headphone Output

Stereo headphone output from master ES8388 built-in headphone amplifier. Output is carried from digital board via interconnect header and buffered/filtered on the analog board before the output pads.

| Parameter | Specification |
|---|---|
| Source | ES8388 built-in HP amplifier (on digital board) |
| Load impedance | 32Ω to 300Ω headphones |
| Output coupling | AC coupled — 220µF electrolytic per channel at output pads |
| Output pads | HP_L, HP_R, GND — 2.54mm through-hole, 3 pads |
| Protection | PTC thermistor or 100mA polyfuse in series on each channel |

### 4.4 Line Output

Stereo line output from master ES8388 DAC, buffered by op-amp unity-gain stage on analog board.

| Parameter | Specification |
|---|---|
| Source | ES8388 DAC output (on digital board via header) |
| Buffer topology | Unity-gain OPA2134U buffer per channel |
| Output impedance | ~600Ω (set by series resistor at output) |
| Output level | ~1Vrms nominal at 0dBFS |
| Output coupling | AC coupled — 10µF film cap per channel |
| Output pads | LINE_L, LINE_R, GND — 2.54mm through-hole, 3 pads |

### 4.5 Analog Board I/O — 2.54mm Through-Hole Pads

All user-facing connections are 2.54mm pitch through-hole pads on the board edge. Silkscreen labels required on all pads.

| Pad Group | Signals | Pin Count | Notes |
|---|---|---|---|
| Audio inputs CH1–CH8 | IN_L, IN_R, GND per channel | 24 pins | CH1 & CH2 also accept electret mic |
| Mic bias (CH1 & CH2) | MIC_IN_1, MIC_IN_2, GND | 4 pins (shared with above or separate — TBD) | Bias resistor fitted for CH1/CH2 |
| Headphone output | HP_L, HP_R, GND | 3 pins | Protected output |
| Line output | LINE_L, LINE_R, GND | 3 pins | Buffered, ~600Ω |
| Board interconnect | See Section 2.2 | 40 pins (2×20) | Mates with digital board header |

---

## 5. Grounding & Shielding

- Digital ground (DGND) and analog ground (AGND) must be separate pours on the analog board, joined at a single star point at the power entry from the interconnect header.
- On the digital board, the ES8388 analog ground should be a local island connected to DGND at one point only, near the ES8388 AGND pin.
- 3V3_ANA must be routed on a separate pour from 3V3_DIG. Use a ferrite bead (600Ω @ 100MHz) in series between the LDO output and the 3V3_ANA pour.
- MCLK must be routed with a ground return trace alongside it. Avoid routing MCLK adjacent to analog input traces.
- Pour top and bottom copper floods on all unused areas — DGND on digital board, separate DGND/AGND pours on analog board.
- Use stitching vias between ground planes at regular intervals (≤5mm grid) on digital board.

---

## 6. Key Components Summary

| Component | Part / Value | Qty | JLCPCB # | Board |
|---|---|---|---|---|
| ESP32-S3-WROOM-1-N16R8 | Master module, PCB antenna | 1 | C2913202 | Digital |
| ESP32-S3-WROOM-1U-N16R8 | Slave modules, U.FL (unpopulated) | 4 | C3013946 | Digital |
| ES8388 | Stereo audio codec, QFN-28-EP (4x4mm) | 5 | C365736 — ~$0.67 @ 100+, Economic PCBA | Digital |
| BQ25798RQMR | 2S LiPo charger IC with integrated USB-C PD | 1 | TBC by designer | Digital |
| 74HC4052 (or equiv.) | Dual 4:1 analog mux for UART | 1 | TBC by designer | Digital |
| LDO (3V3_ANA) | LP5907MFX-3.3 or TLV70233 | 1 | TBC by designer | Digital |
| Buck converter (3V3_DIG) | TPS62125 or equiv, 2A+ | 1 | TBC by designer | Digital |
| USB-C connector | Through-hole or SMD, 2.54mm holes | 1 | TBC by designer | Digital |
| USBLC6-2SC6 | USB ESD protection | 1 | TBC by designer | Digital |
| OPA2134U | Low-noise dual op-amp SOIC-8 SMD — preamp stages + line out buffers | 5 | TBC by designer | Analog |
| Nidec ST-4EA 10kΩ | SMD top-adjust trim pot, 4×4mm — one per input channel | 8 | C132879 | Analog |
| 2×20 header (male) | 2.54mm pitch, 40-pin | 1 | TBC by designer | Digital |
| 2×20 header (female) | 2.54mm pitch, 40-pin | 1 | TBC by designer | Analog |

---

## 7. Notes for PCB Designer

- This is a prototype/development revision. Prioritise correctness and debuggability over board density.
- All SMD components should be on the top side of each board where possible, to allow single-side reflow.
- The 5 ESP32-S3 WROOM modules require Standard PCBA at JLCPCB (not Economic). X-ray inspection is required for these parts — JLCPCB handles this automatically.
- All modules have MSL3 rating — baking may be required if stored before assembly. Flag this to JLCPCB at order time.
- Include test points on: 3V3_DIG, 3V3_ANA, VBAT, MCLK, TDM BCLK, LRCLK, each TDM DATA line, I2C SDA/SCL, and USB D+/D−.
- Include 100nF decoupling caps on every power pin of every IC, placed as close as possible to the pin.
- Add 10µF bulk decoupling near each ESP32-S3 module.
- Silkscreen all 2.54mm pad groups clearly with signal names.
- Schematic and BOM to be shared with client for review before layout begins.
- Board outline should include 3mm mounting holes at corners if space permits.

---

*Revision 0.1 — Draft. All part numbers and values subject to change during schematic review.*
