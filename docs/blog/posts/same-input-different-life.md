---
date: 2026-09-07
authors: [selja]
categories: [Evals]
description: "Questions from an image-matching experiment: what changes when the same subject arrives through a different input?"
notebook_date: true
written: 2026-10-13
---

# When the same subject becomes a different input

While discussing an image-matching experiment, I asked whether we should run a thousand test cases. A little later, while a run was under way, I asked whether the embeddings were deterministic. Then I wanted to understand what would happen with photographs taken in different places and different lighting.

<!-- more -->

I was asking about the same system, but each question needed different evidence. A larger run could tell us more about the cases it contained. Repeating an identical input could help check whether the processing was repeatable under the same conditions. Neither question, by itself, answered what would happen when the input changed in the way a person using the system would expect it to change.

That last part is easy to leave vague. We say "the same thing" while moving between the same file, the same visible content, and the same subject photographed again. A test needs a more precise meaning, because the computer receives a particular representation of that thing.

## A small example I would use

Take a generated image of a printed card with a fictional product code. No personal information is needed for this example. Suppose the task is to recognise the code and associate the image with the right catalogue record.

Sending the identical image through the pipeline repeatedly would let me inspect repeatability. I would keep the model and processing settings fixed and record whether the output changed. If it did, I would first want to understand that variation before adding more moving parts.

Next, I would create controlled versions of the image: rotate it, reduce the contrast, or crop part of the surrounding background. Each change would need a reason. Rotation could approximate a camera held at an angle. A crop could test whether the system depends on information outside the card. These would be deliberate test inputs, with a known expected record.

Even that would leave a gap. Editing an existing image doesn't reproduce everything involved in taking a new photograph. I would treat those synthetic changes as diagnostic checks and keep a separate set of independently captured inputs for the conditions the application is intended to handle. This is a proposed test plan, not a description of checks I completed in that experiment.

## The result needs to retain the distinction

If I put all of those cases into one total, it becomes harder to see what is working. Hundreds of easy repeated inputs could make a much smaller group of difficult inputs almost invisible in an overall score. I would want the results split by the conditions that were deliberately changed, with the failures available to inspect.

I would also include different cards that look similar. Recognising a changed version of the correct card and avoiding a confident match to the wrong one are both relevant to this task. An empty answer would need to remain visible too, so that a pipeline returning less information couldn't quietly appear more accurate.

The questions I asked during the experiment point to a more useful next step than simply increasing the number of cases. Before asking for a larger run, I would write down what is allowed to vary and what the answer should preserve. Then I could choose the additional inputs that test that expectation, and report the conditions I still hadn't tested.
