# Adventure Planning

A command line tool for planning adventures.

Initial Document:

```
The Artist's Way shows us the value in process. Understanding ourselves in order to find control. In other words, a framework to drive the story forward. Adventure Planning a similar framework, but based around a slightly different data model and all through the command line.
At the core of Adventure Planning is The Routine. The Routine exists because Days exist. Nature is cyclical, Adventure Planning is cyclical. So it goes.
Adventure Planning is pretty simple. Based on the observation that every day is a new adventure, and that an adventure demands some level of preparedness and thought, creating a framework to resort to is critical in order to squeeze the most out of those days and avoid complacency as we all await our deaths.
The Routine
planning
prepping
set out
mid journey
way home
settle in
The Routine specifies a sequence, not necessarily an order. For example, if you like to sleep in, and wake up right before work, you’re a wake-up-and-set-out person and should just do your planning and prepping the night before. You’re also welcome to feel gratitude first thing in the morning; or whenever you like, really. But the sequence should stay the same. Plan before you Set Out.
Each Step in The Routine may or may not take some input and produce some output. The input to Planning is a list of Vectors, and its output is The Plan. Prepping takes The Plan as input, but produces no output. Prepping is about shifting mindset. Or at least being thoughtful about it.
Set Out, Mid Journey, and Way Home is a three-part loop to be repeated throughout the day as many times as necessary. The point here is that we start from somewhere known, adventure out, and then make sure we record/document/do science on whatever it is we learned during the adventure, thus building out home base into something larger and more data dense. Settling in is the end of adventure stuff. Charging laptops, tidying up, don’t sprint until bedtime. Let the body digest the world. It can’t do any deep learning without time to think.
The Plan is an unordered set of things to do. A glorified to do list. But it represents a cross section of all Vectors combined. In other words, The Plan should include a concrete, achievable thing to do (goal) for each of the vectors. Min block of time is 30 seconds. But it needs to be daily. At least once, for each Vector.
The Plan is the ongoing repetition of The Loop with the aim of maintaining an upward angle for each Vector. By continuously doing work on all Vectors, nothing gets lost and new things can get added with as little commitment as 30 seconds per day. But keep em included in the Adventure. So the very very early mvp of Adventure Planning is a series of documents representing The Plan, and a master list of Vectors. Committed to some repository.
Each vector needs a backlog so that vectors can maintain healthy backlogs of work to pull from, ideally in all different sizes for fluctuating attention. Furthermore, Vectors need to be pause-able and resume-able so that they can go w/out being forgotten. It should all feel very good. Undone items from the previous day can be brought into today or will be automatically archived and available when wanted.
I should be able to prioritize vectors.
Vector groups are called Chapters and should be thought of as chapters in your life. Starting off on new Journeys should be exciting and easy if you simply write down the initial steps. “Buy a tent”, “Book a day off work”, “Run to the end of the block and back”. 30 seconds is the only commitment you need to make.
From the In Progress page, where you’re working through a Step, you should be able to click a button like “something else to do” and it takes you back to the exploratory page of Vectors + Steps with type/chapter filters.
The feeling to write to AP is when you’re in the middle of some work, and you realize that you have a knowledge gap. And instead of completely derailing and going through the process of trying to learn everything or not, you simply go to the chapter and add a new vector or update an existing vector with new steps. But You can move on and include those learnings in your eod blocks of time.
Reduce ambiguity between Chapters and Vectors and Steps. What is the top tier? Maybe that abstraction is just up to the user and a case-by-case thing… Need to test.
It’s always best to just take a step.
Steps can optionally have a strategy attached to it (these will eventually be a plugin layer). Strategies will be related to similar step types, and offer a Step-specific UI for dealing with that particular step type. For example the LeetCode Journey might have a UI built for solving and documenting solutions to LeetCode problems. Same could be true of day-job type work, repetitive “monitor the thing” tasks. Or anything, but it could be a bring-your-own-ui type of a situation.
All text data should be stored such that it can be searched and compressed locally by some llm into meaningfully queryable data “Have I ever mentioned X in Vector Y?”.
Day start and day end are critical to the ongoing Adventure. In a day, you get done what you get done. You go to bed when it’s time to go to bed, and you get up when it’s time to get up.


When reading some article/thing in a particular vector, http often links to other interesting, related, next-level information that should be appendable to the current vector (if vector type is reading?). Note should be available for each reading thing and each vector should make available, a complete joined log of notes, obviously searchable and parsed by a local LLM to which you can ask about your complete history of written language. 


[WORK GEN] Step/Vector Type. For when there isn’t enough work and things need to get ticketed (backlog grooming but fuck me not backlog grooming). Exploratory planning.

```

