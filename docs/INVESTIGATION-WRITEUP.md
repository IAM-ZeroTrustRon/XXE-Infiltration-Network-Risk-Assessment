# XXE Infiltration: Following the Evidence, Not the Answer Sheet

**Author: Ron Richardson**  
**Platform:** [CyberDefenders](https://cyberdefenders.org/) — [XXE Infiltration](https://cyberdefenders.org/blueteam-ctf-challenges/xxe-infiltration/)

## Objective and preparation
Investigate unusual XML submissions, determine what data the server disclosed, and assess subsequent access. Open the provided capture in Wireshark; work on the saved file, not a live capture interface. Set the time display to UTC date/time for consistent correlation. Preserve packet and TCP-stream identifiers alongside screenshots.

I used the official walkthrough as a reference and checked its claims against packet responses. This is a guided investigation, not a claim of an unaided solve. This article teaches the method without listing challenge answers. Exact supporting artifacts and confidence limits are maintained in the separate evidence record.

## 1. Reconnaissance: identify server replies
Apply:
```
tcp.flags.syn == 1 && tcp.flags.ack == 1
```
Identify replies originating from the suspected victim and compare TCP source ports. SYN-ACK means a port accepted the initial connection request. It also appears in ordinary traffic: rapid probing across many ports and connection behavior provide scanning context. Do not count the client's ephemeral destination port as an exposed server service.

## 2. Locate XML upload attempts
Apply:
```
http.request.method == "POST"
```
Inspect upload requests in chronological order. Right-click a relevant request and follow its HTTP stream. Read multipart filenames, XML declarations, external entity definitions and the entity's use in the body. A request asking the parser to read a local file establishes intent. An empty HTTP response does not show that the file was actually disclosed.

The first inspected malicious upload returned an empty response. I recorded it as an attempt rather than an achieved file read.

## 3. Confirm configuration disclosure
Inspect later XML uploads and compare request targets with server replies. Prefer Follow HTTP Stream for gzip-compressed responses: reading raw compressed TCP bytes can hide the content. Scroll below the response headers and check whether returned data contains configuration code rather than merely echoing the request.

The later response exposed database connection settings. Crucially, the database-name field differed from the database-user field. I distinguished them instead of repeating the reference walkthrough's account label. This confirmed a credential disclosure, not yet successful database access.

## 4. Correlate database traffic
Apply:
```
mysql.login_request
```
Compare the earliest post-disclosure connection with the disclosure time. Follow that connection using:
```
tcp.stream == STREAM_NUMBER
```
Replace STREAM_NUMBER with the observed stream ID. Inspect greeting, SSL negotiation and subsequent protocols. A short packet labeled Login Request may actually be a request to switch to TLS, explaining an empty username. In this connection TLS 1.3 protected the application exchange. Without decrypted content or database audit logs, I cannot establish the authenticated identity, login outcome or queries executed.

## 5. Investigate the suspected shell
Inspect the final XML upload and its response. A remote PHP reference and a Base64-read wrapper are not proof that a file was written to disk or executed. Here the reply contained only a minimal XML declaration.

Next search requests for the referenced PHP basename, using:
```
http.request.uri contains "OBSERVED_FILENAME"
```
Replace OBSERVED_FILENAME with the basename found in the XML. Separate earlier probing from later command-bearing requests to an upload directory. Follow a command request and read the actual server response.

A request asking which account was executing returned the web-service account. That request/response pair supports an operational web shell and remote command execution. It does not reveal how the shell reached disk or prove privileged access. The XXE-to-shell causal step remains a hypothesis requiring server filesystem, upload and application logs.

## Conclusions and next evidence
Confirmed: malicious XML requests, configuration/credential disclosure and web-shell command execution. Observed: a subsequent encrypted database connection. Unconfirmed: successful database authentication, data extraction, root access and the exact shell installation method.

Request application logs, database audit records, server filesystem metadata and endpoint telemetry to resolve those gaps. The key lesson is that chronology suggests a chain, but each causal or impact claim needs its own evidence.

## References and submission context
- [CyberDefenders lab](https://cyberdefenders.org/blueteam-ctf-challenges/xxe-infiltration/)
- [Submission guidance](https://help.cyberdefenders.org/en/articles/8938030-submit-cyberrange-lab-walkthroughs)
- [Evidence record](EVIDENCE-TIMELINE.md)

CyberDefenders lists the lab as retired at the time of preparation. No original PCAP, official walkthrough copy or extracted malicious executable is redistributed.
