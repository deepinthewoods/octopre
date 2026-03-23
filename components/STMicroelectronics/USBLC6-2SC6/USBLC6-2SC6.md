# Very low capacitance ESD protection

![img-0.jpeg](./images/img-0.jpeg)
SOT666

![img-1.jpeg](./images/img-1.jpeg)
SOT23-6L

![img-2.jpeg](./images/img-2.jpeg)
Functional diagram (top view)

# Features

- 2 data-line protection
- Protects VBUS
- Very low capacitance: 3.5 pF max.
- Very low leakage current: 150 nA max.
- SOT-666 and SOT23-6L packages
- RoHS compliant

# Benefits

- Very low capacitance between lines to GND for optimized data integrity and speed
- Low PCB space consumption: 2.9 mm² max for SOT-666 and 9 mm² max for SOT23-6L
- Enhanced ESD protection: IEC 61000-4-2 level 4 compliance guaranteed at device level, hence greater immunity at system level
- ESD protection of VBUS
- High reliability offered by monolithic integration
- Low leakage current for longer operation of battery powered devices
- Fast response time
- Consistent D+ / D- signal balance:
- Very low capacitance matching tolerance I/O to GND = 0.015 pF
- Compliant with USB 2.0 requirements

# Complies with the following standards:

- IEC 61000-4-2 level 4:
- 15 kV (air discharge)
- 8 kV (contact discharge)

# Product status link

USBLC6-2

# Applications

- USB 2.0 ports up to 480 Mb/s (high speed)
- Compatible with USB 1.1 low and full speed
- Ethernet port: 10/100 Mb/s
- SIM card protection
- Video line protection
- Portable electronics

# Description

The USBLC6-2SC6 and USBLC6-2P6 are monolithic application specific devices dedicated to ESD protection of high speed interfaces, such as USB 2.0, Ethernet links and video lines.

The very low line capacitance secures a high level of signal integrity without compromising in protecting sensitive chips against the most stringently characterized ESD strikes.

# 1 Characteristics

Table 1. Absolute ratings (Tamb = 25 °C)

|  Symbol | Parameter |   | Value | Unit  |
| --- | --- | --- | --- | --- |
|  V_{PP} | Peak pulse voltage | IEC 61000-4-2 level 4 standard: |  |   |
|   |   |  Air discharge | 15 | kV  |
|   |   |  Contact discharge | 15  |   |
|   |   |  MIL STD883G-Method 3015-7 | 25  |   |
|  T_{stg} | Storage temperature range |   | -55 to +150 | °C  |
|  T_{j} | Operating junction temperature range |   | -40 to +150 | °C  |
|  T_{L} | Maximum lead temperature for soldering during 10 s at 5 mm |   | 260 | °C  |

Table 2. Electrical characteristics (Tamb = 25 °C)

|  Symbol | Parameter | Test conditions | Value |   |   | Unit  |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |  Min. | Typ. | Max.  |   |
|  I_{RM} | Leakage current | V_{RM} = 5.25 V |  | 10 | 150 | nA  |
|  V_{BR} | Breakdown voltage between | I_{R} = 1 mA | 6 |  |  | V  |
|   |  V_{BUS} and GND  |   |   |   |   |   |
|  V_{F} | Forward voltage | I_{F} = 10 mA |  |  | 1.1 | V  |
|  V_{CL} | Clamping voltage | I_{PP} = 1 A, 8/20 μs
Any I/O pin to GND |  |  | 12 | V  |
|   |   |  I_{PP} = 5 A, 8/20 μs |  |  |   |   |
|   |   |  Any I/O pin to GND |  |  | 17  |   |
|  C_{i/o-GND} | Capacitance between I/O and GND | V_{R} = 1.65 V |  | 2.5 | 3.5 | pF  |
|  ΔC_{i/o-GND} |  |  |  | 0.015 |   |   |
|  C_{i/o-i/o} | Capacitance between I/O | V_{R} = 1.65 V |  | 1.2 | 1.7 | pF  |
|  ΔC_{i/o-i/o} |  |  |  | 0.04 |   |   |

# 1.1 Characteristics (curves)

![img-3.jpeg](./images/img-3.jpeg)
Figure 1. Capacitance versus voltage (typical values)

![img-4.jpeg](./images/img-4.jpeg)
Figure 2. Line capacitance versus frequency (typical values)

![img-5.jpeg](./images/img-5.jpeg)
Figure 3. Relative variation of leakage current versus junction temperature (typical values)

![img-6.jpeg](./images/img-6.jpeg)
Figure 4. Frequency response

# 2 Technical information

## 2.1 Surge protection

The USBLC6-2 is particularly optimized to perform surge protection based on the rail to rail topology.

The clamping voltage $V_{CL}$ can be calculated as follow:

