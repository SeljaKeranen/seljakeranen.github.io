---
date: 2026-09-05
written: 2026-10-13
notebook_date: true
authors: [selja]
categories: [Evals]
description: A difficult translation example needs enough context for a person to solve it and a precise account of what the model got wrong.
---

# Making a translation test that a person could pass

Finding a sentence that makes a strong translation model fail took more thinking than I expected. Making a sentence strange is easy. Keeping it natural enough that a person would understand it, while still exposing a model's limitation, is a more demanding writing exercise.

<!-- more -->

That was part of my experience contributing to the [Last Translation Benchmark](https://arxiv.org/abs/2609.04173v2). It collects human-written, peer-reviewed examples with verification rules for specific translation failures. I contributed a small part, including Kainuu dialect, which I also wrote about in [my original post](https://www.linkedin.com/posts/selja-ker%C3%A4nen-95b4b1150_a-first-version-of-the-last-translation-benchmark-ugcPost-7501954439155638272-Iroj). Apparently this was a practical use for local language knowledge all along.

The part I keep returning to is the verification rule. A reference translation shows one acceptable answer. A rule can describe the meaning that needs to survive even when the words change.

Here is an invented Finnish exchange to make the design concrete, not an example from my benchmark submission or a demonstrated model failure:

> Miltä keitto maistuu?
> Ei hullumpaa. Otan lisää.

One acceptable English version is: "How's the soup? Not bad. I'll have some more." The reply gives mild approval and says the speaker will take more. A verification rule could require both meanings to survive. Translating it as dislike would fail; "Pretty good. I'll have more" could pass even though it uses different words.

If I score the result by resemblance to one English sentence, I might penalise another perfectly good expression of approval. A meaning-specific rule gets closer to the error I want to catch. It still takes someone who understands the source language to establish the intended reading.

The context matters just as much. If only the author knows that the speaker was being ironic, the model is being asked to recover information it never received. A human translator given the same text would have the same problem. Adding difficulty by removing necessary information makes a poor test of understanding.

## What I would write down beside the example

I would keep the intended reading, the evidence for it in the supplied context, and the specific error that would make the answer fail. I would also include an acceptable alternative phrasing if there is a likely disagreement about wording. This gives a reviewer something to challenge beyond whether they happen to prefer my English.

That last part is useful even before running a model. If two competent readers cannot agree on the intended meaning, the example needs attention. Maybe a bit of context is missing. Maybe both readings are valid. Either way, a binary score would hide the disagreement instead of resolving it.

There are limits to what a collection of difficult examples can tell us. Selecting cases because models struggle with them is useful for studying remaining failures. It doesn't estimate how often those failures occur in everyday translation. A model can struggle badly on that collection and still be useful for many ordinary texts. I want both pieces of information, and I would use different samples to get them.

This work gave my language background a very concrete role in evaluation. Someone has to notice the meaning that disappeared, explain why it matters, and turn that observation into a check another person can apply. For the next example, I would spend at least as much time on that explanation as on finding a sentence that breaks the model.
