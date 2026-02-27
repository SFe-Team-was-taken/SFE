# Section 11: Program specification

## 11.1 Program compatibility levels

These are guidelines to help SFE program developers write their programs. Not all of them need to be followed, but doing so will ensure that your program works with all SFE 4.0 banks.

All SFE programs must meet level 1 requirements. If they do not, guarantees that an SFE file will work on the program can not be made.

Level 1 is the level that embedded applications should be expected to include. Level 2 is the minimum 32-bit level for computers. Level 3 is the recommended 64-bit level for a good experience. Level 4 is maxed out. Requirements for levels 1-4 will increase with new versions.

If an implementation is unable to reach the layering requirements without crashing, it does not entirely meet the level.

### 11.1.1 File format specifications

|                                                    | **Level 1**                                                                                             | **Level 2**                                                                                          | **Level 3**                                                                                          | **Level 4**                                                                                          |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **File size representation**                       | Unsigned 32-bit integer  <br>You must not use signed integers                                           | Unsigned 32-bit integer  <br>You must not use signed integers                                        | Unsigned 64-bit integer  <br>You must not use signed integers                                        | Unsigned 64-bit integer  <br>You must not use signed integers                                        |
| **File size limit** (since 4.0.29)                 | System memory                                                                                           | 32-bit: 4 GiB <br> 64-bit: 8 GiB                                                                     | 32-bit: 4 GiB <br> 64-bit: 32 GiB*                                                                   | 32-bit: 4 GiB <br> 64-bit: No limit*                                                                 |
| **Sample streaming**                               | System memory                                                                                           | System memory and disk streaming                                                                     | System memory and disk streaming                                                                     | System memory and disk streaming                                                                     |
| **Total file size limit** (since 4.0.29)           | System memory                                                                                           | At least 32 GiB                                                                                      | No limit*                                                                                            | No limit*                                                                                            |
| **Multiple files**                                 | Optional                                                                                                | 8 or more                                                                                            | 256 or more                                                                                          | No limit                                                                                             |
| **Legacy support**                                 | Full quality: SF2.01 and Werner SF3 <br>Playback: SF2.04                                                | Full quality: SF2.01 and Werner SF3 <br>Playback: SF2.04                                             | Full quality: SF2.01, SF2.04 and Werner SF3                                                          | Full quality: SF2.01, SF2.04 and Werner SF3                                                          |
| **Header support** (since 4.0.5)                   | 32-bit static                                                                                           | 32-bit static                                                                                        | 32-bit static, 64-bit static                                                                         | 32-bit static, 64-bit static                                                                         |
| **Sample containers** (since 4.0.9)                | SFE Compression/UCC  <br>Uncompressed, OGG  <br>Incompatible formats forbidden for write                | SFE Compression/UCC  <br>Uncompressed, OGG  <br>Incompatible formats forbidden for write             | SFE Compression/UCC  <br>Uncompressed, OGG  <br>Incompatible formats forbidden for write             | SFE Compression/UCC  <br>Uncompressed, OGG, OPUS, FLAC  <br>Incompatible formats forbidden for write |
| **File extension**                                 | SFE: `.sf4` <br>SF2.0x: `.sf2`  <br>Werner SF3: `.sf3`  <br>Any other uncompressed format is allowed    | SFE: `.sf4` <br>SF2.0x: `.sf2`  <br>Werner SF3: `.sf3`  <br>Any other uncompressed format is allowed | SFE: `.sf4` <br>SF2.0x: `.sf2`  <br>Werner SF3: `.sf3`  <br>Any other uncompressed format is allowed | SFE: `.sf4` <br>SF2.0x: `.sf2`  <br>Werner SF3: `.sf3`  <br>Any other uncompressed format is allowed |
| **Information/Metadata**                           | New chunks, feature flags                                                                               | New chunks, feature flags                                                                            | New chunks, feature flags                                                                            | New chunks, feature flags                                                                            |

\*Or platform limit, whichever is less. (since 4.0.29) 

### 11.1.2 Sample specifications

