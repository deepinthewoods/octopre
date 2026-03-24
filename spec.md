# PCB Design Specification

## 8-Channel Audio DSP System

**Revision 1.2 · Draft for PCB Designer**

---

## 1. System Overview

This document specifies a two-board audio DSP system comprising a Digital Board and an Analog Board. The system captures up to 8 stereo input channels (plus a stereo line input on the master) via per-channel preamps, performs per-channel and global DSP across five ESP32-S3 processors, and outputs processed audio via headphone and line outputs.

Each slave ESP32+ES8388 pair processes two input channels, applies DSP, and outputs via the ES8388 DAC to an analog overdrive stage (LM13700 OTA) on the analog board. The 8 overdriven outputs are summed to stereo on the analog board and fed back to the master ES8388 ADC. The master ESP32 performs software mixing and outputs via its ES8388 DAC to the headphone and line output stages.

Each ESP32-S3 controls its own ES8388 codec via a dedicated I2S bus. The four slave ESP32-S3 modules additionally output audio to the master ESP32 via a shared TDM bus for software mixing.

The system is powered by a 2S LiPo battery with onboard USB-C charging and programming. All external connections are 2.54mm through-hole pads suitable for soldering DuPont headers or direct wire attachment.

---

## 2. Board Specifications

### 2.1 Common to Both Boards

| Parameter | Specification |
|---|---|
| Board dimensions | 70 × 55 mm |
| Layer count | 6-layer, double-sided |
| Stackup | Signal / GND / Signal / Power / GND / Signal — confirmed available at JLCPCB (select specific prepreg/core variant via JLCPCB impedance calculator) |
| PCB thickness | 1.6 mm |
| Minimum trace width | 0.1 mm (signal), 0.3 mm (power) |
| Surface finish | ENIG (required for consistent QFN reflow on ES8388, SC8922, TPS62140, TPS7A4700, TPS7A39 exposed pads) |
| Default passive package — resistors | **0402** (1005 metric) unless otherwise specified per-component |
| Default passive package — capacitors ≤100nF | **0402** (1005 metric) X7R/C0G |
| Default passive package — capacitors 1µF | **0603** (1608 metric) X7R minimum |
| Default passive package — capacitors 10µF ceramic | **0805** (2012 metric) X7R/X5R — see DC bias derating notes |
| Default passive package — capacitors 22µF+ ceramic | **0805 or 1206** — verify effective capacitance under DC bias before sizing down |
| Default passive package — electrolytics | Size per capacitance/voltage — cannot be substituted with smaller ceramic without functional impact |
| Solder mask | Both sides |
| Manufacturing | JLCPCB Standard PCBA |

### 2.2 Board Interconnect Headers

The two boards connect face-to-face (sandwich configuration) via **five separate 2.54mm pitch headers** — one per ESP32+ES8388 module pair. This allows shorter analog signal paths and more flexible routing.

Signals crossing the connectors are purely analog (audio signals, PWM control) plus power and ground. No I2S or high-frequency digital signals cross between boards.

**Master header (1× 2×6, 12-pin):**

| Pin | Signal | Direction | Notes |
|---|---|---|---|
| 1 | GND | Common | Ground |
| 2 | GND | Common | Ground |
| 3 | AIN_L | Analog → Digital | Master stereo line input left (to ES8388 ADC) |
| 4 | AIN_R | Analog → Digital | Master stereo line input right (to ES8388 ADC) |
| 5 | DAC_L | Digital → Analog | Master ES8388 DAC left (to line output buffer) |
| 6 | DAC_R | Digital → Analog | Master ES8388 DAC right (to line output buffer) |
| 7 | HP_L | Digital → Analog | ES8388 headphone amp left |
| 8 | HP_R | Digital → Analog | ES8388 headphone amp right |
| 9 | GND | Common | Ground |
| 10 | GND | Common | Ground |
| 11 | VBAT | Digital → Analog | Raw battery voltage (6.0–8.4V) for analog board power supply |
| 12 | 5V_ANA | Analog → Digital | Clean 5V from TPS7A4700 on analog board, feeds TPS7A2033 3V3_ANA LDO on digital board for ES8388 AVDD |

**Slave headers (4× 2×5, 10-pin each):**

| Pin | Signal | Direction | Notes |
|---|---|---|---|
| 1 | GND | Common | Ground |
| 2 | GND | Common | Ground |
| 3 | AIN_L | Analog → Digital | Preamp output left (to ES8388 ADC) |
| 4 | AIN_R | Analog → Digital | Preamp output right (to ES8388 ADC) |
| 5 | DAC_L | Digital → Analog | ES8388 DAC left (to LM13700 overdrive) |
| 6 | DAC_R | Digital → Analog | ES8388 DAC right (to LM13700 overdrive) |
| 7 | GND | Common | Ground |
| 8 | GND | Common | Ground |
| 9 | PWM_L | Digital → Analog | Overdrive control left (ESP32 PWM → LM13700 bias) |
| 10 | PWM_R | Digital → Analog | Overdrive control right (ESP32 PWM → LM13700 bias) |

> **NOTE:** Pin ordering places ground pins as shields between analog signal groups and PWM control lines. Designer to add series resistors (33Ω, **0402**) on PWM control lines at the connector. VBAT is carried only on the master header — the analog board distributes it internally to the power supply.
>
> **GROUNDING:** All header ground pins are common GND — there is no separate AGND on the headers. The analog board maintains its own internal AGND/DGND split topology with a star-point join (see Section 6). Carrying separate AGND through the headers would create a ground loop via the parallel GND return path and must be avoided.

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

Five ES8388 stereo audio codecs, one per ESP32-S3. All codecs reside on the digital board. Each ES8388 is controlled exclusively by its paired ESP32-S3 via a dedicated I2S bus — there is no shared codec control bus.

| Designator | Part | Package | Paired With | Role |
|---|---|---|---|---|
| U6 | ES8388 | QFN-28 (4×4mm) | U1 (Master) | Master codec — stereo line in (ADC), stereo mix out (DAC), headphone amp |
| U7 | ES8388 | QFN-28 (4×4mm) | U2 (Slave 1) | Slave codec — 2ch audio input (ADC) + 2ch audio output (DAC) |
| U8 | ES8388 | QFN-28 (4×4mm) | U3 (Slave 2) | Slave codec — 2ch audio input (ADC) + 2ch audio output (DAC) |
| U9 | ES8388 | QFN-28 (4×4mm) | U4 (Slave 3) | Slave codec — 2ch audio input (ADC) + 2ch audio output (DAC) |
| U10 | ES8388 | QFN-28 (4×4mm) | U5 (Slave 4) | Slave codec — 2ch audio input (ADC) + 2ch audio output (DAC) |

> **NOTE:** ES8388 requires a low-noise analog supply (AVDD). Route AVDD from a dedicated LDO with LC filtering. Keep ES8388 analog ground pour as a local island on the digital board, connected to the main digital ground at a single point near each ES8388's AGND pin. The island should extend just far enough to cover the ES8388 analog pin decoupling caps (**100nF 0402 X7R** per analog power pin, **10µF 0805 X7R** bulk per codec) and the AVDD LDO output filter — no further.

**ES8388 I2S connections (per ESP32+ES8388 pair):**

Each ESP32-S3 has a dedicated I2S connection to its own ES8388. These are point-to-point links — not bussed.

- MCLK: from paired ESP32-S3 to its own ES8388 only
- BCLK: from paired ESP32-S3 to its own ES8388 only
- LRCLK (WS): from paired ESP32-S3 to its own ES8388 only
- SDIN (to codec ADC): from paired ESP32-S3 to its own ES8388 only
- SDOUT (from codec DAC): from paired ES8388 to its own ESP32-S3 only

> **NOTE:** The master ESP32 (U1) drives a single MCLK output, star-routed to both its own ES8388 (U6) and the four slave ESP32-S3 modules (U2–U5) via the TDM bus. Series 22–33Ω damping resistors (**0402**) are placed at the source before each star branch. The master ESP32 uses one I2S peripheral for its dedicated codec bus (BCLK, LRCLK, SDIN, SDOUT to U6) and a second I2S peripheral for the TDM bus (BCLK, LRCLK, DATA×4 to slaves). The MCLK output pin is shared between both peripherals — only one physical MCLK line exists.

### 3.3 TDM Bus

The four slave ESP32-S3 modules (U2–U5) output audio via I2S TDM to the master (U1). Each slave occupies two TDM slots (stereo). Clock master is U1. This bus carries inter-processor audio data only — it is separate from the per-codec I2S buses in Section 3.2.

