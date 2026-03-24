# TPS7A20 300mA、超低噪声、低 IQ、高 PSRR LDO

## 1 特性

- 低输出电压噪声：7 μV RMS
- 无需噪声旁路电容
- 高 PSRR：1kHz 时为 95dB
- 超低 IQ：6.5 μA
- 输入电压范围：1.6V 至 6.0V
- 输出电压范围：0.8V 至 5.5V
- 输出电压容差：±1.5% （最大值）
- 超低压降：
- 在 300mA 下为 140mV（最大值）（VOUT = 3.3V）
- 在 300mA 下为 145mV（最大值）（VOUT = 3.3V，DBV）
- 低浪涌电流
- 智能使能端下拉
- 与最低 1μF 的陶瓷输出电容搭配使用可保持稳定
- 封装：
- 1mm × 1mm X2SON (DQN)
- 0.16mm × 0.16mm DSBGA (YCK)
- 0.612mm × 0.612mm DSBGA (YCJ)
- 2.9mm × 2.8mm SOT23-5 (DBV)

## 2 应用

- 智能手机和平板电脑
- IP 网络摄像头
- 便携式医疗设备
- 智能仪表和现场变送器
- 电机驱动器
- 可穿戴设备

## 3 说明

TPS7A20 是一款超小型低压降 (LDO) 线性稳压器，可提供 300mA 的输出电流。TPS7A20 旨在提供符合射频和其他敏感模拟电路要求的低噪声、高 PSRR 和出色的负载和线路瞬态性能。TPS7A20 采用创新的设计技术，无需噪声旁路电容便可提供超低的噪声性能。TPS7A20 的优点还在于具有低静态电流，适用于任何电池供电的应用 TPS7A20 具有 1.6V 至 6.0V 的输入电压范围和 0.8V 至 5.5V 的输出电压范围，可用于各种应用。该器件使用精密基准电路，可在不同负载、线路和温度变化之间提供 1.5% 的最大精度。

TPS7A20 具备内部软启动功能，旨在降低浪涌电流，因此可在启动过程中最大限度地降低输入电压降。该器件在与小型陶瓷电容搭配使用时可保持稳定，因此可实现小尺寸总体解决方案。

TPS7A20 具有带内部控制下拉电阻的智能使能输入电路，该电阻即使在 EN 引脚悬空时也能让 LDO 保持禁用状态，因而无需使用外部组件来下拉 EN 引脚。

### 封装信息

|  器件型号 | 封装(1) | 封装尺寸(2)  |
| --- | --- | --- |
|  TPS7A20 | DQN (X2SON, 4) | 1mm × 1mm  |
|   |  YCJ (DSBGA, 4) | 0.612mm × 0.612mm  |
|   |  YCK (DSBGA, 4) | 0.616mm × 0.616mm  |
|   |  DBV (SOT-23, 5) | 2.9mm × 2.8mm  |

(1) 如需更多信息，请参阅 机械、封装和可订购信息。
(2) 封装尺寸（长 × 宽）为标称值，并包括引脚（如适用）。

![img-0.jpeg](./images/img-0.jpeg)
应用原理图

# Table of Contents

1 特性...1
2 应用...1
3 说明...1
4 Pin Configuration and Functions...3
5 Specifications...5
5.1 Absolute Maximum Ratings...5
5.2 ESD Ratings...5
5.3 Recommended Operating Conditions...5
5.4 Thermal Information...6
5.5 Electrical Characteristics...6
5.6 Switching Characteristics...7
5.7 Typical Characteristics...8
6 Detailed Description...23
6.1 Overview...23
6.2 Functional Block Diagram...23
6.3 Feature Description...24
6.4 Device Functional Modes...26
7 Application and Implementation...27
7.1 Application Information...27
7.2 Typical Application...30
7.3 Power Supply Recommendations...31
7.4 Layout...31
8 Device and Documentation Support...33
8.1 Device Support...33
8.2 接收文档更新通知...33
8.3 支持资源...33
8.4 Trademarks...33
8.5 静电放电警告...33
8.6 术语表...33
9 Revision History...34
10 Mechanical, Packaging, and Orderable Information...34
10.1 Mechanical Data...35

# 4 Pin Configuration and Functions

![img-1.jpeg](./images/img-1.jpeg)
图 4-1. YCJ and YCK Packages, 4-Pin DSBGA (Top View)

![img-2.jpeg](./images/img-2.jpeg)
图 4-2. YCJ and YCK Packages, 4-Pin DSBGA (Bottom View)

Pin Functions: DSBGA

|  PIN |   | I/O | DESCRIPTION  |
| --- | --- | --- | --- |
|  NO. | NAME  |   |   |
|  A1 | IN | I | Input voltage supply. For best transient response and to minimize input impedance, use the nominal value or larger capacitor from IN to ground as listed in the Recommended Operating Conditions table. Place the input capacitor as close to the IN and GND pins of the device as possible.  |
|  A2 | OUT | O | Regulated output voltage. A low equivalent series resistance (ESR) capacitor is required from OUT to ground for stability. For best transient response, use the nominal recommended value or larger capacitor listed in the Recommended Operating Conditions table. Place the output capacitor as close to the OUT and GND pins of the device as possible.  |
|  B1 | EN | I | Enable input. A low voltage (< V_EN(LON)) on this input turns the regulator off and discharges the output pin to GND. A high voltage (> V_EN(HI)) on this pin enables the regulator output. This pin has an internal 500k Ω pulldown resistor to hold the regulator off by default. When V_EN > V_EN(HI), the 500k Ω pulldown is disconnected to reduce input current.  |
|  B2 | GND | — | Common ground.  |

![img-3.jpeg](./images/img-3.jpeg)
图 4-3. DQN Package, 4-Pin X2SON (Top View)

![img-4.jpeg](./images/img-4.jpeg)
图 4-4. DBV Package, 5-Pin SOT-23 (Top View)

Pin Functions: X2SON, SOT-23

|  PIN |   |   | I/O | DESCRIPTION  |
| --- | --- | --- | --- | --- |
|  NAME | X2SON | SOT-23  |   |   |
|  IN | 4 | 1 | I | Input voltage supply. For best transient response and to minimize input impedance, use the nominal value or larger capacitor from IN to ground as listed in the Recommended Operating Conditions table. Place the input capacitor as close to the IN and GND pins of the device as possible.  |
|  OUT | 1 | 5 | O | Regulated output voltage. A low equivalent series resistance (ESR) capacitor is required from OUT to ground for stability. For best transient response, use the nominal recommended value or larger capacitor listed in the Recommended Operating Conditions table. Place the output capacitor as close to the OUT and GND pins of the device as possible. An internal 150 Ω (typical) pulldown resistor prevents a charge from remaining on V_{OUT} when the regulator is in shutdown mode (V_{EN} < V_{EN(LOW)}).  |
|  EN | 3 | 3 | I | Enable input. A low voltage (< V_{EN(LOW)}) on this pin turns the regulator off and discharges the output pin to GND. A high voltage (> V_{EN(HI)}) on this pin enables the regulator output. This pin has an internal 500k Ω pulldown resistor to hold the regulator off by default. When V_{EN} > V_{EN(HI)}, the 500k Ω pulldown is disconnected to reduce input current.  |
|  GND | 2 | 2 | — | Common ground.  |
|  N/C | — | 4 | — | No internal electrical connection.  |
|  Thermal Pad | 5 | — | — | Thermal pad for the X2SON package. Connect this pad to GND or leave floating. Do not connect to any potential other than GND. Connect the thermal pad to a large-area ground plane for best thermal performance.  |

# 5 Specifications

## 5.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted)(1) (3)

|   |   | MIN | MAX | UNIT  |
| --- | --- | --- | --- | --- |
|  Voltage | VIN | - 0.3 | 6.5 | V  |
|   |  VOUT | - 0.3 | 6.5 or VIN + 0.3 (2)  |   |
|   |  VEN | - 0.3 | 6.5  |   |
|  Current | Maximum output(4) | Internally limited |   | A  |
|  Temperature | Operating junction, TJ | - 40 | 150 | °C  |
|   |  Storage, Tstg | - 65 | 150 | °C  |

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) The maximum value of $V_{\text{OUT}}$ is the lesser of 6.5 V or $(V_{\text{IN}} + 0.3 \, \text{V})$.
(3) All voltages are with respect to the GND pin.
(4) Internal thermal shutdown circuitry protects the device from permanent damage.

## 5.2 ESD Ratings

|   |   |   | VALUE | UNIT  |
| --- | --- | --- | --- | --- |
|  V_{(ESD)} | Electrostatic discharge | Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1) | ±2000 | V  |
|   |   |  Charged-device model (CDM), per JEDEC specification JESD22-C101(2) | ±750  |   |

(1) JEDEC document JEP155 states that 500-V HBM allows safemanufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safemanufacturing with a standard ESD control process.

## 5.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)(1)

|   |   | MIN | NOM | MAX | UNIT  |
| --- | --- | --- | --- | --- | --- |
|  V_{IN} | Input supply voltage | 1.6 |   | 6.0 | V  |
|  V_{EN} | Enable input voltage | 0 |   | 6.0 | V  |
|  V_{OUT} | Nominal output voltage range | 0.8 |   | 5.5 | V  |
|  I_{OUT} | Output current | 0 |   | 300 | mA  |
|  C_{IN} | Input capacitor(2) | 1 |   |   | μF  |
|  C_{OUT} | Output capacitor(3) | 1 |   | 200 | μF  |
|  ESR | Output capacitor effective series resistance |  |   | 100 | mΩ  |
|  T_{J} | Operating junction temperature | - 40 |   | 125 | °C  |

(1) All voltages are with respect to GND.
(2) An input capacitor is not required for LDO stability. However, an input capacitor with an effective value of 0.47 μF minimum is recommended to counteract the effect of source resistance and inductance, which may in some cases cause symptoms of system-level instability such as ringing or oscillation, especially in the presence of load transients.
(3) Effective output capacitance of 0.47 μF minimum and 200 μF maximum is required for stability.

5.4 Thermal Information

|  THERMAL METRIC(1) | TPS7A20 |   |   |   | UNIT  |   |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |  DBV (SOT-23) | DQN (X2SON) | YCJ (DSBGA) |   | YCK (DSBGA)  |
|   |   |  5 PINS | 4 PINS | 4 PINS |   | 4 PINS  |
|  R J A | Junction-to-ambient thermal resistance | 187.1 | 166.1 | 199.6 | 201.4 | °C/W  |
|  R J C(top) | Junction-to-case (top) thermal resistance | 85.5 | 103.6 | 2.8 | 2.8 | °C/W  |
|  R J B | Junction-to-board thermal resistance | 54.4 | 110.6 | 67.5 | 69.3 | °C/W  |
|  θ JT | Junction-to-top characterization parameter | 27.1 | 3.0 | 1.4 | 1.4 | °C/W  |
|  θ JB | Junction-to-board characterization parameter | 54.1 | 103.3 | 67.4 | 69.2 | °C/W  |
|  R J C(not) | Junction-to-case (bottom) thermal resistance | N/A | 98.8 | N/A | N/A | °C/W  |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

