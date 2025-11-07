# Section 4: Terminology

## 4.1 Data structure terminology

The data structure terminology used in SFE 4.0 is broadly the same as legacy SF2.04, with these additions:

- Branch - A subdivision of a tree structure containing either sub-branches or leaves that include values.
- Cognitone SF4 - An incompatible modification to Werner SF3 to allow support for FLAC audio compression. Because it is considered an incompatible compression format, usage is not allowed in SFE. (since 4.0.2)
- FLAC - A lossless audio compression format commonly used in open-source software. Supported by Werner SF3, but not commonly used for that purpose.
- Leaf - A value found in a tree structure at the end of a branch.
- Lossless compression - Said of a compression format that retains all of its data when compressed. In terms of audio, there is no loss in quality in losslessly compressed audio.
- Lossy compression - Said of a compression format that does not retain all of its data when compressed. In terms of audio, there is a loss in quality in lossily compressed audio.
- OGG - See "Vorbis".
- Opus - A lossy audio compression format, slightly newer than OGG but with less wide adoption.
- Quirk - Any player-specific function that is automatically enabled and modifies the behaviour of any numeric parameters used by legacy SF2.0x, including preset locations, parameters, units, modulators or NRPNs.
- Quirks mode - A mode in an SFE-compatible player that enables the implementation quirks.
- RIFF-type format - Formats similar to RIFF (Resource Interchange File Format), see "RIFF" in `SFSPEC24.PDF` for more information.
- RIFS - "RIFF-like static 64-bit", a simple 64-bit RIFF-like format that uses the exact same syntax as RIFF but with 8-byte chunk size instead of 4-byte. (since 4.0.17)
- SFE - A family of enhancements to the SoundFont® 2.04 formats, unofficially created after E-mu/Creative abandoned the original format. May not be structurally compatible with legacy SF2.04.
- SFE 4 - This new specification, based on SoundFont® 2.04 and Werner SF3, with a set of new features making it more realistic. Not to be confused with the incompatible Cognitone SF4 file format.
- SFE-compatible - Indicates files, data, synthesisers, hardware or software that conform to the SFE specification.
- SFE Compression - The compression system based on Werner SF3 that SFE programs should be compliant with.
- Static RIFF - Any RIFF-type format with a fixed chunk size field width, including RIFF or RIFS. See "RIFF-type format", "RIFF" and "RIFS". (since 4.0.17)
- Tree structure - A structure consisting of branches and leaves.
- Vorbis - A lossy audio compression format commonly used in open-source software. The basic compression format that most Werner SF3 and SFE-compatible software should be expected to implement.
- Werner SF3 - A small upgrade to SoundFont® 2.04 created by Werner Schweer to allow an open source compression solution for SoundFont® programs. Standardised as SFE Compression.

And these changes:

- RIFF - The 32-bit static RIFF format used by SoundFont® 2.04 and the unmodified version of the format described by Microsoft in 1991.

## 4.2 Synthesis terminology

The synth terminology used in SFE 4.0 is broadly the same as legacy SF2.04, with these additions:

- AWE64 - The successor to the famous AWE32, adding features such as waveguide synthesis. Used the EMU8000 synthesizer chip, like the preceding AWE32. Available in "Value" or "Gold" versions.
- DAHDSR - Stands for Delay, attack, hold, decay, sustain, release. The six-step envelope system used in SF and SFE.
- EMU10K1 - The successor to the EMU8000, designed by E-mu® for the Creative Labs SB Live!.
- EMU10K2 - An update to the EMU10K1, designed by E-mu® for the Creative Labs SB Audigy.
- EMU20K1 - The successor to the EMU10K2, designed by E-mu® for the Creative Labs SB X-Fi.
- EMU20K2 - An update to the EMU20K1, please refer [here](https://en.wikipedia.org/wiki/Sound_Blaster_X-Fi) for information on SB X-Fi cards that include it.
- Hold - The portion of the DAHDSR envelope after the attack portion, but before the decay portion starts.
- Legacy sound card - A Sound Blaster® (or other sound card) that uses a hardware MIDI synthesiser capable of using banks in the SoundFont® format.
- ROM samples - Obsolete feature used in legacy sound cards, most modern SF2 files do not use this feature.
- Sharp - Said of a tone that is higher in pitch than another reference tone.
- SB - Abbreviation of "Sound Blaster®". For example, "SB X-Fi".
- Sound Blaster® Live! - The successor to the AWE64, which improved the synthesizer chip to the EMU10K1, supporting modulators.
- Sound Blaster® Audigy - The successor to the SB Live!, containing the EMU10K2 chip.
- Sound Blaster® X-Fi - The successor to the SB Audigy, containing the EMU20K1 or EMU20K2 chip. Supports 24-Bit SoundFont® 2 files (2.04).
- Synth - Abbreviation of "Synthesiser," see "Synthesiser" in `SFSPEC24.PDF` for more information.

These changes:

- Articulation - Modulation of available parameters and usage of extra samples to produce expressive musical notes.
- Case-insensitive - Indicates that a UTF-8 character or string treats alphabetic characters of upper or lower case as identical.
- Case-sensitive - Indicates that a UTF-8 character or string treats alphabetic characters of upper or lower case as distinct.
- Downloadable - legacy SF2.0x, Werner SF3 or SFE file obtained from the internet. (Old meaning referred to the obsolete ROM system)
- MIDI Bank - Groups of up to 128 presets, which can be selected by the two MIDI "Bank Select" control changes (CC00 and CC32).

And these removals:

- Preditor (refers to an old legacy SF2.0x editor made by E-mu)

## 4.3 Parameter terminology

The parameter terminology used in SFE 4.0 is broadly the same as legacy SF2.04, with these additions:

- Amplification - An increase in volume or amplitude of a signal.
- Flat - Said of a tone that is lower in pitch than another reference tone.
