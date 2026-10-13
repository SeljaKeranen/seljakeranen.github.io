---
date: 2026-09-12
authors: [selja]
categories: [Evals, Systems]
description: Collecting every matching grant removes one sampling problem while leaving the search terms to decide what the funding ratio can mean.
notebook_date: true
written: 2026-10-13
---

# What belongs underneath the funding ratio

During our longevity hackathon, I asked for an outside check on the amount of research we had fetched. We had a dataset and a pipeline, but I wasn't comfortable treating those as evidence that we had all the research needed for the claim.

<!-- more -->

We were working towards a comparison of funding for the biology of ageing and funding for its consequences. The appealing output was a simple percentage, something a person could understand without reading the whole method first. The denominator was still doing a lot of unresolved work.

Start with the collection step. We searched grant sources using terms related to ageing. If a source returned more records than we kept, removing that cap would improve coverage of the query. Fetching every result would let us stop worrying about which matching records happened to fit inside the cap.

It would still leave the query deciding what could enter the dataset.

A relevant study might describe a disease, a biological mechanism or a care intervention without using the ageing vocabulary in our search. Fetching the same query more thoroughly would never find it. The [pipeline documentation](https://github.com/SeljaKeranen/hackliferepo/blob/2c47b1d70a1acce0b5a3d56eb638b85fd8e77728/ratio/README.md) calls the resulting collection a census of the search nets. That is the scope of its completeness.

There are several decisions between a public funding database and a percentage on a map. We choose the source, choose the search terms, retrieve records, decide which are relevant, assign categories and aggregate the money. Each decision can change what belongs underneath the ratio. A classifier can be consistent about the records it sees while the collection misses a whole kind of research.

For example, suppose a search finds 100 grants, and the classifier places 30 in the numerator. Reading all 100 would settle the sampling question within that result set. It would tell us little about an additional set of relevant grants that never matched the search. This is an illustrative example, not one of our funding results.

The direction of the error depends on what was missed. Missing mostly numerator grants and missing mostly other grants would move the percentage differently. Without examining coverage, “we probably missed some” is too vague to tell us how to interpret the number.

Comparing sources adds another difficulty. Swedish, European and US databases have different coverage, metadata and search behaviour. A comparable-looking table can conceal different routes into each row. Our [source cross-check](https://github.com/SeljaKeranen/hackliferepo/blob/2c47b1d70a1acce0b5a3d56eb638b85fd8e77728/ratio/data/CROSSCHECK.md) documents those limits, including gaps that further classification work cannot repair.

I had also asked for a funnel view showing the restrictions. That view has a useful job: make it possible to see where records leave the analysis and why. A single final count cannot show whether a record was absent from the source, missed by the query, rejected as irrelevant or left ambiguous by classification.

Our resulting percentages needed to be read within those collection choices. They could describe the classified funding we had retrieved. Turning them into claims about a country's total spending would require evidence about the research outside the search net as well.