|                                                 | **Level 1**                                               | **Level 2**                                               | **Level 3**                                               | **Level 4**                                               |
|-------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| **Maximum sample rate**                         | 44 100 Hz or greater                                      | 50 000 Hz or greater                                      | 96 000 Hz or greater                                      | No limit                                                  |
| **Sample bit depth**                            | 16-bit or greater  <br>Ignore unsupported sdta sub-chunks | 16-bit or greater  <br>Ignore unsupported sdta sub-chunks | 24-bit or greater  <br>Ignore unsupported sdta sub-chunks | 32-bit or greater  <br>Ignore unsupported sdta sub-chunks |
| **8-bit samples**                               | Optional                                                  | Optional                                                  | Optional                                                  | Mandatory                                                 |
| **Maximum individual sample length**            | 16,777,216 samples or greater                             | 4,294,967,296 samples or greater                          | 4,294,967,296 samples or greater                          | Based on chunk header type                                |
| **Loop point sets**                             | 1                                                         | 1                                                         | 1                                                         | 1                                                         |
| **Sample linking** (since 4.0.5)                | Mono, Left/Right <br>Includes SFE Compression             | Mono, Left/Right, "Link"  <br>Includes SFE Compression    | Mono, Left/Right, "Link"  <br>Includes SFE Compression    | Mono, Left/Right, "Link"  <br>Includes SFE Compression    |
| **Number of channels**                          | Mono, Stereo\*                                            | Mono, Stereo\*                                            | Mono, Stereo\*                                            | Mono, Stereo\*                                            |
| **Sample name length**                          | Display 8 characters  <br>Write 20 characters             | Display 20 characters  <br>Write 20 characters            | Display 20 characters  <br>Write 20 characters            | Display 20 characters  <br>Write 20 characters            |
| **Sample compression algorithms** (since 4.0.5) | WAV, OGG                                                  | WAV, OGG, FLAC                                            | WAV, OGG, OPUS, FLAC                                      | WAV, OGG, OPUS, FLAC                                      |

\*Stereo samples are implemented as two mono samples linked together. (since 4.0.9)

### 11.1.3 Instrument specifications

|                                  | **Level 1**                                   | **Level 2**                                    | **Level 3**                                    | **Level 4**                                    |
|----------------------------------|-----------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| **Samples per instrument**       | 64 or greater                                 | 4096 or greater                                | 16384 or greater                               | No limit                                       |
| **Simultaneous sample playback** | 2 or greater                                  | 32 or greater                                  | 64 or greater                                  | No limit                                       |
| **Modulators**                   | All 4.0 modulators                            | All 4.0 modulators                             | All 4.0 modulators                             | All 4.0 modulators                             |
| **Default modulators**           | All 4.0 default modulators                    | All 4.0 default modulators plus DMOD           | All 4.0 default modulators plus DMOD           | All 4.0 default modulators plus DMOD           |
| **Enumerators**                  | All 4.0 enumerators                           | All 4.0 enumerators                            | All 4.0 enumerators                            | All 4.0 enumerators                            |
| **Instrument name length**       | Display 8 characters  <br>Write 20 characters | Display 20 characters  <br>Write 20 characters | Display 20 characters  <br>Write 20 characters | Display 20 characters  <br>Write 20 characters |

### 11.1.4 Preset specifications

|                                  | **Level 1**                                   | **Level 2**                                    | **Level 3**                                    | **Level 4**                                    |
|----------------------------------|-----------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| **Instruments per preset**       | 2 or greater                                  | 16 or greater                                  | 64 or greater                                  | No limit                                       |
| **Simultaneous sample playback** | 4 or greater                                  | 256 or greater  <br>Or up to polyphony limit   | 512 or greater  <br>Or up to polyphony limit   | No limit                                       |
| **Preset name length**           | Display 8 characters  <br>Write 20 characters | Display 20 characters  <br>Write 20 characters | Display 20 characters  <br>Write 20 characters | Display 20 characters  <br>Write 20 characters |

### 11.1.5 Player specifications

