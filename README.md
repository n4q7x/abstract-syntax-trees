# abstract-syntax-trees
Just some experimenting and thinking.

***

I would like to write some kind of symbolic logic engine for first-order logic in a programming language, and then carry out proofs and the rewriting of formulae using it. However, there are some conceptual questions that come up, along the way, that I would like to think through.

There was a period of time where I considered "multiplicities of things" to be more or less an indispensable, even unavoidable, primitive notion. I also regarded it as a very natural idea, like, it captures how humans commonly think about their world.

It seemed that there were certain concepts where it would not be possible to model them without this notion of multiplicities. Especially anything that is a sort of dependent entity, like the idea that to make a certain something requires 2 things as input.

This led me to try to model basically everything via tuples, when I was programming in Python. But this sometimes led to dissatisfying and inelegant situations.

I have known about currying for a long time, but sometimes it takes a lot of thinking before you have digested an idea and considered connecting it to something else you have been thinking about.

In order to build abstract syntax trees for first-order logic, I was originally planning on using tuples. For example, a formula like "for all x, P(x) implies Q(x)" might be grouped as (all, x, (implies, (P, x), (Q, x))).

It has so far turned out that even with tuples, there are those arbitrary design choices that really bother me. Should we constrain tuples to be duples, or n-ary? If duples, should we group forall as (quant, (var, formula)) or ((quant, var), formula)? Should leaves be a bare symbol like "c", or should we require everything to be *some* tuple, hence "c" would be (c,)?

Another thing that frequently bothers me is how we need the notion of tuples to define (n > 1)-ary functions, yet tuples seem like an arbitrary construct that need their own definition, for which functions seem like the solution: we can say the "pair of a and b" is some arbitrary thing "c", whose "inherent form" is opaque; yet we establish two functions which allow us to recover "element 1" and "element 2" from it (projection functions). The problem with this is that we have to just *assert* the pair exists; we cannot *construct* it from any two arbitrary x and y in some domain. If we want to be able to construct ordered pairs, then we need a binary function pair(a,b) -> c. And now, we are painfully back where we started: what's the point of having a "pair" function if we need a notion of "ordered pair" to define it? We give it a "primordial" ordered pair, and it returns some... "conceptual" ordered pair. It's confusing.

My hope is to finally embrace currying and functionals to completely remove the need for tuples as primitive notions in a formal theory.
