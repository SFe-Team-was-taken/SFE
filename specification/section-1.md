# Section 1: Introduction

## 1.1 Preamble

The SFE standard has been created to provide a successor to E-mu Systems®'s SoundFont® 2.04 standard.

- Large files (above 4 GiB) must use a 64-bit chunk header format.
- Programs that are designed to create existing SF2 files can easily be adapted to 64-bit with SFE.
- 64-bit headers will allow creators of sound banks to replace split banks with a large number of SF2 files, with large monolithic banks, where all samples and instruments can be used in every preset.
- SFE compatible players require a certain standard of features, which is in the program specification in section 11. This improves compatibility of SFE banks with players.

## 1.2 Changelog

| Revision | Date              | Description                                                                                                                           |
|----------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 4.0.32   | 16 February 2026  | Fixed missing SFE chunks <br> Fixed some capitalisation                                                                               |
| 4.0.31   | 8 February 2026   | Modernised integer type names <br> Added more structural information in new section 5.9 <br> A few other formatting fixes             |
| 4.0.30   | 7 November 2025   | Revised capitalisation                                                                                                                |
| 4.0.29   | 23 October 2025   | Further containerisation clarification <br> Size limits more clear <br> Disclaimer that we do not have a Trello board                 |
| 4.0.28   | 29 September 2025 | sfSampleType fixes                                                                                                                    |
| 4.0.27   | 25 September 2025 | Fix some issues <br> Sample linking is now permitted with compressed samples                                                          |
| 4.0.26   | 25 September 2025 | Default modulators are reformatted <br> Reworked sfSampleType <br> A few more clarifications                                          |
| 4.0.25   | 24 September 2025 | Added guidance on UTF-8 errors <br> Renamed some sfSampleType enums <br> Few other formatting changes                                 |
| 4.0.24   | 23 September 2025 | New feature flags for WAV containers!                                                                                                 |
| 4.0.23   | 21 September 2025 | New member of SFE Team added! <br> Another versioning update <br> Further sample containerisation clarification                       | 
| 4.0.22   | 21 September 2025 | Sample containerisation update <br> Versioning update                                                                                 |
| 4.0.21   | 14 July 2025      | Default modulator update                                                                                                              |
| 4.0.20   | 8 July 2025       | Versioning change                                                                                                                     |
| 4.0.19   | 6 July 2025       | Made it clearer that samples need to be containerised!                                                                                |
| 4.0.18   | 30 June 2025      | Fix typo                                                                                                                              |
| 4.0.17   | 27 June 2025      | RIFF64 headers replaced with simpler RIFS format                                                                                      | 
| 4.0.16   | 27 June 2025      | Added xdta-list subchunk <br> SFE Compression update                                                                                  |
| 4.0.15   | 18 June 2025      | Added DMOD subchunk                                                                                                                   |
| 4.0.14   | 15 June 2025      | Information on compression has been updated <br> sfSampleType information rewritten                                                   |
| 4.0.13   | 21 April 2025     | Clarified that the ISFe chunks are nested inside of ISFe-list                                                                         |
| 4.0.12   | 10 April 2025     | Made changes in SFty values                                                                                                           |
| 4.0.11   | 5 April 2025      | Simplified the isng chunk implementation                                                                                              |
| 4.0.10   | 3 April 2025      | Further restricted the use of non-containerised sdta formats.                                                                         |
| 4.0.9    | 3 April 2025      | Renamed USDP mode to UCC mode <br> Made a few other clarifications about sdta structure modes and stereo samples <br> Fixed dead link |
| 4.0.8    | 1 April 2025      | Removed sm32 and old 8-bit mode <br> 64-bit ifil versions now equal specification versions <br> Added info on sdta structure modes    |
| 4.0.7    | 25 February 2025  | Added names of two new SFE Team members                                                                                               |
| 4.0.6    | 24 February 2025  | SFE Compression no longer supports MP3 as a compression format <br> Clarified difference between wav in container and raw wave data   |
| 4.0.5    | 20 February 2025  | Removed RIFX <br> Limited compatible compression formats <br> Simplified base preset fallback <br> SiliconSFE is now optional         |
| 4.0.4    | 20 February 2025  | Removed a name from special thanks on request                                                                                         |
| 4.0.3    | 9 February 2025   | Improved the base preset fallback implementation <br> Versioning changes                                                              |
| 4.0.2    | 9 February 2025   | Added base preset fallback <br> Renamed "proprietary compression" to "incompatible compression"                                       |
| 4.0.1    | 8 February 2025   | A few clarifications                                                                                                                  |
| 4.0      | 8 February 2025   | Initial release                                                                                                                       |