|                                                                                                                                            | **Level 1**                                                            | **Level 2**                                                              | **Level 3**                                                              | **Level 4**                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------|
| **Polyphony limit**                                                                                                                        | 32 or greater with mono samples  <br>16 or greater with stereo samples | 256 or greater with mono samples  <br>128 or greater with stereo samples | 512 or greater with mono samples  <br>256 or greater with stereo samples | No limit                                                     |
| **Percussion toggle**                                                                                                                      | `byBankMSB`/`byBankLSB` bit 1                                          | `byBankMSB`/`byBankLSB` bit 1                                            | `byBankMSB`/`byBankLSB` bit 1                                            | `byBankMSB`/`byBankLSB` bit 1                                |
| **Control change 0/32 (Bank select)**                                                                                                      | CC0: `byBankMSB` bits 2-8  <br>CC32: `byBankLSB` bits 2-8              | CC0: `byBankMSB` bits 2-8  <br>CC32: `byBankLSB` bits 2-8                | CC0: `byBankMSB` bits 2-8  <br>CC32: `byBankLSB` bits 2-8                | CC0: `byBankMSB` bits 2-8  <br>CC32: `byBankLSB` bits 2-8    |
| **Control change 7/39/8**  <br>**Control change 40/10/42**                                                                                 | Mandatory                                                              | Mandatory                                                                | Mandatory                                                                | Mandatory                                                    |
| **Control change 1/33/2/34/4/36**  <br>**Control change 5/37/11/43/84**                                                                    | CC1/33 (modulation wheel) required                                     | CC1/33 (modulation wheel) required                                       | Mandatory                                                                | Mandatory                                                    |
| **Control change 6/38**                                                                                                                    | GM1 data entry required                                                | GM1 data entry required                                                  | GM1 data entry required                                                  | GM1 data entry required                                      |
| **Control change 12/13/44/45**  <br>**Control change 16/17/18/19**  <br>**Control change 48/49/50/51**  <br>**Control change 80/81/82/83** | Mandatory                                                              | Mandatory                                                                | Mandatory                                                                | Mandatory                                                    |
| **Control change 64/66/67**                                                                                                                | Mandatory                                                              | Mandatory                                                                | Mandatory                                                                | Mandatory                                                    |
| **Control change 68/69**                                                                                                                   | Optional                                                               | Optional                                                                 | Mandatory                                                                | Mandatory                                                    |
| **Control change 70/71/72/73/74**  <br>**Control change 75/76/77/78/79** (since 4.0.21)                                                    | CC72 release time  <br>CC73 attack time  <br>CC74 brightness           | CC72 release time  <br>CC73 attack time  <br>CC74 brightness             | CC72 release time  <br>CC73 attack time  <br>CC74 brightness             | CC72 release time  <br>CC73 attack time  <br>CC74 brightness |
| **Control change 91/93**                                                                                                                   | Reverb and chorus                                                      | Reverb and chorus                                                        | Reverb and chorus                                                        | Reverb and chorus                                            |
| **Control change 92/94/95**                                                                                                                | GM1 level effects unit required                                        | GM1 level effects unit required                                          | GM1 level effects unit required                                          | GM1 level effects unit required                              |
| **Control change 96/97/98**  <br>**Control change 99/100/101**                                                                             | Mandatory                                                              | Mandatory                                                                | Mandatory                                                                | Mandatory                                                    |
| **Control change 120/121/122/123**  <br>**Control change 124/125/126/127**                                                                 | Mandatory                                                              | Mandatory                                                                | Mandatory                                                                | Mandatory                                                    |
| **GM1 reset**                                                                                                                              | Mandatory                                                              | Mandatory                                                                | Mandatory                                                                | Mandatory                                                    |
| **SMF formats**                                                                                                                            | 0 and 1                                                                | 0 and 1                                                                  | 0, 1 and 2                                                               | Any                                                          |
| **Number of channels**                                                                                                                     | 16 or greater                                                          | 16 or greater                                                            | 64 or greater                                                            | No limit                                                     |
| **ROM emulator** (since 4.0.5)                                                                                                             | ROM sample support or emulator optional                                | ROM sample support or emulator optional                                  | ROM sample support or emulator optional                                  | ROM sample support or emulator optional                      |

## 11.2 Converting between legacy SF and SFE

### 11.2.1 Conversion from legacy SF2.04 to SFE

- Upgrade the `ifil` version in the header from `wMajor=2`, `wMinor=4` to `wMajor=2`, `wMinor=1024`.
- Overwrite the `isng` value with `SFE 4`. (since 4.0.11)
- Create an `ISFe-list` sub-chunk with information: `SFty = "SFE standard"`, `SFvx = 4, 0, Final, 0, "4.0u12"`, `flag` corresponding to features used in the bank. (since 4.0.12)
- Automatically modify the bank to take into account any of the program's implementation quirks (if applicable). (since 4.0.11)

### 11.2.2 Conversion from SFE to legacy SF2.04

- Downgrade the `ifil` version in the header from `wMajor=2`, `wMinor=1024` to `wMajor=2`, `wMinor=4`.
- Overwrite the `isng` value with `X-Fi`.
- Decompress/de-containerise the samples if the bank uses SFE Compression.
- Convert the sdta structure to legacy 24-bit.
- If the first 8 bits of either `wPreset` or `wBank` are identical to another patch, keep only the patch with bits 9-16 clear. If this is not found, keep only the last of the patches in the record. Clear bits 9-16 of all patches afterward.
- Remove the `ISFe-list` sub-chunk.

### 11.2.3 Conversion from SFE to legacy SF2.01

- Downgrade the `ifil` version in the header from `wMajor=2`, `wMinor=1024` to `wMajor=2`, `wMinor=1`.
- Overwrite the `isng` value with `EMU8000` or `E-mu 10K1`.
- Decompress/de-containerise the samples if the bank uses SFE Compression.
- Convert the sdta structure to legacy 16-bit.
- If the first 8 bits of either `wPreset` or `wBank` are identical to another patch, keep only the patch with bits 9-16 clear. If this is not found, keep only the last of the patches in the record. Clear bits 9-16 of all patches afterward.
- Remove the `ISFe-list` sub-chunk.

## 11.3 Converting between chunk header types

### 11.3.1 Conversion of 32-bit static to 64-bit static (since 4.0.17)

- Replace `RIFF` with `RIFS`.
- Convert all `ckSize` values to 8 bytes.
- Replace `sfbk` with `sfen`.
- Upgrade the `ifil` version in the header to `wMajor=4`.

### 11.3.2 Conversion of 64-bit static to 32-bit static (since 4.0.17)