| Signal | Direction | Note |
|---|---|---|
| BCLK | U1 → U2–U5 | Shared clock — series 33Ω (**0402**) at source |
| LRCLK | U1 → U2–U5 | Shared frame sync — series 33Ω (**0402**) at source |
| DATA (×4) | U2–U5 → U1 | One data line per slave |
| MCLK | U1 → U2–U5 | 256× or 512× Fs — star topology, series 22–33Ω (**0402**) damping resistor at source before each branch |

> **NOTE:** Keep TDM data lines short and matched in length (within 1–2mm). At 44.1kHz × 32bit × 8slot = ~11.3MHz BCLK, trace impedance and crosstalk matter. Route with ground stitching vias alongside signal traces. Maintain ≥3mm clearance between TDM traces and ES8388 analog input traces.

### 3.4 UART Programming Mux

A 4-channel UART multiplexer allows the master ESP32 to bridge USB-CDC UART to any slave for firmware flashing. GPIO-controlled mux IC (e.g. 74HC4052 or equivalent dual 4:1 mux) routes TX/RX. GPIO0 and EN (reset) lines from master to each slave are required for bootloader entry.

| Signal | From | To | Note |
|---|---|---|---|
| USB_TX / USB_RX | USB-C (native USB) | Master U1 | Primary programming port |
| UART_TX / UART_RX | Master U1 | Mux input | Bridged via firmware |
| MUX_A / MUX_B | Master U1 GPIO | Mux select pins | 2 GPIOs select 1-of-4 slave |
| GPIO0 (×4) | Master U1 GPIO | Each slave GPIO0 | Bootloader entry |
| EN / RST (×4) | Master U1 GPIO | Each slave EN pin | Reset control |

### 3.5 Power System

#### 3.5.1 Battery & Charger

| Parameter | Specification |
|---|---|
| Battery | 2S LiPo (7.4V nominal, 8.4V max, 6.0V cutoff) |
| Battery connector | JST-PH 2.0mm 2-pin |
| Charger IC | SC8922QDLR (Southchip Semiconductor) |
| JLCPCB # | C252426 |
| Charge input | USB-C VBUS (5V) — same port as programming |
| Charge topology | Synchronous boost, steps up 5V USB to 8.4V for 2S charging |
| Cell count selection | CSEL pin — leave open for 8.4V (2S) target |
| Max charge current | 1A, set via 12kΩ 1% resistor (**0402**) on ICHG pin to GND. Per SC8922 datasheet: ICC = K × VREF / RICHG where K = 10000, VREF = 1.2V → RICHG = 12kΩ for 1A. Suitable for ≥1000mAh 2S packs (1C or less). To change charge current for different battery capacity, substitute RICHG: 6kΩ → 2A, 24kΩ → 0.5A |
| Input current limit | 2A max (internal VINREG regulates input current to prevent USB overload) |
| Power path | SC8922 provides power path management via VSYS pin — system can run from USB while charging. Battery supplements system power when USB current is insufficient (supplement mode) |
| Cell balancing | SC8922 includes integrated 2S cell balance function |
| NTC thermistor | Optional — connect NTC pin to battery thermistor or short to GND to disable. For prototype: short to GND. Pads provided for optional NTC (10kΩ B3950 or equivalent) |
| Charge status | PG pin — active low during charge, high when complete. Connect to status LED |
| Interface | Standalone — no I2C or firmware required. All parameters set by external resistors |

> **NOTE:** The SC8922 QFN-24 (4×4mm) has an exposed thermal pad. This must be soldered to a ground copper pour with ≥4 thermal vias (0.3mm drill). At 1A boost charging from 5V to 8.4V, the SC8922 dissipates meaningful power and requires adequate thermal relief.
>
> **PROTECTION:** Add a separate 2S battery protection IC (HY2120-CB, JLCPCB C116509) with dual back-to-back MOSFETs (FS8205A, JLCPCB C908265) between the battery connector and the SC8922 BAT pins. This provides over-charge, over-discharge, over-current, and short-circuit protection independent of the charger IC. The SC8922's cell balance function does not replace the need for per-cell protection.

#### 3.5.2 Power Rails

| Rail | Voltage | Source | Consumers | Notes |
|---|---|---|---|---|
| VBAT | 6.0–8.4V | 2S LiPo | Buck converter (digital board), pre-regulator buck + TPS7A4700 LDO (analog board via master header) | Fused, reverse polarity protected. SC8922 VSYS provides power path during USB charging |
| 3V3_DIG | 3.3V | TPS62140 buck converter from VBAT | All 5 ESP32-S3 modules, ES8388 DVDD, logic ICs, UART mux | TPS62140RGTR (JLCPCB C129366), 3–17V input, 2A output, QFN-16 3×3mm. 2A is sufficient — only master ESP32 runs WiFi, slaves have antenna disconnected/disabled |
| 3V3_ANA | 3.3V | Ultra-low-noise LDO from 5V_ANA | ES8388 AVDD (on digital board only) | TPS7A2033PDBVR (JLCPCB C2862740), SOT-23-5, 300mA, 10µVrms noise, 65dB PSRR @ 100kHz, 140mV dropout. Input from 5V_ANA via master interconnect header. LC filter on output (**10µH 0805 inductor + 10µF 0805 X7R cap**) |
| 6V_PRE | ~6.0V | TPS62140 buck converter from VBAT (analog board) | TPS7A4700 input only | Pre-regulator buck on analog board within DGND island. Reduces TPS7A4700 input voltage to ~6V regardless of battery state — see Section 4.2 for detailed description |
| 5V_ANA | 5.0V | TPS7A4700 ultra-low-noise LDO from 6V_PRE | LM2776 charge pump, TPS7A39 positive input (analog board), TPS7A2033 3V3_ANA LDO (digital board) | TPS7A4700RGWR (JLCPCB C114839), VQFN-20 5×5mm, 1A, max input 36V, 4µVrms noise, 78dB PSRR, 307mV dropout. Located on analog board. Output voltage set to 5.0V via ANYOUT pin strapping (short 3.2V + 0.4V pins, all others open = 1.4 + 3.2 + 0.4 = 5.0V). Pre-regulated input at ~6V gives max dissipation of (6.0V−5.0V) × 0.3A = 0.3W — see Section 4.2 for thermal analysis |
| −5V_RAW | approx. −5V (unregulated) | LM2776 charge pump from 5V_ANA | TPS7A39 negative input only | LM2776DBVR (JLCPCB C69527), SOT-23-6, 200mA, 2MHz switching. Unregulated inverting charge pump — output is approximately −5V_ANA plus losses (typ. −4.6V at 150mA load). Output noise is rejected by TPS7A39 negative LDO (≥50dB PSRR at 2MHz). Three external ceramic caps required (C_IN, C_FLY, C_OUT — all 1µF X7R minimum). Place adjacent to TPS7A4700 in power supply corner |
| +3.0V | +3.0V | TPS7A39 positive LDO from 5V_ANA | All OPA2134 op-amps (V+), LM13700 OTAs (V+), summing amplifier (V+) | TPS7A3901DSCR (JLCPCB C2685819), WSON-10 3×3mm. Positive output set to +3.0V via external feedback resistors R1/R2. 150mA max. 21µVrms noise, 69dB PSRR @ 120Hz, ≥50dB PSRR to 2MHz |
| −3.0V | −3.0V | TPS7A39 negative LDO from −5V_RAW | All OPA2134 op-amps (V−), LM13700 OTAs (V−), summing amplifier (V−) | Same TPS7A3901DSCR. Negative output set to −3.0V via external feedback resistors R3/R4. 150mA max. Ratiometric startup tracking ensures both rails come up together — eliminates op-amp latch-up risk during power-on |
| 1V8 | 1.8V | ES8388 DVDD accepts 1.8–3.3V | ES8388 digital core — DVDD pin | ES8388 does not have an internal 1.8V LDO. DVDD is fed directly from 3V3_DIG in this design. Requires 10µF + 100nF bypass caps on DVDD pin of each ES8388. Note: if LRCK frequency were below 16kHz, a 1.8V DVDD supply would be required to avoid noise — not applicable at 44.1kHz |
| 5V_USB | 5V | USB-C VBUS | SC8922 input (VIN) | Protected with TVS diode |

