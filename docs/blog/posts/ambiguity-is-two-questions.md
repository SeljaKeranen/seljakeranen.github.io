---
date: 2026-09-13
authors: [selja]
categories: [Evals]
description: A grant-labelling tool separates a difficult category boundary from an abstract that does not give the reader enough information.
notebook_date: true
written: 2026-10-13
---

# Ambiguity is two questions

A small detail in our grant-labelling tool was the distinction between “borderline” and “couldn't tell from this text”. Both leave a reviewer uncertain, but they leave us with different work to do afterwards.

<!-- more -->

The project was about research funding and ageing. To estimate where money goes, we first needed a defensible way to decide which grants study ageing itself. That sounds manageable until you start reading abstracts. A study can involve older people without studying ageing. Cancer research can also be geroscience. A grant can investigate a mechanism without proposing a treatment.

Our eventual question was “Is this geroscience?”, with yes, no and borderline as the answers. Cancer research had its own checkbox because the two categories can overlap. There was also a separate flag for insufficient information in the text.

The [tool's rubric](https://github.com/SeljaKeranen/hackliferepo/blob/2c47b1d70a1acce0b5a3d56eb638b85fd8e77728/label/taxonomy.py) describes borderline as a case where the text is clear and the grant reads both ways. The reviewer understands what the researchers propose, but the work sits across the boundary we have drawn.

That boundary needs care. Work on an ageing mechanism and cancer can qualify as both geroscience and cancer research under this rubric; overlap alone doesn't make it borderline. The borderline answer is there for cases where the reviewer has enough information but still finds the geroscience definition difficult to apply. Adjudicating those cases would help us understand where the definition needs work.

Now imagine an abstract that says the research will improve health in older populations, with little explanation of how. The category might be perfectly adequate. The source just hasn't given the reviewer enough to apply it. Asking a second model to sound more certain would not add the missing information.

If both cases go into one “uncertain” bucket, the next person looking at the dashboard has to reconstruct why. They might spend time rewriting instructions when they need fuller abstracts, or gathering more documents when the real disagreement concerns the definition.

Keeping the responses separate also changes what we can ask of reviewers. They can tell us about the limits of the text without having to pretend those limits are a scientific judgment about the grant. Their inability to classify something becomes useful evidence about the input.

For the prepared study, we used 40 real grants with full abstracts. Earlier parts of the project had worked from titles and short extracted quotes. Providing fuller text was a concrete improvement to the review material, though a full abstract can still leave a relevant question unanswered.

The batch also leaned toward grants where earlier classifications disagreed. That makes it useful for investigating difficult boundaries. It does not make it a representative sample from which to announce the classifier's overall accuracy.

There were no collected judgments in the [committed study](https://github.com/SeljaKeranen/hackliferepo/blob/2c47b1d70a1acce0b5a3d56eb638b85fd8e77728/label/README.md). The instrument was built, but we had no evidence yet that the distinction would improve agreement or make review faster. What we had was a place to record two different problems, and enough source text for researchers to begin telling us which one they were encountering.