For draft specification revision history, see [draft revision history.](../draft-revision-history.md)

Changes from the previous version of the specification are highlighted.

## 1.3 History of improvements to the SF format

In 2005, E-mu released SoundFont® 2.04 (specification date September 2002), the last version before abandoning the format. It included 24-bit support, and was designed for the Sound Blaster® X-Fi. Creative Technology Ltd is still around, but their current sound cards (such as the AE-9) do not support the SoundFont® format.

At an unknown time, Kenneth Rundt, the author of SynthFont and a series of products based on it, added some custom features, mostly ported over from the DLS format:

- Always play the sample to the end
- Velocity to volume envelope attack (from DLS)
- Velocity to modulation envelope attack (from DLS)
- Vibrato LFO to volume (from DLS)

Werner Schweer found a way to compress SoundFont® 2 files (with the lossy Vorbis format) around 2010.

- The resulting format was known as SF3.
- It is commonly used by open source programs, such as MuseScore and FluidSynth.
- This is the reason why this format is not called .SF3.
- SFE incorporates the Werner SF3 specification as SFE Compression.

Another development was done by Cognitone, which created an open source program that can losslessly compress SoundFont® 2 files (with FLAC). This was done in 2017.

- This was unofficially called SF4.
- This is intended to be the true version 4, as Cognitone SF4 seems to not have been as widespread as SF3.
- SF4 has also been rejected by FluidSynth as too loosely defined.

Finally, stgiga found out that many programs don't mind RIFF64 files.

- RIFF64 files have a much larger size limit than 32-bit RIFF files.
- It gives us a new horizon to experiment with longer, higher quality samples.
- There are also many other advantages of the RIFF64 format.

The SFE project started in 2020 as a proposal for a successor to legacy SF2.04 by Polyphone developer and SFE team member davy7125. Starting off as "SF3", it was renamed to avoid confusion with Werner SF3, firstly to "SF32 and SF64", then to "SFe" but eventually to **SFE**.

## 1.4 Scope and purpose

This is the specification for the SFE 4.0 file format, based on the famous E-mu Systems® SoundFont® 2.04, and Werner SF3 standards, and is intended to be a source of information on SFE.

- To create files that support SFE, you will need:
    - The SFE format, compatibility, and program specifications
    - E-mu's provided documents for legacy SF2.04 ([SFSPEC24.PDF](https://raw.githubusercontent.com/davy7125/soundfont-standard-v3/117539e5dc2d35d7a6273ba7bc319e7d1e1c9a67/sfspec24.pdf))
- All features from legacy SF2.04 will be retained.

## 1.5 Important differences from the legacy SF specification document

- This is not a standalone document; it refers to `SFSPEC24.PDF`. All relevant information from the Werner SF3 specification is included.
- This document is unofficial and was not created by E-mu. If they want this to be removed, we will remove it, but we hope that this is because they have their own official update to the SF format ready.
- For copyright reasons, we cannot copy information from the original standard, except for what is required to interpret this document and what is allowed under fair use.
- The SFE specification includes many additional requirements over reading the file format.
- Document organisation has been significantly modified to accommodate the intricacies of the SFE format, and to make it easier to read.

## 1.6 Document organisation

The sections in this specification are different to the sections in `SFSPEC24.PDF`, however they roughly correspond to some of these sections:

- Sections 1-3 of this specification to sections 0-1 of `SFSPEC24.PDF`
- Section 4 of this specification to section 2 of `SFSPEC24.PDF`
- Section 5 of this specification to sections 3-7 of `SFSPEC24.PDF`
- Section 6 of this specification to section 8 of `SFSPEC24.PDF`
- Section 7 of this specification to section 9 of `SFSPEC24.PDF`
- Section 8 of this specification to section 10 of `SFSPEC24.PDF`
- Section 9 of this specification to section 11 of `SFSPEC24.PDF`
- Section 12 of this specification to section 12 of `SFSPEC24.PDF`

Section 6 also contains feature flags along with enumerators, section 9 also contains information about the AWE ROM emulator that can be implemented, and sections 10 and 11 include information on compatibility concerns and guidance on writing SFE-compatible software respectively.

Significant differences from the previous version of the specification will be highlighted.