> **NOTE:** VBAT is routed to the analog board via the master interconnect header only. The analog board generates its own regulated bipolar supply locally — see Section 4.2. The digital and analog power paths are completely separate: VBAT → TPS62140 buck → 3V3_DIG (digital board), VBAT → pre-regulator buck → TPS7A4700 → 5V_ANA → TPS7A39/LM2776 → ±3.0V (analog board). No digital supply rail crosses to the analog board.
>
> **NOTE:** The 3V3_ANA rail for ES8388 AVDD on the digital board is fed from the 5V_ANA intermediate rail via the TPS7A2033PDBVR LDO. This provides two-stage dropout: 8.4V → 6V (pre-regulator buck, on analog board) → 5V (TPS7A4700, on analog board) → 3.3V (TPS7A2033, on digital board). The TPS7A2033 dissipation is (5V−3.3V) × 0.1A = 0.17W. Route the 5V_ANA rail from the analog board to the digital board via pin 12 on the master interconnect header.
>
> **NOTE: 5V_ANA CURRENT BUDGET.** The total load on the 5V_ANA rail is significantly higher than just the TPS7A39 positive rail current. All loads: TPS7A39 positive rail (~100mA), LM2776 charge pump input supplying the TPS7A39 negative rail (~110mA including losses), TPS7A2033 on digital board for ES8388 AVDD (~50mA for 5 codecs), TPS7A39 quiescent (~3mA). Total: ~260mA typical, up to ~300mA worst case. The pre-regulator buck and TPS7A4700 are both rated for 1A+ and have ample headroom.
>
> **NOTE: TPS7A39 CURRENT BUDGET WARNING.** The TPS7A39 is rated at 150mA per rail. Estimated analog current is 90–120mA per rail (6× OPA2134 dual @ ~4mA/section = 48mA, 4× LM13700 @ ~10mA = 40mA, TPS7A39 quiescent ~1.5mA, plus signal currents). This provides 20–40% margin. If prototype measurement shows consumption exceeding 130mA on either rail, the TPS7A39 must be replaced with separate TPS7A4700 (positive, 1A) + TPS7A3301 (negative, 200mA) LDOs. Measure ±3.0V rail currents during full-load testing (all 8 channels active, overdrive at maximum bias) before committing to production layout.

#### 3.5.3 TPS62140 Thermal Note (Digital Board)

The TPS62140 QFN-16 (3×3mm) has an exposed thermal pad that must be soldered to a ground copper pour with ≥4 thermal vias (0.3mm drill). At full digital load (~1–1.5A), the buck dissipates ~0.15–0.3W depending on battery voltage. Place the inductor and input/output capacitors directly adjacent to the IC per the TPS62140 datasheet recommended layout. Keep the input current loop (VIN cap → IC → inductor → output cap → GND return) as tight as possible.

### 3.6 USB-C Interface

| Parameter | Specification |
|---|---|
| Connector | USB-C, TYPE-C-31-M-12 (Korean Hroparts), 16-pin SMD (JLCPCB C165948) |
| Function | Programming (USB-CDC) + 2S LiPo charging (5V only, no PD) |
| USB bridge | Use ESP32-S3 native USB-CDC (no external IC required) on master U1 |
| ESD protection | TVS diode array on VBUS and data lines (e.g. USBLC6-2SC6) |
| CC resistors | 5.1kΩ (**0402**) on CC1 and CC2 to GND for USB-C sink identification. These are standard pull-downs — the SC8922 charger has no CC pins and is not involved in USB-C negotiation |
| D+/D− | Connected to ESP32-S3 native USB for CDC. Not connected to SC8922 (SC8922 has no D+/D− detection) |

### 3.7 Digital Board I/O — 2.54mm Through-Hole Pads

| Pad/Header | Signals | Count | Notes |
|---|---|---|---|
| USB-C connector | VBUS, D+, D−, CC1, CC2, GND | — | Panel-edge preferred |
| Battery connector | VBAT+, GND | 2 pins | JST-PH or through-hole pads |
| Master interconnect | See Section 2.2 | 12 pins (2×6) | 2.54mm pitch header |
| Slave interconnects (×4) | See Section 2.2 | 10 pins (2×5) each | 2.54mm pitch headers |
| Debug/JTAG header | TDI, TDO, TCK, TMS, GND, 3V3 | 6 pins | Master ESP32-S3 only |
| Status LEDs | Charge status, power good, user LED | 3× | On-board, not on header |

---

## 4. Analog Board

### 4.1 Input Preamp — 8 Channels

Eight identical input preamp channels, each accepting unbalanced line-level or instrument-level signal via 2.54mm through-hole pads. Two channels (CH1 and CH2) additionally support electret condenser microphone input via a switchable bias circuit.

| Parameter | Specification |
|---|---|
| Topology | Non-inverting op-amp stage per channel |
| Op-amp | OPA2134U (dual, SOIC-8 SMD) — one per 2 channels |
| Supply | ±3.0V regulated bipolar supply (see Section 4.2) |
| Input impedance | ≥100kΩ (suitable for both line and electret mic source) |
| Gain | Variable 0 to +30dB via Nidec ST-4EA 10kΩ SMD trim pot per channel — top-adjust, 4×4mm SMT footprint, reflow solderable |
| Input coupling | AC coupled — 10µF electrolytic or **0805 X5R ceramic** input cap per channel |
| Input protection | Schottky clamp diodes to V+ and V− rails (**SOD-323** or smaller) |
| Output | DC coupled to ES8388 analog input on digital board via per-module interconnect header |

### 4.2 Analog Board Power Supply — Pre-Regulated Bipolar Rails

The analog board generates its own clean bipolar supply from VBAT received via the master interconnect header. A four-stage architecture provides noise isolation and thermal management:

1. A synchronous buck converter pre-regulates VBAT down to ~6V, absorbing the variable battery voltage drop efficiently as a switching converter and reducing the thermal load on the downstream LDO.
2. An ultra-low-noise LDO steps the pre-regulated ~6V down to a clean 5.0V intermediate rail (5V_ANA), filtering the buck converter's output ripple to produce a pristine analog supply reference.
3. An unregulated charge pump inverts the 5V_ANA rail to generate a raw negative voltage (~−4.6V).
4. A dual high-PSRR LDO generates regulated ±3.0V from the 5V_ANA and −5V_RAW rails for all analog stages.

**Power chain:**

```
VBAT (6.0–8.4V)
  │
  ▼
TPS62140 buck pre-regulator ──→ ~6V (6V_PRE)
  │                                │
  │  [switching noise contained    │
  │   within DGND island]         ▼
  │                          TPS7A4700 LDO ──→ 5.0V (5V_ANA)
  │                            (4µVrms)          │
  │                                              ├──→ TPS7A39 positive input ──→ +3.0V
  │                                              ├──→ LM2776 charge pump ──→ −5V_RAW
  │                                              │                              │
  │                                              │                              ▼
  │                                              │         TPS7A39 negative input ──→ −3.0V
  │                                              │
  │                                              └──→ Master header pin 12 ──→ digital board
  │                                                    ──→ TPS7A2033 ──→ 3V3_ANA (ES8388 AVDD)
```

#### 4.2.1 Pre-Regulator Buck Converter (NEW in v1.1)

| Parameter | Specification |
|---|---|
| IC | TPS62140RGTR (JLCPCB C129366) — same part as digital board 3V3_DIG buck |
| Package | QFN-16 3×3mm |
| Input | VBAT (6.0–8.4V) from master header |
| Output | ~6.0V, set via external feedback resistor divider |
| Switching frequency | 2.5MHz (force PWM mode via FSEL pin — do not allow pulse-skipping at light loads) |
| Output current | ~300mA typical (5V_ANA total load), well within 2A rating |
| Inductor | 2.2µH, shielded drum-core or moulded ferrite, ≤3.2×3.2mm footprint, ≥600mA saturation rating. **SHIELDED INDUCTOR REQUIRED — DO NOT SUBSTITUTE UNSHIELDED** |
| Input capacitor | 10µF X7R ceramic (**0805**) + 100nF X7R ceramic (**0402**), placed directly at VIN pin |
| Output capacitor | 22µF X7R ceramic (**0805 or 1206** — verify effective capacitance ≥15µF at 6V DC bias) + 100nF X7R ceramic (**0402**) — this cap is shared with (or placed immediately adjacent to) the TPS7A4700 input capacitor |
| Purpose | Reduces the voltage drop across the TPS7A4700 from up to 3.4V (at full battery) to a fixed ~1.0V, cutting LDO dissipation from 1.0W+ to ~0.3W. The TPS7A4700 then operates as a post-DC-DC ripple filter — the topology it was explicitly designed for |

