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

I have also been trying really hard to eliminate types as a primitive notion from theories, instead wanting them to be built up internally in the theory. The only way I know how to do this so far is by using an element "bottom" to denote when the application of something is simply considered invalid or undefined.

I wonder if I can build up first-order logic, right now. Let's see.

***

In my approach to ontology, we always consider the collection of, well, possible things, D. We don't really know what they are, and we choose to leave it vague and undefined.

I am already digressing, but it's ok.

Cognitively and metaphysically, in the mind's eye, what is a "collection of things"? One thing I would say is it has a kind of *mixed identity*: composite objects are recognized by our mind as simultaneously one thing, and the things it is made of. Is a set a thing which has things *inside* it, or is it just the natural sum total of some collection of things, being a *part* of it? There *is* a difference! 

If we want to characterize it relationally, through statements, it is the conventional route to simply say what is and is not inside it. 

Intriguingly, I would say the notion of a collection of things is decidedly not opaque. In the mind's eye, it is very easy to see that group of things. There is a kind of mental *movement* as our attention can move back and forth between the things, while knowing in our higher, background mental context that "these things are in the same collection right now".

Then there is the idea that in order to describe what a thing is *like*, we can regard it *experientially*; which implies how it dynamically unfolds in time, interacts with things, changes, and also *can* change. Since actions I believe are inherently functional, like, one action, one outcome (perhaps it being the very nature of an action that we simply choose a changed state the object can go to and call that "some action", so the actions follow from the state changes, not vice versa?), we can sort of characterize the mental image of a set in terms of how it can be changed, I guess: can the spatial dimensions or boundaries grow and contract? Can the set be split, scattering its contents? Can we add or take away things; combine sets into larger ones; and so on?

This is sort of leading to a recent theme in my thinking which is that relations and functions are not as similar as we are sometimes told. Relations are static descriptions; functions change what is being talked about. The formulation of a statement, introducing it into the current context of discourse, is an action. 

***

Anyway, let's see if we can define our first-order logic formulae, now.

I want to be able to say that there are kinds of things. But I want kinds of things to be a posteriori, not a priori. So I can introduce certain things into a context, of what we have been talking about so far.

So here's... formalizing a formalization...:

D is an arbitrary set of values, say of possible things.

Which set is the current discourse context is not something we can express in set theory. We can only say that for some given set, a person can add more to the context.

Like:

<pre>
```math
D
d \subseteq D
x \in D
add(x,d) \subseteq D
```
</pre>

That means that our "states" are kind of pegged to what collection of d's we currently have; which is like a subset of D.


