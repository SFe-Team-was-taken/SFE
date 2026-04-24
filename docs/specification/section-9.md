# Section 9: SiliconSFE and the AWE ROM emulator

## 9.1 SiliconSFE overview

While we are unaware of any shipping products using the SiliconSF system found in `SFSPEC24.PDF` (the AWE cards used an early predecessor of SiliconSF), you can use ROM samples formatted in the SiliconSF format with SFE. However, SiliconSFE support is explicitly optional. (since 4.0.5)

## 9.2 Header format

### 9.2.1 About the header format

The SiliconSFE header format is almost identical to legacy SF2.04, however an explanation is provided here due to poor documentation of SiliconSF.

Here is the SiliconSFE header format:

```c
typedef struct romHdrType{
    uint32_t romRiffHdr;
    uint32_t romByteSize;
    int8_t romInterleaveIndex;
    int8_t romRevision[3];
    int8_t romVer[4];
    int16_t bankChecksum;
    int16_t bankChecksum2sComplement;
    int8_t bankSFEVersion;
    int8_t bankProduct[16];
    uint8_t bankSampleCompType;
    int8_t filler1[2];
    int8_t bankStyle[16];
    int8_t bankCopyright[80];
    uint32_t romSFEBankStart;
    uint32_t romSineWaveStart;
    uint32_t filler2[124];
    int16_t sampleSineWave[SINEWAVESIZE];
} romHdr;
```

### 9.2.2 romRiffHeader

In SiliconSFE, it is defined as the FourCC used by the chunk header type used by the integrated SF bank, for example `RIFF`, `RIFS`, `RIFD`, `RF64` etc. (since 4.0.17)

In the legacy SF2.04 specification, this is named `romRsrc` and was declared by Creative as "unused". The name in SiliconSFE more accurately describes its usage. The reasoning is that `RIFF` stands for `Resource Interchange File Format`.

### 9.2.3 romByteSize

This is a `uint32_t` value with the size of the SiliconSFE ROM blob in bytes. It is limited to 4 GiB in SiliconSFE 1.0. (With the exception of TSC/Trailing Sample Chunk and offset adjustments assuming this value is not ignored in favor of the size of the unheadered SFE.) Signed integers and floats are prohibited.

### 9.2.4 romInterleaveIndex

This is used for interleaved ROMs. You can interleave up to 256 ROMs with one SiliconSFE blob.

In the legacy SF2.04 specification, this is named `interleaveIndex`.

### 9.2.5 romRevision

This is a revision identifier as an integer. It is 3 bytes long and is independent of the version number found in `romVer`.

In the legacy SF2.04 specification, this is named `revision`.

### 9.2.6 romVer

This corresponds to the `iver` value in the integrated SF bank.

In the legacy SF2.04 specification, this is named `id` and is erroneously listed as corresponding to the `irom` value. The name in SiliconSFE more accurately describes its usage.

### 9.2.7 bankChecksum

This stores the SNES-type (16-bit simple checksum of ALL bytes, in little endian, operating at the 16-bit level) of the whole SiliconSFE file.

In the legacy SF2.04 specification, this is named `checksum`.

### 9.2.8 bankChecksum2sComplement

This stores the twos-complement of the value found in `bankChecksum`.

In the legacy SF2.04 specification, this is named `checksum2sComplement`.

### 9.2.9 bankSFEVersion

This value should be the same as the `wSFESpecMajorVersion` value in the `SFvx` sub-chunk in SFE, and the same as the `wMajor` value in the `ifil` sub-chunk in non-SFE. For an unknown or other format, this value is `0`.

In the legacy SF2.04 specification, this is named `bankFormat` and was declared by Creative as "unused".

### 9.2.10 bankProduct

This is a UTF-8 string that stores the product name (conventionally `SiliconSFE`).

In the legacy SF2.04 specification, this is named `product`.

### 9.2.11 sampleCompType

For the purpose of SiliconSFE, this value is `1` if any kind of sample precompensation is used, and `0` otherwise.

In the legacy SF2.04 specification, Creative said that it indicates the type of sample precompensation that is used in the SiliconSF blob, but they do not give a table or list of values.

### 9.2.12 bankStyle

