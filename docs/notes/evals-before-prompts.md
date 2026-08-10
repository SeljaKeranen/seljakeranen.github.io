---
description: >-
  Define what "good" means, with the people who know the domain, before you
  touch a model.
hide:
  - navigation
  - toc
---

[&larr;&nbsp;Notes](index.md){ .folio-link }

# Evals before prompts

The first thing I want on a new project is a small, honest set of examples where
we have agreed what a good answer looks like, built with the people who actually
know the domain. The prompt and the model come later. Once that golden set
exists, most of the loud early arguments get quiet. You can just run them.

If you are choosing a vector database before you have agreed on the success
metric, the hard decisions are still ahead of you, and you have spent your first
week on the easy ones. I would rather start from the thing that is genuinely
uncertain, which is almost never the infrastructure.

A golden set does two more things people underrate. It gives the domain experts a
place to put their judgment that is not a meeting, and it turns "the model feels
worse today" into a number you can actually look at. When the eval and the expert
disagree, that disagreement is the most useful artifact on the project. Usually
the spec was wrong, not the person.

This is a living note. I expect to keep adding the parts I only learn by getting
them wrong.
