---
hide:
  - navigation
  - toc
---

# Code of conduct

### Updated 28 June 2026

Our code of conduct is very simple, but please read it before contributing.

## Rules

### Be respectful

**Please be respectful to other people and other projects.** Don't harass other projects because of disagreements, or for any other reason. Hate speech, racism, homophobia, transphobia, etc. isn't tolerated. 

If you contribute to other projects, you must follow their terms of service and code of conduct.

### Work constructively

**When working with other projects, please work constructively.** Constructive criticism, for example about features, is allowed and encouraged. However, do not make unconstructive and derogatory comments.

- *Permitted: We should work together with this project to include SFE support.*
- *Case-by-case: In my opinion, this project doesn't support SFE properly, so let's discuss this with their maintainers.*
- *Not permitted: This project sucks because it doesn't have SFE.*

### No objectionable content

**Don't do anything illegal, inappropriate, or otherwise objectionable.** You must never post or create anything that isn't safe for work, life, and/or violates copyrights and/or other laws.

### We aren't affiliated with Creative

**We aren't affiliated with Creative Technology Ltd.** Therefore, please don't claim that we are, and definitely do not use Creative logos.

### AI Use Policy

**Use of generative AI (for example GitHub Copilot, OpenAI Codex, Google Antigravity, Claude Code, Cursor etc.) is usually acceptable only to understand how something works, and for research.** However, you should not use AI tools to generate publicly facing text, images, music or video.

If you will use AI tools to help you with programming, you must check your code, you must understand what your code does and you must take responsibility. If you blindly submit a pull request that is obviously written by an AI tool without human oversight, then expect us to not accept it. We will review output quality on a case-by-case basis, but you should not be surprised if we are critical of your AI-generated code.

- *Permitted: I don't understand this person's suggestion, so I will use AI to get the key points.*
- *Case-by-case: To implement this SFE feature into the reference implementation, I will use AI to help me write the code.*
- *Not permitted: Let's use AI to write release notes for the next version of SFE to save time, generating the images of diagrams for us.*

### No feature removal

**To remove a feature from the specification, a suitable reason (for example safety or security) must be provided.** Feature removal without considering these points is in most cases considered vandalism. Redundancy is not considered a valid reason for the purpose of this rule.

Deprecation is permitted, and it is possible to remove features that have been superseded if the usage of the feature can cleanly be converted to a new feature. This allowance is only valid between major versions. If the feature cannot be cleanly converted to a new version, it should not be removed.

- *Permitted: We are removing this feature because it cannot be implemented safely.*
- *Case-by-case: Nobody used this feature, and we've developed a better alternative, so it should be safe to remove this exact method of access in the next major release.*
- *Not permitted: We are removing this feature because there are multiple ways to achieve the same behaviour.*

### No unsolicited sample requests

**Don't make unsolicited requests for audio samples.** SFE for the most part does not manage audio samples (except as may be required by our obligation to provide a reference implementation for the SFE format), and if you can't find samples that meet your requirements, we probably can't either.

- *Permitted: Let's talk to a soundfont developer about implementing SFE.*
- *Case-by-case: It might be useful for us to have accessible samples to test this particular feature planned for the next version of SFE, but it's not necessarily needed.*
- *Not permitted: Please contribute samples to my incomplete SFE project so I can release it.*

## Guidelines

These guidelines are not required to be followed, but are included in the code of conduct for reference, and you should definitely follow them anyway. 

Before 20 December 2025, these points were included in the SFE license, but have been moved here for clarity.

### Share your modifications to the spec

**While not required, please share your modifications to the SFE specification under the SFE license.** This ensures that everyone who implements the SFE specification can use them. 

By doing this, we avoid a feature issues similar to what happened with "ARIA-specific SFZ extensions" and "DLS 2+/2++ specific features" in other formats.

### Link to the latest version of the spec

**When redistributing parts of the SFE specification, please keep the link to the latest version of the specification intact.** While our specification can be freely distributed with any modification made, keeping the link to the latest version of the specification ensures that SFE program developers are provided with the latest updates on features and compatibility, which is helpful for everyone.

### Right to repair

**If you incorporate SFE in hardware, please respect the right to repair.** For any hardware that incorporates the SFE format, we strongly recommend that you provide suitable repair information and that you do not place any arbitrary restrictions on third-party repair of your hardware.

## Failure to follow these rules

If you don't follow these rules, you may not be able to continue contributing to the project. In all but the most severe cases, you will be given at least one warning before being blocked from the project or organisation.