# 5.5 Electrical Characteristics

at operating temperature range ( $T_J = -40^{\circ}C$  to  $+125^{\circ}C$ ),  $V_{IN} = V_{OUT(NOM)} + 0.3V$  or  $1.6V$ , whichever is greater,  $V_{EN} = 1.0V$ ,  $I_{OUT} = 1mA$ ,  $C_{IN} = 1\mu F$ ,  $C_{OUT} = 1\mu F$  (unless otherwise noted); all typical values are at  $T_J = 25^{\circ}C$

|  PARAMETER |   | TEST CONDITIONS |   | MIN | TYP | MAX | UNIT  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  ΔVOUT | Output voltage tolerance | VIN=(VOUT(NOM)+0.3 V) to 6.0 V, IOUT=1 mA to 300 mA, VOUT≥1.85 V (DQN, YCJ, YCK packages) |   | -1.5 | 1.5 |   | %  |
|   |   |  VIN=(VOUT(NOM)+0.3 V) to 6.0 V, IOUT=1 mA to 300 mA, VOUT≥2.8 V (DBV package) |   | -1.5 | 1.5  |   |   |
|   |   |  VIN=(VOUT(NOM)+0.5 V) to 6.0 V, IOUT=1 mA to 300 mA, VOUT<1.85 V (DQN, YCJ, YCK packages) |   | -30 | 30 |   | mV  |
|   |   |  VIN=(VOUT(NOM)+0.3 V) to 6.0 V, IOUT=1 mA to 300 mA, VOUT<2.8 V (DBV package) |   | -40 | 40  |   |   |
|  ΔVOUT | Line regulation | VIN=(VOUT(NOM)+0.3 V) to 6.0 V, IOUT=1 mA |   | 0.03 |   |   | %/V  |
|  ΔVOUT | Load regulation | IOUT=1 mA to 300 mA (DQN, YCJ, YCK packages) |   | 13 |   |   | mV  |
|   |   |  IOUT=1 mA to 300 mA (DBV package) |   | 19  |   |   |   |
|  IOND | Quiescent ground current | VEN=VIN=6 V, IOUT=0 mA | TJ=25°C | 6.5 | 8.5 |   | μA  |
|   |   |   |  TJ=-40°C to 85°C | 10  |   |   |   |
|   |   |   |  TJ=-40°C to 125°C | 15  |   |   |   |
|   |   |  VEN=VIN=6 V, IOUT=300 mA |   | 2000  |   |   |   |
|  ISHON | Shutdown ground current | VEN=0 V (disabled), VIN=6.0 V, TJ=25°C |   | 0.07 | 0.2 |   | μA  |
|  IOND(DO) | IOND in dropout | VIN≤VOUT(NOM), IOUT=0 mA, VEN=VIN |   | 6.5 | 15 |   | μA  |
|  VDO | Dropout voltage | IOUT=300 mA, VOUT=95% x VOUT(NOM), (DQN, YCJ, YCK packages unless otherwise noted) | 0.8 V ≤ VOUT<1.0 V(1) | 690 |   |   | mV  |
|   |   |   |  1.0 V ≤ VOUT<1.2 V(1) | 490  |   |   |   |
|   |   |   |  1.2 V ≤ VOUT<1.5 V(1) | 355  |   |   |   |
|   |   |   |  1.5 V ≤ VOUT<2.5 V | 200  |   |   |   |
|   |   |   |  1.5 V ≤ VOUT<2.5 V (DBV) | 205  |   |   |   |
|   |   |   |  2.5 V ≤ VOUT<5.5 V | 140  |   |   |   |
|   |   |   |  2.5 V ≤ VOUT<5.5 V (DBV) | 145  |   |   |   |

# 5.5 Electrical Characteristics (续)

at operating temperature range  $(\mathrm{T_J} = -40^{\circ}\mathrm{C}$  to  $+125^{\circ}\mathrm{C})$ $V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3\mathrm{V}$  or  $1.6\mathrm{V}$ , whichever is greater,  $V_{\mathrm{EN}} = 1.0\mathrm{V}$ ,  $I_{\mathrm{OUT}} = 1\mathrm{mA}$ ,  $C_{\mathrm{IN}} = 1\mu \mathrm{F}$ ,  $C_{\mathrm{OUT}} = 1\mu \mathrm{F}$  (unless otherwise noted); all typical values are at  $\mathrm{T_J} = 25^{\circ}\mathrm{C}$

|  PARAMETER |   | TEST CONDITIONS |   | MIN | TYP | MAX | UNIT  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  ICL | Output current limit | VOUT=0.9 x VOUT(NOM), VIN=VOUT(NOM)+0.5 V | VOUT<1.5 V (YCJ, YCK packages) | 360 | 520 | 770 | mA  |
|   |   |  VOUT=0.9 x VOUT(NOM), VIN=VOUT(NOM)+0.5 V | VOUT<1.5 V (DQN package) | 360 | 520 | 730  |   |
|   |   |  VOUT=VOUT(NOM)-150 mV, VIN=VOUT(NOM)+0.5 V | VOUT<1.5 V (DBV package) | 360 | 520 | 730  |   |
|   |   |  VOUT=0.9 x VOUT(NOM), VIN=VOUT(NOM)+0.3 V | VOUT≥1.5 V (YCJ, YCK packages) | 360 | 520 | 770  |   |
|   |   |  VOUT=0.9 x VOUT(NOM), VIN=VOUT(NOM)+0.3 V | VOUT≥1.5 V (DQN package) | 360 | 520 | 730  |   |
|  ISC | Short-circuit current limit | VOUT=0 V |   | 160 |   |   | mA  |
|  PSRR | Power-supply rejection ratio | IOUT=20 mA, VIN=VOUT+1.0 V | f=100 Hz | 95 |   |   | dB  |
|   |   |   |  f=1 kHz | 95  |   |   |   |
|   |   |   |  f=10 kHz | 75  |   |   |   |
|   |   |   |  f=100 kHz | 75  |   |   |   |
|   |   |   |  f=1 MHz | 45  |   |   |   |
|   |   |  IOUT=300 mA, VIN=VOUT+1.0 V | f=100 Hz | 65  |   |   |   |
|   |   |   |  f=1 kHz | 92  |   |   |   |
|   |   |   |  f=10 kHz | 75  |   |   |   |
|   |   |   |  f=100 kHz | 60  |   |   |   |
|   |   |   |  f=1 MHz | 40  |   |   |   |
|  VN | Output noise voltage | BW=10 Hz to 100 kHz, VOUT=2.8 V | IOUT=300 mA | 7 |   |   | μVRMS  |
|   |   |   |  IOUT=1 mA | 10  |   |   |   |
|  RPULLDOWN | Output automatic discharge pulldown resistance | VEN< VEN(LOW) (output disabled), VIN=3.1 V |   | 150 |   |   | Ω  |
|  TSD | Thermal shutdown | TJ rising |   | 165 |   |   | °C  |
|   |   |  TJ falling |   | 140  |   |   |   |
|  VEN(LOW) | Low input threshold | VIN=1.6 V to 6.0 V, VEN falling until the output is disabled |   | 0.3 |   |   | V  |
|  VEN(HI) | High input threshold | VIN=1.6 V to 6.0 V VEN rising until the output is enabled |   | 0.9 |   |   | V  |
|  VUVLO | UVLO threshold | VIN rising (YCJ and YCK packages) |   | 1.11 | 1.35 | 1.59 | V  |
|   |   |  VIN rising (DBV and DQN packages) |   | 1.17 | 1.35 | 1.59  |   |
|   |   |  VIN falling (YCJ and YCK packages) |   | 1.05 | 1.3 | 1.55  |   |
|   |   |  VIN falling (DBV and DQN packages) |   | 1.11 | 1.3 | 1.55  |   |
|  VUVLO(HYST) | UVLO hysteresis |  |   | 50 |   |   | mV  |
|  IEN | EN input leakage current | VEN=6.0 V and VIN=6.0 V |   | 90 | 250 |   | nA  |
|  REN(PULL-DOWN) | Smart enable pulldown resistor | VEN=0.25 V |   | 500 |   |   | KΩ  |

(1) Design simulation data only

# 5.6 Switching Characteristics

at operating temperature range  $(\mathrm{T_J} = -40^{\circ}\mathrm{C}$  to  $+125^{\circ}\mathrm{C})$ $V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3\mathrm{V}$  or  $1.6\mathrm{V}$ , whichever is greater,  $V_{\mathrm{EN}} = 1.0\mathrm{V}$ ,  $I_{\mathrm{OUT}} = 1\mathrm{mA}$ ,  $C_{\mathrm{IN}} = 1\mu \mathrm{F}$ ,  $C_{\mathrm{OUT}} = 1\mu \mathrm{F}$  (unless otherwise noted); all typical values are at  $\mathrm{T_J} = 25^{\circ}\mathrm{C}$

|  PARAMETER |   | TEST CONDITIONS | MIN | TYP | MAX | UNIT  |
| --- | --- | --- | --- | --- | --- | --- |
|  ISTR | Start-up time | From VEN > VEN(HI) to VOUT = 95% of VOUT(NOM). |  | 750 | 1150 | μs  |

# 5.7 Typical Characteristics

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-5.jpeg](./images/img-5.jpeg)
$\mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-1. Line Regulation vs  $V_{\mathrm{IN}}$

![img-6.jpeg](./images/img-6.jpeg)
$\mathrm{V_{OUT}} = 5.5 \mathrm{~V}, \mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-2. Line Regulation vs  $V_{\mathrm{IN}}$

![img-7.jpeg](./images/img-7.jpeg)
$\mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DBV}$  package
图5-3. Line Regulation vs  $V_{\mathrm{IN}}$

![img-8.jpeg](./images/img-8.jpeg)
$\mathrm{V_{OUT}} = 5.5 \mathrm{~V}, \mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DBV}$  package
图5-4. Line Regulation vs  $V_{\mathrm{IN}}$

![img-9.jpeg](./images/img-9.jpeg)
$\mathrm{V_{IN}} = 3.1 \mathrm{~V}, \mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-5. Load Regulation vs  $I_{\mathrm{OUT}}$

![img-10.jpeg](./images/img-10.jpeg)
$\mathrm{V_{IN}} = 3.1 \mathrm{~V}, \mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-6. Load Regulation vs  $I_{\mathrm{OUT}}$

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-11.jpeg](./images/img-11.jpeg)
$\mathrm{V_{IN}} = 2.8\mathrm{V},\mathrm{V_{EN}} = 1\mathrm{V}$  DBV package
图5-7. Load Regulation vs Iout

