# XXE Infiltration — Network Forensics & IAM Risk Assessment

**Ron Richardson | CyberDefenders training case study | October 5, 2026**

I investigated an XML external entity attack in Wireshark, correlated credential disclosure with a later database connection, and confirmed remote command execution through a web shell. This portfolio translates packet evidence into identity safeguards, remediation priorities and defensible incident conclusions.

[Lab](https://cyberdefenders.org/blueteam-ctf-challenges/xxe-infiltration/) · [My achievement](https://cyberdefenders.org/blueteam-ctf-challenges/achievements/ronrichardsonit/xxe-infiltration/)

## Read by purpose
| Artifact | Purpose |
|---|---|
| [Investigation walkthrough](docs/INVESTIGATION-WRITEUP.md) | Reproducible analysis and evidence interpretation; teaching rather than an answer sheet |
| [Evidence and timeline](docs/EVIDENCE-TIMELINE.md) | Packet/stream references, screenshots and confidence limits |
| [Risk register & remediation plan](docs/RISK-REGISTER-REMEDIATION-PLAN.md) | Likelihood–impact heat map, risk ratings, proposed owners/targets and closure tests |
| [Executive brief](docs/EXECUTIVE-BRIEF.md) | Business impact, decisions and response priorities |

## Start with the management decision
Read the [risk heat map and treatment priorities](docs/RISK-REGISTER-REMEDIATION-PLAN.md#risk-heat-map) for a stakeholder view. The [PNG download](assets/risk-heat-map.png) is suitable for a presentation or LinkedIn attachment.

All seven investigation screenshots appear once in the [evidence gallery](docs/EVIDENCE-TIMELINE.md#screenshot-exhibits), with observations and limits beside each exhibit. The walkthrough explains the investigation method; the risk register tracks treatment and closure requirements.

## Scope
This is a completed simulated lab, not a production incident or healthcare engagement. Screenshots were captured during guided analysis with the official walkthrough as a reference. Findings below are grounded in the supplied screenshots; the original PCAP was not supplied to this workspace for independent reanalysis. No real patient data, root compromise, database theft or performed remediation is claimed.

The screenshots include historical, simulated lab credentials. They are not live credentials; no real credentials are included. Full training answers are not repeated as a question-by-question submission. [Screenshot hashes](evidence/manifest.json) protect the provenance of the files received, not authenticity of the original capture.

## Publication status
Public GitHub repository published October 5, 2026. The investigation write-up was submitted through CyberDefenders’ XXE Infiltration write-up form; the site confirmed successful submission and pending review. Submission is not acceptance or endorsement. The authenticated lab page confirmed 7/7 questions and 100% completion.