> **NOTE: WHY A PRE-REGULATOR IS NEEDED.** The 5V_ANA rail feeds three downstream loads: the TPS7A39 positive rail (~100mA), the LM2776 charge pump (~110mA including losses for the negative rail), and the TPS7A2033 on the digital board (~50mA for 5× ES8388 AVDD). Total 5V_ANA load is ~260mA typical, up to ~300mA worst case. Without the pre-regulator, TPS7A4700 dissipation at full battery would be (8.4V−5.0V) × 0.3A = 1.02W. With θJA of ~40–50°C/W on this small board (70×55mm, limited DGND island copper), junction temperature at 40°C ambient would reach 81–91°C — uncomfortably close to derating limits and degrading noise performance. The pre-regulator buck absorbs the variable voltage drop at >90% efficiency, reducing LDO dissipation to a fixed ~0.3W regardless of battery state.
>
> **NOTE: CONDUCTED NOISE PATH.** The TPS62140 at 2.5MHz produces ~10–30mV peak-to-peak output ripple depending on load. The TPS7A4700 provides ≥55dB PSRR across 10Hz–10MHz, attenuating this to ~50µV at the 5V_ANA output. The TPS7A39 provides a further ≥50dB PSRR. Total conducted noise rejection from buck output to ±3.0V analog rails is ~100dB+. This is superior to the current design where VBAT arrives from the digital board carrying the TPS62140 digital-side buck noise through a long header pin and PCB trace with no pre-filtering.
>
> **NOTE: SWITCHING FREQUENCY SELECTION.** The buck operates at 2.5MHz, which is close to the LM2776 charge pump frequency (2MHz). This avoids introducing new spectral content — both switching sources produce harmonics in the same frequency band, where the TPS7A4700 and TPS7A39 PSRR curves remain effective. A lower frequency (e.g. 500kHz) would need a larger inductor, radiate more, and produce harmonics closer to the audio band. A much higher frequency (4MHz+) would create more aggressive switch-node edges and reduce efficiency.
>
> **NOTE: PWM MODE.** The FSEL pin of the TPS62140 must be configured to force continuous PWM mode (connect to VIN). In power-save mode, the TPS62140 uses pulse-skipping at light loads, which produces variable-frequency switching that is harder to filter. At ~300mA load, the converter is always above the pulse-skip threshold, but forcing PWM mode ensures deterministic switching noise under all conditions.

#### 4.2.2 TPS7A4700 Ultra-Low-Noise LDO — 5V_ANA

| Parameter | Specification |
|---|---|
| IC | TPS7A4700RGWR (JLCPCB C114839) |
| Package | VQFN-20 (5×5mm), exposed thermal pad |
| Input | ~6.0V from pre-regulator buck (6V_PRE) |
| Output | 5.0V (5V_ANA) |
| Output voltage programming | ANYOUT pin strapping: short the 3.2V and 0.4V pins to GND. Leave all other ANYOUT pins open (no connect). VOUT = VREF + 3.2V + 0.4V = 1.4 + 3.2 + 0.4 = 5.0V. Refer to TPS7A4700 datasheet Table 2 for pin-to-voltage mapping. Double-check strapping before fabrication — incorrect configuration will produce wrong voltage |
| Noise | 4µVrms (10Hz–100kHz) |
| PSRR | 82dB @ 100Hz, ≥55dB across 10Hz–10MHz |
| Dropout | 307mV @ 1A (less at 300mA — ~200mV typical) |
| Max load | ~300mA (5V_ANA total — see current budget in Section 3.5.2) |
| Thermal dissipation | (6.0V − 5.0V) × 0.3A = 0.3W worst case. With θJA ~40–50°C/W on this board, junction temperature rise is 12–15°C above ambient — no thermal concern |
| Thermal pad | VQFN-20 exposed pad must be soldered to DGND island copper pour with ≥6 thermal vias (0.3mm drill). Although thermal dissipation is now modest (0.3W vs. the original 1.0W+), good thermal connection to the ground pour is still required for reliable operation and maintains a heat-spreading path that benefits the entire DGND island |
| Input decoupling | 10µF X7R (**0805**) + 100nF X7R (**0402**) ceramic, placed directly at VIN pin. The buck output capacitor may serve as or supplement this — place both as close to the TPS7A4700 VIN pin as possible |
| Output decoupling | 10µF X7R (**0805**) + 100nF X7R (**0402**) ceramic at VOUT pin. Additional 47µF bulk ceramic (**1206** X5R) or tantalum within 5mm |
| NR pin | 1µF X7R ceramic (**0603**) from NR pin to GND for optimised noise and PSRR performance |

#### 4.2.3 LM2776 Inverting Charge Pump — −5V_RAW

| Parameter | Specification |
|---|---|
| IC | LM2776DBVR (JLCPCB C69527) |
| Package | SOT-23-6 |
| Input | 5V_ANA |
| Output | −5V_RAW (unregulated, approximately −4.6V at 150mA load) |
| Switching frequency | 2MHz |
| Purpose | Generates the raw negative supply for the TPS7A39 negative LDO input. The output is intentionally unregulated — charge pump ripple and switching noise are rejected by the TPS7A39's ≥50dB PSRR at 2MHz |
| External capacitors | C_IN 1µF X7R 10V (**0603**), C_FLY 1µF X7R 10V (**0603**), C_OUT 1µF X7R 10V (**0603**). All three mandatory. C_FLY traces ≤5mm, placed as close as possible to C1+ and C1− pins. C_IN at VIN pin, C_OUT at VOUT pin. **X7R REQUIRED — DO NOT SUBSTITUTE Y5V/Z5U** |
| Placement | Adjacent to TPS7A4700 within the DGND island power supply corner |

#### 4.2.4 TPS7A39 Dual Bipolar LDO — ±3.0V

| Parameter | Specification |
|---|---|
| IC | TPS7A3901DSCR (JLCPCB C2685819) |
| Package | WSON-10 (3×3mm) |
| Positive input | 5V_ANA (headroom: 5.0V − 3.0V = 2.0V, well above ~300mV dropout) |
| Negative input | −5V_RAW (headroom: 4.6V − 3.0V = 1.6V, well above ~400mV dropout) |
| Positive output | +3.0V, set via R1 = 180kΩ, R2 = 120kΩ feedback divider (gain = 1 + R1/R2 = 2.5, VOUT+ = 1.2V × 2.5 = 3.0V) |
| Negative output | −3.0V, set via R3 = 180kΩ, R4 = 120kΩ feedback divider (symmetrical with positive side) |
| Feedback resistors | 0.1% tolerance, **0402** package. Place directly adjacent to FB pins |
| Feed-forward capacitors | 10nF CFF (**0402** X7R) from each FB pin to corresponding OUT pin |
| NR/SS capacitor | 10nF (**0402** X7R) from NR/SS pin to GND — controls startup ramp rate |
| Output decoupling | 10µF X7R (**0805**) + 100nF X7R (**0402**) ceramic on each output rail, placed directly at OUT+ and OUT− pins. Additional bulk 100µF electrolytic (**6.3×5.4mm or smaller, 6.3V minimum**) on each rail within 10mm of the TPS7A39 |
| Input decoupling | 10µF X7R (**0805**) + 100nF X7R (**0402**) ceramic on each input rail (CIN+ at INP pin, CIN− at INN pin) |
| Noise | 21µVrms (10Hz–100kHz) |
| PSRR | 69dB @ 120Hz, ≥50dB across 10Hz–2MHz |
| Startup tracking | Ratiometric — both rails come up together, eliminating op-amp latch-up risk during power-on |
| Enable | EN pin connected to 5V_ANA (INP) for automatic enable at power-on. Enable threshold ~1.2V |
| Consumers | All OPA2134U preamp/buffer stages, all LM13700 overdrive stages, analog summing amplifier |
| Placement | Between the DGND island (power supply corner) and the signal path. GND pin connects to the AGND side of the star point. The TPS7A39 acts as the physical and electrical boundary between the switching power section and the clean analog section |

> **NOTE:** The ±3.0V rails give the OPA2134 (minimum ±2.5V) comfortable headroom — output swing at ±3.0V is approximately ±2.0V (1.4Vrms), well above the 1Vrms line output target. The LM13700 (minimum ±2V) also benefits from the additional margin.

#### 4.2.5 Power Supply Thermal Summary

