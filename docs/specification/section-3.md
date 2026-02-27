# Section 3: Versioning and updates

## 3.1 Specification Versioning

Final specifications have version numbers in the format x.y.z, where x, y and z are numbers:

- x is incremented when a change in the SFE format is made in a way that makes the resulting files incompatible with the previous version.
- y is incremented when there are new features added to the SFE format.
- SFE should not skip "y" versions.
- z is incremented when there are small changes made to the specification.
- Release candidates have very similar version numbers to final specifications, but include "rc" between y and z.
- An example of a final specification version would be 4.0.22.

<img title="Figure 1" src="../../figures/figure_1.png" alt="SFE 4.x versions are compatible with legacy players but with reduced sound quality. No changes are made to actual file structure in 'L' versions. Later 'y' versions are compatible with earlier players but with reduced sound quality.">

Figure 1: SFE 4.x versions are compatible with legacy players but with reduced sound quality. No changes are made to actual file structure in "L" versions. Later "y" versions are compatible with earlier players but with reduced sound quality.

<img title="Figure 2" src="../../figures/figure_2.png" alt="SFE 'x' versions are not compatible with each other, but can be converted, resulting in reduced sound quality. Compatibility layers can be added to newer players to use older banks. It is also possible to upgrade banks to newer versions.">

Figure 2: SFE "x" versions are not compatible with each other, but can be converted, resulting in reduced sound quality. Compatibility layers can be added to newer players to use older banks. It is also possible to upgrade banks to newer versions.

Draft specification milestones have version numbers in the format `x.ydz.a`, where `x, y, z` and `a` are numbers and d and u are the letter "d". In this case, the versioning works similarly to a final specification, but with these changes:

- `z` is incremented when the draft undergoes a larger change, or large updates are made to the software.
- `a` is incremented when there are small changes, but only when pointed out by others. The first version will not include a or a "." in its version number.
- An example of a draft specification version would be 4.1d1.

During the development of specifications, version numbers will be in the format `x.y.aaaabbccL`, where x, y, z, a, b and c are numbers, and L is a letter. The versioning is similar to final specifications and milestone drafts, but `aaaabbcc` is the day in which the specification was updated, and L is incremented when updated.

Only final specifications are included in the changelog in section 1.2.

<img title="Figure 3" src="../../figures/figure_3.png" alt="The SFE development process.">

Figure 3: The SFE development process.

## 3.2 Future improvements

SFE is designed for future improvements.

- These will be done in a more liberal way than the conservative manner of the SoundFont® 2 updates that E-mu has done.
- SFE is not affected by limitations created by the EMU8000 sound processor and Sound Blaster® cards, and therefore will have more improvements.
- Additionally, starting from SFE 5, SFE won't be affected by limitations created by legacy SF players.
- To avoid over-stress of developers of the SFE Team, as well as SFE instrument banks, features will be spread out across versions, and similar features will arrive at the same time.

Here are a few things that are planned for SFE:

- Polyphone 3 will be the first program that supports SFE. It will use it by default with legacy SF being an option. (Polyphone 2.5.x seems to be planned as an LTS release for legacy SF.)
- Developers of Bassmidi-based programs have already provided feedback, and negotiations with more SF program developers such as FluidSynth will start soon.
- For SFE 4.1, support for the `PNMM` sub-chunk will also be included, as well as Markdown support for `ICMT`.
- A MIDI lyrics specification for MIDI players, along with Spessasus/Falcosoft RMIDI support, will become available in SFE 4.2.
- We will negotiate with the Synthfont author Kenneth Rundt about getting the Synthfont Custom Features added for SFE 4.2. Care has been taken to ensure that SFE parameter usage does not conflict with SFCF.

## 3.3 Long term support of SFE 4

SFE 4 is a "long-term support" version, and will get feature updates along with later versions such as SFE 5. While this is the case, some features are structurally incompatible with legacy SF2.04, and will not be available in SFE 4.

If an earlier major version of SFE is the main version used for a longer time than expected, then it can be declared as another LTS version. Such a LTS version will be declared in this section.
