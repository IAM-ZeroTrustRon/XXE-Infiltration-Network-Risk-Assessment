# GRC / IAM Control Assessment

This is a qualitative training assessment. Proposed risk priorities assume a customer-facing web service and confidential data; actual customer dataset, volume, regulatory applicability and monetary loss are unknown. No HIPAA violation or healthcare breach is asserted. Treatments below are proposals, not performed fixes. Current residual risk is unassessed until controls are implemented and tested.

| Risk | Evidence / control concern | Potential business impact | Priority | Proposed accountable function | Proposed treatment | Closure evidence |
|---|---|---|---|---|---|---|
| R01 | E03: XML parser returns local configuration | Secret disclosure and follow-on access | High | Application engineering | Disable external entity/DTD resolution as supported by parser; block unnecessary file/network access; preserve required functionality | Same authorized synthetic file-read test rejected; legitimate XML processed; code/config review |
| R02 | E03: database secret readable by web process | Unapproved database access if stolen identity remains valid | High | IAM / database owner | Rotate/revoke exposed credentials; managed secret delivery; minimal database permissions; review shared identities | Old secret denied; approved new access works; entitlement review and audited rotation |
| R03 | E01/E04: database reachable from probing source | Expanded attack surface beyond application tier | High | Network / database operations | Restrict DB access to approved tiers/management paths; retain encryption and auditability | Unauthorized source denied; approved app path works; firewall/log review |
| R04 | E07: command endpoint executes as service identity | Server compromise and possible data/availability harm | Critical response priority | Incident response / platform owner | Preserve evidence; isolate affected service; remove unauthorized shell; restore trusted deployment; constrain upload execution and service permissions | Shell unreachable; no execution from upload path; forensic scope reviewed; trusted rebuild validation |
| R05 | E04: PCAP cannot show encrypted authentication | Uncertain identity usage and investigation scope | High | Security operations / DBA | Correlate DB audit/application/endpoint logs with network flow; alert on abnormal source and account use | Test login/outcome visible in protected audit records; timestamps synchronized |

Critical response priority expresses urgent containment for confirmed execution, not a CVSS rating. Database privilege and shell-installation attribution remain unverified. Do not treat network encryption as a defect: it protects traffic; endpoint/server audit records supply accountability without routine bulk decryption.

## Recommended sequence
1. Preserve logs/capture and isolate the compromised service; record responder actions.
2. Revoke/rotate exposed identities and inspect downstream use without assuming it succeeded.
3. Recover a trusted deployment and correct XML/upload controls.
4. Validate network boundaries, identity privileges and monitoring before returning service.
5. Have the business risk owner review unresolved scope and authorize return with documented exceptions.

No production remediation was carried out in this lab write-up. Closure requires authorized retests, operational checks and independent reviewer sign-off.
