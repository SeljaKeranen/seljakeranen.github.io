---
description: >-
  The demo proves the happy path exists. Making it hold on every other path is
  the actual job.
hide:
  - navigation
  - toc
---

[&larr;&nbsp;Notes](index.md){ .folio-link }

# From proof of concept to production

A demo is a promise that the happy path exists. Production is the work of keeping
that promise on every other path, on a Tuesday, when the input is nothing like
the three examples in the notebook.

The gap is usually not the model. It is everything around it: the input that
arrives malformed, the step that quietly stops being deterministic, the retrieval
that was fine until the corpus doubled, the cost that was invisible at ten
requests and alarming at ten thousand. None of that shows up in the demo, which
is exactly why the demo felt so easy.

So I treat "it works" as the start of the interesting part, not the end. What
does it do when it is wrong? How do we notice before the user does? What is the
plainest version we can actually maintain, rather than the clever one we will be
afraid to touch in three months? I would rather ship something simple that holds
than something impressive I have to babysit.

Living note. The list of ways a system finds to embarrass you in production is,
in my experience, not finite.