$V_{CL} + = V_{TRANSIL} + V_{F}$ for positive surges

$V_{CL} - = - V_{F}$ for negative surges

with: $V_{F} = V_{T} + R_{d} \cdot \text{lp}$

($V_{F}$ forward drop voltage) / ($V_{T}$ forward drop threshold voltage)

and $V_{TRANSIL} = V_{BR} + R_{d\_TRANSIL} \cdot I_{P}$

### Calculation example

We assume that the value of the dynamic resistance of the clamping diode is typically:

$R_{d} = 0.5\ \Omega$ and $V_{T} = 1.1\ \text{V}$

We assume that the value of the dynamic resistance of the transil diode is typically:

$R_{d\_TRANSIL} = 0.5\ \Omega$ and $V_{BR} = 6.1\ \text{V}$ For an IEC 61000-4-2 surge level 4 (Contact Discharge: $V_{g} = 8\ \text{kV}$, $R_{g} = 330\ \Omega$), $V_{BUS} = +5\ \text{V}$, and if in first approximation, we assume that:

$I_{p} = V_{g} / R_{g} = 24\ \text{A}$

So, we find:

$V_{CL} + = +31.2\ \text{V}$

$V_{CL} - = -13\ \text{V}$

**Note:** The calculations do not take into account phenomena due to parasitic inductances.

## 2.2 Surge protection application example

If we consider that the connections from the pin $V_{BUS}$ to $V_{CC}$, from I/O to data line and from GND to PCB GND plane are done by tracks of 10 mm long and 0.5 mm large, we assume that the parasitic inductances $L_{VBUS}$, $L_{I/O}$ and $L_{GND}$ of these tracks are about 6 nH. So when an IEC 61000-4-2 surge occurs on data line, due to the rise time of this spike ($t_r = 1\ \text{ns}$), the voltage $V_{CL}$ has an extra value equal to $L_{I/O} \cdot \text{dI/dt} + L_{GND} \cdot \text{dI/dt}$.

The dI/dt is calculated as:

$\text{dI/dt} = I_{p} / t_{r} = 24\ \text{A/ns}$

The overvoltage due to the parasitic inductances is:

$L_{I/O} \cdot \text{dI/dt} = L_{GND} \cdot \text{dI/dt} = 6\ \text{nH} \times 24\ \text{A/ns} = 144\ \text{V}$

By taking into account the effect of these parasitic inductances due to unsuitable layout, the clamping voltage will be:

$V_{CL} + = +31.2 + 144 + 144 = 319.2\ \text{V}$

$V_{CL} - = -13.1 - 144 - 144 = -301.1\ \text{V}$

We can significantly reduce this phenomena with simple layout optimization. It is for this reason that some recommendations have to be followed (see).

![img-7.jpeg](./images/img-7.jpeg)
Figure 5. ESD behavior: parasitic phenomena due to unsuitable layout

$$
V _ {C L} + = V _ {T R A N S I L} + V _ {F} + L _ {I / O} \frac {d i}{d t} + L _ {G N D} \frac {d i}{d t} \quad \text {s u r g e} &gt; 0
$$

$$
V _ {C L -} = - V _ {F} - L _ {I / O} \frac {d i}{d t} - L _ {G N D} \frac {d i}{d t} \quad \text {s u r g e} &gt; 0
$$

$$
V _ {T R A N S I L} \quad V _ {B R} + R d. I p = 1
$$

![img-8.jpeg](./images/img-8.jpeg)

![img-9.jpeg](./images/img-9.jpeg)

## 2.3 How to ensure good ESD protection

While the USBLC6-2 provides high immunity to ESD surge, efficient protection depends on the layout of the board. In the same way, with the rail to rail topology, the track from data lines to I/O pins, from VCC to VBUS pin and from GND plane to GND pin must be as short as possible to avoid overvoltages due to parasitic phenomena (see Figure 6. ESD behavior: layout optimization and Figure 5. ESD behavior: parasitic phenomena due to unsuitable layout for layout consideration).

![img-10.jpeg](./images/img-10.jpeg)
Figure 6. ESD behavior: layout optimization

![img-11.jpeg](./images/img-11.jpeg)
Figure 7. ESD behavior: measurement conditions

![img-12.jpeg](./images/img-12.jpeg)
Figure 8. ESD response to IEC 61000-4-2 (+15 kV air discharge)

![img-13.jpeg](./images/img-13.jpeg)
Figure 9. ESD response to IEC 61000-4-2 (-15 kV air discharge)

Note: Important: A good precaution to take is to put the protection device as close as possible to the disturbance source (generally the connector).

# 2.4 Crosstalk behavior

# 2.4.1 Crosstalk phenomenon

![img-14.jpeg](./images/img-14.jpeg)
Figure 10. Crosstalk phenomenon

