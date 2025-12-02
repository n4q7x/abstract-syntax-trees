# abstract-syntax-trees
Just some experimenting and thinking.

***

I would like to write some kind of symbolic logic engine for first order logic in a programming language, and then carry out proofs and the rewriting of formulae using it. However, there are some conceptual questions that come up, along the way, that I would like to think through.

There was a period of time where I considered "multiplicities of things" to be more or less an indispensable, even unavoidable, primitive notion. I also regarded it as a very natural idea, like, it captures how humans commonly think about their world.

It seemed that there were certain concepts where it would not be possible to model them without this notion of multiplicities. Especially anything that is a sort of dependent entity, like the idea that to make a certain something requires 2 things as input.

This led me to try to model basically everything via tuples, when I was programming in Python. But this sometimes led to dissatisfying and inelegant situations.

I have known about currying for a long time, but sometimes it takes a lot of thinking before you have digested an idea and considered connecting it to something else you have been thinking about.

In order to build abstract syntax trees for first-ordee logic, I was originally planning on using tuples. For example,
