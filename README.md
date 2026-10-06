# XXE Infiltration — Network Forensics & IAM Risk Assessment

**Ron Richardson | CyberDefenders training case study | October 5, 2026**

I investigated an XML external entity attack in Wireshark, correlated credential disclosure with a later database connection, and confirmed remote command execution through a web shell. This portfolio translates packet evidence into identity safeguards, remediation priorities and defensible incident conclusions.

[Lab](https://cyberdefenders.org/blueteam-ctf-challenges/xxe-infiltration/) · [My achievement](https://cyberdefenders.org/blueteam-ctf-challenges/achievements/ronrichardsonit/xxe-infiltration/)

## Read by purpose
| Artifact | Purpose |
|---|---|
| [Investigation walkthrough](docs/INVESTIGATION-WRITEUP.md) | Reproducible analysis and evidence interpretation; teaching rather than an answer sheet |
| [Evidence and timeline](docs/EVIDENCE-TIMELINE.md) | Packet/stream references, screenshots and confidence limits |
| [GRC / IAM assessment](docs/GRC-IAM-ASSESSMENT.md) | Proposed control treatments, accountable functions and closure tests |
| [Executive brief](docs/EXECUTIVE-BRIEF.md) | Business impact, decisions and response priorities |

## Evidence preview
![Database connection transitions to TLS](evidence/04-database-tls-connection.png)
A connection to the database follows the disclosure, but encrypted application traffic does not independently prove a successful login.

![Web-shell command result](evidence/07-webshell-command-result.png)
A command request receives a web-service account name, supporting remote execution without establishing administrator access.

## Scope
This is a completed simulated lab, not a production incident or healthcare engagement. Screenshots were captured during guided analysis with the official walkthrough as a reference. Findings below are grounded in the supplied screenshots; the original PCAP was not supplied to this workspace for independent reanalysis. No real patient data, root compromise, database theft or performed remediation is claimed.

The screenshots include historical, simulated lab credentials. They are not live credentials; no real credentials are included. Full training answers are not repeated as a question-by-question submission. [Screenshot hashes](evidence/manifest.json) protect the provenance of the files received, not authenticity of the original capture.

## Publication status
Public GitHub repository published October 5, 2026. The investigation write-up was submitted through CyberDefenders’ XXE Infiltration write-up form; the site confirmed successful submission and pending review. Submission is not acceptance or endorsement. The authenticated lab page confirmed 7/7 questions and 100% completion.
