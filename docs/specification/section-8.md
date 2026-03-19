# Section 8: SFE error handling

## 8.1 Structurally Unsound errors

"Structurally Unsound" errors are those defined by E-mu (in legacy SF2.04), Werner Schweer (in Werner SF3) and the SFE Team (in SFE) to prevent the bank from working properly in a way that means that it can not be used. These errors must be fixed before an SF player can load it, unless the SF player implements SFE automatic repair.

The error correction process for structural errors in SFE is slightly different from that in legacy SF2.04; if a `RIFS` header is found in a file, SFE players that do not support 64-bit chunk headers should output a specific error, as mentioned in the SFE program specification. (since 4.0.17)

## 8.2 Non-critical errors

"Non-critical" errors are errors that mean that data cannot be read properly, however as they are not Structurally Unsound errors, the file can be loaded. What usually happens is that the damaged data is ignored, and the rest of the bank is loaded.

While non-critical errors don't prevent the use of the bank, it is important that they are fixed to ensure that the bank functions work as intended on all SF players that conform to a specification, whether that be legacy SF2.04, Werner SF3 or SFE.

## 8.3 Duplicated preset locations within files

This occurs when the file is structurally damaged or manually edited in a manner where more than one preset has the same value of byBankMSB, byBankLSB and wPreset (for instance, `015:000:081`).

- In legacy SF2.04, the first preset in the location would be used by default, but the other presets would still be retained.
- Such other presets must be moved before they can be used.
- In SFE, the preset to be used is no longer necessarily the first one. Instead, selecting the correct preset (or combination of presets) to use will be permissible.
- Such a feature is optional, and if not implemented, the player should use the legacy SF2.04 behavior in these cases (use the first preset found).
- Editors should warn the user if such presets are found.
- This behavior might change in future versions, so please take the `ifil` value, and later versions of this specification, into account.

## 8.4 Duplicated preset locations across files

This occurs when multiple files are loaded simultaneously (now a required feature for SFE), but some or all of the files have presets with identical `byBankMSB`, `byBankLSB` and `wPreset` values.

- Behavior was undefined in legacy SF2.04.
- This was because multiple file loading was not a standard feature mandated in the legacy SoundFont® standard.
- Legacy SF2.04 and Werner SF3 compatible software developers therefore had the liberty to implement multiple file loading; however, they wanted to.
- This edge case will now be defined in SFE.
- If multiple presets across loaded files have the same value of `byBankMSB`, `byBankLSB` and `wPreset`, then the preset to be used may be selectable from all the presets with the same bank location (in the way described in section 8.3).
- Such a feature is optional, and if not implemented, the player should use the legacy SF2.04 behavior in these cases (use the first preset found).
- Editors should warn the user if such presets are found.
- This behavior might change in future versions, so please take the `ifil` value, and later versions of this specification, into account.

## 8.5 Undefined chunks

Legacy SF2.04 players should ignore SFE-specific sub-chunks, as prescribed by E-mu.

Also, SFE 4.0 compatible players, which do not support future versions, should ignore sub-chunks which are used in future versions.

## 8.6 Unknown Enumerators

Any `SFvx` versions of 4.1 or above may have unknown enumeration values for an SFE 4.0 player.

This is entirely expected, and if unknown enumeration values are found, the Generator/Modulator should be ignored.

## 8.7 Maximum File Size Limit Exceeded

This occurs when the user loads a file that is larger than the maximum size that the SFE program can accommodate.

- In the AWE32 and AWE64, the limit was dependent on the memory installed on the card, which was up to 28 MiB.
- Later, the sound cards allowed the user to load files with file sizes up to system memory.
- SFE has defined limits that are found in the separate program specification.
- If these limits are reached, you can reject loading of the file with an error, or attempt to load the file anyway.
- SFE programs should warn the user if processing was automatically done to a file to reduce the file size to be in range.
- If multiple files are loaded, and the limit is reached, the order of files to be loaded can be defined by the author of the SFE-compatible software.

## 8.8 MIDI Errors

If a non-existent bank/preset combination is selected, the software should use the lowest value for the selected bank that results in an existent combination. If this doesn't exist, then the software should select the next available preset. (since 4.0.5)

If the `wPreset` value cannot be matched, then the first preset value that is available is used. (since 4.0.3)

This behavior might change in future versions, so please take the `ifil` value, and later versions of this specification, into account. (since 4.0.3)

## 8.9 UTF-8 errors (since 4.0.25)

Because SFE uses UTF-8, there may be some circumstances where UTF-8 fields will be invalid. In this case, replace the invalid characters with replacement characters.

## 8.10 Illegal parameter values, out of range values, missing required items and illegal enumerators

These are handled as in legacy SF2.04.

---