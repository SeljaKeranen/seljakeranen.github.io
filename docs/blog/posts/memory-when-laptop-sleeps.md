---
date: 2026-08-30
authors: [selja]
categories: [Systems]
description: "Designing work state for remote agents started with a fairly ordinary question: what happens when my laptop sleeps?"
notebook_date: true
written: 2026-10-13
---

# Where does the work live when my laptop sleeps?

I wanted to be able to say an idea aloud, work through the unclear parts, and leave a useful ticket for an agent to pick up. Some work would happen on my laptop, some on a remote machine. My own platform would give me a view of what was going on without requiring me to follow every individual chat.

<!-- more -->

Quite quickly, that became a conversation about where the tickets should live. Could a local database hold them? Could the same place also hold my Obsidian second brain? The interface could make all of this look quite tidy, but somewhere underneath it we needed an answer about which copy counted.

Then I asked what happens when the MacBook is asleep and only the remote agents are working.

That was a useful constraint to put into the design. If a remote agent needs the laptop to claim a ticket or record a result, closing the laptop interrupts the workflow even though the agent itself is still running. Moving the agent process elsewhere only solves part of the problem.

The proposal I accepted was to give live ticket state a home on the remote host. My laptop would be an interface to it. This was a design decision in that discussion, with the implementation and recovery checks still to prove.

There was another distinction I wanted to keep understandable: bringing things into one interface doesn't require giving them identical storage rules. A note that I edit in Obsidian and a ticket that an agent is currently claiming have different needs.

In the proposed design, the notes would remain ordinary Markdown. A search index could help the platform find and connect them, but deleting that index should leave the notes intact. Live ticket state would have its own authority: who has claimed the work, what stage it is at, and where the supporting evidence is. Losing that state and losing a rebuildable index would be very different incidents.

For SQLite, there is also a practical detail here. Having a database on the remote machine doesn't mean opening its live file from every other machine over a shared filesystem. [SQLite's own guidance](https://sqlite.org/useovernet.html) describes the reliability problems that can introduce. One arrangement it documents keeps reads and writes on the database machine and lets remote clients send requests to a process there.

That still leaves decisions to make. An agent might claim work and disappear before finishing it. A request might succeed while its response is lost. On waking the laptop, I would want to see what happened while I was away, including work that stopped halfway through. None of those cases becomes resolved just because the database has a server address.

For this design, I would start verification with a small ticket and the laptop disconnected. Let a remote worker claim it, interrupt the worker, then reconnect and inspect the recorded state. Could another worker safely continue? Could I tell the difference between a completed action and an intention to do it? Those checks would give me something more useful than a dashboard that happens to load while both machines are awake.
