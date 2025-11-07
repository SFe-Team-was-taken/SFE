# Section 10: Compatibility information

## 10.1 Specification and structural compatibility

### 10.1.1 Legacy SF2.04 specification compatibility

SFE banks are not SoundFonts, and will not play properly on a legacy SF player! However, SFE banks are very similar to SoundFonts in terms of file structure, and should thus ideally be able to at least load on legacy SF players.

If a legacy SF player is not fully compatible with legacy SF2.04, then SFE files might not load at all.

### 10.1.2 INFO chunk and legacy compatibility

SFE files that use 32-bit chunk headers should be as compliant with the legacy standard as possible. `SFSPEC24.PDF` tells implementations to ignore additional sub-chunks in the `INFO-list` chunk, therefore it is possible to use the `INFO-list` chunk for additional data related to SFE.

If SFE files that use 32-bit chunk headers cannot be loaded on legacy sound cards, then something has gone wrong.

SFE 4 does not support increased maximum length changes due to backward compatibility concerns.

### 10.1.3 phdr sub-chunk

This sub-chunk must contain at least two entries. Failure to do so will affect the compatibility with legacy SF players.

On legacy SF2.0x players, both `byBankMSB` and `byBankLSB` are read (as part of a larger `wBank` field), but only presets with a `byBankLSB` value of zero will be loaded.

You may also want to use the VArranger system for implementing LSB: for example, `115@ConcertGrand`. Support for the VArranger system is defined by bit 5 of leaf `00:07` in the `flag` sub-chunk.

Byte 7 of `byBankLSB` is reserved and should be preserved as read, and written as clear, to ensure backwards compatibility with legacy SF2.04. File editors should warn the user if byte 7 of `byBankLSB` is set.

### 10.1.4 Player implementation quirks

Some legacy SF2.0x players include quirks which are automatically loaded for all legacy SF banks. For example, a player may include bank translation when a reset is detected, to support standards that require the use of both bank select MSB and LSB, or may include changes to the modulator implementation to improve sound quality.

If an SFE bank uses an `isng` value of `SFE 4`, then programs must disable implementation quirks that were used with legacy SoundFonts. When converting legacy SoundFonts to SFE banks, programs must take implementation quirks that were used with legacy SoundFonts and translate them into the equivalent functions in SFE (if implemented) to the maximum extent possible. (since 4.0.11)

### 10.1.5 Generators and modulators

In case of compatibility issues, the `shAmount` and `wAmount` options have been kept in for SFE 4. They may be removed in future versions of SFE.

If the `iver` value is below `2.1024`, and the `isng` value is equal to `EMU8000` or another E-mu sound engine:

- A 12dB low pass filter is used to ensure compatibility with the original AWE32 sound processor.
- Controller sources remain amplitude based.
- Ignore the whole modulator structure if a reserved source type is found.
- The Controller Source Type #16-#20 acts identically to the Controller Source Type #0-#4.

If the `iver` value is `2.04` or below, ignore the whole modulator structure if a reserved source type is found.

While default modulators 1-4 are not used in SFE 4.0, SFE programs must still use them for older versions. (since 4.0.21)

- If the `iver` value is `2.04`, use the SF2.04 version of the Default Modulator 2 (optional).
- If the `iver` value is `2.01`, use the SF2.01 version of the Default Modulator 2 (optional).
- If the `isng` value is `EMU8000`, trigger legacy sound card mode.
- If the `isng` value is `E-mu 10K1`, `E-mu 10K2`, `X-Fi`, or `SFE 4`, do not trigger legacy sound card mode.

In SFE 4.0, programs should not define their own default modulators. This can cause playback issues if a SFE bank is used with a player that uses a different default modulator configuration to that of the editing software used.

Parameter units remain the same as SF2.04.

### 10.1.6 Error handling

Legacy SF players may halt on undefined chunks. Section 10.2 of `SFSPEC21.PDF` and `SFSPEC24.PDF` forbid the addition of sub-chunks to the `sdta-list` chunk, but Creative/E-mu themselves decided to do it anyway when developing SF2.04 (by using the `sm24` sub-chunk).

Legacy SF players may halt on unknown enums, which goes against the legacy SF2.04 specification. However, at least some legacy sound cards do not error out on an unknown enum.

The base preset fallback implementation in section 8.8 is designed to work with almost any `byBankMSB` and `byBankLSB` structure, including missing presets. However, this implementation may be too complicated, and players compatible with SFE 4.0 levels 1 to 3 may use a simpler system to implement base preset fallback. (since 4.0.3)

### 10.1.7 xdta-list sub-chunk (since 4.0.16)

The sub-chunks nested inside the `xdta-list` sub-chunk use the exact same structure and rules as their `pdta-list` counterparts, allowing the reuse of `pdta-list` parsers with minimal changes.

If an application cannot display more than forty characters, the extended name fields may be ignored.

Software may copy `pdta-list` values into `xdta-list`, but values must be handled as described in this specification, for example ignoring values.

## 10.2 Sample compatibility

### 10.2.1 SFE Compression and uncompressed containerised mode (since 4.0.9)

Support for the uncompressed containerised mode is a requirement for SFE Compression compatibility, because it uses the same features as SFE Compression except uncompressed samples instead of compressed ones.

If a player doesn't support certain sample parameters that it finds inside the container, then it should attempt to play back the sample with the highest quality that is possible.

While the legacy Werner SF3 method of combining compressed and uncompressed samples is deprecated, support for this method is required for SFE Compression compatibility to ensure that all Werner SF3 banks work properly. Official support for non-containerised samples will be removed in a future SFE version, but can be kept in to ensure compatibility with legacy SF2.0x.

### 10.2.2 Legacy sdta structure modes (since 4.0.8)

All players must implement legacy 16-bit mode.

While legacy 24-bit mode support is optional, we recommend that if you implement 24-bit support for uncompressed containerised mode, then non-containerised 24-bit mode is implemented to ensure compatibility with legacy SF2.04 banks. This ensures that a player's 24-bit support is not limited to just SFE banks. This does not include SFE-only players, which are not currently permitted. (since 4.0.9)

Support for legacy structure modes is deprecated and will be removed in a future SFE version. SFE editors must save SFE files in a containerised format, and SFE converters must output a bank in a containerised format. (since 4.0.10)

### 10.2.3 ROM samples

ROM samples may still be used; therefore bit 16 should not be ignored.

### 10.2.4 Incompatible compression formats

If an incompatible compression format is found, then the program may offer decompression of the incompatible file before use if you have permission from the original author of the compression formats. SF compression programs are notorious for restrictive licensing. (since 4.0.2)