- Make sure file size does not exceed 4GiB.
- Replace `RIFS` with `RIFF`.
- Rename `sfen` to `sfbk`.
- Downgrade the `ifil` version in the header to `wMajor=2`.

## 11.4 File repair programs

### 11.4.1 Repairing Structurally Unsound errors

#### ifil sub-chunk errors

To fix `ifil` sub-chunk errors, file repair programs must determine the correct version number of the SFE program by inspecting the file structure. File repair programs should never simply add the current SFE specification version, as that can cause a non-critical error relating to an ifil version mismatch due to the specification version being written in `ISFe-list` (`SFvx`) and not `ifil`.

If the file is too damaged to determine the correct `ifil` version, then the repair program should repair these problems first. If, after this, a definitive SF version cannot be determined, the user should be given the option to manually enter a new SF file version. The correct data in `ISFe-list` should also be included if the file is an SFE bank.

Alternatively, file repair programs can allow the user to manually enter the SF file version without allowing the program to automatically determine the necessary version.

#### PHDR sub-chunk errors

In the case of a missing `PHDR` sub-chunk, the program should just reconstruct an "empty" `PHDR` sub-chunk. The bank will not be usable until the `PHDR` sub-chunk is manually re-created.

If the `PHDR` sub-chunk contains at least two records, but is not a multiple of 38 bytes, then this indicates a structural error in one or more records. Each record can be inspected and the structure repaired. The user should also be given the choice between repairing the records and just deleting them. Repaired records must be indicated so the user can make any required adjustments. This does not have to be in the file, rather just in the user interface of the program.

Non-monotonic preset bag indices should be reordered if encountered.

The `PBAG` sub-chunk size is usually corrected by correcting the incorrect value(s). The correct value can be reconstructed once the preset bag indices have been reordered.

#### PBAG sub-chunk errors

In the case of a missing `PBAG` sub-chunk, the program should just reconstruct an "empty" `PBAG` sub-chunk. The bank will not be usable until the `PBAG` sub-chunk is manually re-created.

If the `PHDR` sub-chunk is not a multiple of 4 bytes, or if there is a mismatch between the generator or modulator indices and corresponding `PGEN`/`PMOD`sub-chunk sizes, then this indicates a structural error in one or more of the preset zones. Each zone can be inspected and the structure repaired. The user should also be given the choice between repairing the zones and just deleting them. Repaired zones must be indicated so the user can make any required adjustments. This does not have to be in the file, rather just in the user interface of the program.

Non-monotonic generator or modulator indices should be reordered if encountered.

The `PGEN`/`PMOD` sub-chunk sizes are usually corrected by correcting the incorrect value(s). The correct value can be reconstructed once the preset bag indices have been reordered.

#### PMOD sub-chunk errors

In the case of a missing `PMOD` sub-chunk, the program should just reconstruct an "empty" `PMOD` sub-chunk. The bank may be usable, but there will be a significant quality loss until the `PMOD` sub-chunk is manually re-created.

If the `PMOD` sub-chunk is not a multiple of 10 bytes, then this indicates a structural error in one or more of the preset modulators. Each modulator can be inspected and the structure repaired. The user should also be given the choice between repairing the modulators and just deleting them. Repaired modulators must be indicated so the user can make any required adjustments. This does not have to be in the file, rather just in the user interface of the program.

#### PGEN sub-chunk errors

In the case of a missing `PGEN` sub-chunk, the program should just reconstruct an "empty" `PGEN` sub-chunk. The bank will not be usable until the `PGEN` sub-chunk is manually re-created.

If the `PGEN` sub-chunk is not a multiple of 4 bytes, then this indicates a structural error in one or more of the preset generators. Each generator can be inspected and the structure repaired. The user should also be given the choice between repairing the generators and just deleting them. Repaired generators must be indicated so the user can make any required adjustments. This does not have to be in the file, rather just in the user interface of the program.

The instrument generator value is usually corrected by correcting the incorrect value(s) by inspecting the structure and determining the correct value for the instrument generator value or terminal instrument.

#### INST sub-chunk errors

In the case of a missing `INST` sub-chunk, the program should just reconstruct an "empty" `INST` sub-chunk. The bank will not be usable until the `INST` sub-chunk is manually re-created.

If the `INST` sub-chunk contains at least two records, but is not a multiple of 22 bytes, then this indicates a structural error in one or more records. Each record can be inspected and the structure repaired. The user should also be given the choice between repairing the records and just deleting them. Repaired records must be indicated so the user can make any required adjustments. This does not have to be in the file, rather just in the user interface of the program.

Non-monotonic instrument bag indices should be reordered if encountered.

The `INST` sub-chunk size is usually corrected by correcting the incorrect value(s). The correct value can be reconstructed once the instrument bag indices have been reordered.

#### IBAG sub-chunk errors

In the case of a missing `IBAG` sub-chunk, the program should just reconstruct an "empty" `IBAG` sub-chunk. The bank will not be usable until the `IBAG` sub-chunk is manually re-created.