![img-12.jpeg](./images/img-12.jpeg)
$\mathrm{V_{IN}} = 2.8\mathrm{V},\mathrm{V_{EN}} = 1\mathrm{V}$  DBV package
图5-8. Load Regulation vs Iout

![img-13.jpeg](./images/img-13.jpeg)
$\mathrm{V_{OUT}} = 5.5\mathrm{V},\mathrm{V_{EN}} = 1\mathrm{V}$  DQN, YCJ, and YCK packages
图5-9. Load Regulation vs Iout

![img-14.jpeg](./images/img-14.jpeg)
$\mathrm{V_{OUT}} = 5.5\mathrm{V},\mathrm{V_{EN}} = 1\mathrm{V}$  DQN, YCJ, and YCK packages
图5-10. Load Regulation vs Iout

![img-15.jpeg](./images/img-15.jpeg)
$\mathrm{V_{OUT}} = 5.5\mathrm{V},\mathrm{V_{EN}} = 1\mathrm{V}$  DBV package
图5-11. Load Regulation vs Iout

![img-16.jpeg](./images/img-16.jpeg)
$\mathrm{V_{OUT}} = 5.5\mathrm{V},\mathrm{V_{EN}} = 1\mathrm{V}$  DBV package
图5-12. Load Regulation vs Iout

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-17.jpeg](./images/img-17.jpeg)
$\mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-13. Output Voltage Accuracy vs  $I_{\text{OUT}}$

![img-18.jpeg](./images/img-18.jpeg)
图5-14. Output Voltage Accuracy vs  $I_{\text{OUT}}$

![img-19.jpeg](./images/img-19.jpeg)
图5-15. Output Voltage Accuracy vs  $I_{\text{OUT}}$

![img-20.jpeg](./images/img-20.jpeg)
图5-16. Output Voltage Accuracy vs  $I_{\text{OUT}}$

![img-21.jpeg](./images/img-21.jpeg)
图5-17. Output Voltage Accuracy vs  $I_{\text{OUT}}$

![img-22.jpeg](./images/img-22.jpeg)
图5-18. Output Voltage Accuracy vs  $I_{\text{OUT}}$

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-23.jpeg](./images/img-23.jpeg)
$\mathrm{V_{OUT}} = 5.5\mathrm{V},\mathrm{V_{EN}} = 1\mathrm{V}$  DBV package

![img-24.jpeg](./images/img-24.jpeg)
图5-20. Output Voltage Accuracy vs  $I_{\mathrm{OUT}}$

![img-25.jpeg](./images/img-25.jpeg)
图5-19. Output Voltage Accuracy vs  $I_{\mathrm{OUT}}$
$\mathrm{V_{EN}} = 1\mathrm{V}, I_{\mathrm{OUT}} = 1\mathrm{mA}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages

![img-26.jpeg](./images/img-26.jpeg)
图5-22. Output Voltage Accuracy vs  $V_{\mathrm{IN}}$

![img-27.jpeg](./images/img-27.jpeg)
图5-21. Output Voltage Accuracy vs  $V_{\mathrm{IN}}$
$\mathrm{V_{EN}} = 1\mathrm{V}, I_{\mathrm{OUT}} = 1\mathrm{mA}, \mathrm{DBV}$  package
图5-23. Output Voltage Accuracy vs  $V_{\mathrm{IN}}$

![img-28.jpeg](./images/img-28.jpeg)
图5-24. Output Voltage Accuracy vs  $V_{\mathrm{IN}}$

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-29.jpeg](./images/img-29.jpeg)
$\mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-25. Dropout Voltage vs  $I_{\mathrm{OUT}}$

![img-30.jpeg](./images/img-30.jpeg)
$\mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-26. Dropout Voltage vs  $I_{\mathrm{OUT}}$

![img-31.jpeg](./images/img-31.jpeg)
$\mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DBV}$  package
图5-27. Dropout Voltage vs  $I_{\mathrm{OUT}}$

![img-32.jpeg](./images/img-32.jpeg)
$\mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DBV}$  package
图5-28. Dropout Voltage vs  $I_{\mathrm{OUT}}$

![img-33.jpeg](./images/img-33.jpeg)
$\mathrm{V_{OUT}} = 1.8 \mathrm{~V}, \mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-29. Dropout Voltage vs  $I_{\mathrm{OUT}}$

![img-34.jpeg](./images/img-34.jpeg)
$\mathrm{V_{OUT}} = 1.8 \mathrm{~V}, \mathrm{V_{EN}} = 1 \mathrm{~V}, \mathrm{DQN}, \mathrm{YCJ},$  and YCK packages
图5-30. Dropout Voltage vs  $I_{\mathrm{OUT}}$

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-35.jpeg](./images/img-35.jpeg)

![img-36.jpeg](./images/img-36.jpeg)

![img-37.jpeg](./images/img-37.jpeg)
图5-31. Dropout Voltage vs Iout

![img-38.jpeg](./images/img-38.jpeg)
图5-32. Dropout Voltage vs Iout
图5-34. I GND vs VIN

![img-39.jpeg](./images/img-39.jpeg)
图5-33. Dropout Voltage vs VOUT
图5-35. IGND vs VIN

![img-40.jpeg](./images/img-40.jpeg)
图5-36. IGND vs VIN in the Dropout Region

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-41.jpeg](./images/img-41.jpeg)
图5-37.  $I_{\mathrm{GND}}$  vs  $V_{\mathrm{IN}}$  in the Dropout Region

![img-42.jpeg](./images/img-42.jpeg)
图5-38.  $I_{\mathrm{GND}}$  vs  $I_{\mathrm{OUT}}$

![img-43.jpeg](./images/img-43.jpeg)
图5-39.  $I_{\mathrm{GND}}$  vs  $I_{\mathrm{OUT}}$

![img-44.jpeg](./images/img-44.jpeg)
图5-40.  $I_{\mathrm{GND}}$  vs  $I_{\mathrm{OUT}}$

![img-45.jpeg](./images/img-45.jpeg)
图5-41. Shutdown Current vs  $V_{\mathrm{IN}}$

![img-46.jpeg](./images/img-46.jpeg)
图5-42. Shutdown Current vs  $V_{\mathrm{IN}}$

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-47.jpeg](./images/img-47.jpeg)
图5-43. Enable Pin Leakage Current vs  $V_{\text{EN}} - V_{\text{IN}}$

![img-48.jpeg](./images/img-48.jpeg)
图5-44. Current Limit

![img-49.jpeg](./images/img-49.jpeg)
图5-45. Current Limit

![img-50.jpeg](./images/img-50.jpeg)
图5-46. UVLO Threshold vs Temperature

![img-51.jpeg](./images/img-51.jpeg)
图5-47. Enable Logic High Threshold vs Temperature

![img-52.jpeg](./images/img-52.jpeg)
图5-48. Enable Logic Low Threshold Low vs Temperature

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-53.jpeg](./images/img-53.jpeg)
图5-49. Output Pulldown Resistor vs Temperature

![img-54.jpeg](./images/img-54.jpeg)
图5-50. Smart Enable Pulldown Resistor vs Temperature and  $V_{\mathrm{IN}}$

![img-55.jpeg](./images/img-55.jpeg)
图5-51. Load Transient

![img-56.jpeg](./images/img-56.jpeg)
图5-52. Load Transient

![img-57.jpeg](./images/img-57.jpeg)
图5-53. Load Transient

![img-58.jpeg](./images/img-58.jpeg)
图5-54. Load Transient

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-59.jpeg](./images/img-59.jpeg)

![img-60.jpeg](./images/img-60.jpeg)

![img-61.jpeg](./images/img-61.jpeg)
图5-55. Load Transient

![img-62.jpeg](./images/img-62.jpeg)
图5-56. Load Transient

![img-63.jpeg](./images/img-63.jpeg)
图5-57. Load Transient
$V_{\mathrm{IN}} = 3.1 \mathrm{~V} \rightarrow 4.1 \mathrm{~V} \rightarrow 3.1 \mathrm{~V}, V_{\mathrm{IN}} t_{\mathrm{RISING}} = 5 \mu \mathrm{s}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}$
图5-59. Line Transient

![img-64.jpeg](./images/img-64.jpeg)
图5-60. Line Transient

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-65.jpeg](./images/img-65.jpeg)
图5-61. PSRR vs  $V_{\mathrm{IN}}$  vs Frequency and  $V_{\mathrm{IN}}$

![img-66.jpeg](./images/img-66.jpeg)
图5-62. PSRR vs Frequency and  $V_{\mathrm{IN}}$

![img-67.jpeg](./images/img-67.jpeg)
图5-63. PSRR vs Frequency and  $I_{\mathrm{OUT}}$

![img-68.jpeg](./images/img-68.jpeg)
图5-64. PSRR vs Frequency and  $C_{\mathrm{OUT}}$

![img-69.jpeg](./images/img-69.jpeg)
$V_{\mathrm{RMS}}$  BW = 10 Hz to 100 kHz
图5-65. Noise vs Frequency and  $I_{\mathrm{OUT}}$

![img-70.jpeg](./images/img-70.jpeg)
$I_{\mathrm{OUT}} = 20 \mathrm{~mA}, V_{\mathrm{RMS}} \mathrm{BW} = 10 \mathrm{~Hz}$  to  $100 \mathrm{kHz}$
图5-66. Noise vs Frequency and  $V_{\mathrm{IN}}$

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-71.jpeg](./images/img-71.jpeg)
$\mathrm{I_{OUT} = 300mA,V_{RMS}BW = 10Hz}$  to  $100\mathrm{kHz}$

![img-72.jpeg](./images/img-72.jpeg)
$\mathrm{V_{IN}} = 3.8 \mathrm{~V}, \mathrm{I_{OUT}} = 20 \mathrm{~mA}, \mathrm{V_{RMS}} \mathrm{BW} = 10 \mathrm{~Hz}$  to  $100 \mathrm{kHz}$

![img-73.jpeg](./images/img-73.jpeg)
图5-67. Noise vs Frequency and  $V_{\mathrm{IN}}$

![img-74.jpeg](./images/img-74.jpeg)
图5-68. Noise vs Frequency and  $C_{\mathrm{OUT}}$
$\mathrm{V_{OUT}} = 0.8 \mathrm{~V}, \mathrm{V_{RMS}} \mathrm{BW} = 10 \mathrm{~Hz}$  to  $100 \mathrm{kHz}$

![img-75.jpeg](./images/img-75.jpeg)
图5-69. Noise vs Frequency and  $C_{\mathrm{OUT}}$
$\mathrm{V_{OUT}} = 0.8 \mathrm{~V}, \mathrm{V_{IN}} = 1.8 \mathrm{~V}, \mathrm{V_{RMS}} \mathrm{BW} = 10 \mathrm{~Hz}$  to  $100 \mathrm{kHz}$
图5-71. Noise vs Frequency and  $I_{\mathrm{OUT}}$

