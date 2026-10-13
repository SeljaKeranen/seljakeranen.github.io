---
date: 2026-09-15
authors: [selja]
categories: [Systems, Tools]
description: An agent can finish its changes before CI finishes checking them. Readiness needs a fresh result tied to the version being delivered.
notebook_date: true
written: 2026-10-13
---

# When the agent says ready

I asked how to make sure our agents keep responsibility for their work until CI is green. I wanted that expectation to hold across projects, including work handed to another agent. A completion message should let me understand what is actually ready to happen next.

<!-- more -->

There are several reasonable meanings of “finished” in a coding session. The agent has written the change. Its local tests have passed. It has pushed the branch. The remote checks have finished. These events can be minutes apart, and the same cheerful status message can cover any of them.

The distinction starts to matter when another part of the workflow acts on that message. A supervising agent might present a pull request for approval, release its worker or move on to something else. If remote testing is still running, somebody still owns the result that hasn't arrived.

Here is an illustrative sequence. At 10:00, an agent pushes version A. At 10:01, the tests start. At 10:02, it reports that the work is ready. At 10:04, one check fails.

The message at 10:02 cannot establish that version A passed. It could accurately say the change was pushed and testing was under way. Whether that is enough for the next step depends on what we have agreed that step requires.

Now add a small correction. At 10:05, the agent pushes version B. A successful result from version A would still describe the earlier code. Checking the right repository and pull request is insufficient if the evidence belongs to the wrong version.

GitHub's [check-run API](https://docs.github.com/en/rest/checks/runs) makes that connection explicit: a check run carries a commit identifier, a status and a conclusion. Those are useful pieces of evidence for a readiness decision. The agent's summary can explain them, but cannot replace them.

## The cases a readiness check needs to keep apart

Running checks mean the answer is still pending. Failing checks give a concrete problem to investigate. Passing checks provide evidence about the version they tested, within whatever coverage those tests have.

An unavailable result needs its own treatment. If the service cannot be reached, the workflow has failed to establish the answer. Treating that as success would turn a temporary visibility problem into permission to proceed.

There is another quiet case: no checks appear at all. Perhaps the project genuinely has no applicable automated checks, or perhaps the expected workflow never started. A blanket “green” would conceal that difference. The project needs an explicit rule for what evidence is required, including any legitimate exception.

This is the behaviour I was asking for, rather than evidence that every project already enforced it. It also leaves room for different delivery stages. Code can be ready for someone to read while it is still waiting for the checks required before merging.

For that handoff, a useful message would name the version, say that review can begin, and keep the pending test result visible. If the tests then fail, the work remains assigned to someone who can investigate. If another commit arrives, its checks become the relevant ones. The person approving the change can see which decision is available now and which evidence is still missing.