This is a UTF-8 string that describes the musical style of the contents of the integrated SF bank.

In the legacy SF2.04 specification, this is named `style`.

### 9.2.13 bankCopyright

This is a UTF-8 string that stores copyright information about the SiliconSFE blob.

In the legacy SF2.04 specification, this is named `copyright`.

### 9.2.14 romSFEBankStart

This stores the location in the SiliconSFE blob where the integrated SF bank starts.

In the legacy SF2.04 specification, this is named `sampleStart`. The name in SiliconSFE more accurately describes its usage. The standard is murky, but THIS approach allows SFE banks larger than 16-bit and/or 4GiB to work in the event they are needed and headered right.

### 9.2.15 romSineWaveStart

This stores the location in the SiliconSFE blob where the test sine wave sample starts.

In the legacy SF2.04 specification, this is named `sineWaveStart`.

### 9.2.16 sampleSineWave

This contains `int16_t` values that correspond to a sine wave sample.

In the legacy SF2.04 specification, this is named `sineWave`.

## 9.3 AWE ROM emulator

### 9.3.1 Introducing the AWE ROM emulator

Except for when size concerns prohibit its inclusion, SFE players should include an AWE ROM emulator.

- The AWE ROM emulator includes 152 samples.
- The file size should be 1MB, as all samples should be to the same standard as the original.
- Samples which the program developer has the right to use can be used as a replacement for the original ROM samples.
- Freely-usable reference implementation samples are available, but are not intended for production use.
- Sample names will remain the same, but there will be acceptable alias names.
- Emulators should also be able to open up SF files (either legacy SF or SFE) containing samples and metadata.
- There may or may not be instruments or presets.

### 9.3.2 ROM emulator sample specification

