---
date: 2026-08-07
authors:
  - selja
categories:
  - Notes
description: >-
  A first post. What I plan to write about here, and why it won't be
  another "AI changes everything" feed.
---

# Starting a blog, mostly to think out loud

At least my feed (maybe it is just me) is full of posts explaining that AI changes everything. I wanted a quieter place to write about the part I actually spend my days on, which is getting these systems to work and then keep working.

<!-- more -->

I build production AI systems for a living. RAG pipelines, document extraction, agents, and a lot of evaluation. The interesting problems almost never show up in the demo. They show up three weeks later, when the real data turns out messier than the sample, the users ask things nobody planned for, and "it feels better" turns out to be a very expensive way to decide whether a change actually helped.

So this is where I want to write about that. A few things I expect to keep coming back to:

- Evals. How you decide what "good" means before you start tuning prompts, and why a golden set built with someone who knows the domain beats a nice-looking demo every time.
- The unglamorous production work. Chunking, document headings (there are more ways to store a heading than you would believe), latency, cost, and the errors you only find once something is live.
- Tools I've actually run. Not the feature list from the announcement, but what happened when I took the thing for a walk and where it stopped being fun.
- Where the hype is ahead of the evidence, and the occasional case where it isn't.

I'll try to keep it concrete and honest, including the parts that didn't work. A lot of this field still feels quite rough round the edges, and I think that is more useful to read about than another victory lap.

That is the plan. What would you actually want to read more about, the eval side or the messy production details?
