# Layout Guidance — 8-Channel Audio DSP System

## Digital Board (70 x 55 mm, 6-layer)

### Critical Placement Constraints

**U1 (ESP32-S3 Master, PCB antenna):**
- Antenna must protrude beyond board edge
- 3.7mm copper keepout on all antenna sides, all layers
- Place near board edge with antenna pointing outward
- USB-C connector (J_USB) nearby for short USB D+/D- traces

**U2–U5 (ESP32-S3 Slaves, U.FL):**
- Can be placed interior — no antenna keepout needed
- U.FL pad present but not populated
- Group near their respective ES8388 codecs

### Component Proximity Groups

**Group 1: USB + Charger (board edge)**
- J_USB (USB-C connector) — board edge
- U_ESD (USBLC6) — adjacent to J_USB
- U_CHG (BQ25798) — near J_USB for short VBUS path
- J_BAT (battery connector) — board edge

**Group 2: Power (central area)**
- U_BUCK (TPS62130) — near battery input
- U_LDO (LP5907) — near battery input, away from digital noise
- FB_ANA (ferrite bead) — between LDO and analog rail

**Group 3: Master ESP32 + Master Codec**
- U1 (ESP32 master) — board edge for antenna
- U6 (ES8388 master codec) — near U1 for short I2S traces
- Keep MCLK trace short between U1 and U6

**Group 4–7: Slave ESP32 + Slave Codecs (one group per slave)**
- U2 + U7 — close together
- U3 + U8 — close together
- U4 + U9 — close together
- U5 + U10 — close together
- Each pair should have its ES8388 within 10mm of its ESP32

**Group 8: UART Mux**
- U_MUX (74HC4052) — near U1 master, central to slave UART routing

**Group 9: Interconnect Header**
- J_CONN (2x20 header) — board edge, preferably opposite to USB-C
- Analog signals on one end of header, digital on the other

### Routing Guidelines

- **TDM bus (BCLK, LRCLK, DATA x4):** Match trace lengths within 5mm. Route with ground stitching vias alongside. Keep away from analog traces.
- **MCLK:** Star topology from U1 to all 5 ES8388 codecs. Route with adjacent ground return. Avoid running parallel to analog inputs.
- **I2C (SDA, SCL):** Shared bus, can be routed freely with 4.7k pull-ups near U1.
- **USB D+/D-:** Differential pair, 90 ohm impedance, as short as possible from J_USB to U1.
- **3V3_ANA pour:** Separate from 3V3_DIG. Connect through ferrite bead only. Keep digital switching noise away.
- **AGND islands:** Each ES8388 gets a local AGND island, connected to main GND at one star point near power entry.

### Stackup (6-layer, confirm with JLCPCB)
```
L1: Signal (top) — components, short signal traces
L2: GND — continuous ground plane
L3: Signal — internal routing
L4: Power — 3V3_DIG, VBAT, 3V3_ANA pours
L5: GND — continuous ground plane
L6: Signal (bottom) — routing, test points
```

---

## Analog Board (70 x 55 mm, 6-layer)

### Critical Placement Constraints

**OPA2134 op-amps (U_PRE1–U_PRE4):**
- Place each near its channel's input pads
- Keep analog signal paths short
- Power pins need local decoupling

### Component Proximity Groups

**Group 1: Input channels CH1+CH2 (board edge)**
- J_IN1, J_IN2 (input pads) — board edge
- J_MIC1, J_MIC2 (mic input pads) — near J_IN1, J_IN2
- U_PRE1 (OPA2134) — between input pads and interconnect header

**Group 2: Input channels CH3+CH4**
- J_IN3, J_IN4 — board edge
- U_PRE2 — between inputs and header

**Group 3: Input channels CH5+CH6**
- J_IN5, J_IN6 — board edge
- U_PRE3 — between inputs and header

**Group 4: Input channels CH7+CH8**
- J_IN7, J_IN8 — board edge
- U_PRE4 — between inputs and header

**Group 5: Line output buffer**
- U_LINE (OPA2134) — near interconnect header and J_LINE output pads
- J_LINE — board edge

**Group 6: Headphone output**
- J_HP — board edge
- HP coupling caps and protection near J_HP

**Group 7: Interconnect header**
- J_CONN (2x20 female header) — board edge, matching digital board orientation

### Routing Guidelines

- **AGND / DGND separation:** Separate ground pours. Star point at power entry from interconnect header.
- **3V3_ANA pour:** Separate from 3V3_DIG. Route on dedicated copper area.
- **Input preamp traces:** Keep short, avoid running parallel to digital signals or power traces.
- **Trim pot placement:** Each channel's gain trim pot should be accessible from the top side for adjustment.
- **Output coupling caps (220uF HP):** These are physically large — allocate space near output pads.

### Stackup
Same as digital board — 6-layer, signal/GND/signal/power/GND/signal.