| Number | Original Sample Name | Acceptable Aliases                                                                                                                              | Sample length | Loop points | Description                                                                              |
|--------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-------------|------------------------------------------------------------------------------------------|
| 1      | acbasse1             | Acoustic Bass E1                                                                                                                                | 1535          | 1408-1530   |                                                                                          |
| 2      | accordax2            | Accordion A#2       <br> Accordian A#2                                                                                                          | 620           | 566-616     | Either spelling is acceptable                                                            |
| 3      | accordfx2            | Accordion F#2       <br> Accordian F#2                                                                                                          | 1049          | 979-1044    | Either spelling is acceptable                                                            |
| 4      | accordfx3            | Accordion F#3       <br> Accordian F#3                                                                                                          | 858           | 794-854     | Either spelling is acceptable                                                            |
| 5      | acgtrb3              | Acoustic Guitar B3                                                                                                                              | 6241          | 6168-6236   |                                                                                          |
| 6      | acgtrg2              | Acoustic Guitar G2                                                                                                                              | 4882          | 4800-4877   |                                                                                          |
| 7      | agogolotone          | Agogo Low Tone      <br> Agogo Bell                                                                                                             | 4467          | 7-4463      |                                                                                          |
| 8      | applause             | Applause                                                                                                                                        | 8161          | 7-8156      |                                                                                          |
| 9      | arcocelloax2         | Arco Cello A#2                                                                                                                                  | 847           | 799-842     |                                                                                          |
| 10     | arcocellod2          | Arco Cello D2                                                                                                                                   | 1200          | 1127-1195   |                                                                                          |
| 11     | arcoviolinc3         | Arco Violin C3                                                                                                                                  | 1767          | 1702-1762   |                                                                                          |
| 12     | arcoviolinc4         | Arco Violin C4                                                                                                                                  | 1634          | 1569-1629   |                                                                                          |
| 13     | arcovioline3         | Arco Violin E3                                                                                                                                  | 1086          | 1035-1081   |                                                                                          |
| 14     | arcoviolingx2        | Arco Violin G#2                                                                                                                                 | 1732          | 1691-1727   |                                                                                          |
| 15     | arcoviolingx3        | Arco Violin G#3                                                                                                                                 | 1075          | 1032-1070   |                                                                                          |
| 16     | asaxc2               | Alto Sax C2                                                                                                                                     | 1150          | 1054-1145   |                                                                                          |
| 17     | asaxc4               | Alto Sax C4                                                                                                                                     | 1191          | 1130-1186   |                                                                                          |
| 18     | asaxd3               | Alto Sax D3                                                                                                                                     | 696           | 643-691     |                                                                                          |
| 19     | asaxe2               | Alto Sax E2                                                                                                                                     | 1228          | 1150-1223   |                                                                                          |
| 20     | asaxf3               | Alto Sax F3                                                                                                                                     | 910           | 863-905     |                                                                                          |
| 21     | asaxg2               | Alto Sax G2                                                                                                                                     | 1639          | 1567-1634   |                                                                                          |
| 22     | bagpipedrna          | Bag Drone A1        <br> Bag Drone                                                                                                              | 1921          | 1764-1913   | Based on name in 8MB E-mu bank                                                           |
| 23     | banjod3              | Banjo D3                                                                                                                                        | 3583          | 3540-3579   |                                                                                          |
| 24     | banjog2              | Banjo G2                                                                                                                                        | 2850          | 2784-2845   |                                                                                          |
| 25     | bassguitloop         | Bass Guitar Loop                                                                                                                                | 125           | 9-120       |                                                                                          |
| 26     | bassoonc2            | Bassoon C2          <br> Bassoon                                                                                                                | 1059          | 938-1053    | Only sample of that instrument                                                           |
| 27     | bd15                 | Bass Drum           <br> Kick Drum                                                                                                              | 1603          | 7-1599      |                                                                                          |
| 28     | belltree             | Bell Tree                                                                                                                                       | 7466          | 6263-7461   |                                                                                          |
| 29     | bockclave            | Claves                                                                                                                                          | 1774          | 7-1770      |                                                                                          |
| 30     | brasssectc3          | Brass Section C3                                                                                                                                | 5600          | 5533-5595   |                                                                                          |
| 31     | brasssectf5          | Brass Section F5                                                                                                                                | 5581          | 4989-5035   |                                                                                          |
| 32     | bsawtoothwavea3      | Sawtooth Wave Sample<br> Bass SawtoothWave A3<br> Bass Sawtooth Wave                                                                            | 70            | 15-65       | Real time synthesis activated without "Sample" suffix                                    |
| 33     | cabasastrk           | Cabasa                                                                                                                                          | 2679          | 7-2675      | Based on name in 8MB E-mu bank                                                           |
| 34     | chanterax1           | Bagpipe A#1         <br> Bagpipe             <br> Chanter A#1         <br> Chanter                                                              | 1858          | 1802-1850   | Based on name in 8MB E-mu bank  <br>Only sample of that instrument                       |
| 35     | chcrash              | China Crash Cymbal                                                                                                                              | 9700          | 6162-9695   | Based on name in 8MB E-mu bank                                                           |
| 36     | clarinetb2           | Clarinet B2                                                                                                                                     | 701           | 586-695     |                                                                                          |
| 37     | clarinetd2           | Clarinet D2                                                                                                                                     | 677           | 596-671     |                                                                                          |
| 38     | clavc2               | Clav C2             <br> Clav                                                                                                                   | 2985          | 2836-2980   | Only sample of that instrument                                                           |
| 39     | coldglass7wave       | Tinkle Bell Wave 1  <br> Tinker Bell Wave 1                                                                                                     | 70            | 17-65       | The alias is because of its use in the 1MB E-mu bank.  <br>Either spelling is acceptable |
| 40     | coldglass12wave      | Tinkle Bell Wave 2  <br> Tinker Bell Wave 2                                                                                                     | 91            | 15-86       | The alias is because of its use in the 1MB E-mu bank.  <br>Either spelling is acceptable |
| 41     | contraviobass        | Contrabass                                                                                                                                      | 1443          | 1302-1438   |                                                                                          |
| 42     | cowbell              | Cowbell                                                                                                                                         | 1760          | 7-1756      |                                                                                          |
| 43     | crash5               | Crash Cymbal                                                                                                                                    | 13534         | 8024-13529  |                                                                                          |
| 44     | distgtra2            | Distortion Guitar A2<br> Dist Gtr A2                                                                                                            | 1832          | 1745-1827   | Based on name in 8MB E-mu bank                                                           |
| 45     | distgtra3            | Distortion Guitar A3<br> Dist Gtr A3                                                                                                            | 1243          | 1195-1238   | Based on name in 8MB E-mu bank                                                           |
| 46     | distgtrd4            | Distortion Guitar A4<br> Dist Gtr A4                                                                                                            | 1766          | 1593-1761   | Based on name in 8MB E-mu bank                                                           |
| 47     | distgtre3            | Distortion Guitar E3<br> Dist Gtr E3                                                                                                            | 1432          | 1372-1427   | Based on name in 8MB E-mu bank                                                           |
| 48     | dlcmrc3              | Dulcimer C3         <br> Dulcimer                                                                                                               | 3835          | 3778-3830   | Only sample of that instrument                                                           |
| 49     | ebongostone          | H Bongo Rim                                                                                                                                     | 3204          | 7-3200      | Based on name in 8MB E-mu bank                                                           |
| 50     | elguitard2           | Electric Guitar D2  <br> Electric Guitar                                                                                                        | 1481          | 1401-1476   | Only sample of that instrument                                                           |
| 51     | enghorndx3           | English Horn D#3    <br> English Horn                                                                                                           | 1540          | 1479-1534   | Only sample of that instrument                                                           |
| 52     | epiano2ms            | E Piano 2                                                                                                                                       | 1173          | 1120-1168   | Only sample of that instrument                                                           |
| 53     | femalevoiceg2        | Female Voice G2     <br> Female Voice                                                                                                           | 8759          | 338-8755    | Only sample of that instrument                                                           |
| 54     | filtersnap           | Filter Snap                                                                                                                                     | 420           | 7-414       |                                                                                          |
| 55     | floortombrite        | Floor Tom           <br> Acoustic Tom                                                                                                           | 7172          | 5236-7167   | Based on name in 8MB E-mu bank                                                           |
| 56     | flutec4              | Flute C4                                                                                                                                        | 1432          | 1365-1427   | Only sample of that instrument                                                           |
| 57     | frenchhorng4         | French Horn G4      <br> French Horn                                                                                                            | 1485          | 1420-1480   | Only sample of that instrument                                                           |
| 58     | fretlessa2           | Fretless Bass A2    <br> Fretless Bass                                                                                                          | 2341          | 2165-2336   | Only sample of that instrument                                                           |
| 59     | glockloopc4          | Glockenspiel C4     <br> Glockenspiel        <br> Glockenspiel Loop                                                                             | 216           | 7-211       | Only sample of that instrument                                                           |
| 60     | gsbassd2             | Finger Bass D2      <br> Finger Bass                                                                                                            | 905           | 750-900     | Only sample of that instrument                                                           |
| 61     | guiro2               | Guiro Up                                                                                                                                        | 2764          | 7-2759      | Based on name in 8MB E-mu bank                                                           |
| 62     | guirodown            | Guiro Down                                                                                                                                      | 2648          | 7-2644      |                                                                                          |
| 63     | guitar1              | Bandoneon                                                                                                                                       | 140           | 69-135      | The alias is because of its use in the 1MB E-mu bank.                                    |
| 64     | guitarfret           | Guitar Fret         <br> Fret Noise                                                                                                             | 3572          | 7-3567      | Based on name in 8MB E-mu bank                                                           |
| 65     | gunshot              | Gun Shot                                                                                                                                        | 5396          | 7-5392      | Based on name in 8MB E-mu bank                                                           |
| 66     | harmguitard3         | Guitar Harmonics D3 <br> Guitar Harmonics    <br> GtrHarmonics D3                                                                               | 344           | 298-338     | Based on name in 8MB E-mu bank  <br>Only sample of that instrument                       |
| 67     | harmonicaa3          | Harmonica A3        <br> Harmonica                                                                                                              | 974           | 915-969     | Only sample of that instrument                                                           |
| 68     | harpsichordc3        | Harpsichord C3      <br> Harpsichord                                                                                                            | 1391          | 1294-1386   | Only sample of that instrument                                                           |
| 69     | hatopenms            | Open High Hat                                                                                                                                   | 11710         | 5828-11705  | Based on name in 8MB E-mu bank                                                           |
| 70     | hrmnmutec3           | Harmon Mute C3                                                                                                                                  | 1485          | 1420-1481   |                                                                                          |
| 71     | hrmnmutec4           | Harmon Mute C4                                                                                                                                  | 903           | 840-898     |                                                                                          |
| 72     | htrumpetax3          | Trumpet A#3                                                                                                                                     | 1663          | 1602-1658   |                                                                                          |
| 73     | htrumpetc3           | Trumpet C3                                                                                                                                      | 1653          | 1598-1648   |                                                                                          |
| 74     | htrumpetd2           | Trumpet D2                                                                                                                                      | 1674          | 1628-1669   |                                                                                          |
| 75     | htrumpetf3           | Trumpet F3                                                                                                                                      | 1497          | 1454-1492   |                                                                                          |
| 76     | htrumpetg2           | Trumpet G2                                                                                                                                      | 1636          | 1598-1631   |                                                                                          |
| 77     | jazzguitloop         | Jazz Guitar         <br> Jazz Guitar Loop                                                                                                       | 119           | 9-114       |                                                                                          |
| 78     | kotod3               | Koto D3             <br> Koto                                                                                                                   | 5709          | 5666-5704   | Only sample of that instrument                                                           |
| 79     | kpianob1             | Piano B1                                                                                                                                        | 17232         | 10655-17227 |                                                                                          |
| 80     | kpianob4             | Piano B4                                                                                                                                        | 25217         | 15428-25212 |                                                                                          |
| 81     | kpianob5             | Piano B5                                                                                                                                        | 5399          | 2963-5394   |                                                                                          |
| 82     | kpianocx4            | Piano C#4                                                                                                                                       | 21574         | 21506-21569 |                                                                                          |
| 83     | kpianodx5            | Piano D#5                                                                                                                                       | 6146          | 6093-6141   |                                                                                          |
| 84     | kpianof5             | Piano F5                                                                                                                                        | 6980          | 6848-6974   |                                                                                          |
| 85     | kpianof5 #02         | Piano F5#02                                                                                                                                     | 6980          | 4148-4202   |                                                                                          |
| 86     | kpianog2             | Piano G2                                                                                                                                        | 22131         | 17637-22127 |                                                                                          |
| 87     | lefone               | Telephone                                                                                                                                       | 1585          | 8-1577      | Based on name in 8MB E-mu bank                                                           |
| 88     | lowtumba             | Low Tumba Tone                                                                                                                                  | 4022          | 7-4018      | Based on name in 8MB E-mu bank                                                           |
| 89     | maracas              | Maracas                                                                                                                                         | 3254          | 7-3250      |                                                                                          |
| 90     | marimbac3            | Marimba C3          <br> Marimba                                                                                                                | 817           | 788-812     | Only sample of that instrument                                                           |
| 91     | mbongotone           | M Bongo Tone                                                                                                                                    | 2724          | 7-2720      | Based on name in 8MB E-mu bank                                                           |
| 92     | mgtr                 | Muted Guitar        <br> Gtr Mute                                                                                                               | 836           | 766-831     | Based on name in 8MB E-mu bank                                                           |
| 93     | nguitb2              | Nylon Guitar B2     <br> N Guitar B2                                                                                                            | 5193          | 5125-5188   | Based on name in 8MB E-mu bank                                                           |
| 94     | nguitf2              | Nylon Guitar F2     <br> N Guitar F2                                                                                                            | 3829          | 3727-3824   | Based on name in 8MB E-mu bank                                                           |
| 95     | oboeax3              | Oboe A#3                                                                                                                                        | 998           | 958-992     |                                                                                          |
| 96     | oboecx3              | Oboe C#3                                                                                                                                        | 892           | 832-886     |                                                                                          |
| 97     | oboefx3              | Oboe F#3                                                                                                                                        | 1226          | 1177-1220   |                                                                                          |
| 98     | oboeresynwaved4      | Oboe Resynth D4     <br> Oboe Resynth                                                                                                           | 140           | 69-135      |                                                                                          |
| 99     | ocarinafx2           | Ocarina F#2         <br> Ocarina                                                                                                                | 1187          | 1144-1182   | Only sample of that instrument                                                           |
| 100    | octavewave           | Octave Wave                                                                                                                                     | 140           | 69-135      |                                                                                          |
| 101    | oohvoicec3           | Ooh Voice C3        <br> Ooh Voice                                                                                                              | 9102          | 35-9097     | Only sample of that instrument                                                           |
| 102    | orchhit2             | Orchestra Hit       <br> Orch Hit                                                                                                               | 4566          | 7-4562      | Based on name in 8MB E-mu bank                                                           |
| 103    | organ19d4wave        | Space Voice                                                                                                                                     | 140           | 69-135      | The alias is because of its use in the 1MB E-mu bank.                                    |
| 104    | organwave            | Organ Wave          <br> Organ Wave 1                                                                                                           | 2675          | 2614-2669   |                                                                                          |
| 105    | organwavea3          | Organ Wave A3       <br> Organ Wave 2                                                                                                           | 2940          | 2900-2934   |                                                                                          |
| 106    | paisteping           | Ride Cymbal         <br> Ride Ping                                                                                                              | 13293         | 7459-13288  | Based on name in 8MB E-mu bank                                                           |
| 107    | pizzviolinc3         | Pizzicato Strings C3<br> Pizzicato Strings   <br> Pizzicato Violin C3 <br> Pizzicato Violin    <br> Pizz Violin C3      <br> Pizz Violin        | 1560          | 1499-1555   | Based on name in 8MB E-mu bank  <br>Only sample of that instrument                       |
| 108    | pluckharp            | Pluck Harp          <br> Harp                                                                                                                   | 3478          | 3409-3473   |                                                                                          |
| 109    | quicadown            | Quica Downstroke                                                                                                                                | 1627          | 7-1623      | Based on name in 8MB E-mu bank                                                           |
| 110    | quintoslap           | Quinto Slap         <br> QuintoClosedSlap                                                                                                       | 2923          | 7-2919      | Based on name in 8MB E-mu bank                                                           |
| 111    | quintotone           | Quinto Tone                                                                                                                                     | 3091          | 7-3087      | Based on name in 8MB E-mu bank                                                           |
| 112    | recorderax2          | Recorder A#2        <br> Recorder                                                                                                               | 1360          | 1298-1352   | Only sample of that instrument                                                           |
| 113    | resynth4d4wave       | Bowed Glass D4      <br> Bowed Glass                                                                                                            | 140           | 69-135      | Only sample of that instrument                                                           |
| 114    | rhodeschime          | E Piano 1 Chime                                                                                                                                 | 284           | 7-279       |                                                                                          |
| 115    | rideping             | Ride Bell                                                                                                                                       | 6034          | 3614-6029   | Based on name in 8MB E-mu bank                                                           |
| 116    | sambawhistle         | Samba Whistle                                                                                                                                   | 1687          | 1121-1673   |                                                                                          |
| 117    | sawstackwavems       | Saw Stack Wave      <br> Saw Stack                                                                                                              | 13749         | 289-13745   |                                                                                          |
| 118    | sb2                  | Slap Bass 2                                                                                                                                     | 2464          | 2345-2459   |                                                                                          |
| 119    | scratch              | Scratch                                                                                                                                         | 1661          | 7-1657      |                                                                                          |
| 120    | shakua2              | Shakuhachi A2       <br> Shakuhachi                                                                                                             | 7468          | 2085-7463   | Only sample of that instrument                                                           |
| 121    | sikue2               | Siku E2             <br> Siku                <br> Bottle Blow E2      <br> Bottle Blow                                                          | 5314          | 7-5310      | Only sample of that instrument                                                           |
| 122    | sinetick             | Sinetick                                                                                                                                        | 73            | 7-68        |                                                                                          |
| 123    | sinewave             | Sine Wave Sample                                                                                                                                | 140           | 69-135      | Real time synthesis activated without "Sample" suffix                                    |
| 124    | sitardx4             | Sitar D#4           <br> Sitar                                                                                                                  | 2316          | 2275-2311   | Only sample of that instrument                                                           |
| 125    | slapbass1c3          | Slap Bass 1 C3      <br> Slap Bass 1                                                                                                            | 2121          | 1817-2115   | Only sample of that instrument                                                           |
| 126    | snare24              | Snare                                                                                                                                           | 3877          | 7-3873      |                                                                                          |
| 127    | squarewave           | Square Wave Sample                                                                                                                              | 2427          | 2365-2420   | Real time synthesis activated without "Sample" suffix                                    |
| 128    | ssaxdx4              | Soprano Sax D4      <br> Soprano Sax                                                                                                            | 1189          | 1136-1184   | Only sample of that instrument                                                           |
| 129    | steeldrum            | Steel Drum          <br> SteelDrum                                                                                                              | 2898          | 2857-2891   | Based on name in 8MB E-mu bank                                                           |
| 130    | stix                 | Drum Stick          <br> Side Stick                                                                                                             | 370           | 7-366       | Based on name in 8MB E-mu bank                                                           |
| 131    | stringsdx4           | Strings D#4                                                                                                                                     | 10727         | 3098-10722  |                                                                                          |
| 132    | stringsf3            | Strings F3                                                                                                                                      | 8647          | 3415-8642   |                                                                                          |
| 133    | stringsg2            | Strings G2                                                                                                                                      | 9309          | 2609-9304   |                                                                                          |
| 134    | synthbassloop        | Synth Bass Loop     <br> Synth Bass                                                                                                             | 441           | 8-435       |                                                                                          |
| 135    | synthstringsc4       | Synth Strings C4    <br> Synth Strings                                                                                                          | 9967          | 1272-9962   | Only sample of that instrument                                                           |
| 136    | tamborine            | Tambourine          <br> Brass Tambourine                                                                                                       | 3604          | 2157-3585   | Based on name in 8MB E-mu bank                                                           |
| 137    | tbelld4wave          | Tubular Bell D4     <br> Tubular Bell        <br> Tubular Bell Wave D4<br> Tubular Bell Wave                                                    | 5417          | 4829-5412   | Only sample of that instrument                                                           |
| 138    | timpani              | Timpani             <br> Timp Drum                                                                                                              | 7699          | 7079-7695   | Based on name in 8MB E-mu bank                                                           |
| 139    | triangle             | Triangle            <br> Triangle Wave                                                                                                          | 2069          | 336-2064    | Based on name in 8MB E-mu bank                                                           |
| 140    | troma3               | Trombone A3                                                                                                                                     | 1334          | 1275-1329   |                                                                                          |
| 141    | tromb2               | Trombone B2                                                                                                                                     | 1331          | 1232-1326   |                                                                                          |
| 142    | tromd4               | Trombone D4                                                                                                                                     | 1121          | 1074-1116   |                                                                                          |
| 143    | tromg4               | Trombone G4                                                                                                                                     | 1569          | 1504-1564   |                                                                                          |
| 144    | tubaax1              | Tuba A#1            <br> Tuba                                                                                                                   | 1964          | 1831-1960   | Only sample of that instrument                                                           |
| 145    | verbclickwave        | Reverb Click Wave                                                                                                                               | 1208          | 7-1204      |                                                                                          |
| 146    | vibese2              | Vibes E2            <br> Vibes                                                                                                                  | 782           | 696-777     | Only sample of that instrument                                                           |
| 147    | vibraloop            | Vibra Loop                                                                                                                                      | 788           | 9-783       |                                                                                          |
| 148    | voxdodo              | Doo                 <br> Voice Oohs                                                                                                             | 3059          | 2999-3054   | Based on name in 8MB E-mu bank                                                           |
| 149    | whitenoisewave       | White Noise Sample                                                                                                                              | 8294          | 7-8289      | Real time synthesis activated without "Sample" suffix                                    |
| 150    | woodblock            | Wood Block                                                                                                                                      | 1164          | 7-1160      |                                                                                          |
| 151    | xyloe4looped         | Xylophone E4        <br> Xylophone           <br> Xylo Unlooped E4    <br> Xylo Unlooped       <br> XylophoneUnlooped E4<br> Xylophone Unlooped | 980           | 7-976       | Only sample of that instrument                                                           |
| 152    | xyloe4unlooped       | Xylo Looped E4      <br> Xylo Looped         <br> Xylophone Looped E4 <br> Xylophone Looped                                                     | 980           | 7-976       | Only sample of that instrument                                                           |

Sample specification is fixed at 44.1khz Mono with no links and tuning at 60 with no fine-tuning. You can either use discrete samples, or create your own SiliconSFE ROM containing the emulator samples.