If the `IHDR` sub-chunk is not a multiple of 4 bytes, or if there is a mismatch between the generator or modulator indices and corresponding `IGEN`/`IMOD`sub-chunk sizes, then this indicates a structural error in one or more of the instrument zones. Each zone can be inspected and the structure repaired. The user should also be given the choice between repairing the zones and just deleting them. Repaired zones must be indicated so the user can make any required adjustments. This does not have to be in the file, rather just in the user interface of the program.

Non-monotonic generator or modulator indices should be reordered if encountered.

The `IGEN`/`IMOD` sub-chunk sizes are usually corrected by correcting the incorrect value(s). The correct value can be reconstructed once the instrument bag indices have been reordered.

#### IMOD sub-chunk errors

In the case of a missing `IMOD` sub-chunk, the program should just reconstruct an "empty" `IMOD` sub-chunk. The bank may be usable, but there will be a significant quality loss until the `IMOD` sub-chunk is manually re-created.

If the `IMOD` sub-chunk is not a multiple of 10 bytes, then this indicates a structural error in one or more of the instrument modulators. Each modulator can be inspected and the structure repaired. The user should also be given the choice between repairing the modulators and just deleting them. Repaired modulators must be indicated so the user can make any required adjustments. This does not have to be in the file, rather just in the user interface of the program.

#### IGEN sub-chunk errors

In the case of a missing `IGEN` sub-chunk, the program should just reconstruct an "empty" `IGEN` sub-chunk. The bank will not be usable until the `IGEN` sub-chunk is manually re-created.

If the `IGEN` sub-chunk is not a multiple of 4 bytes, then this indicates a structural error in one or more of the instrument generators. Each generator can be inspected and the structure repaired. The user should also be given the choice between repairing the generators and just deleting them. Repaired generators must be indicated so the user can make any required adjustments. This does not have to be in the file, rather just in the user interface of the program.

The `sampleID` generator value is usually corrected by correcting the incorrect value(s) by inspecting the structure and determining the correct value for the `sampleID` generator value or terminal `sampleID`.

#### SHDR sub-chunk errors

If there is no usable sample data, the program should just reconstruct an "empty" `SHDR` sub-chunk. However, if there is usable sample data, the program may attempt to partially reconstruct the `SHDR`sub-chunk. User input will be required.

If there is no valid `irom` sub-chunk, the program can clean these samples if they aren't being used in the bank. If they are used by the bank, then the program should then attempt to read the sample as a non-ROM sample, and if the samples are valid, then this means that the problem is fixed. If there is no valid sample, then either a new sample must be provided by the user, or a ROM should be defined for the iromsub-chunk.

#### Unknown sub-chunk errors

Unknown sub-chunk errors can easily be fixed; the unknown sub-chunks are simply removed.

#### Compressed sample errors

In SFE Compression, all PCM samples must go before compressed samples. This is fixed by rearranging the sample data in the `smpl` chunk, and then updating the `shdr` sub-chunk.

#### ckSize errors

`ckSize` errors are easily solved by checking the `ckSize` values and fixing them with the correct chunk sizes.

#### Incompatible chunk header errors

Incompatible chunk header errors are solved by replacing chunk headers with a compatible version, or swapping the endianness of the data.

#### Incompatible SFty errors

TSC-related errors are corrected by rearranging the chunks.

### 11.4.2 Repairing non-critical errors

#### isng sub-chunk errors

In the case of a missing `isng` sub-chunk, a value of `SFE 4` should be written.

If it doesn't end in a zero-valued byte, then add a zero-valued byte and warn the user to verify if the value is correct.

#### ICRD sub-chunk errors

In the case of a missing `ICRD` sub-chunk, a value corresponding to the current ISO-8601 date and time should be written.

Should the `ICRD` sub-chunk not be a valid ISO-8601 date or time, firstly attempt to parse the current value. For example, it may be in a different language. If it can't be parsed, then write a value corresponding to the current ISO-8601 date and time.

#### INAM, IENG, IPRD, ICOP, ICMT or ISFT sub-chunk errors

Missing sub-chunks should be filled in intuitively. For example, for an `INAM` sub-chunk, the file name or `Unnamed bank` are good starting points.

If it doesn't end in a zero-valued byte, then add a zero-valued byte and warn the user to verify if the value is correct.

Except the `INAM` chunk, if the sub-chunk's value cannot be faithfully copied as a string, the user should be given a chance to add the correct value in UTF-8.

#### irom or iver sub-chunk errors

Missing sub-chunks should not be filled in unless there are ROM samples that are linked.

#### PHDR sub-chunk errors

Any `dwLibrary`, `dwGenre` or `dwMorphology` value should be cleared because current versions of SFE do not implement this yet. Presets without any zones should be given a zone named `Empty preset` or similar.

#### PBAG sub-chunk errors

These problems can easily be fixed by giving zones after the first (including the global zone) an instrument generator.

#### PMOD or IMOD sub-chunk errors

