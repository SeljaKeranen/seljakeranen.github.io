---
date: 2026-09-23
written: 2026-10-13
notebook_date: true
authors: [selja]
categories: [Field]
description: Teaching Git alongside agents means explaining where work lives, what has been shared, and how someone can recover from a mistake.
---

# Teaching Git to people who already have work to do

In September, I took a group through some Git basics. Push, pull, main. Small words with quite a lot hiding behind them if you haven't worked with software development tools before. We were there to talk about AI-native projects, and suddenly version control was part of the curriculum too.

<!-- more -->

I wrote about the session in [my September update](https://www.linkedin.com/posts/selja-ker%C3%A4nen-95b4b1150_quite-full-weeks-lately-a-bit-overdue-for-ugcPost-7508455326845857792-IvUZ). People were learning how to work with agents while also learning the environment those agents work in. I appreciate the willingness to do that. There is a lot to take in alongside the work they came to do.

It has made me think about what I would put first in the next session. A tour of the commands is useful eventually, but I would start with one ordinary situation: you and a colleague are changing the same document.

Your copy now contains a new paragraph. The shared version doesn't. The agent says it saved the change. What can your colleague see?

That question gives the vocabulary somewhere to attach. Editing a file, recording a version locally and sharing that version are separate events. The word "saved" can hide all three. Someone can understand the task perfectly and still have the wrong picture of where their work is.

## A small exercise I would use

Give two people copies of a harmless document. Let one person change a heading while the other changes the opening paragraph. Then bring the changes together and inspect what happened. Repeat with both people changing the same sentence.

The second round earns the explanation of a conflict. Until then, "Git will help us work together" sounds pleasantly automatic. Now there is a decision to make about which wording should survive, and the person who understands the document has a useful job even if they don't yet remember the command.

I would also make recovery part of the exercise. Before sharing a change, show the difference from the previous version. After sharing, explain what correcting a shared version means for other people using it. Local experimentation and changing shared history have different consequences. A reassuring "you can always undo it" skips the part a new user needs to understand.

An agent can help with the mechanics, but the person should still be able to say what they intend: keep my colleague's change, remove mine, preserve both, or stop because I don't understand the difference yet. That is a much better place to ask for help from.

There is also a product question here. If a workflow needs a long Git lesson before someone can safely edit a report, perhaps we have handed them too much of the engineering interface. They may need version history and review without needing every operation Git exposes.

For now, repositories are where quite a lot of agent work happens. I want to make that environment less mysterious for the people joining it. An exercise has worked when someone can explain where their change is and what will happen when they share it. Remembering whether the next command is push or pull can come a little later. The names have not exactly done the teaching for us.