![img-76.jpeg](./images/img-76.jpeg)
图5-70. Noise vs Frequency and  $I_{\mathrm{OUT}}$
$\mathrm{V_{OUT}} = 5.5 \mathrm{~V}, \mathrm{V_{IN}} = 6 \mathrm{~V}, \mathrm{V_{RMS}} \mathrm{BW} = 10 \mathrm{~Hz}$  to  $100 \mathrm{kHz}$
图5-72. Noise vs Frequency and  $I_{\mathrm{OUT}}$

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-77.jpeg](./images/img-77.jpeg)
From  $V_{\text{EN}} = V_{\text{EN(HI)}}$  to  $V_{\text{OUT}} = 95\%$  of  $V_{\text{OUT(NOM)}}$ ,  $I_{\text{OUT}} = 0 \, \text{mA}$

![img-78.jpeg](./images/img-78.jpeg)
$V_{\mathrm{OUT}} = 0.8 \mathrm{~V}, V_{\mathrm{IN}} = 0 \mathrm{~V}$  to  $1.8 \mathrm{~V}, V_{\mathrm{EN}} = 0 \mathrm{~V}$  to  $1.8 \mathrm{~V}, V_{\mathrm{EN}}$  rises  $500 \mu \mathrm{s}$  behind  $V_{\mathrm{IN}}, V_{\mathrm{IN}}$  and  $V_{\mathrm{EN}}$  slew rate  $= 1 \mathrm{~V} / \mu \mathrm{s}$

![img-79.jpeg](./images/img-79.jpeg)
图5-73. Start-Up Turn-On Time
$V_{\mathrm{OUT}} = 0.8 \mathrm{~V}, V_{\mathrm{IN}} = 0 \mathrm{~V}$  to  $1.8 \mathrm{~V}, V_{\mathrm{EN}} = 0 \mathrm{~V}$  to  $1.8 \mathrm{~V}, V_{\mathrm{EN}}$  rises  $500 \mu \mathrm{s}$  ahead of  $V_{\mathrm{IN}}, V_{\mathrm{IN}}$  and  $V_{\mathrm{EN}}$  slew rate  $= 1 \mathrm{~V} / \mu \mathrm{s}$

![img-80.jpeg](./images/img-80.jpeg)
图5-74. Start-Up
$V_{\mathrm{OUT}} = 0.8 \mathrm{~V}, V_{\mathrm{IN}} = 0 \mathrm{~V}$  to  $1.8 \mathrm{~V}, V_{\mathrm{EN}} = V_{\mathrm{IN}}$ $V_{\mathrm{IN}}$  slew rate  $= 1 \mathrm{~V} / \mu \mathrm{s}$

![img-81.jpeg](./images/img-81.jpeg)
图5-75. Start-Up
$V_{\mathrm{IN}} = 0 \mathrm{~V}$  to  $3.8 \mathrm{~V}, V_{\mathrm{EN}} = 0 \mathrm{~V}$  to  $3.8 \mathrm{~V}, V_{\mathrm{EN}}$  rises  $500 \mu \mathrm{s}$  behind  $V_{\mathrm{IN}}, V_{\mathrm{IN}}$  and  $V_{\mathrm{EN}}$  slew rate  $= 1 \mathrm{~V} / \mu \mathrm{s}$

![img-82.jpeg](./images/img-82.jpeg)
图5-76. Start-Up
$V_{\mathrm{IN}} = 0 \mathrm{~V}$  to  $3.8 \mathrm{~V}, V_{\mathrm{EN}} = 0 \mathrm{~V}$  to  $3.8 \mathrm{~V}, V_{\mathrm{EN}}$  rises  $500 \mu \mathrm{s}$  ahead of  $V_{\mathrm{IN}}, V_{\mathrm{IN}}$  and  $V_{\mathrm{EN}}$  slew rate  $= 1 \mathrm{~V} / \mu \mathrm{s}$
图5-77. Start-Up
图5-78. Start-Up

# 5.7 Typical Characteristics (continued)

$V_{\mathrm{IN}} = V_{\mathrm{OUT(NOM)}} + 0.3 \mathrm{~V}$  or  $1.6 \mathrm{~V}$  (whichever is greater),  $V_{\mathrm{OUT}} = 2.8 \mathrm{~V}, I_{\mathrm{OUT}} = 1 \mathrm{~mA}, C_{\mathrm{IN}} = 1 \mu \mathrm{F}, C_{\mathrm{OUT}} = 1 \mu \mathrm{F},$  and  $T_{\mathrm{A}} = 25^{\circ} \mathrm{C}$  (unless otherwise noted)

![img-83.jpeg](./images/img-83.jpeg)
$\mathrm{V_{IN}} = 0\mathrm{V}$  to  $3.8\mathrm{V},\mathrm{V_{EN}} = 0\mathrm{V}$  to  $3.8\mathrm{V},\mathrm{V_{EN}} = \mathrm{V_{IN}},\mathrm{V_{IN}}$  and slew rate  $= 1\mathrm{V} / \mu \mathrm{s}$

图5-79. Start-Up
![img-84.jpeg](./images/img-84.jpeg)
$\mathrm{V_{OUT}} = 5.5\mathrm{V},\mathrm{V_{IN}} = 0\mathrm{V}$  to  $6.0\mathrm{V},\mathrm{V_{EN}} = 0\mathrm{V}$  to  $6.0\mathrm{V},\mathrm{V_{EN}}$  rises  $500~\mu \mathrm{s}$  ahead of  $\mathrm{V_{IN}},\mathrm{V_{IN}}$  and  $\mathrm{V_{EN}}$  slew rate  $= 1\mathrm{V} / \mu \mathrm{s}$

图5-80. Start-Up
![img-85.jpeg](./images/img-85.jpeg)
$\mathrm{V_{OUT}} = 5.5\mathrm{V},\mathrm{V_{IN}} = 0\mathrm{V}$  to  $6.0\mathrm{V},\mathrm{V_{EN}} = 0\mathrm{V}$  to  $6.0\mathrm{V},\mathrm{V_{EN}}$  rises  $500~\mu \mathrm{s}$  behind  $\mathrm{V_{IN}},\mathrm{V_{IN}}$  and  $\mathrm{V_{EN}}$  slew rate  $= 1\mathrm{V} / \mu \mathrm{s}$

图5-81. Start-Up
![img-86.jpeg](./images/img-86.jpeg)
$\mathrm{V_{OUT}} = 0.8\mathrm{V},\mathrm{V_{IN}} = 1.8\mathrm{V},\mathrm{V_{EN}} = 0\mathrm{V}$  to  $1.8\mathrm{V},$ $\mathrm{V_{EN}}$  slew rate  $= 1\mathrm{V} / \mu \mathrm{s},\mathrm{C_{OUT}} = 10~\mu \mathrm{F}$

图5-82. Start-Up
![img-87.jpeg](./images/img-87.jpeg)
$\mathrm{V_{OUT}} = 5.5\mathrm{V},\mathrm{V_{IN}} = 0\mathrm{V}$  to  $6\mathrm{V},\mathrm{V_{EN}} = \mathrm{V_{IN}},\mathrm{V_{IN}}$  slew rate  $= 1\mathrm{V} / \mu \mathrm{s}$

图5-83. Inrush Current
![img-88.jpeg](./images/img-88.jpeg)
$\mathrm{V_{IN}} = 3.8\mathrm{V},\mathrm{V_{EN}} = 0\mathrm{V}$  to  $3.8\mathrm{V},\mathrm{V_{EN}}$  slew rate  $= 1\mathrm{V} / \mu \mathrm{s},$ $C_{OUT} = 10~\mu \mathrm{F}$

图5-84. Inrush Current
![img-89.jpeg](./images/img-89.jpeg)
图5-83.  $\mathrm{IV}$  /  $\mu \mathrm{s}$  -s

# 5.7 Typical Characteristics (continued)

$V_{\text{IN}} = V_{\text{OUT(NOM)}} + 0.3 \, \text{V}$  or  $1.6 \, \text{V}$  (whichever is greater),  $V_{\text{OUT}} = 2.8 \, \text{V}, I_{\text{OUT}} = 1 \, \text{mA}, C_{\text{IN}} = 1 \, \mu \text{F}, C_{\text{OUT}} = 1 \, \mu \text{F},$  and  $T_{\text{A}} = 25^{\circ} \text{C}$  (unless otherwise noted)

![img-90.jpeg](./images/img-90.jpeg)
图 5-85. Inrush Current

# 6 Detailed Description

## 6.1 Overview

Designed to meet the needs of sensitive RF and analog circuits, the TPS7A20 provides low noise, high PSRR, low quiescent current, as well as low line and load transient response figures. Using innovative design techniques, the TPS7A20 offers class-leading noise performance without the need for a separate noise filter capacitor.

The TPS7A20 is designed to operate with a single 1-μF input capacitor and a single 1-μF ceramic output capacitor.

## 6.2 Functional Block Diagram

![img-91.jpeg](./images/img-91.jpeg)

# 6.3 Feature Description

## 6.3.1 Low Output Noise

Any internal noise at the TPS7A20 reference voltage is reduced by a first-order, low-pass RC filter before being passed to the output buffer stage. The low-pass RC filter has a -3dB cut-off frequency of approximately 0.1Hz.

During start-up, the filter resistor is bypassed to reduce output rise time; the filter begins normal operation after the output voltage reaches the correct value.

## 6.3.2 Smart Enable

The enable (EN) input polarity is active high. The output voltage is enabled when the voltage of the enable input is greater than $V_{\mathrm{EN(HI)}}$ and disabled when the enable input voltage is less than $V_{\mathrm{EN(LOW)}}$. If independent control of the output voltage is not needed, connect EN to IN.

This device has a smart enable circuit to reduce quiescent current. When the voltage on the enable pin is driven above $V_{\mathrm{EN(HI)}}$, as listed in the Electrical Characteristics table, the device is enabled and the smart enable internal pulldown resistor ($R_{\mathrm{EN(PULLDOWN)}}$) is disconnected. When the enable pin is floating, the $R_{\mathrm{EN(PULLDOWN)}}$ is connected and pulls the enable pin low to disable the device. The $R_{\mathrm{EN(PULLDOWN)}}$ value is listed in the Electrical Characteristics table.

## 6.3.3 Dropout Voltage

Dropout voltage ($V_{\mathrm{DO}}$) is defined as the input voltage minus the output voltage ($V_{\mathrm{IN}} - V_{\mathrm{OUT}}$) at the rated output current ($I_{\mathrm{RATED}}$), where the pass transistor is fully on. $I_{\mathrm{RATED}}$ is the maximum $I_{\mathrm{OUT}}$ listed in the Recommended Operating Conditions table. The pass transistor is in the ohmic or triode region of operation, and acts as a switch. The dropout voltage indirectly specifies a minimum input voltage greater than the nominal programmed output voltage at which the output voltage is expected to stay in regulation. If the input voltage falls to less than the value required to maintain output regulation, then the output voltage falls as well.

