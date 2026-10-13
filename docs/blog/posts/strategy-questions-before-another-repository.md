---
date: 2026-10-11
written: 2026-10-13
notebook_date: true
authors: [selja]
categories: [Notes]
description: Reading about AI and strategy from an engineering background, with a worked example of the questions I would want an experienced strategist to challenge.
---

# A few strategy questions before opening another repository

I've been getting more interested in strategy. Coming from AI and data, I keep connecting the reading to what is happening in software development: more of the work goes into deciding what to ask for, supplying useful context and figuring out whether the result deserves to be used.

<!-- more -->

Felipe A. Csaszar's article on [AI and strategic decision-making](https://csaszar.info/research/2026-hbr-ai-sdm) gave me more to think about here. His argument starts with the limits of people's attention, memory and processing capacity. Those limits shape which alternatives get explored and how a complicated business gets represented. AI could change the capacity of the whole decision process by helping explore more options, maintain richer representations and organise challenge around proposals.

He also places potential advantage in the company-specific data and working processes built around models. Access to a model is widely available; the accumulated knowledge and repeated learning around a decision are harder to reproduce. That is an argument about how a company works, with people still accountable for the choices.

## One decision, followed a little further

Imagine a small software company considering a new customer segment. This is a hypothetical exercise, not a project result.

An agent could gather possible segments and produce a comparison. Before building that, I would want to understand what makes two options meaningfully different. A list of twenty industry labels might conceal the same route to market twenty times. Selling to a new buyer through an existing customer relationship could be a more substantial alternative than simply changing the industry name.

Then there is the information used to compare them. Support tickets can tell us where existing customers struggle, but they say much less about people who never bought the product. A model with excellent access to internal documents may reproduce that blind spot very efficiently. I would want the missing evidence visible beside the recommendation.

The evaluation also needs a decision attached to it. Suppose the comparison favours a segment because of its estimated willingness to pay. What would the team do with that claim? Interview potential buyers, run a limited sales experiment, or commit to a product change? Those actions have different costs and give different feedback. I would be uncomfortable using the same confidence score to justify all of them.

I can help trace a claim back to its source and design a workflow that records assumptions. The questions I want to understand better concern which assumptions are consequential and when waiting for more evidence is itself the expensive choice.

Giving another agent the job of critic could help bring objections into the discussion. But I would check whether it changes the decision in a useful way. A convincing criticism of a proposal can be as poorly grounded as the proposal. Agreement between two agents would give me very little reassurance if both rely on the same missing customer evidence.

My instinct is already to think about the workflow we could build. Before doing that, I would like to work through a decision with someone who can explain why they rejected an apparently reasonable option. That explanation would tell me more about what the system needs to support than another list of possible AI use cases.