To fix unknown or inappropriate "link" values, they should be corrected to a value given by the user. Out-of-range modulator indexes should be fixed by letting the user select the correct modulator, or define a new modulator if it doesn't exist. Circularly linked modulators should be highlighted to allow the user to break the circular links. Modulators with the same enumerators should also be highlighted, so the enumerators can be changed by the user.

#### PGEN sub-chunk errors

Unknown `sfGenOper` values should be corrected to a value given by the user. Modulators with the same `sfGenOper` enumerator as another modulator should be highlighted, so it can be changed by the user. Generators and modulators in inappropriate places should also be moved with references corrected. Non-global lists that don't have an instrument generator at the end should have an instrument generator added.

#### INST sub-chunk errors

To fix this issue, the instrument should be deleted unless it's being used by a preset. If so, the instrument should be kept, but the user should be warned so they can fix the problem.

#### IBAG sub-chunk errors

These problems can easily be fixed by giving zones after the first (including the global zone) a `sampleID` generator.

#### IGEN sub-chunk errors

Unknown `sfGenOper` values should be corrected to a value given by the user. Modulators with the same `sfGenOper` enumerator as another modulator should be highlighted, so it can be changed by the user. Generators and modulators in inappropriate places should also be moved with references corrected. Non-global lists that don't have a `sampleID` generator at the end should have an `sampleID` generator added.

#### SHDR sub-chunk errors

If the sample rate is zero, then it should be corrected automatically to the correct value via automatic pitch detection and then highlighted for the user to verify. Bad original pitch values should be corrected to the value with automatic pitch detection.

You should not edit the sample rate unless it is zero.

#### Undefined and unknown enum, palette value and source type errors

Anything that uses these values should either be removed or highlighted so the user can inspect it. If a value is undefined for the `SFvx` version, but defined for a newer version, then the program can also offer to update the version to a newer version.

#### Precedence errors

In this case, the user should be allowed to change the generator value or to remove the offending generator entirely.

#### Parameter value and padding errors

In this case, the illegal or missing parameter value should be shown to the user, so they can rectify it. Padding should automatically be added wherever possible.

#### Unknown chunk errors

If a chunk is undefined in the `SFvx` version given, but defined in a later version, then the `SFvx` and/or `ifil` versions should be updated. If it is undefined in any version, then it can safely be deleted.

#### Compression errors

The user should be given the choice of compression algorithms to use for the sample, and `wSampleLink` values should be set to zero.

#### ISFe chunk errors

The `ISFe-list` sub-chunk can be repaired, however information in the `ISFe-list` sub-chunk should be reconstructed.

#### ifil chunk errors

If features or feature flags from a newer `ifil` or `SFvx` version of SFE are found on a bank with an older declared version of `SFvx`, then the version should be updated to the detected version of `SFvx`.

#### Incompatible compression errors

If an incompatible compression format is supported by the SFE program, then it should be decompressed and automatically recompressed into a lossless format using SFE Compression. (since 4.0.2)

#### wPreset value errors

If invalid `wPreset` values are found, then they should be highlighted by the program, and the user should have the opportunity to select a different `wPreset` value.

#### Duplicated preset location errors

Duplicated preset locations should be highlighted, and the user should have the opportunity to select a different preset value.

#### File size limit errors

32-bit static headers and structures can be replaced with 64-bit counterparts if the file size was found to exceed 4 GiB. Alternatively, if TSC mode is supported by the SFE program, then it can be activated by moving the sdta-info chunk to the end and setting the correct feature flag in the `ISFe-list` sub-chunk.

#### Feature flag errors

Feature flags can be updated to accurately reflect the features that the bank uses.

### 11.4.3 Manual repair

Manual repair is used to completely fix a broken SFE bank. It can be partially automated, however some parts of manual repair are not automatable, and the parts that aren't automatable are highlighted.

Manual repair is intended to be part of SFE bank development tools such as SFE editors or dedicated file repair programs. It is also suitable for situations where control over the repair process by the user is required. However, it is not suitable for SF players.

Manual repair can be used to repair all Structurally Unsound errors and non-critical errors listed in section 11.4. This is the main advantage that it holds over automatic repair.

You can use it to fix a corrupted bank. A manual repair program is very useful if you develop banks, as your data may be damaged at any time for any reason.

### 11.4.4 Automatic repair

Automatic repair allows SFE players to play some "Structurally Unsound" banks by automatically repairing them at load time. It consists of a partial file repair program built directly into the SFE player. With future versions of this specification, SFE players that only support a higher version of the format will also gain the ability to translate old banks to run properly.

Automatic repair is intended to be part of SFE players. It is an aid to help SFE players play banks that are otherwise "Structurally Unsound". It is not a substitute for repairing the bank using file repair programs. File repair programs should always include an option to use manual repair.

Automatic repair fixes structural defects in SFE and legacy SF2.04 banks seamlessly and transparently. It should automatically repair all Structurally Unsound errors listed in section 11.4.1 except for compressed sample errors and anything that requires user input.