For a CMOS regulator, the dropout voltage is determined by the drain-source on-state resistance ($R_{\mathrm{DS(ON)}}$) of the pass transistor. Therefore, if the linear regulator operates at less than the rated current, the dropout voltage for that current scales accordingly. The following equation calculates the $R_{\mathrm{DS(ON)}}$ of the device.

$$
R_{\mathrm{DS(ON)}} = \frac{V_{\mathrm{DO}}}{I_{\mathrm{RATED}}} \tag{1}
$$

## 6.3.4 Foldback Current Limit

The device has an internal current limit circuit that protects the regulator during transient high-load current faults or shorting events. The current limit is a hybrid brick-wall-foldback scheme. The current limit transitions from a brick-wall scheme to a foldback scheme at the foldback voltage ($V_{\mathrm{FOLDBACK}}$). In a high-load current fault with the output voltage above $V_{\mathrm{FOLDBACK}}$, the brick-wall scheme limits the output current to the current limit ($I_{\mathrm{CL}}$). When the voltage drops below $V_{\mathrm{FOLDBACK}}$, a foldback current limit activates that scales back the current as the output voltage approaches GND. When the output is shorted, the device supplies a typical current called the short-circuit current limit ($I_{\mathrm{SC}}$). $I_{\mathrm{CL}}$ and $I_{\mathrm{SC}}$ are listed in the Electrical Characteristics table.

The output voltage is not regulated when the device is in current limit. When a current limit event occurs, the device begins to heat up because of the increase in power dissipation. When the device is in brick-wall current limit, the pass transistor dissipates power $[(V_{\mathrm{IN}} - V_{\mathrm{OUT}}) \times I_{\mathrm{CL}}]$. When the device output is shorted and the output is below $V_{\mathrm{FOLDBACK}}$, the pass transistor dissipates power $[(V_{\mathrm{IN}} - V_{\mathrm{OUT}}) \times I_{\mathrm{SC}}]$. If thermal shutdown is triggered, the device turns off. After the device cools down, the internal thermal shutdown circuit turns the device back on. If the output current fault condition continues, the device cycles between current limit and thermal shutdown. For more information on current limits, see the Know Your Limits application note.

图6-1 shows a diagram of the foldback current limit.

![img-92.jpeg](./images/img-92.jpeg)
图6-1. Foldback Current Limit

# 6.3.5 Undervoltage Lockout (UVLO)

The device has an independent undervoltage lockout (UVLO) circuit that monitors the input voltage, allowing a controlled and consistent turn on and off of the output voltage. To prevent the device from turning off if the input drops during turn on, the UVLO has hysteresis as specified in the Electrical Characteristics table.

# 6.3.6 Thermal Shutdown

A thermal shutdown protection circuit disables the LDO when the junction temperature  $(T_{\mathrm{J}})$  of the pass transistor rises to  $T_{\mathrm{SD(shutdown)}}$  (typical). Thermal shutdown hysteresis assures that the device resets (turns on) when the temperature falls to  $T_{\mathrm{SD(reset)}}$  (typical).

The thermal time-constant of the semiconductor die is fairly short, thus the device may cycle on and off when thermal shutdown is reached until power dissipation is reduced. Power dissipation during startup can be high from large  $V_{\text{IN}} - V_{\text{OUT}}$  voltage drops across the device or from high inrush currents charging large output capacitors. Under some conditions, the thermal shutdown protection disables the device before startup completes.

For reliable operation, limit the junction temperature to the maximum listed in the Recommended Operating Conditions table. Operation above this maximum temperature causes the device to exceed its operational specifications. Although the internal protection circuitry of the device is designed to protect against thermal overload conditions, this circuitry is not intended to replace proper heat sinking. Continuously running the device into thermal shutdown or above the maximum recommended junction temperature reduces long-term reliability.

## 6.3.7 Active Discharge (P Version Only)

An internal pulldown MOSFET connects a resistor from OUT to ground when the device is disabled to actively discharge the output capacitance. The active discharge circuit is activated by driving EN low or by the voltage on IN falling below the undervoltage lockout (UVLO) threshold.

Do not rely on the active discharge circuit for discharging a large amount of output capacitance after the input supply has collapsed because reverse current can possibly flow from the output to the input. This reverse current flow can cause damage to the device. Limit reverse current to no more than 5% of the device rated current for a short period of time.

## 6.4 Device Functional Modes

### 6.4.1 Device Functional Mode Comparison

表 6-1 shows the conditions that lead to the different modes of operation. See the Electrical Characteristics table for parameter values.

表 6-1. Device Functional Mode Comparison

|  OPERATING MODE | PARAMETER  |   |   |   |
| --- | --- | --- | --- | --- |
|   |  V_{IN} | V_{EN} | I_{OUT} | T_{J}  |
|  Normal operation | V_{IN} > V_{OUT(nom)} + V_{DO} and V_{IN} > V_{IN(min)} | V_{EN} > V_{EN(HI)} | I_{OUT} < I_{OUT(max)} | T_{J} < T_{SD(shutdown)}  |
|  Dropout operation | V_{IN(min)} < V_{IN} < V_{OUT(nom)} + V_{DO} | V_{EN} > V_{EN(HI)} | I_{OUT} < I_{OUT(max)} | T_{J} < T_{SD(shutdown)}  |
|  Disabled
(any true condition
disables the device) | V_{IN} < V_{UVLO} | V_{EN} < V_{EN(LOW)} | Not applicable | T_{J} > T_{SD(shutdown)}  |

### 6.4.2 Normal Operation

The device regulates to the nominal output voltage when the following conditions are met:

- The input voltage is greater than the nominal output voltage plus the dropout voltage (V<out(nom) +="" v<do="">)
- The output current is less than the current limit (I<out <="" i<cl="">)
- The device junction temperature is less than the thermal shutdown temperature (T<j <="" t<sd="">
- The enable voltage has previously exceeded the enable rising threshold voltage and has not yet decreased to less than the enable falling threshold

### 6.4.3 Dropout Operation

If the input voltage is lower than the nominal output voltage plus the specified dropout voltage, but all other conditions are met for normal operation, the device operates in dropout mode. In this mode, the output voltage tracks the input voltage. During this mode, the transient performance of the device becomes significantly degraded because the pass transistor is in the ohmic or triode region, and acts as a switch. Line or load transients in dropout can result in large output-voltage deviations.

When the device is in a steady dropout state (defined as when the device is in dropout, V<in <="" <="" and="" current="" during="" for="" is="" it="" it<out(nom)="" of="" or="" pump),="" r<op),="" startup),="" the="" to="" voltage="" voltage="" with="">), the pass transistor is driven into the ohmic or triode region. When the input voltage returns to a value greater than or equal to the nominal output voltage plus the dropout voltage (V<out(nom) +="" v<do="">), the output voltage can overshoot for a short period of time while the device pulls the pass transistor back into the linear region.

### 6.4.4 Disabled

The output of the LDO can be shut down by driving EN to less than V<en(low) ##="" (see="" (t<sub="" 2024="" 6.4.4="" <table="" and="" activated="" based="" be="" by="" can="" circuit="" circuit)="" data).="" discharge="" effectical="" end="" essential="" for="" from="" hand="" in="" is="" it="" linear="" loss="" mode,="" non="" of="" output="" p<sup="" pass="" range="" resistance="" resistance)="" results="" same="" sch="" sch(cr)="" that="" the="" three="" to="" used="" voltage="" when="" with="">) <in></en(low)></in></out(nom)></out(nom)># 7 Application and Implementation

备注

以下应用部分中的信息不属于 TI 器件规格的范围，TI 不担保其准确性和完整性。TI 的客户应负责确定器件是否适用于其应用。客户应验证并测试其设计，以确保系统功能。

# 7.1 Application Information

## 7.1.1 Recommended Capacitor Types

The device is designed to be stable using low equivalent series resistance (ESR) ceramic capacitors at the input and output. Multilayer ceramic capacitors have become the industry standard for these types of applications and are recommended, but must be used with good judgment. Ceramic capacitors that employ X7R-, X5R-, and C0G-rated dielectric materials provide relatively good capacitive stability across temperature, whereas the use of Y5V-rated capacitors is discouraged because of large variations in capacitance.

Regardless of the ceramic capacitor type selected, the effective capacitance varies with operating voltage and temperature. As a rule of thumb, expect the effective capacitance to decrease by as much as 50%. The input and output capacitors recommended in the Recommended Operating Conditions table account for an effective capacitance of approximately 50% of the nominal value.

## 7.1.2 Input and Output Capacitor Requirements

Although the LDO itself is stable without an input capacitor, good analog design practice is to connect a capacitor from IN to GND, with a value at least equal to the nominal value specified in the Recommended Operating Conditions table. The input capacitor counteracts reactive input sources and improves transient response, input ripple, and PSRR, and is recommended if the source impedance is greater than 0.5 Ω. When the source resistance and inductance are sufficiently high, especially in the presence of load transients, the overall system may be susceptible to instability (including ringing and sustained oscillation) and other performance degradation if there is insufficient capacitance between IN and GND. A capacitor with a value greater than the minimum may be necessary if large, fast-rise-time load or line transients are anticipated or if the device is located more than a few centimeters from the input power source.

An output capacitor of an appropriate value helps ensure stability and improve dynamic performance. Use an output capacitor within the range specified in the Recommended Operating Conditions table.

## 7.1.3 Load Transient Response

The load-step transient response is the output voltage response by the LDO to a step in load current, whereby output voltage regulation is maintained. There are two key transitions during a load transient response: the transition from a light to a heavy load and the transition from a heavy to a light load. The regions shown in 图 7-1 are broken down as follows. Regions A, E, and H are where the output voltage is in steady-state.

![img-93.jpeg](./images/img-93.jpeg)
图 7-1. Load Transient Waveform

During transitions from a light load to a heavy load, the:

- Initial voltage dip is a result of the depletion of the output capacitor charge and parasitic impedance to the output capacitor (region B)

- Recovery from the dip results from the LDO increasing its sourcing current, and leads to output voltage regulation (region C)

During transitions from a heavy load to a light load, the:

- Initial voltage rise results from the LDO sourcing a large current, and leads to the output capacitor charge to increase (region F)
- Recovery from the rise results from the LDO decreasing its sourcing current in combination with the load discharging the output capacitor (region G)

A larger output capacitance reduces the peaks during a load transient but slows down the response time of the device. A larger DC load also reduces the peaks because the amplitude of the transition is lowered and a higher current discharge path is provided for the output capacitor.

## 7.1.4 Undervoltage Lockout (UVLO) Operation

The UVLO circuit ensures that the device stays disabled before its input supply reaches the minimum operational voltage range, and ensures that the device shuts down when the input supply collapses. 图 7-2 shows the UVLO circuit response to various input voltage events. The diagram can be separated into the following parts:

