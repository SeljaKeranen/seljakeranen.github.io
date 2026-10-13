---
date: 2026-10-13
authors: [selja]
categories: [Notes]
description: Reading Stephen Witt on Nvidia, with a kitchen explanation of GPUs and a question about how much of a successful story anyone could have planned.
---

# The Thinking Machine, and making room for luck

I enjoyed getting a history of GPUs alongside the portrait of Jensen Huang in Stephen Witt's *The Thinking Machine*. The technical history made the company story more interesting for me. It also left me thinking about how accidents and luck shape what we eventually describe as someone's career, or a company's strategy.

<!-- more -->

With Nvidia, we already know enough of the ending to make the earlier decisions look rather obvious. Reading about how it got there, I kept coming back to what people could actually have known when they made those decisions. It must be lovely to write a strategy with the next twenty years available for reference.

## A short detour through the chips

For anyone who doesn't spend their days thinking about processors: a CPU, or central processing unit, is the computer's versatile general-purpose processor. A GPU, or graphics processing unit, is especially good at doing large amounts of similar calculation in parallel.

Imagine a restaurant kitchen handling a changing set of orders. Someone has to follow the recipes, deal with substitutions and decide what happens next. That is the kind of varied work a CPU handles well. Now imagine preparing thousands of portions of the same dish, with enough people and workstations to divide up the repetitive preparation. That is closer to the work a GPU is built for. Sending all those people to supervise one boiling egg would be less helpful.

The comparison has limits. Modern CPUs also do work in parallel, and a GPU usually works alongside a CPU. The advantage depends on having work that can use all that parallel capacity. [Nvidia's programming guide explains the distinction](https://docs.nvidia.com/cuda/archive/13.0.3/cuda-c-programming-guide/index.html#introduction).

Graphics provided plenty of that work. A game has to calculate how objects and light should appear, repeatedly and quickly enough to keep the scene moving. Nvidia, [founded in 1993](https://www.nvidia.com/en-us/about-nvidia/corporate-timeline/), built its business around increasingly demanding graphics. The calculations mattered long before anyone was asking a chatbot to rewrite an email.

Nvidia [introduced CUDA in November 2006](https://docs.nvidia.com/cuda/archive/13.0.3/cuda-c-programming-guide/index.html#introduction), giving developers a programming platform for using its GPUs beyond graphics. Training a neural network also involves large batches of arithmetic that can be divided up and calculated in parallel. The chip doesn't need to know whether those numbers describe light falling on a game character or part of a model learning to recognise an image.

In 2012, Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton described training the image-recognition network now known as AlexNet on two Nvidia GTX 580 GPUs. Training took five to six days. Their [original paper](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) is a useful reminder that the model design and training data mattered too. The chips were part of something several groups of people were figuring out.

## What could they have known at the time?

Witt says in an [interview about the book](https://www.ykeith.com/p/witt) that AI was an application Nvidia had not originally anticipated. Huang wanted the hardware to have more uses, without knowing this particular one would become so important.

CUDA gave people outside Nvidia a way to try things with the hardware. The eventual use could come from someone working on a problem the company hadn't set out to solve. There was a practical route for that surprise to become useful.

The portrait of Huang complicates this further. Witt describes someone willing to sustain an uncertain investment for years, but also to abandon projects he judged had failed. He describes a demanding workplace, including shouting at employees, alongside a willingness to retain people whose initiatives didn't work. I can admire the patience behind an investment and still wonder what working under that pressure costs people.

Other people's choices mattered to its survival, too. In his [2023 commencement address](https://blogs.nvidia.com/blog/huang-ntu-commencement/), Huang recalled an early console project that put Nvidia at risk of bankruptcy, and help from Sega's leadership that allowed it to continue. It is his retrospective account, but even in that telling, determination alone would not have paid the bills.

This is where Christian Busch's work on serendipity helped me connect the technical history with the question about luck. Busch is an [associate professor at USC Marshall](https://www.marshall.usc.edu/personnel/christian-busch) and the author of *The Serendipity Mindset*. His [research on serendipity](https://onlinelibrary.wiley.com/doi/full/10.1111/joms.12890) considers how people encounter unexpected things, recognise a possible use for them and act on it. There is some agency in that process, even though the particular outcome remains unpredictable.

I read the CUDA story through that lens. Building a tool that researchers could use for their own questions increased the possible encounters between Nvidia's hardware and work happening elsewhere. Recognising what was happening, and responding to it, still required judgment.

It would be a fairly cruel jump from there to saying everyone makes their own luck. Time, money and access to people affect which opportunities we can pursue, and how many unsuccessful attempts we can afford. Busch [makes that distinction himself](https://ssir.org/books/excerpts/entry/cultivating_serendipity). His academic paper also warns about hindsight and survivor bias. We get to read the biography of the company that made it.

For my own work, this leaves me thinking about what I make available for other people to try. If I build something around a problem I understand, can someone with a different problem use it, question it, or show me where my assumptions stop working? I may have a fairly clear idea of what I am building and still have very little idea who will find the most interesting use for it.