| Component | Input | Output | Max Current | Max Dissipation | Thermal Mitigation |
|---|---|---|---|---|---|
| TPS62140 pre-regulator buck (analog board) | 6.0–8.4V (VBAT) | ~6.0V | 300mA | ~0.07W (switching losses at >90% efficiency) | QFN-16 thermal pad to DGND island, ≥4 thermal vias |
| TPS7A4700 LDO | ~6.0V | 5.0V | 300mA | 0.3W | VQFN-20 thermal pad to DGND island, ≥6 thermal vias |
| LM2776 charge pump | 5.0V | −4.6V | 110mA | ~0.06W (charge pump losses) | SOT-23-6, minimal dissipation |
| TPS7A39 dual LDO | +5.0V / −4.6V | ±3.0V | 120mA per rail | ~0.43W total (0.24W positive + 0.19W negative) | WSON-10 thermal pad on AGND side of star point |
| TPS7A2033 LDO (digital board) | 5.0V | 3.3V | 50mA | 0.09W | SOT-23-5, minimal dissipation |
| **Total analog power path** | | | | **~0.95W** | Distributed across analog + digital boards |

### 4.3 Electret Microphone Bias (CH1 & CH2)

Channels 1 and 2 support optional electret condenser microphone input. A bias resistor network provides the required DC bias voltage. The mic input and line input share the same 2.54mm pads — the user selects the source by populating the appropriate input.

| Parameter | Specification |
|---|---|
| Mic type | 3.5mm electret condenser (standard PC/headset type) |
| Bias voltage | ~2.5V derived from V+ rail via 2.2kΩ (**0402**) bias resistor |
| AC coupling | 1µF (**0603** X7R) series cap between bias node and preamp input |
| Input pads | Shared 2.54mm through-hole pads with line input (CH1 and CH2 only) |
| Designators | MIC_IN_1, MIC_IN_2 — labelled on silkscreen |

### 4.4 Overdrive Stage — 8 Channels (LM13700 OTA)

Eight channels of digitally-controlled analog overdrive, post-DAC, using LM13700 dual operational transconductance amplifiers. The overdrive character is controlled per-channel via PWM signals from the ESP32-S3 modules.

| Parameter | Specification |
|---|---|
| Topology | LM13700 OTA per channel — signal input to OTA, output via linearizing diodes and buffer |
| IC | LM13700M/NOPB (dual OTA, SOIC-16) — 4 packages for 8 channels |
| Supply | ±3.0V regulated bipolar supply (see Section 4.2) |
| Signal input | ES8388 DAC output from slave interconnect headers |
| Signal output | Feeds analog summing bus (see Section 4.5) |
| Control input | PWM from ESP32 GPIO, RC low-pass filtered (1kΩ **0402** + 100nF **0402** X7R, fc ≈ 1.6kHz) to DC, fed through resistor to I_ABC (amplifier bias current) pin. ESP32 PWM frequency must be ≥40kHz to ensure adequate attenuation (≥25dB) at the filter output |
| Control range | 0–3.3V PWM (3.3V logic level from ESP32) → 0 to ~330µA bias current via 10kΩ (**0402**) resistor. Sweeps from clean (low bias) to full saturation (high bias) |
| Overdrive character | Soft clipping / tanh-like saturation, musically smooth. Controlled continuously from clean to saturated. Fast ~1ms response enables per-note envelope following and tremolo effects |

**Per-channel circuit:**

- ESP32 PWM pin → 33Ω series resistor (**0402**, at header connector, digital board side) → header → 1kΩ (**0402**) + 100nF (**0402** X7R) RC filter (on analog board side) → 10kΩ (**0402**) series resistor → LM13700 I_ABC pin
- DAC output → AC coupling cap (**1µF 0603 X7R**) → LM13700 signal input
- LM13700 output → linearizing diode network → LM13700 internal buffer → summing bus

> **NOTE:** Place LM13700 packages close to their corresponding slave headers to minimise analog trace lengths. The LM13700 linearizing diodes should be connected for improved THD at low overdrive settings. Bypass each LM13700 V+ and V− pin with 100nF ceramic (**0402** X7R) directly at the pin — additionally add 10µF (**0805** X7R) on V− at each LM13700 to suppress any residual ripple on the negative rail. The 1kΩ (**0402**) + 100nF (**0402** X7R) RC filter (fc ≈ 1.6kHz) gives ~1ms response for fast envelope-following and tremolo effects. ESP32 PWM frequency must be set to ≥40kHz in firmware to keep ripple well above audio band with ≥25dB attenuation at the filter.

### 4.5 Analog Summing Bus — Stereo

The 8 overdrive outputs (4 stereo pairs from 4 slave channels) are summed to a stereo pair on the analog board using a resistor summing network and a summing amplifier. The summed output is routed to the master ES8388 ADC input via the master interconnect header.

| Parameter | Specification |
|---|---|
| Topology | Inverting summing amplifier — one OPA2134U (dual) for stereo L+R summing |
| Input resistors | 4× matched 10kΩ (**0402**, 1% metal film) per summing channel (4 left signals summed, 4 right signals summed) |
| Feedback resistor | 10kΩ (**0402**, 1%) per channel (unity sum gain — equal mix of all 4 inputs), with Nidec ST-4EA 10kΩ SMD trim pot (4×4mm, top-adjust) in series for adjustable sum level |
| Output | AC coupled via 10µF cap (**0805** X5R ceramic or electrolytic) to master header AIN_L / AIN_R pins → master ES8388 ADC. AC coupling prevents DC offset from the summing amp eating into codec dynamic range and eliminates power-on click |
| Supply | ±3.0V regulated bipolar supply |

> **NOTE:** Use 1% tolerance metal film resistors (**0402**) for the summing network to maintain channel balance. The inverting topology introduces a phase inversion — this will be corrected in firmware on the master ESP32 (invert ADC samples after read). The feedback trim pot allows adjusting the overall summing level; set to midpoint (5kΩ) for unity sum gain by default.

### 4.6 Master Stereo Line Input

A dedicated stereo line input for the master ESP32+ES8388 pair. This receives the analog summed output of all 8 overdrive channels from the summing bus (Section 4.5), routed to the master ES8388 ADC via the master interconnect header. An alternative external line input is selectable via a 3-pin jumper header.

| Parameter | Specification |
|---|---|
| Source (default) | Analog summing bus output (Section 4.5) |
| Source (alternative) | External line input pads: LINE_IN_L, LINE_IN_R, GND — 2.54mm through-hole, 3 pads |
| Input selection | 3-pin 2.54mm header per channel (×2, one for L and one for R). Centre pin connects to master header AIN_L / AIN_R. One outer pin connects to summing bus output, other outer pin connects to external line input pad. User bridges centre pin to one neighbour with a 2.54mm jumper cap to select source. Default: jumper bridges summing bus to AIN. Silkscreen label: "SUM" on summing bus side, "EXT" on external input side |
| Routing | Selected source → master header AIN_L / AIN_R → master ES8388 ADC input |

> **NOTE:** Place the two 3-pin jumper headers adjacent to the master interconnect header. Keep traces from both sources to the jumper short and equal length where practical. The jumper introduces negligible contact resistance (~50mΩ) at the signal levels involved. Label clearly on silkscreen — the user must not bridge both sources simultaneously.

### 4.7 Headphone Output

Stereo headphone output from master ES8388 built-in headphone amplifier. Output is carried from digital board via master interconnect header and filtered on the analog board before the output pads.

| Parameter | Specification |
|---|---|
| Source | ES8388 built-in HP amplifier (on digital board), via master header HP_L / HP_R |
| Load impedance | 32Ω to 300Ω headphones |
| Output coupling | AC coupled — 220µF electrolytic per channel at output pads (−3dB at ~22Hz into 32Ω). **Electrolytic required — do not substitute smaller ceramic; capacitance sets the low-frequency corner** |
| Output pads | HP_L, HP_R, GND — 2.54mm through-hole, 3 pads |
| Protection | PTC thermistor or 100mA polyfuse in series on each channel (**1206** or smaller SMD polyfuse) |

### 4.8 Line Output

Stereo line output from master ES8388 DAC, buffered by op-amp unity-gain stage on analog board. This is the master's mixed and processed output.

| Parameter | Specification |
|---|---|
| Source | Master ES8388 DAC output via master header DAC_L / DAC_R |
| Buffer topology | Unity-gain OPA2134U buffer per channel |
| Supply | ±3.0V regulated bipolar supply |
| Output impedance | 100Ω (set by series resistor (**0402**) at output) |
| Output level | ~1Vrms nominal at 0dBFS |
| Output coupling | AC coupled — 10µF cap per channel (**0805** X5R ceramic or electrolytic) |
| Output pads | LINE_L, LINE_R, GND — 2.54mm through-hole, 3 pads |