- Region A: The device does not start until the input reaches the UVLO rising threshold.
- Region B: Normal operation, regulating device.
- Region C: Brownout event above the UVLO falling threshold (UVLO rising threshold - UVLO hysteresis). The output may fall out of regulation but the device remains enabled.
- Region D: Normal operation, regulating device.
- Region E: Brownout event below the UVLO falling threshold. The device is disabled in most cases and the output falls because of the load and active discharge circuit. The device is re-enabled when the UVLO rising threshold is reached by the input voltage and a normal start-up follows.
- Region F: Normal operation followed by the input falling to the UVLO falling threshold.
- Region G: The device is disabled when the input voltage falls below the UVLO falling threshold to 0 V. The output falls because of the load and active discharge circuit.

![img-94.jpeg](./images/img-94.jpeg)
图 7-2. Typical UVLO Operation

## 7.1.5 Power Dissipation $(P_{D})$

Circuit reliability demands that proper consideration be given to device power dissipation, location of the circuit on the printed circuit board (PCB), and correct sizing of the thermal plane. The PCB area around the regulator must be as free as possible of other heat-generating devices that cause added thermal stresses.

As a first-order approximation, power dissipation in the regulator depends on the input-to-output voltage difference and load conditions. Use 方程式 2 to approximate $P_{D}$:

$$
P_{D} = (V_{IN} - V_{OUT}) \times I_{OUT} \tag{2}
$$

Power dissipation can be minimized, and thus greater efficiency achieved, by proper selection of the system voltage rails. Proper selection allows the minimum input-to-output voltage differential to be obtained. The low dropout of the TPS7A20 allows for maximum efficiency across a wide range of output voltages.

The main heat conduction path for the device is through the thermal pad on the package. As such, the thermal pad must be soldered to a copper pad area under the device. This pad area contains an array of plated vias that conduct heat to any inner plane areas or to a bottom-side copper plane.

The maximum power dissipation determines the maximum allowable junction temperature (T_{J}) for the device. According to 方程式 3, power dissipation and junction temperature are most often related by the junction-to-ambient thermal resistance (R_{θ JA}) of the combined PCB and device package and the temperature of the ambient air (T_{A}). 方程式 4 rearranges 方程式 3 for output current. T_{J} = T_{A} + (R_{θ JA} × P_{D})I_{OUT} = (T_{J} - T_{A}) / [R_{θ JA} × (V_{IN} - V_{OUT})]

Unfortunately, this thermal resistance (R_{θ JA}) is highly dependent on the heat-spreading capability built into the particular PCB design, and therefore varies according to the total copper area, copper weight, and location of the planes. The R_{θ JA} recorded in the Thermal Information table is determined by the JEDEC standard, PCB, and copper-spreading area, and is only used as a relative measure of package thermal performance. For a well-designed thermal layout, R_{θ JA} is actually the sum of the X2SON package junction-to-case (bottom) thermal resistance (R_{θ JC(bot)}) plus the thermal resistance contribution by the PCB copper.

##### Estimating Junction Temperature

The JEDEC standard now recommends the use of psi (Ψ) thermal metrics to estimate the junction temperatures of the LDO when in-circuit on a typical PCB board application. These metrics are not strictly speaking thermal resistances, but rather offer practical and relative means of estimating junction temperatures. These psi metrics are determined to be significantly independent of the copper-spreading area. The key thermal metrics (Ψ_{JT} and Ψ_{JB}) are used in accordance with 方程式 5 and are given in the Thermal Information table. Ψ_{JT} : T_{J} = T_{T} + Ψ_{JT} × P_{D} and Ψ_{JB} : T_{J} = T_{B} + Ψ_{JB} × P_{D}

where: P_{D} is the power dissipated as explained in 方程式 2T_{T} is the temperature at the center-top of the device packageT_{B} is the PCB surface temperature measured 1 mm from the device package and centered on the package edge

##### Recommended Area for Continuous Operation

The operational area of an LDO is limited by the dropout voltage, output current, junction temperature, and input voltage. The recommended area for continuous operation for a linear regulator is given in 图 7-3 and can be separated into the following parts: Dropout voltage limits the minimum differential voltage between the input and the output (V_{IN} - V_{OUT}) at a given output current level. See the Dropout Operation section for more details.The rated output currents limits the maximum recommended output current level. Exceeding this rating causes the device to fall out of specification.The rated junction temperature limits the maximum junction temperature of the device. Exceeding this rating causes the device to fall out of specification and reduces long-term reliability. - The shape of the slope is given by 方程式 4. The slope is nonlinear because the maximum-rated junction temperature of the LDO is controlled by the power dissipation across the LDO; thus when V_{IN} - V_{OUT} increases the output current must decrease.The rated input voltage range governs both the minimum and maximum of V_{IN} - V_{OUT}.图 7-3 shows the recommended area of operation for this device on a JEDEC-standard high-K board with a $R_{\parallel JA}$ as given in the Thermal Information table.

![img-95.jpeg](./images/img-95.jpeg)
图 7-3. Region Description of Continuous Operation Regime

## 7.2 Typical Application

图 7-4 shows the typical application circuit for the TPS7A20. Input and output capacitances may need to be increased above the $1\,\mu\mathrm{F}$ minimum for some applications.

![img-96.jpeg](./images/img-96.jpeg)
图 7-4. TPS7A20 Typical Application

## 7.2.1 Design Requirements

表 7-1 summarizes the design requirements for 图 7-4.

表 7-1. Design Parameters

|  DESIGN PARAMETER | EXAMPLE VALUE  |
| --- | --- |
|  Input voltage range | 3.1 V to 3.6 V  |
|  Output voltage | 2.8 V  |
|  Output current | 200 mA  |
|  Maximum ambient temperature | 85°C  |

## 7.2.2 Detailed Design Procedure

For this design example, the 2.8V output version (TPS7A2028) is selected. A nominal 3.3V input supply is assumed. A minimum $1.0\,\mu\mathrm{F}$ input capacitor is recommended to minimize the effect of resistance and inductance between the 3.3V source and the LDO input. A minimum $1.0\,\mu\mathrm{F}$ output capacitor is also recommended for stability and good load transient response. The dropout voltage $(V_{DO})$ is less than $140\,\mathrm{mV}$ maximum at a 2.8V output voltage and $300\,\mathrm{mA}$ output current, so there are no dropout issues with a minimum input voltage of 3.0V and a maximum output current of $200\,\mathrm{mA}$.

## 7.2.3 Application Curves

![img-97.jpeg](./images/img-97.jpeg)
图 7-5. Start-Up

![img-98.jpeg](./images/img-98.jpeg)
图 7-6. PSRR

## 7.3 Power Supply Recommendations

This device is designed to operate from an input supply voltage range of 1.6V to 6.0V. The input supply must be well regulated and free of spurious noise. To ensure that the output voltage is well regulated and dynamic performance is optimum, the input supply must be at least $V_{\mathrm{OUT(nom)}} + 0.3\,\mathrm{V}$ or 1.6V, whichever is greater. TI highly recommends using a $1\,\mu\mathrm{F}$ or greater input capacitor to reduce the impedance of the input supply, especially during transients.

## 7.4 Layout

### 7.4.1 Layout Guidelines

- Place input and output capacitors as close to the device as possible.
- Use copper planes for device connections to optimize thermal performance.
- Place thermal vias around the device to distribute the heat.
- Do not place a thermal via directly beneath the thermal pad of the DQN package. A via can wick solder or solder paste away from the thermal pad joint during the soldering process, leading to a compromised solder joint on the thermal pad.

# 7.4.2 Layout Examples

![img-99.jpeg](./images/img-99.jpeg)
图 7-7. DBV Package (SOT-23) Typical Layout

![img-100.jpeg](./images/img-100.jpeg)
图 7-8. DQN Package (X2SON) Typical Layout

![img-101.jpeg](./images/img-101.jpeg)
图 7-9. YCJ and YCK Package (DSBGA) Typical Layout

# 8 Device and Documentation Support

## 8.1 Device Support

### 8.1.1 Device Nomenclature

表 8-1. Device Nomenclature

|  PRODUCT (1) (2) | VOUT  |
| --- | --- |
|  TPS7A20xx(x)Pyyyz | xx(x) is the nominal output voltage. For output voltages with a resolution of 100 mV, two digits are used in the ordering number; otherwise, three digits are used (for example, 28 = 2.8V; 125 = 1.25V).
P indicates an active output discharge feature.
yyy is the package designator.
z is the package quantity. R is for reel (3000 pieces for DQN and DBV; 12000 pieces for YCJ and YCK).  |

(1) For the most current package and ordering information see the Package Option Addendum at the end of this document, or visit the device product folder on www.ti.com.
(2) Output voltages from 0.8V to 5.5V in 25mV increments are available. Contact the factory for details and availability.

## 8.2 接收文档更新通知

要接收文档更新通知，请导航至 ti.com 上的器件产品文件夹。点击通知进行注册，即可每周接收产品信息更改摘要。有关更改的详细信息，请查看任何已修订文档中包含的修订历史记录。

## 8.3 支持资源

TI E2E™ 中文支持论坛是工程师的重要参考资料，可直接从专家处获得快速、经过验证的解答和设计帮助。搜索现有解答或提出自己的问题，获得所需的快速设计帮助。

链接的内容由各个贡献者“按原样”提供。这些内容并不构成 TI 技术规范，并且不一定反映 TI 的观点；请参阅 TI 的使用条款。

## 8.4 Trademarks

TI E2E™ is a trademark of Texas Instruments.

所有商标均为其各自所有者的财产。

## 8.5 静电放电警告

![img-102.jpeg](./images/img-102.jpeg)

静电放电 (ESD) 会损坏这个集成电路。德州仪器 (TI) 建议通过适当的预防措施处理所有集成电路。如果不遵守正确的处理和安装程序，可能会损坏集成电路。

ESD 的损坏小至导致微小的性能降级，大至整个器件故障。精密的集成电路可能更容易受到损坏，这是因为非常细微的参数更改都可能会导致器件与其发布的规格不相符。

## 8.6 术语表

TI 术语表

本术语表列出并解释了术语、首字母缩略词和定义。

# 9 Revision History

注：以前版本的页码可能与当前版本的页码不同

## Changes from Revision G (May 2022) to Revision H (July 2024)

- 更改了特性中的封装要点，以进行澄清...1
- 更改了应用原理图的标题...1
- Deleted discussion of pulldown resistor from OUT pin description in YCJ and YCK package Pin Functions table...3
- Added clarification to Active Discharge (P Version Only) section that this feature only applies to the P device version...26
- Changed active output discharge feature discussion in Device Nomenclature table...33

## Changes from Revision F (April 2022) to Revision G (May 2022)

- Changed UVLO condition from rising to falling for YCJ and YCK packages...6

## 10 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

# 10.1 Mechanical Data

YCJ0004-C02

![img-103.jpeg](./images/img-103.jpeg)

PACKAGE OUTLINE

