
Given n slot machines M1, M2, ... , M_n, each machine returns some amount of money according to some distribution D_i.  

If the distribution D_i is independent of the time (i.e. every time, machine i returns money according to the fixed D_i), then
our strategy would be finding the machine M_i which have greater mean. And then always use that machine.

Now, we consider a very bad situation, the person who owns the machines can adjust the distribution of each machine at any time,
he can actually decreases the mean of the machine which gave more money previously. Informally, this kind of situation 
is adversarial multi armed bandit. Now it is really hard to see which machine we should choose at each time to get better
gains.

In this folder, there is an animation (which is "main.py") made by pygame package to show the schemes of the opponet (the person who owns the 
machines), and the strategy we used to try to defeat the opponent.


"drawmachine.py", "exp3.py", "multiarm.py", "randomarm.py" are ingredients of the "main.py". "coin.wav" is used to display 
the sound of gaining money.

"picture" is the screenshot of the animation.