The crosstalk phenomenon is due to the coupling between 2 lines. The coupling factor ( $\beta 12$  or  $\beta 21$ ) increases when the gap across lines decreases, particularly in silicon dice. In the above example the expected signal on load  $R_{L2}$  is  $\alpha_2 V_{G2}$ , in fact the real voltage at this point has got an extra value  $\beta_{21} V_{G1}$ . This part of the  $V_{G1}$  signal represents the effect of the crosstalk phenomenon of the line 1 on the line 2. This phenomenon has to be taken into account when the drivers impose fast digital data or high frequency analog signals in the disturbing line. The perturbed line will be more affected if it works with low voltage signal or high load impedance (few kΩ).

![img-15.jpeg](./images/img-15.jpeg)
Figure 11. Analog crosstalk measurements
Figure 11. Analog crosstalk measurements shows the measurement circuit for the analog application. In usual frequency range of analog signals (up to  $240\mathrm{MHz}$ ) the effect on disturbed line is less than  $-55\mathrm{dB}$  (see Figure 12. Analog crosstalk results).

![img-16.jpeg](./images/img-16.jpeg)
Figure 12. Analog crosstalk results

As the USBLC6-2 is designed to protect high speed data lines, it must ensure a good transmission of operating signals. The frequency response (Figure 4. Frequency response) gives attenuation information and shows that the USBLC6-2 is well suitable for data line transmission up to 480 Mbit/s while it works as a filter for undesirable signals like GSM (900 MHz) frequencies, for instance.

## 2.5 Application examples

![img-17.jpeg](./images/img-17.jpeg)
Figure 13. USB 2.0 port application diagram using USBLC6-2

|  Mode | SW1 | SW2  |
| --- | --- | --- |
|  Low Speed LS | Open | Closed  |
|  Full Speed FS | Closed | Open  |
|  High Speed HS | Closed then open | Open  |

![img-18.jpeg](./images/img-18.jpeg)
Figure 14. T1/E1/Ethernet protection

# 2.6 PSpice model

Figure 15. PSpice model shows the PSpice model of one USBLC6-2 cell. In this model, the diodes are defined by the PSpice parameters given in Figure 16. PSpice parameters.

![img-19.jpeg](./images/img-19.jpeg)
Figure 15. PSpice model

Note: This simulation model is available only for an ambient temperature of  $27^{\circ}C$

Figure 16. PSpice parameters

|   | Dlow | Dhigh | Dzener  |
| --- | --- | --- | --- |
|  BV | 50 | 50 | 7.3  |
|  CJ0 | 0.9p | 2.0p | 40p  |
|  IBV | 1m | 1m | 1m  |
|  M | 0.3333 | 0.3333 | 0.3333  |
|  RS | 0.2 | 0.52 | 0.84  |
|  VJ | 0.6 | 0.6 | 0.6  |
|  TT | 0.1u | 0.1u | 0.1u  |
|  LI/O | 750p  |
| --- | --- |
|  RI/O | 110m  |
|  LGND | 550p  |
|  RGND | 60m  |

![img-20.jpeg](./images/img-20.jpeg)
Figure 17. USBLC6-2 PCB layout considerations

# 3 Package information

In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages, depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product status are available at: www.st.com. ECOPACK is an ST trademark.

# 3.1 SOT23-6L package information

![img-21.jpeg](./images/img-21.jpeg)
Figure 18. SOT23-6L package outline

Table 3. SOT23-6L package mechanical data

|  Ref. | Dimensions  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|   |  Millimeters |   |   | Inches(1)  |   |   |
|   |  Min. | Typ. | Max. | Min. | Typ. | Max.  |
|  A | 0.9 |  | 1.45 | 0.0354 |  | 0.0571  |
|  A1 | 0 |  | 0.15 | 0 |  | 0.0059  |
|  A2 | 0.9 |  | 1.3 | 0.0354 |  | 0.0512  |
|  b | 0.30 |  | 0.5 | 0.0118 |  | 0.0197  |
|  c | 0.09 |  | 0.2 | 0.0035 |  | 0.0079  |
|  D | 2.8 |  | 3.05 | 0.1102 |  | 0.1201  |
|  E | 1.5 |  | 1.75 | 0.0591 |  | 0.0689  |
|  e |  | 0.95 |  |  | 0.0374 |   |
|  H | 2.6 |  | 3 | 0.1024 |  | 0.1181  |
|  L | 0.3 |  | 0.6 | 0.0118 |  | 0.0236  |
|  θ | 0 |  | 10 | 0 |  | 0.3937  |

1. Value in inches are converted from mm and rounded to 4 decimal digits

![img-22.jpeg](./images/img-22.jpeg)
Figure 19. Footprint recommendations, dimensions in mm (inches)

# 3.2 SOT-666 package information