DSBGA - 0.35 mm max height

DIE SIZE BALL GRID ARRAY

![img-104.jpeg](./images/img-104.jpeg)

![img-105.jpeg](./images/img-105.jpeg)

D: Max = 0.636 mm, Min = 0.596 mm

E: Max = 0.636 mm, Min = 0.596 mm

4226216/A 09/2020

# NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.

# EXAMPLE BOARD LAYOUT

YCJ0004-C02

DSBGA - 0.35 mm max height

DIE SIZE BALL GRID ARRAY

![img-106.jpeg](./images/img-106.jpeg)
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 50X

![img-107.jpeg](./images/img-107.jpeg)
NON-SOLDER MASK DEFINED

![img-108.jpeg](./images/img-108.jpeg)
SOLDER MASK DEFINED (PREFERRED)
SOLDER MASK DETAILS
NOT TO SCALE

4226216/A 09/2020

NOTES: (continued)

3. Final dimensions may vary due to manufacturing tolerance considerations and also routing constraints.
See Texas Instruments Literature No. SNVA009 (www.ti.com/lit/snva009).

# EXAMPLE STENCIL DESIGN

YCJ0004-C02

DSBGA - 0.35 mm max height

DIE SIZE BALL GRID ARRAY

![img-109.jpeg](./images/img-109.jpeg)
SOLDER PASTE EXAMPLE
BASED ON 0.075 mm THICK STENCIL
SCALE: 50X

4226216/A 09/2020

NOTES: (continued)

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release.

![img-110.jpeg](./images/img-110.jpeg)

![img-111.jpeg](./images/img-111.jpeg)

![img-112.jpeg](./images/img-112.jpeg)

D: Max = 0.636 mm, Min = 0.596 mm
E: Max = 0.636 mm, Min = 0.596 mm

4228575/A 03/2022

# NOTES:

1. All linear dimensions are in millimeters. Dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.

# EXAMPLE BOARD LAYOUT

# YCK0004-C01

# DSBGA - 0.33mm MAX HEIGHT

DIE SIZE BALL GRID ARRAY

![img-113.jpeg](./images/img-113.jpeg)
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:60X

![img-114.jpeg](./images/img-114.jpeg)
NON SOLDERMASK DEFINED

![img-115.jpeg](./images/img-115.jpeg)
SOLDERMASK DEFINED (PREFERRED)

SOLDERMASK DETAILS
NOT TO SCALE

4228575/A 03/2022

NOTES: (continued)

3. Final dimensions may vary due to manufacturing tolerance considerations and also routing constraints. Refer to Texas Instruments Literature No. SNVA009 (www.ti.com/lit/snva009).

# EXAMPLE STENCIL DESIGN

YCK0004-C01

DSBGA - 0.33mm MAX HEIGHT

DIE SIZE BALL GRID ARRAY

![img-116.jpeg](./images/img-116.jpeg)
SOLDERPASTE EXAMPLE
BASED ON 0.075 mm THICK STENCIL
SCALE:80X

4228575/A 03/2022

NOTES: (continued)

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release.

PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PTPS7A2025PDQNR | Active | Preproduction | X2SON (DQN) | 4 | 3000 | LARGE T&R | - | Call TI | Call TI | -40 to 125 |  |
| PTPS7A2025PDQNR.A | Active | Preproduction | X2SON (DQN) | 4 | 3000 | LARGE T&R | - | Call TI | Call TI | -40 to 125 |  |
| PTPS7A2045PDQNR | Active | Preproduction | X2SON (DQN) | 4 | 3000 | LARGE T&R | - | Call TI | Call TI | -40 to 125 |  |
| PTPS7A2045PDQNR.A | Active | Preproduction | X2SON (DQN) | 4 | 3000 | LARGE T&R | - | Call TI | Call TI | -40 to 125 |  |
| TPS7A2008DQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QH |
| TPS7A2008DQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QH |
| TPS7A2009PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2GBF |
| TPS7A2009PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GBF |
| TPS7A2009PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KT |
| TPS7A2009PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KT |
| TPS7A20105PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KS |
| TPS7A20105PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KS |
| TPS7A20115PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QE |
| TPS7A20115PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QE |
| TPS7A2011PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | Q |
| TPS7A2011PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | Q |
| TPS7A2012DQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QI |
| TPS7A2012DQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QI |
| TPS7A2012PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2ATF |
| TPS7A2012PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 125 | 2ATF |
| TPS7A2012PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2ATF |
| TPS7A2012PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2ATF |
| TPS7A2012PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JC |
| TPS7A2012PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JC |
| TPS7A2012PYCJR | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | M |
| TPS7A2012PYCJR.A | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | M |
| TPS7A20135PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | MM |
| TPS7A20135PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | MM |
| TPS7A2013DQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QJ |

| Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPS7A2013DQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QJ |
| TPS7A2015PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2DTF |
| TPS7A2015PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 125 | 2DTF |
| TPS7A2015PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | -40 to 125 | JD |
| TPS7A2015PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JD |
| TPS7A2016YCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | Z |
| TPS7A2016YCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | Z |
| TPS7A201825PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | -40 to 125 | IQ |
| TPS7A201825PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | IQ |
| TPS7A201825PDQNRM3 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | IQ |
| TPS7A201825PDQNRM3.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | IQ |
| TPS7A20185PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2CBF |
| TPS7A20185PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2CBF |
| TPS7A20185PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2CBF |
| TPS7A20185PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2CBF |
| TPS7A20185PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | -40 to 125 | JE |
| TPS7A20185PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JE |
| TPS7A20185PDQNRM3 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JE |
| TPS7A20185PDQNRM3.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JE |
| TPS7A20185PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | T |
| TPS7A20185PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | T |
| TPS7A2018DQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QK |
| TPS7A2018DQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QK |
| TPS7A2018PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2AUF |
| TPS7A2018PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AUF |
| TPS7A2018PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AUF |
| TPS7A2018PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AUF |
| TPS7A2018PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | -40 to 125 | JF |
| TPS7A2018PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JF |
| TPS7A2018PDQNRM3 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JF |
| TPS7A2018PDQNRM3.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JF |

| Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPS7A2018PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | D |
| TPS7A2018PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | D |
| TPS7A2018PYCKRM3 | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | D |
| TPS7A2018YCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | Y |
| TPS7A2018YCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | Y |
| TPS7A2020PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | S |
| TPS7A2020PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | S |
| TPS7A20225PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | PX |
| TPS7A20225PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | PX |
| TPS7A202275PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | B |
| TPS7A202275PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | B |
| TPS7A2022PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | K |
| TPS7A2022PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | K |
| TPS7A2024PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2CCF |
| TPS7A2024PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 125 | 2CCF |
| TPS7A2025DQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QL |
| TPS7A2025DQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QL |
| TPS7A2025PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2AVF |
| TPS7A2025PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AVF |
| TPS7A2025PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AVF |
| TPS7A2025PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AVF |
| TPS7A2025PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JG |
| TPS7A2025PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JG |
| TPS7A2025PYCJR | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | L |
| TPS7A2025PYCJR.A | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | L |
| TPS7A2027PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KO |
| TPS7A2027PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KO |
| TPS7A2027PYCJR | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | N |
| TPS7A2027PYCJR.A | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | N |
| TPS7A20285PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2GCF |
| TPS7A20285PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 125 | 2GCF |

| Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPS7A20285PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KN |
| TPS7A20285PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KN |
| TPS7A20285PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | P |
| TPS7A20285PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | P |
| TPS7A2028DQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QM |
| TPS7A2028DQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QM |
| TPS7A2028PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2AWF |
| TPS7A2028PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AWF |
| TPS7A2028PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | -40 to 125 | JH |
| TPS7A2028PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JH |
| TPS7A2028PDQNRM3 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JH |
| TPS7A2028PDQNRM3.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JH |
| TPS7A2028PYCJR | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | E |
| TPS7A2028PYCJR.A | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | E |
| TPS7A2028PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | E |
| TPS7A2028PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | E |
| TPS7A2029PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JI |
| TPS7A2029PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JI |
| TPS7A2030DQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QN |
| TPS7A2030DQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QN |
| TPS7A2030PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2AXF |
| TPS7A2030PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 125 | 2AXF |
| TPS7A2030PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AXF |
| TPS7A2030PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AXF |
| TPS7A2030PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JJ |
| TPS7A2030PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JJ |
| TPS7A2030PDQNRG4 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JJ |
| TPS7A2030PDQNRG4.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JJ |
| TPS7A2030YCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | X |
| TPS7A2030YCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | X |
| TPS7A2031PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2GDF |

| Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPS7A2031PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GDF |
| TPS7A2031PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GDF |
| TPS7A2031PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GDF |
| TPS7A2032PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2GEF |
| TPS7A2032PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GEF |
| TPS7A2033DQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QO |
| TPS7A2033DQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | QO |
| TPS7A2033PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2AZF |
| TPS7A2033PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2AZF |
| TPS7A2033PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | -40 to 125 | JA |
| TPS7A2033PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JA |
| TPS7A2033PDQNRM3 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JA |
| TPS7A2033PDQNRM3.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JA |
| TPS7A2033PYCJR | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | O |
| TPS7A2033PYCJR.A | Active | Production | DSBGA (YCJ) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | O |
| TPS7A2033YCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | V |
| TPS7A2033YCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | V |
| TPS7A2036PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2GIF |
| TPS7A2036PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GIF |
| TPS7A2036PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KP |
| TPS7A2036PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KP |
| TPS7A2040PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KQ |
| TPS7A2040PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KQ |
| TPS7A2040PDQNRG4 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KQ |
| TPS7A2040PDQNRG4.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KQ |
| TPS7A2042PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2GFF |
| TPS7A2042PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GFF |
| TPS7A2042PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GFF |
| TPS7A2042PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GFF |
| TPS7A2042PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KV |
| TPS7A2042PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KV |

| Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPS7A2045PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2GGF |
| TPS7A2045PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GGF |
| TPS7A2045PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JB |
| TPS7A2045PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | JB |
| TPS7A2050PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2B1F |
| TPS7A2050PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 125 | 2B1F |
| TPS7A2050PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2B1F |
| TPS7A2050PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2B1F |
| TPS7A2050PDQNR | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KR |
| TPS7A2050PDQNR.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KR |
| TPS7A2050PDQNRG4 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KR |
| TPS7A2050PDQNRG4.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KR |
| TPS7A2050PDQNRM3 | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KR |
| TPS7A2050PDQNRM3.A | Active | Production | X2SON (DQN) | 4 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | KR |
| TPS7A2050PYCKR | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | H |
| TPS7A2050PYCKR.A | Active | Production | DSBGA (YCK) | 4 | 12000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | -40 to 125 | H |
| TPS7A2055PDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | -40 to 125 | 2GHF |
| TPS7A2055PDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 125 | 2GHF |
| TPS7A2055PDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GHF |
| TPS7A2055PDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2GHF |

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

