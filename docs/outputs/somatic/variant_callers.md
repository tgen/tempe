---
title: Somatic Variant Callers
nav_order: 8
---

## Somatic Variant Callers

In the Tempe workflow we offer five somatic SNV/INDEL callers. These are:

- Mutect2
- Strelka2
- Octopus
- VarDict
- Lancet

These variant callers have a combination of strengths and weaknesses, and as
such it is recommended to use the output of VcfMerger2. VcfMerger2 homogenizes
many of the FORMAT fields such that variant calls can be merged into a single
line with no loss of information. These are additionally annotated with the
count of variant callers in agreement for a given variant. This count in stored
in INFO/CC and a minimum users should filter this file to CC>=2, and if all
five callers are used, then the CC>=3 is recommended. We're effectively looking
to filter to variants that _most_ of the variant callers agree on.