![img-23.jpeg](./images/img-23.jpeg)
Figure 20. SOT-666 package outline

![img-24.jpeg](./images/img-24.jpeg)

![img-25.jpeg](./images/img-25.jpeg)

![img-26.jpeg](./images/img-26.jpeg)

Table 4. SOT-666 package mechanical data

|  Ref. | Dimensions  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|   |  Millimeters |   |   | Inches(1)  |   |   |
|   |  Min. | Typ. | Max. | Min. | Typ. | Max.  |
|  A | 0.45 |  | 0.62 | 0.018 |  | 0.025  |
|  A3 | 0.08 |  | 0.18 | 0.003 |  | 0.007  |
|  b | 0.17 |  | 0.34 | 0.007 |  | 0.013  |
|  D | 1.50 |  | 1.70 | 0.059 |  | 0.067  |
|  E | 1.50 |  | 1.70 | 0.059 |  | 0.067  |
|  E1 | 1.10 |  | 1.30 | 0.043 |  | 0.051  |
|  e |  | 0.50 |  |  | 0.020 |   |
|  L1 |  | 0.19 |  |  | 0.007 |   |
|  L2 | 0.10 |  | 0.30 | 0.004 |  | 0.012  |

1. Value in inches are converted from mm and rounded to 4 decimal digits

![img-27.jpeg](./images/img-27.jpeg)
Figure 21. Footprint recommendations, dimensions in mm

## 3.3 Packing information

![img-28.jpeg](./images/img-28.jpeg)
Figure 22. Marking layout (refer to ordering information table for marking)

![img-29.jpeg](./images/img-29.jpeg)
Figure 23. Package orientation in reel
Nine:
- Pocket dimensions are not on scale
- Pocket shape may vary depending on package

![img-30.jpeg](./images/img-30.jpeg)
Figure 24. Tape and reel orientation

![img-31.jpeg](./images/img-31.jpeg)
Figure 25. Reel dimensions (mm)

![img-32.jpeg](./images/img-32.jpeg)
Figure 26. Inner box dimensions (mm)

Figure 27. Tape and reel outline
![img-33.jpeg](./images/img-33.jpeg)
Note: Pocket dimensions are not on scale
Pocket shape may vary depending on package

Table 5. Tape and reel mechanical data

|  Ref. | Dimensions  |   |   |
| --- | --- | --- | --- |
|   |  Millimeters  |   |   |
|   |  Min. | Typ. | Max.  |
|  P1 | 3.9 | 4 | 4.1  |
|  P0 | 3.9 | 4 | 4.1  |
|  D0 | 1.45 | 1.5 | 1.6  |
|  D1 | 1 |  |   |
|  F | 3.45 | 3.5 | 3.55  |
|  K0 | 1.3 | 1.4 | 1.6  |
|  P2 | 1.95 | 2 | 2.05  |
|  W | 7.9 | 8 | 8.3  |

# 4 Ordering information

![img-34.jpeg](./images/img-34.jpeg)
Figure 28. Ordering information scheme

Table 6. Ordering information

|  Order code | Marking | Package | Weight | Base qty. | Delivery mode  |
| --- | --- | --- | --- | --- | --- |
|  USBLC6-2SC6 (1) | UL26 | SOT23-6L | 16.7 mg | 3000 | Tape and reel  |
|  USBLC6-2P6(1) | F | SOT-666 | 2.9 mg | 3000 | Tape and reel  |

1. The marking code can be rotated by 90° to differentiate assembly location.

# Revision history

Table 7. Document revision history

|  Date | Version | Changes  |
| --- | --- | --- |
|  14-Mar-2005 | 1 | Initial release.  |
|  07-Jun-2005 | 2 | Format change to figure 3; no content changed.  |
|  20-Mar-2008 | 3 | Added marking illustrations - Figures 21 and 23. Added ECOPACK statement. Updated operating junction temperature range in absolute ratings, page 2. Technical information section updated. Reformatted to current standards.  |
|  27-Jun-2011 | 4 | Updated leakage current for VRM = 5.25 V as specified in USB standard. Updated marking illustrations Figure 21 and Figure 23.  |
|  24-Oct-2011 | 5 | Updated legal statement.  |
|  16-Oct-2020 | 6 | Minor text changes.  |
|  24-Dec-2021 | 7 | Updated Section ■ Disclaimer
Updated Section 1 Characteristics  |

# IMPORTANT NOTICE – PLEASE READ CAREFULLY

STMicroelectronics NV and its subsidiaries (“ST”) reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST products are sold pursuant to ST’s terms and conditions of sale in place at the time of order acknowledgement.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of Purchasers’ products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. For additional information about ST trademarks, please refer to www.st.com/trademarks. All other product or service names are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2021 STMicroelectronics – All rights reserved