(4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer: The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

# TAPE AND REEL INFORMATION

![img-117.jpeg](./images/img-117.jpeg)
REEL DIMENSIONS

![img-118.jpeg](./images/img-118.jpeg)
TAPE DIMENSIONS

|  A0 | Dimension designed to accommodate the component width  |
| --- | --- |
|  B0 | Dimension designed to accommodate the component length  |
|  K0 | Dimension designed to accommodate the component thickness  |
|  W | Overall width of the carrier tape  |
|  P1 | Pitch between successive cavity centers  |

![img-119.jpeg](./images/img-119.jpeg)
QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

*All dimensions are nominal

|  Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS7A2008DQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2009PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2009PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A20105PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A20115PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2011PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2011PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2012DQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2012PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2012PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2012PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2012PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2012PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2012PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A20135PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2013DQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |

|  Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS7A2015PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2015PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2016YCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A201825PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 9.5 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A201825PDQNR | X2SON | DQN | 4 | 3000 | 178.0 | 8.4 | 1.13 | 1.13 | 0.53 | 4.0 | 8.0 | Q2  |
|  TPS7A201825PDQNRM3 | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A20185PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A20185PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A20185PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A20185PDQNR | X2SON | DQN | 4 | 3000 | 178.0 | 8.4 | 1.13 | 1.13 | 0.53 | 4.0 | 8.0 | Q2  |
|  TPS7A20185PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 9.5 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A20185PDQNRM3 | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A20185PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2018DQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2018PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2018PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2018PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2018PDQNR | X2SON | DQN | 4 | 3000 | 178.0 | 8.4 | 1.13 | 1.13 | 0.53 | 4.0 | 8.0 | Q2  |
|  TPS7A2018PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 9.5 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2018PDQNRM3 | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2018PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2018PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2018PYCKRM3 | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2018PYCKRM3 | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2018YCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2020PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2020PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A20225PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A202275PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A202275PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2022PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2024PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2024PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2024PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2025DQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2025PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2025PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2025PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2025PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2025PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |

|  Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS7A2025PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2025PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2027PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2027PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2027PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A20285PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A20285PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A20285PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2028DQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2028PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2028PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2028PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2028PDQNRM3 | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2028PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2028PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2028PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2028PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2029PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2030DQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2030PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2030PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2030PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2030PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2030PDQNRG4 | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2030YCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2031PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2031PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2032PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2033DQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2033PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2033PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 9.5 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2033PDQNR | X2SON | DQN | 4 | 3000 | 178.0 | 8.4 | 1.13 | 1.13 | 0.53 | 4.0 | 8.0 | Q2  |
|  TPS7A2033PDQNRM3 | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2033PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2033PYCJR | DSBGA | YCJ | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2033YCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2036PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2036PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2040PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 9.5 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2040PDQNRG4 | X2SON | DQN | 4 | 3000 | 180.0 | 9.5 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2042PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |

|  Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS7A2042PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2042PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2045PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2045PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2045PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2050PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2050PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2050PDQNR | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2050PDQNRG4 | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2050PDQNRM3 | X2SON | DQN | 4 | 3000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2  |
|  TPS7A2050PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2050PYCKR | DSBGA | YCK | 4 | 12000 | 180.0 | 8.4 | 0.71 | 0.71 | 0.42 | 2.0 | 8.0 | Q1  |
|  TPS7A2055PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2055PDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 9.0 | 3.3 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |
|  TPS7A2055PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3  |

![img-120.jpeg](./images/img-120.jpeg)
TAPE AND REEL BOX DIMENSIONS

*All dimensions are nominal

|  Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS7A2008DQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2009PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |
|  TPS7A2009PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20105PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20115PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2011PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2011PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2012DQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2012PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |
|  TPS7A2012PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2012PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2012PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2012PYCJR | DSBGA | YCJ | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2012PYCJR | DSBGA | YCJ | 4 | 12000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20135PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2013DQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2015PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |
|  TPS7A2015PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |

|  Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS7A2016YCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A201825PDQNR | X2SON | DQN | 4 | 3000 | 184.0 | 184.0 | 19.0  |
|  TPS7A201825PDQNR | X2SON | DQN | 4 | 3000 | 205.0 | 200.0 | 33.0  |
|  TPS7A201825PDQNRM3 | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20185PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20185PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20185PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20185PDQNR | X2SON | DQN | 4 | 3000 | 205.0 | 200.0 | 33.0  |
|  TPS7A20185PDQNR | X2SON | DQN | 4 | 3000 | 184.0 | 184.0 | 19.0  |
|  TPS7A20185PDQNRM3 | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20185PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2018DQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2018PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |
|  TPS7A2018PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2018PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2018PDQNR | X2SON | DQN | 4 | 3000 | 205.0 | 200.0 | 33.0  |
|  TPS7A2018PDQNR | X2SON | DQN | 4 | 3000 | 184.0 | 184.0 | 19.0  |
|  TPS7A2018PDQNRM3 | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2018PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2018PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2018PYCKRM3 | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2018PYCKRM3 | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2018YCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2020PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2020PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A20225PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A202275PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A202275PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2022PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2022PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2024PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2024PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2024PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2025DQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2025PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2025PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2025PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2025PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2025PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2025PYCJR | DSBGA | YCJ | 4 | 12000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2025PYCJR | DSBGA | YCJ | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2027PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2027PYCJR | DSBGA | YCJ | 4 | 12000 | 182.0 | 182.0 | 20.0  |

|  Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS7A2027PYCJR | DSBGA | YCJ | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A20285PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |
|  TPS7A20285PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A20285PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2028DQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2028PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2028PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2028PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2028PDQNRM3 | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2028PYCJR | DSBGA | YCJ | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2028PYCJR | DSBGA | YCJ | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2028PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2028PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2029PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2030DQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2030PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |
|  TPS7A2030PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2030PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2030PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2030PDQNRG4 | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2030YCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2031PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2031PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2032PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2033DQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2033PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |
|  TPS7A2033PDQNR | X2SON | DQN | 4 | 3000 | 184.0 | 184.0 | 19.0  |
|  TPS7A2033PDQNR | X2SON | DQN | 4 | 3000 | 205.0 | 200.0 | 33.0  |
|  TPS7A2033PDQNRM3 | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2033PYCJR | DSBGA | YCJ | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2033PYCJR | DSBGA | YCJ | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2033YCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2036PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |
|  TPS7A2036PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2040PDQNR | X2SON | DQN | 4 | 3000 | 184.0 | 184.0 | 19.0  |
|  TPS7A2040PDQNRG4 | X2SON | DQN | 4 | 3000 | 184.0 | 184.0 | 19.0  |
|  TPS7A2042PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2042PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2042PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2045PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2045PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2045PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2050PDBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0  |

|  Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  TPS7A2050PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2050PDQNR | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2050PDQNRG4 | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2050PDQNRM3 | X2SON | DQN | 4 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2050PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2050PYCKR | DSBGA | YCK | 4 | 12000 | 182.0 | 182.0 | 20.0  |
|  TPS7A2055PDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |
|  TPS7A2055PDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 180.0 | 18.0  |
|  TPS7A2055PDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0  |

![img-121.jpeg](./images/img-121.jpeg)

![img-122.jpeg](./images/img-122.jpeg)

![img-123.jpeg](./images/img-123.jpeg)

4214839/K 08/2024

# NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Reference JEDEC MO-178.
4. Body dimensions do not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.25 mm per side.
5. Support pin may differ or may not be present.

![img-124.jpeg](./images/img-124.jpeg)
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:15X

![img-125.jpeg](./images/img-125.jpeg)
NON SOLDER MASK
DEFINED
(PREFERRED)

![img-126.jpeg](./images/img-126.jpeg)
SOLDER MASK
DEFINED
SOLDER MASK DETAILS

4214839/K 08/2024

NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

SMALL OUTLINE TRANSISTOR

![img-127.jpeg](./images/img-127.jpeg)
SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
SCALE:15X

4214839/K 08/2024

NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
9. Board assembly site may have different recommendations for stencil design.

![img-128.jpeg](./images/img-128.jpeg)

Images above are just a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

4210367/F

![img-129.jpeg](./images/img-129.jpeg)

![img-130.jpeg](./images/img-130.jpeg)

![img-131.jpeg](./images/img-131.jpeg)

4215302/E 12/2016

# NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for optimal thermal and mechanical performance.
4. Features may not exist. Recommend use of pin 1 marking on top of package for orientation purposes.
5. Shape of exposed side leads may differ.
6. Number and location of exposed tie bars may vary.

![img-132.jpeg](./images/img-132.jpeg)
LAND PATTERN EXAMPLE
SCALE: 40X

![img-133.jpeg](./images/img-133.jpeg)
SOLDER MASK
DEFINED

SOLDER MASK DETAIL

4215302/E 12/2016

NOTES: (continued)

7. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).
8. If any vias are implemented, it is recommended that vias under paste be filled, plugged or tented.

![img-134.jpeg](./images/img-134.jpeg)

SOLDER PASTE EXAMPLE
BASED ON 0.075 - 0.1mm THICK STENCIL

EXPOSED PAD
88% PRINTED SOLDER COVERAGE BY AREA
SCALE: 60X

4215302/E 12/2016

NOTES: (continued)

9. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

# 重要通知和免责声明

TI“按原样”提供技术和可靠性数据（包括数据表）、设计资源（包括参考设计）、应用或其他设计建议、网络工具、安全信息和其他资源，不保证没有瑕疵且不做出任何明示或暗示的担保，包括但不限于对适销性、与某特定用途的适用性或不侵犯任何第三方知识产权的暗示担保。

这些资源可供使用TI产品进行设计的熟练开发人员使用。您将自行承担以下全部责任：(1) 针对您的应用选择合适的TI产品，(2) 设计、验证并测试您的应用，(3) 确保您的应用满足相应标准以及任何其他安全、安保法规或其他要求。

这些资源如有变更，恕不另行通知。TI授权您仅可将这些资源用于研发本资源所述的TI产品的相关应用。严禁以其他方式对这些资源进行复制或展示。您无权使用任何其他TI知识产权或任何第三方知识产权。对于因您对这些资源的使用而对TI及其代表造成的任何索赔、损害、成本、损失和债务，您将全额赔偿，TI对此概不负责。

TI提供的产品受TI销售条款)、TI通用质量指南或ti.com上其他适用条款或TI产品随附的其他适用条款的约束。TI提供这些资源并不会扩展或以其他方式更改TI针对TI产品发布的适用的担保或担保免责声明。除非德州仪器(TI)明确将某产品指定为定制产品或客户特定产品，否则其产品均为按确定价格收入目录的标准通用器件。

TI反对并拒绝您可能提出的任何其他或不同的条款。

版权所有 © 2026，德州仪器 (TI) 公司

最后更新日期：2025年10月