### 4.9 Analog Board I/O — 2.54mm Through-Hole Pads

All user-facing connections are 2.54mm pitch through-hole pads on the board edge. Silkscreen labels required on all pads.

| Pad Group | Signals | Pin Count | Notes |
|---|---|---|---|
| Audio inputs CH1–CH8 | IN_L, IN_R, GND per channel | 24 pins | CH1 & CH2 also accept electret mic |
| Mic bias (CH1 & CH2) | MIC_IN_1, MIC_IN_2, GND | Shared with CH1 & CH2 audio input pads above | Bias resistor fitted for CH1/CH2 |
| Master line input | LINE_IN_L, LINE_IN_R, GND | 3 pins | External line input pads |
| Line input selector | SUM/AIN/EXT per channel (×2) | 6 pins (2× 3-pin headers) | Jumper selects summing bus or external line input — see Section 4.6 |
| Headphone output | HP_L, HP_R, GND | 3 pins | Protected output |
| Line output | LINE_L, LINE_R, GND | 3 pins | Buffered, 100Ω |
| Master interconnect | See Section 2.2 | 12 pins (2×6) | Mates with digital board |
| Slave interconnects (×4) | See Section 2.2 | 10 pins (2×5) each | Mates with digital board |

---

## 5. Signal Flow Summary

```
SLAVE CHANNELS (×4 pairs, 8 channels total):

  Analog Input ──→ Preamp ──→ [Slave Header] ──→ ES8388 ADC ──→ ESP32 DSP
                                                                     │
                                          (dedicated I2S per pair)   │
                                                                     ▼
  Summing Bus ◄── LM13700 OD ◄── [Slave Header] ◄── ES8388 DAC ◄── ESP32 DSP
      │                                                              │
      │                                                    (TDM DATA to master)
      ▼
  Summing Amp ──→ [Master Header] ──→ Master ES8388 ADC ──→ Master ESP32
                                                                  │
                                              (dedicated I2S)     │
                                                              (Software Mix)
                                                                  │
                                                                  ▼
                                                          Master ES8388 DAC
                                                            │          │
                                                            ▼          ▼
                              HP Out ◄── [Master Header] ◄── DAC   HP Amp
                              Line Out ◄── Line Buffer ◄──────┘
```

---

## 6. Grounding & Shielding

### 6.1 Grounding Philosophy

A single ground reference (GND) is used at all board-to-board connections. The analog board uses a simplified grounding topology with a local ground island under the switching components (pre-regulator buck, TPS7A4700 LDO, and LM2776 charge pump) and a main AGND pour for all signal path components. The TPS7A39 dual LDO provides high-PSRR isolation (≥50dB) between the switching power section and the analog signal path, allowing a much simpler ground layout than would otherwise be required. No separate AGND is carried through the interconnect headers — doing so creates a ground loop via the parallel return path through GND header pins.

### 6.2 Digital Board Grounding

- The digital board uses a single continuous ground plane (GND) on layers 2 and 5 of the 6-layer stackup.
- Each ES8388 has a local analog ground island beneath and around its analog pins (AVDD, AVSS, analog I/O). This island connects to the main GND plane at a single point near the ES8388 AGND pin. The island should extend just far enough to cover the ES8388 analog pin decoupling caps and the AVDD LDO output filter — no further.
- 3V3_ANA power pour on the digital board must be a separate copper region from 3V3_DIG, connected via a ferrite bead (**0402**, 600Ω @ 100MHz, ≥300mA rated).
- Do not split the main ground plane on the digital board. Ground islands for ES8388 analog sections are local exceptions only.

### 6.3 Analog Board Grounding

- The analog board uses a single primary ground pour: **AGND**, serving all op-amp, OTA, signal path, and TPS7A39 LDO components.
- A **DGND island** (~20×25mm) is used under the pre-regulator buck converter, TPS7A4700, LM2776, and their associated passives in the power supply corner. This island contains all switching-frequency ground return currents from both the buck converter and the charge pump.
- The DGND island connects to the AGND pour at a **single star point** located between the power supply corner and the TPS7A39. The star point connection must be low impedance — use a wide trace (≥0.5mm) or multiple vias at a single defined location. The TPS7A39 GND pin connects to the AGND side of the star point.
- All header ground pins connect to AGND on the analog board — the signal path ground is the primary reference.
- The pre-regulator buck and LM2776 charge pump switching ground currents circulate within the DGND island. Only DC load current flows through the star point to AGND. This is ensured by keeping all switching current loops tight (input cap → IC → inductor/flying cap → output cap → GND return all within the island, with return vias immediately adjacent to each cap).
- VBAT power input from the master header enters via the DGND island, passes through the pre-regulator buck, then the TPS7A4700, then the LM2776, and the TPS7A39 outputs clean ±3.0V to the AGND side.

### 6.4 Board-to-Board Ground

- All GND pins on all five interconnect headers are common GND — no AGND/DGND distinction at the header.
- On the digital board side, header GND pins connect directly to the main GND plane.
- On the analog board side, header GND pins connect to the AGND pour (signal reference ground).
- The star-point join on the analog board provides the only connection between the DGND island and AGND pour on that board, preventing ground loops.

### 6.5 Copper Pours & Stitching

- Pour top and bottom copper floods on all unused areas — GND on digital board, AGND on analog board (with DGND island in power corner).
- Use stitching vias between ground planes at regular intervals (≤5mm grid) on the digital board.
- On the analog board, stitching vias within the AGND pour freely. Within the DGND island, stitch to DGND only. Never place stitching vias between AGND and DGND pours — they connect only at the star point.
- Route most sensitive analog signals (preamp inputs, ES8388 analog I/O) on layers 1 or 6 where they have an immediately adjacent unbroken ground plane (L2 or L5). Avoid routing sensitive analog on inner layer 3, which is referenced to GND above and PWR below.
- The DGND island must be solid, unbroken copper — no signal traces may be routed through the island on any layer. Slots or breaks in the pour force switching return currents to detour, increasing loop area and radiated EMI.

### 6.6 Signal Routing & RF Minimisation

- MCLK (up to 22.6MHz at 512×Fs) must be routed with a ground guard trace or on an inner layer with ground stitching. Add series damping resistors (22–33Ω, **0402**) at the source before each star branch to prevent stub ringing. Keep MCLK traces away from analog input traces — minimum 3mm clearance or ground pour moat.
- TDM bus traces (BCLK, LRCLK, DATA) must maintain ≥3mm clearance from ES8388 analog pins and interconnect header analog pins.
- PWM control lines: the 33Ω (**0402**) series resistors are placed at the connector on the digital board side for impedance damping. The RC low-pass filter (1kΩ **0402** + 100nF **0402** X7R, fc ≈ 1.6kHz) must be on the analog board side so that only filtered DC (not switching waveform) is present on analog board traces. Route PWM traces away from analog signal traces on the analog board.
- ESP32-S3 WiFi antenna (U1): ground plane must be continuous under the module body but fully removed under the antenna area on all layers. Verify JLCPCB assembly process does not add ground flood in the antenna keepout zone. No analog signal traces on any layer within the antenna keepout.
- **Pre-regulator buck converter (analog board):** The switch node trace must be kept as small as possible — minimum copper area, no via fanout. If feasible, route the switch node on inner layer 3 (between GND on L2 and PWR on L4) to shield it between ground planes. The input current loop (VIN cap → buck IC high-side switch → inductor → output cap → GND return) must be as tight as possible — this is the highest-priority loop on the analog board. The inductor must be shielded (drum core or moulded ferrite). Maintain ≥10mm between the buck inductor and the nearest analog signal trace.
- **LM2776 charge pump:** Keep flying capacitor traces short (≤5mm) and route on the same layer. Route charge pump switching traces within the DGND island — do not allow them to cross into AGND pour area. Place the LM2776 adjacent to the TPS7A4700 in the power supply corner, with the TPS7A39 acting as the boundary between the switching section and the signal path. No analog signal traces should pass through or near the power supply corner.
- **TPS7A4700:** The TPS7A4700 is a linear regulator with no switching noise. Its input now comes from the pre-regulator buck (~6V, with some ripple) rather than directly from VBAT. Place input bulk decoupling (10µF **0805** + 100nF **0402** X7R) immediately at the TPS7A4700 input pin — this cap may be shared with the buck output cap if placed sufficiently close. The exposed thermal pad must connect to the DGND island with ≥6 thermal vias.
- **TPS7A39 placement:** Position the TPS7A39 between the power supply corner (DGND island) and the start of the signal path (AGND pour). The TPS7A39 GND pin should be on the AGND side of the star point. Its ±3.0V output traces fan out from here to the signal path ICs. Keep the output decoupling caps (10µF **0805** + 100nF **0402** per rail) directly at the TPS7A39 output pins.
- **No analog traces through power supply corner:** No analog signal traces on any layer may pass through or under the DGND island area. This includes preamp input traces, DAC output traces, summing bus traces, headphone output traces, and line output traces. The power supply corner is a noise exclusion zone.