It should also repair all non-critical errors listed in section 11.4.2 except for compression errors, `wPreset` value errors, file size limit errors and anything that requires user input. The repair of incompatible compression errors is optional and contingent on support for such formats. (since 4.0.2)

The program developers are allowed to use any repair strategy listed in section 11.4.

Automatic repair requires that the implementation give a message when invoked. This is to encourage bank developers not to rely on the feature to implicitly define any parameters.

Automatic repair is a great method to fix issues that prevent SF banks from loading correctly, but it can't repair all defects. For example, anything that requires user input is outside the scope of automatic repair, and should be dealt with by a file repair program or SFE editor program instead.

This feature must also never overwrite files. This is the job of a file repair program. If system memory is low, it is acceptable for automatic repair implementations to create a patched bank in temporary file storage.

You must correctly set up your banks to ensure that they run properly; do not use automatic repair to implicitly define certain parameters. If you do so, then your bank may not run properly on a legacy SF player or an SFE player that doesn't implement automatic repair.

## 11.5 Why these guidelines?

### 11.5.1 File Size Representation

- SFE is a 32-bit or 64-bit format.
- Incorrect numbers of bits will therefore result in program non-compliance.
- Signed integers are not useful because a negative file size is impossible.
- To ensure that file size limits are not arbitrarily "cut in half", signed integers are prohibited.
- Programs using signed integers to represent file size are therefore not compliant with SFE.

### 11.5.2 File Size Limit

- You should not impose additional file size limits in SFE programs.
- SFE files that exceed these limits may not play.
- Because compatibility is not guaranteed, such programs may not be SFE compliant.

### 11.5.3 Sample Streaming

- You should strive to include disk streaming support.
- This is because the file size limit is almost always greater than the system memory installed.
- System memory streaming options may be available for higher performance.

### 11.5.4 Total File Size Limit and Multiple Files

- Always provide space for more than one file.
- SFE allows flexibility in implementing multiple files.
- It will be standardised in the future depending on the most popular system.
- The program specification requires multiple files, to guarantee proper operation of "split bank" files.
- Not implementing multiple file operation will affect compatibility.
- Such programs therefore may not be SFE compliant.

### 11.5.5 Legacy Support

- SFE is designed to reconcile incompatible SF extensions.
- Werner SF3 support is required; the SFE format incorporates Werner SF3 structures (SFE Compression).
- Programs that cannot recognise Werner SF3 format (SFE Compression) may not be able to open SFE files.
- 24-bit support is optional, but if 24-bit is unsupported in an SFE player, legacy SF2.04 files must not be rejected.
- Backward compatibility with legacy SF2.0x is sacrosanct when using 32-bit chunk headers, take care when creating a program.
- "Synthfont Custom Features" support is not currently included in the specification.

### 11.5.6 Header Support

- The header should be `RIFF` and `sfbk` with 32-bit chunk headers to preserve legacy SF2.0x compatibility.
- 32-bit only programs should recognise 64-bit chunk headers and give an error.
- The header should be `RIFS` and `sfen` with 64-bit chunk headers. (since 4.0.17)
- All programs that support 64-bit chunk headers must also support 32-bit chunk headers.

### 11.5.7 Sample Compression

- Compression algorithms vary, but we recommend at least one of each lossy and lossless algorithms.
- OGG and FLAC are specified in the specification.
- Werner SF3 was designed to use OGG files, so OGG is a good start for lossy algorithms.
- Opus is an alternative that is "better" than OGG according to some people.
- FLAC and "Wavpack" are free lossless compression algorithms for sounds.
- Note that while "Wavpack" has advantages over FLAC, it is not widely supported.

### 11.5.8 File Extension, Structure, Information and Metadata

- The file extension is `.sf4`. Chunk headers must be detected.
- Do not save SFE files with an extension `.sf2`, as it may confuse legacy SF2.0x players. Remember that SFE files are not SoundFonts!
- Use the `ifil` and `SFvx` sub-chunks to determine version, do not use the file extension.
- For SFE, you must use the prescribed chunk sizes and limits in the specification.

### 11.5.9 Sample Specifications

- Level 3 requires 96kHz frequency, because it is the next standard frequency above 50kHz as specified by SF2.04.
- 88.2kHz is not recommended because it is non-standard.
- Stray `sdta` sub-chunks must be ignored. Erroring out on extra `sdta` chunks is not compliant with SF2.04.
- There must not be additional limitations to sample length, besides the file size limits.
- Sample linking features from legacy SF2.04 must be supported (except SFE Compression).

### 11.5.10 Instrument Specifications

