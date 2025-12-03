# ngzl

![NGZL icon](https://github.com/syswraith/ngzl/blob/main/assets/ngzl.png)

### Why?

Because its not even 10 pm and its a Tuesday night :/
Okay, for real, because I was trying to learn some of the basic libraries in python and this seemed like the ideal way to do that.
ngzl? Stands for nazgul. Read up.
Usage is prohibited for nefarious purposes.

### How does it work?

- All the "bots" run a Python script that connects to an IRC server and to a particular channel.
- The bot herder issues commands in the channel.
- All the bots execute the commands on their end inside a subprocess (non-interactively, so you don't have to worry about clearing the history).
- They DM the output line-by-line to the botherder. Why line-by-line? Because the server rate-limits the input.

Read an in-depth overview of the codebase in this blogpost
<https://syswraith.github.io/blog/Dissecting-the-Anatomy-of-a-Botnet>
