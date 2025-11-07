# Section 7: Parameters and synthesis model

## 7.1 About the synthesis model

Currently, the synthesis model of SFE 4.0 is identical to that of legacy SF 2.04. However, more changes are coming soon.

When the synthesis model is changed, there will be a detailed description of everything here.

## 7.2 MIDI functions

### 7.2.1 MIDI bank select

Control Change #32 (Bank Select LSB) has been modified to use the `byBankLSB` value.

### 7.2.2 Other MIDI functions

All other MIDI functions are unchanged from legacy SF2.04.

## 7.3 Parameter units, generators, modulators and NRPNs

All of these are the same as legacy SF2.04.

## 7.4 On implementation accuracy

E-mu was very lax when it came to accuracy of legacy SF implementations. This was because of the limitations of computers and legacy sound cards that the legacy SF spec and its implementations were initially designed to run on. While this was the only way that legacy SF could gain the popularity that it did with software implementations, this meant that bank developers often had to declare the program that their file was intended to be used with. This hampered interoperability with different SF players, including those that may have been embedded into musical instruments.

Because today's computers are much faster, and legacy sound cards are no longer in widespread use, the requirements for implementation accuracy in SFE are far stricter. All SFE players are required to recognise the `flag` sub-chunk (section 5.12.2) and warn the user if there is a mismatch between feature flags in the bank and the program's support.

While the `flag` sub-chunk will be useful to alert users about incompatible programs, program developers should make an effort to ensure that their program is 100% compatible.