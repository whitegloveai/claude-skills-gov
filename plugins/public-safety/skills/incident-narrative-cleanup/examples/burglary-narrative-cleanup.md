# Worked Example: Burglary Narrative Cleanup — Cedar Ridge PD

This example shows a fictional Cedar Ridge Police Department burglary case. The author is Officer J. Holloway (Badge 4421). The case was a forced-entry burglary of a habitation reported on the morning of March 14, 2026.

The example shows three artifacts: the raw narrative as the officer drafted it, the cleaned narrative produced by this skill, and the reviewer notes flagging items for the officer to resolve before submitting to RMS.

---

## Raw Narrative (as written by Officer Holloway)

> On 03/14/26 at approx 0738 hrs I was dispatched to 412 W Pecan St in reference to a burglary of habitation just occured. RP was the homeowner Maria Salinas DOB 04/22/1981. I arrived on scene at 0742. Salinas was outside on the front porch she was visibly upset. She stated she got home from a night shift at the hospital around 0710 and noticed the side gate was open and the back door was kicked in. She did not enter the house she called 911. I made contact with her she said nobody was inside as far as she knew but the dog wasnt barking which was unusual.
>
> I cleared the residence with Officer Reyes who arrived at approx 0746. No suspects inside. The back door (north side) had been forced open the door frame was splintered near the deadbolt. A bedroom dresser drawer was on the floor jewelry box open. Living room TV mount was empty but the TV was still on the floor near the back door appeared the suspect was interupted maybe.
>
> Salinas walked through the house with me. She said missing items were her wedding ring (gold band w/ small diamond), a Glock 19 9mm her husband owned ser# unknown to her but she would call him, approx $200 cash from the kitchen drawer.
>
> I photographed the door, the dresser, and the empty TV mount. I collected a partial shoe print from the kitchen floor on a piece of cardboard. CSI not available this morning so I packaged the cardboard evidence bag #2025-0314-01 chain of custody started.
>
> Spoke to neighbor across the street Mr. Henry Doan DOB 11/02/1955. He stated he saw a dark blue or black SUV maybe a Tahoe parked in front of Salinas's house around 0640 this morning when he was walking his dog. He did not see anyone get in or out of the vehicle. It was gone when he came back inside.
>
> Husband Carlos Salinas called back at 0822 confirmed Glock 19 ser# AGB4421US registered to him. Entered into NCIC by dispatch as stolen at 0831.
>
> Cleared scene at 0905. Case forwarded to CID. No suspect at this time.

---

## Cleaned Narrative (produced by this skill)

```
CLEANED NARRATIVE — Case 2026-03-14-077 — Burglary of Habitation
Author: Ofc. J. Holloway, Badge 4421
Reviewing structure (not facts): AI-assisted cleanup, 03/14/2026

INITIAL RESPONSE
On 03/14/2026 at approximately 0738, I was dispatched to 412 W. Pecan St.
in reference to a burglary of a habitation just occurred. I arrived on
scene at 0742. Officer Reyes arrived at approximately 0746. The reporting
party was the homeowner, Salinas, Maria (DOB 04/22/1981).

OBSERVATIONS
Salinas was on the front porch and visibly upset. The side gate to the
north was open. The back door on the north side of the residence had been
forced open. The door frame was splintered near the deadbolt. In the
master bedroom, a dresser drawer was on the floor and the jewelry box was
open. In the living room, the TV mount was empty and the television was
on the floor near the back door.

ACTIONS TAKEN
1. I made contact with Salinas on the front porch. She declined to re-enter
   the residence and stated she had called 911 from outside.
2. With Officer Reyes, I cleared the residence. No suspect was located.
3. I photographed the back door, the dresser, and the TV mount.
4. I collected a partial shoe print from the kitchen floor by placing the
   cardboard substrate in evidence bag 2025-0314-01. Chain of custody
   started at 0810.
5. I walked through the residence with Salinas to identify missing items.
6. I contacted neighbor Doan, Henry (DOB 11/02/1955), across the street.
7. I cleared the scene at 0905. Case forwarded to CID.

STATEMENTS
Salinas, Maria (RP / homeowner)
Salinas returned home from a night shift at the hospital at approximately
0710. She noticed the side gate was open and the back door was kicked in.
She did not enter the residence. She noted the family dog was not barking,
which she described as unusual. She identified missing items as her
wedding ring (gold band with a small diamond), a Glock 19 9mm belonging
to her husband (serial unknown to her at the time of statement), and
approximately $200 cash from a kitchen drawer.

Doan, Henry (neighbor)
Doan stated he saw a dark blue or black SUV, possibly a Tahoe, parked in
front of the Salinas residence at approximately 0640 while he was walking
his dog. He did not see anyone enter or exit the vehicle. The vehicle was
gone when he returned inside.

Salinas, Carlos (husband, by phone at 0822)
Salinas, C. confirmed the Glock 19 serial AGB4421US is registered to him.

EVIDENCE COLLECTED
- Item 1: Partial shoe print on cardboard substrate from kitchen floor.
  Evidence bag 2025-0314-01. Chain of custody started 0810.
- Photographs of point of entry, dresser, TV mount.

DISPOSITION
Glock 19 serial AGB4421US entered into NCIC as stolen at 0831 by dispatch.
Scene cleared at 0905. Case forwarded to CID. No suspect at this time.
```

---

## Reviewer Notes (NOT for submission)

**Internal contradictions:**

- The author's badge number is recorded as 4421, and the husband's Glock serial number includes the string "AGB4421US." This is almost certainly coincidence, but a defense attorney could ask about it on the stand. Worth noting in your supplemental that you flagged the coincidence at intake.

- Evidence bag is labeled "2025-0314-01" but the case date is 03/14/2026. Likely a typo on the bag or in the narrative. Verify the physical bag label matches the case year before submission; correct whichever is wrong.

**Possible missing checklist items (Cedar Ridge PD burglary template):**

- Weather and lighting conditions on arrival not noted.
- Tool marks on the door frame not described (consistent with a kick versus a pry tool); CID will want to know.
- No mention of attempted lift of the partial print from the kitchen floor versus collecting the substrate; if CSI policy permits in-place lift, document why the substrate was collected instead.
- Statement from Salinas, C. was by phone — confirm if a written or recorded statement will be taken later, and reference that follow-up here.

**Phrasing that could weaken testimony:**

- The original phrase "appeared the suspect was interupted maybe" was removed from the cleaned narrative because it is speculative and conclusory. If you want a similar inference in the report, restate it observationally: "The television had been removed from the wall mount but remained on the floor near the point of egress." Consider whether to include it at all; the CID detective can draw the inference.

**Spelling and grammar corrections applied:**

- "occured" corrected to "occurred."
- "interupted" corrected to "interrupted" (and the speculative sentence removed; see above).
- "wasnt" corrected to "was not."
- "Salinas's" used for possessive (consistent with Cedar Ridge PD style guide).
- Times standardized to 24-hour format.
- Names standardized to Last, First with DOB on first reference.

AI-assisted cleanup, reviewed by Ofc. J. Holloway, Badge 4421.
