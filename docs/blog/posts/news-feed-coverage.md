---
date: 2026-09-01
authors: [selja]
categories: [Tools]
description: "A morning AI newspaper also needs to tell me which sources it checked, which failed, and what never made it into the edition."
notebook_date: true
written: 2026-10-13
---

# How many of the sources did we actually get?

I already had a morning newspaper in my own AI platform when I gave the agents a much longer list of sources to follow. Security research, Python, AI engineering, data engineering, and a few people whose work I wanted to keep reading. I wanted a short summary for each section, with the individual posts underneath, and an archive I could return to later.

<!-- more -->

The written version was enough. I specifically said the new sources didn't all need to become part of a podcast.

After the work started, my next question was fairly plain: how many from the list did we manage to get?

I had supplied a reading list, but the visible output was an edition of the newspaper. Looking at the edition alone couldn't tell me how well the list was covered. A long section about security might come from several sources or from one particularly active site. An absent source might have published nothing, failed to load, or never been connected in the first place.

That matters because the missing sources may be exactly why I expanded the list. If the collector handles the convenient feeds and quietly leaves out everything else, I can end up reading a narrower selection than I intended while feeling better informed.

Some of the sources I requested weren't feed-shaped. I asked whether a web agent with read-only access could collect those from the remote machine. That was an option to investigate, with its own access and extraction problems. A source appearing in a configuration file wouldn't tell me whether that approach had worked.

For a pipeline like this, I would want a small report alongside the edition:

| Source status | What I can infer |
| --- | --- |
| Checked, no new items found | The check ran, within the limits of its method. |
| New items collected | There is material available to process. |
| Fetch failed | The pipeline could not retrieve the source. |
| Content retrieved, extraction failed | The page arrived, but usable items did not. |
| Collected, omitted from this edition | Collection worked; selection needs explaining separately. |

I would keep the last successful check and the newest item date beside those statuses. They answer different questions. A blog can be checked successfully today and still have its latest post from last month. A post with today's date doesn't, on its own, prove that today's scheduled run completed.

The archive adds another reason to keep this information. I wanted the material saved in a separate news vault so I could return to it, rather than having each edition disappear into the next morning. When reading an old note, I would want its original source and publication date, along with when it was collected. Otherwise, an old article found today can look like today's development.

This doesn't need to turn the newspaper into an operations console. I still want to read the newspaper. A small coverage view would let me check a missing source when I notice one, and see which gaps need attention before adding another twenty links to the list.