### 6.7 Power Supply Corner Layout — Component Placement Order

The power supply corner occupies approximately 20×25mm in one corner of the analog board, near the master header VBAT/GND pins. Components are placed in the following order from the board corner inward toward the signal path:

```
Board corner (near master header VBAT pins)
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  VBAT in → [C_in_buck] → [TPS62140 BUCK] → [L_shielded] → [C_out]  │
│                                                               │      │
│            [C_in_LDO] → [TPS7A4700 LDO] → [C_out_LDO]       │      │
│                                               │               │      │
│                          [LM2776] + [C_FLY] + [C_IN] + [C_OUT]      │
│                                                                      │
│  ========================= DGND ISLAND ============================  │
│                                                                      │
│                           ★ STAR POINT ★                             │
│                                │                                     │
│                    ════════════╪═══════════════                       │
│                                │                                     │
│                          [TPS7A39]  (GND on AGND side)               │
│                           │       │                                  │
│                         +3.0V   −3.0V → fan out to signal path       │
│                                                                      │
│  ========================== AGND POUR =============================  │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

1. **VBAT entry** — right at the board edge, from master header pin 11
2. **Pre-regulator buck (TPS62140)** — input cap, IC, shielded inductor, output cap — all within ~10mm, tight switching loop. Switch node trace minimal area. Furthest from signal path
3. **TPS7A4700 LDO** — input from buck output (shared or adjacent cap), output cap. LDO — no switching noise. Thermal pad to DGND island
4. **LM2776 charge pump** — input from 5V_ANA, flying cap tight (≤5mm), output cap. Switching currents stay within DGND island
5. **Star point** — single low-impedance connection between DGND island and AGND pour. Only DC current crosses this boundary
6. **TPS7A39** — just across the star point on the AGND side. GND pin on AGND. ±3.0V outputs fan out to signal path ICs

> **NOTE: GROUND CURRENT MANAGEMENT.** The buck draws pulsating current from its input cap at the switching frequency. This current circulates in a tight loop within the DGND island: input cap → buck high-side switch → inductor → output cap → GND return via to input cap GND. The LM2776 similarly circulates switching current in a tight loop: flying cap → LM2776 → input/output caps. Both loops must stay within the DGND island. The TPS7A4700 GND pin carries the difference between input and output current (near-zero for an LDO), so it does not inject switching noise. Only DC load current (~260mA) flows through the star point to AGND. If the component placement and via placement rules above are followed, the star point sees no significant switching-frequency current.

---

## 7. Key Components Summary

| Component | Part / Value | Qty | JLCPCB # | Board |
|---|---|---|---|---|
| ESP32-S3-WROOM-1-N16R8 | Master module, PCB antenna | 1 | C2913202 | Digital |
| ESP32-S3-WROOM-1U-N16R8 | Slave modules, U.FL (unpopulated) | 4 | C3013946 | Digital |
| ES8388 | Stereo audio codec, QFN-28-EP (4×4mm) | 5 | C365736 | Digital |
| SC8922QDLR | 2S synchronous boost charger, QFN-24 (4×4mm) — standalone, power path, cell balance | 1 | C252426 | Digital |
| HY2120-CB | 2S Li-ion battery protection IC, SOT-23-6 | 1 | C116509 | Digital |
| FS8205A | Dual N-ch MOSFET for battery protection, SOT-23-6 | 1 | C908265 | Digital |
| 74HC4052 | Dual 4:1 analog mux for UART, SOP-16 | 1 | C111594 | Digital |
| TPS7A2033PDBVR | Ultra-low-noise LDO, 3.3V 300mA, 10µVrms — ES8388 AVDD supply, fed from 5V_ANA | 1 | C2862740 | Digital |
| TPS62140RGTR | 3–17V 2A synchronous buck converter, QFN-16 3×3mm — 3V3_DIG rail | 1 | C129366 | Digital |
| USB-C connector | TYPE-C-31-M-12 (Korean Hroparts), 16-pin SMD, 5A | 1 | C165948 | Digital |
| USBLC6-2SC6 | USB ESD protection, SOT-23-6 (STMicroelectronics) | 1 | C7519 | Digital |
| OPA2134UA/2K5 | Low-noise dual op-amp SOIC-8 SMD (Texas Instruments) — preamp (×4), line out buffer (×1), summing amp (×1) | 6 | C87361 | Analog |
| Nidec ST-4EA 10kΩ | SMD top-adjust trim pot, 4×4mm — one per input channel (×8) plus summing amp feedback L+R (×2) | 10 | C132879 | Analog |
| LM13700M/NOPB | Dual OTA, SOIC-16 (Texas Instruments) — overdrive stages (4 packages = 8 channels) | 4 | C1346265 | Analog |
| TPS62140RGTR | 3–17V 2A synchronous buck converter, QFN-16 3×3mm — **pre-regulator buck on analog board**, VBAT → ~6V | 1 | C129366 | Analog |
| Shielded inductor 2.2µH | Drum-core or moulded ferrite, ≤3.2×3.2mm, ≥600mA Isat — pre-regulator buck | 1 | TBD (select at schematic review) | Analog |
| TPS7A4700RGWR | Ultra-low-noise LDO, 5.0V 1A, 4µVrms, VQFN-20 5×5mm — 6V_PRE to 5V_ANA | 1 | C114839 | Analog |
| LM2776DBVR | Unregulated inverting charge pump, SOT-23-6 — 5V_ANA to −5V_RAW for TPS7A39 negative input | 1 | C69527 | Analog |
| TPS7A3901DSCR | Dual positive/negative ultra-low-noise LDO, ±3.0V 150mA, 21µVrms, WSON-10 3×3mm — 5V_ANA/−5V_RAW to ±3.0V bipolar supply | 1 | C2685819 | Analog |
| 2×6 header (male/female pair) | 2.54mm pitch, 12-pin — master interconnect | 1 pair | User-soldered, not JLCPCB assembled | Both |
| 2×5 header (male/female pair) | 2.54mm pitch, 10-pin — slave interconnect | 4 pairs | User-soldered, not JLCPCB assembled | Both |

---

## 8. Notes for PCB Designer

### 8.1 General

- This is a prototype/development revision. Prioritise correctness and debuggability over board density.
- All SMD components should be on the top side of each board where possible, to allow single-side reflow.
- The 5 ESP32-S3 WROOM modules require Standard PCBA at JLCPCB (not Economic). X-ray inspection is required for these parts — JLCPCB handles this automatically.
- All modules have MSL3 rating — baking may be required if stored before assembly. Flag this to JLCPCB at order time.
- Silkscreen all 2.54mm pad groups clearly with signal names.
- Schematic and BOM to be shared with client for review before layout begins.
- No mounting holes — board edges are free for routing and interconnect header placement.

### 8.2 Test Points

Include test points on: ±3.0V rails, 5V_ANA, 6V_PRE (pre-regulator buck output), −5V_RAW, VBAT, 3V3_DIG, 3V3_ANA, SC8922 VSYS, each ESP32-to-ES8388 MCLK, TDM BCLK, LRCLK, each TDM DATA line, USB D+/D−, and at least one overdrive output.

### 8.3 Decoupling

- Include 100nF (**0402** X7R) decoupling caps on every power pin of every IC, placed as close as possible to the pin.
- Add 10µF (**0805** X7R) bulk decoupling near each ESP32-S3 module.

### 8.4 Placement

- Place each slave interconnect header near its corresponding preamp channel pair and overdrive stage to minimise analog trace lengths.
- The five interconnect headers should be arranged along one board edge for clean sandwich mating.
- Each ESP32+ES8388 pair should be placed close together on the digital board to keep dedicated I2S traces short.

### 8.5 TPS7A4700 Notes

- **ANYOUT pin strapping:** To set 5.0V output, short the 3.2V and 0.4V ANYOUT pins to GND. Leave all other ANYOUT pins open (no connect). Refer to TPS7A4700 datasheet Table 2 for pin-to-voltage mapping. Double-check strapping before fabrication — incorrect configuration will produce wrong voltage.
- **Thermal pad:** The VQFN-20 exposed pad must be soldered to the DGND island copper pour with ≥6 thermal vias (0.3mm drill).

### 8.6 Pre-Regulator Buck Notes (Analog Board)

- **Inductor:** Must be shielded (drum-core or moulded ferrite). **DO NOT SUBSTITUTE UNSHIELDED.** Place with shortest possible trace from TPS62140 SW pin to inductor input pad.
- **Switch node:** Absolute minimum copper area. No via fanout from SW pin. Route as a short trace on the same layer between IC SW pin and inductor pad. If inner layer routing is used, prefer layer 3 (shielded between L2 GND and L4 PWR).
- **Input capacitor:** 10µF (**0805** X7R) + 100nF (**0402** X7R), positive terminal directly at VIN pin, ground terminal directly at GND pin/exposed pad, return via immediately adjacent. This is the highest-priority tight loop on the analog board.
- **Output capacitor:** 22µF (**0805 or 1206** X7R) + 100nF (**0402** X7R), shared with or placed immediately adjacent to TPS7A4700 input cap.
- **FSEL pin:** Connect to VIN to force continuous PWM mode.
- **Feedback divider:** Set output to ~6.0V. Resistor values to be confirmed at schematic review based on TPS62140 reference voltage.
- **Thermal pad:** QFN-16 exposed pad to DGND island copper pour with ≥4 thermal vias (0.3mm drill).

### 8.7 LM2776 Notes

- C_FLY must be placed as close as possible to the C1+ and C1− pins with traces ≤5mm. C_IN at the VIN pin, C_OUT at the VOUT pin. All three caps 1µF X7R 10V minimum (**0603**). **DO NOT SUBSTITUTE Y5V/Z5U.**

### 8.8 TPS7A39 Notes

- **Feedback resistors:** Place R1/R2 (positive) and R3/R4 (negative) feedback resistor dividers directly adjacent to the FB pins. Use 0.1% tolerance **0402** resistors. Place 10nF (**0402** X7R) CFF capacitors from each FB pin to the corresponding OUT pin. Place 10nF (**0402** X7R) CNR/SS capacitor from NR/SS pin to GND.
- **Output decoupling:** 10µF X7R (**0805**) + 100nF X7R (**0402**) ceramic on each output rail, placed directly at the OUT+ and OUT− pins. Additional bulk 100µF electrolytic (**6.3×5.4mm or smaller, 6.3V minimum**) on each rail within 10mm of the TPS7A39.

### 8.9 Power Supply Corner Layout

- Group pre-regulator buck, TPS7A4700, LM2776, and their associated passives in one corner of the analog board, near the master header VBAT/GND pins. See Section 6.7 for detailed placement order.
- Place TPS7A39 between this corner and the signal path, straddling the star point.
- The DGND island should cover the pre-regulator buck, TPS7A4700, and LM2776 footprints and their immediate passives (~20×25mm). Do not extend DGND under the TPS7A39 or any signal path component.
- The DGND island must be solid, unbroken copper on all layers it occupies. No signal traces may be routed through the island on any layer.
- No analog signal traces on any layer may pass through or under the power supply corner.

### 8.10 Capacitor Dielectric Specification

All ceramic capacitors in the analog board power supply section must be X7R or X5R. Note this in the BOM with "X7R REQUIRED — DO NOT SUBSTITUTE Y5V/Z5U" for the following parts: TPS62140 pre-regulator CIN/COUT, TPS7A4700 CIN/COUT, LM2776 CIN/CFLY/COUT, TPS7A39 CIN+/CIN−/COUT+/COUT−/CFF+/CFF−/CNR/SS.

### 8.11 Passive Package Size Reference (NEW in v1.2)

All passives use the smallest safe package size. The table below summarises the package assignments. Where a specific component calls out a package size inline in earlier sections, that takes precedence.

| Component Type | Package | Notes |
|---|---|---|
| Resistors — all signal, damping, bias, feedback, control, pull-down (including 0.1% tolerance) | **0402** | Includes: MCLK/TDM damping 22–33Ω, PWM series 33Ω, RC filter 1kΩ, OTA bias 10kΩ, summing network 10kΩ 1%, TPS7A39 feedback 180kΩ/120kΩ 0.1%, USB CC 5.1kΩ, SC8922 ICHG 12kΩ, line output 100Ω, mic bias 2.2kΩ |
| Ferrite bead — 3V3_ANA/3V3_DIG isolation | **0402** | 600Ω @ 100MHz, ≥300mA rated |
| Capacitors ≤100nF ceramic (decoupling, CFF, NR/SS, RC filter) | **0402** X7R or C0G | All IC decoupling 100nF, TPS7A39 CFF 10nF, NR/SS 10nF, PWM RC filter 100nF |
| Capacitors 1µF ceramic (LM2776 C_IN/C_FLY/C_OUT, TPS7A4700 NR, mic bias coupling, OTA AC coupling) | **0603** X7R 10V min | LM2776 caps require 10V rating. Do not use 0402 for 1µF — voltage coefficient too severe |
| Capacitors 10µF ceramic (bulk decoupling, LDO input/output, ESP32 bulk, ES8388 DVDD, summing/preamp AC coupling) | **0805** X7R or X5R | Verify effective capacitance under DC bias. At 5V bias a typical 10µF 0805 X7R 10V retains ~6–7µF — acceptable for decoupling. For AC coupling (summing amp output, preamp input), X5R acceptable since DC bias is near zero |
| Capacitors 22µF ceramic (buck output) | **0805 or 1206** X7R | Must verify effective capacitance ≥15µF at operating DC bias (~6V). If 0805 derates below 15µF, use 1206 |
| Capacitors 47µF ceramic (TPS7A4700 bulk output) | **1206** X5R | Bulk energy storage — derating less critical at 5V |
| Capacitors 100µF electrolytic (TPS7A39 ±3.0V bulk) | **6.3×5.4mm or smaller** | 6.3V minimum. Cannot be replaced with ceramic without increasing count significantly |
| Capacitors 220µF electrolytic (headphone output coupling) | **6.3×7.7mm or smaller** | 6.3V minimum. Value sets −3dB point at ~22Hz into 32Ω — do not reduce capacitance |
| Schottky clamp diodes (preamp input protection) | **SOD-323 or smaller** | Low forward voltage, low capacitance preferred |
| Polyfuse (headphone protection) | **1206** | 100mA hold current |

> **NOTE: DC BIAS DERATING.** All ceramic capacitors with values ≥10µF must be checked for effective capacitance at their operating DC bias voltage. X7R and X5R dielectrics lose capacitance under DC bias — the smaller the package, the worse the derating. A 10µF 0805 X7R rated 10V typically retains ~60–70% of nominal capacitance at 5V. If the effective capacitance falls below the minimum required by the IC datasheet, use the next larger package size. The designer should verify against manufacturer datasheets or use the JLCPCB capacitance derating tool before finalising the BOM.
>
> **NOTE: WHY 0603 FOR 1µF.** The LM2776 flying capacitor (C_FLY) sees full rail-to-rail AC stress at 2MHz. 0402 1µF X7R parts have significantly worse voltage coefficient and self-heating at high ripple current compared to 0603. The 0603 package also provides a meaningful ESR reduction at 2MHz, improving charge pump efficiency. All other 1µF caps in the design are standardised to 0603 for BOM simplification.

---

## 9. Deferred Items (Verify at Prototype)

| Item | Status | Action if Failed |
|---|---|---|
| TPS7A39 current budget (150mA per rail) | Estimated 90–120mA per rail with 20–40% margin | Replace with separate TPS7A4700 (positive, 1A) + TPS7A3301 (negative, 200mA) LDOs |
| NTC thermistor for SC8922 | Short to GND for prototype, pads provided for optional NTC | Populate with 10kΩ B3950 NTC for production |
| Pre-regulator buck inductor JLCPCB part number | TBD — select shielded 2.2µH ≥600mA Isat, ≤3.2×3.2mm at schematic review | — |

---

*Revision 1.2 — Draft. Passive package sizes standardised to 0402 where safe. All part numbers and values subject to change during schematic review.*