- High numbers of samples per instrument are specified to ensure that the program works efficiently.
- Ideally, programs should support unlimited numbers of samples per instrument.
- You must not add restrictions to number of samples per instrument or simultaneous samples.
- Modulators are fixed and must be implemented as shown in the specification and not as in SF2.04.
- In legacy SF2.04 compatibility mode, bug compatibility can be implemented.
- When field sizes increase from 20 characters, programs should be able to display at least 64 characters.
- If it is not possible to display the entire field, use an ellipsis or similar.

### 11.5.11 Player Specifications

- A minimum polyphony of 256 notes is in place if possible.
- The `byBankLSB` percussion toggle is to fix the bank select LSB function.
- All control changes listed as "mandatory" must be supported.
- If it is not supported, playback may be severely impacted, resulting in a program that is not SFE compliant.
- This is already a problem with legacy SF2.0x, as not all SF2 players support modulators.
- Reset support and multiple simultaneous drum kits might not be required, but it is suggested.
- 64-channel MIDI file support is suggested, and may be required in the future for SFE.
- The ROM emulator may be required in the future, as many SFE files will make full use of it.

## 11.6 How to test your program with SFSpecTest

### 11.6.1 What does SFSpecTest do?

By using SFSpecTest by mrbumpy409 ([available here](https://github.com/mrbumpy409/SoundFont-Spec-Test)), you can test your SFE player and determine which feature flags to set.

SFSpecTest was written by the author of GeneralUserGS, one of the most popular legacy SF2.0x banks, and is thus a good benchmark for legacy SF2.04 players.

Because SFE is a superset of legacy SF2.04, it is also a good tool to determine what SF2.04 features your program support, allowing you to set the correct feature flags for your program.

### 11.6.2 Branch 00 Foundational synthesis engine

In leaf `00:00`, if your player passes SFSpecTest test #8 (Scale Tune/Root Key), you can set all four defined bits.

In leaf `00:03`, set bits 1-16 to the maximum frequency attained in SFSpecTest test #9 (Initial Filter Cutoff), and bits 17-24 to the maximum resonance attained in SFSpecTest test #10 (Filter Resonance).

In leaf `00:04`, if your player passes SFSpecTest test #11 (Attenuation Amount), you can set the first two defined bits. If your player passes SFSpecTest test #5a (Modulation LFO A) and #12 (Negative Attenuation Amount), you can also set the third bit.

In leaf `00:05`, set bit 1 if you pass SFSpecTest test #17a (Reverb A), bit 2 if you pass SFSpecTest test #17b (Reverb B), bit 3 if you pass SFSpecTest test #17c (Reverb C), bit 9 if you pass SFSpecTest test #18a (Chorus A), bit 10 if you pass SFSpecTest test #18b (Chorus B), and bit 11 if you pass SFSpecTest test #18c (Chorus C). Set bit 4 if your reverb can be adjusted, and set bit 12 if your chorus can be adjusted.

In leaf `00:06`, if your player passes SFSpecTest test #5 (Modulation LFO), you can set bit 4. If your player passes SFSpecTest test #6 (Vibrato LFO) and test #7 (Mod Wheel to LFO), you can set bit 2.

In leaf `00:07`, if your player passes SFSpecTest test #1 (Volume Envelope), you can set bits 1-6. If your player passes SFSpecTest test #2 (Modulation Envelope), you can set bits 9-14. If your player passes SFSpecTest test #3 (Key Number to Decay), you can set bits 8 and 16. If your player passes SFSpecTest test #4 (Key Number to Hold), you can set bits 7 and 15.

In leaf `00:0a`, set bit 3 if you pass SFSpecTest test #21 (Exclusive Class). Set bit 6 if you pass SFSpecTest #16 (Sample Offset).

### 11.6.3 Branch 01 Modulators and NRPN

In leaf `01:01`, set bit 5 if you pass SFSpecTest test #20a (Pitch Bend A) and test #20b (Pitch Bend B). Set bit 6 if you pass SFSpecTest test #20c (Pitch Bend C).

In leaf `01:02`, set bit 1 if you pass SFSpecTest test #15 (CC1 to Filter Cutoff).

In leaf `01:06`, set bit 1 if you pass SFSpecTest test #13 (Velocity to Attenuation Curve), and set bit 2 if you pass SFSpecTest test #14a (Velocity to Initial Filter Cutoff Curve A) and test #14b (Velocity to Initial Filter Cutoff Curve B). Set bit 4 if you pass SFSpecTest test #15 (CC1 to Filter Cutoff). Set bit 17 if you emulate SF2.00 behaviour as shown in test #14c (Velocity to Initial Filter Cutoff Curve C), set bit 18 if you emulate SF2.01 behaviour as shown in test #14d (Velocity to Initial Filter Cutoff Curve D), and set bit 19 if you emulate SF2.04 behaviour as seen in test #14e (Velocity to Initial Filter Cutoff Curve E).

## 11.7 Courtesy actions

For the benefit of the SFE community, please:

- share all modifications implemented in a program under this license
- do not remove the link to the latest version of the specification

The above requirements are not required due to requirements listed by the Open Source Definition, but are good practice when redistributing the specification.