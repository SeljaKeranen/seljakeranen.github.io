---
date: 2026-09-08
written: 2026-10-13
notebook_date: true
authors: [selja]
categories: [Craft]
description: An architecture picture can show where an experiment ran, where fixtures stood in for services, and which connections still need testing.
---

# Draw the test onto the architecture

While preparing a prototype explanation in September, I asked for an architecture illustration that showed what we had tested. I wanted to see the steps. Later in the same discussion I was still asking which part of our solution the explanation referred to and how it worked with what we had built.

<!-- more -->

A diagram can make a proposed system look wonderfully settled. Every box has a name. Every arrow reaches its destination. The authentication service is apparently having a much better day than the rest of us.

The difficult part is showing how much of that picture an experiment actually exercised. A component can exist in code without having run in the environment being discussed. An integration can work with a fixture while the live connection remains untested. Both are useful progress. They support different claims.

Here is a small illustrative system, unrelated to any client architecture:

```text
Document -> Extract fields -> Look up reference -> Human review -> Save
```

Suppose we run extraction on ten synthetic documents, use a fixed reference response, and open the result in a local review screen. We have learned something about extraction and the path into that screen. We haven't learned whether the live reference service accepts our credentials, what its timeouts do to the interface, or whether saving preserves the reviewer's changes.

I would put those distinctions on the same picture, using labels as well as colour so nobody has to guess what a shade of green means.

| Part of the example | What ran | What remains open |
| --- | --- | --- |
| Extraction | Ten synthetic documents through the parser | Performance on representative documents |
| Reference lookup | A fixed response supplied by the test | Live access, missing records and timeouts |
| Review screen | Local display of the extracted fields | Whether a person can correct an error and keep the correction |
| Save | Outside this experiment | Persistence and recovery after failure |

None of these invented test results describes my September prototype. The table is the format I would use to make the boundary visible.

An arrow also deserves evidence. Seeing the extractor and review screen work separately doesn't establish that the correct result reaches the correct field. A useful test would carry one recognisable value through the connection and inspect where it ends up. If the value changes along the way, the diagram should help locate the transformation.

I also want to distinguish "we didn't test this" from "we tested it and it failed". The first creates a task to gather evidence; the second gives us evidence to investigate. Combining them into one vague warning loses information that would help decide what to do next.

There is a communication benefit to being this specific. People can see what the prototype already demonstrates without having to interpret either a confident sales pitch or a large disclaimer. The experiment might justify continuing with a design even while leaving several production questions open.

When the next test runs, I would update the labels and link the result beside the relevant connection. The architecture then becomes a place to ask a precise follow-up: we have exercised this path with a fixture; what is the smallest test that would tell us whether the live path behaves the same way?
