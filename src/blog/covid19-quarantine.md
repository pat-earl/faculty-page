title: How does the start time a quarantines affect the total number of fatalities?
subtitle: Authors: <a href='https://scholar.google.com/citations?user=CcGX9ccAAAAJ&hl=en'>Yuanyuan Feng</a>, <a href='{{site_url}}'>Gautam Iyer</a> and <a href='https://ins.sjtu.edu.cn/people/leili/'>Lei Li</a>
summary: During the spread of an infectious disease, when should you impose a quarantine to minimize the total number of fatalities? If the qurantine is long enough to stop the outbreak, then it should be imposed early when very few people are infected. If the quarantine is not long enough to stop the outbreak, then starting it closer to when the infection peaks, reduces the cumulative number of fatalities when the infection has run its course. In the scenario considered here (with parameters chosen from currently available COVID19 data), a imposing a 30 day quarantine near the time when the infection is at its peak can reduce the number of fatalities by as much as 44% when compared to a 30-day quarantine imposed too early.

{#
<div class='alert alert-info small'>
<b>Under Construction:</b>
We are still working on this article, and it may change substantially before the final version is released.
</div>
#}

**Abstract:** {{summary}}

## Introduction

What's the best outcome of the current (March 2020) quarantines?
Complete and total eradication of COVID19?
Or at least, stopping the outbreak?
How long will that take?
Well, that can be computed quite easily -- on 2020-03-22 there were about 30,000 people (0.01% of the total population) are infected in the US.
A conservative estimate for $R_0$ for COVID-19 is $2.4$.
Suppose we can reduce this to $0.8$ using social distancing and quarantines.
Then this quarantine will have to be imposed for *13 months* to eradicate the disease.
What if we imposed a stronger quarantine that reduced $R_0$ down to $0.1$ instead (some sources say that a Wuhan style lockdown achieved this)?
That would still take *6 months* to eradicate the disease.

What if we don't wait until you eradicate the disease, and just return to normal after a month.
Or maybe after two months?
Would we have at least "flattened the curve"?
No, we won't!
We would only have "shifted the curve" -- that is if we resume normal behaviour a month or two of quarantine, then we would only have delayed the peak of the infection, and not reduced the size of the peak, or the total number of people that will eventually contract the disease.
(Shifting the curve, however, does buy us enough time to allow hospitals to increase their capacity, and thereby reduce the overall number of fatalities.)

If a month long quarantine doesn't flatten the curve, or stop the outbreak, does it help at all?
First, if we do nothing, then over 85% of the susceptible population gets infected in just 6 months.
With a mortality rate of 1%, this means that 0.85% of the susceptible population will die in 6 months!
This is even without counting the increased mortality rate when the hospital capacity is exceeded.

Can we do something to reduce this number? 
Let's say society is willing to tolerate one month of quarantine.
How should we impose it?
Should we impose it all now (when 0.01% of the population is infected), buy us time to increase hospital capacity, and then return to normal when we can't wither the quarantine anymore?
Or, should we instead, we delayed our one month quarantine to start closer to when a larger number of people were infected.

At first sight, this sounds like a bad idea.
Delaying the start of a quarantine to when, say 10%, of the population is infected sounds like it's too late to help.
*This isn't true!*
Delaying the quarantine in this manner actually flattens (or more correctly "truncates") the curve.
In addition to avoiding the hospital capacity being exceeded, it also reduces the total number of people that will be infected at the end of the epidemic.
This directly results in a lower number of fatalities.

Another alternative, that produces comparable results, is to impose the quarantine intermittently -- for instance instead of one continuous month of quarantine say we broke it up into 10 different 3 day periods.
This can be used to forcibly flatten the curve as well: every time the hospital capacity gets close to full, impose a short quarantine and stop the growth of the infection temporarily.
When hospital capacity frees up (or after a pre-specified period), return to normal.
It turns out that this also reduces the total number of people that will be infected at the end of the epidemic.
It also ensures the hospital capacity is never exceeded, and hence also reduces the number of fatalities.

The bottom line is:

> 1. A short quarantine imposed early, when very few people are infected, is only effective if it is long enough to stop the outbreak. If not, such quarantines only "shift the curve right" and don't flatten it. They have almost no effect on the final number of fatalities.
> 2. Quarantines imposed when a larger fraction of the population is infected do in fact "flatten the curve". They reduce the total number of people that will be infected by the end of the epidemic, and also reduce the total number of fatalities.

Numerical simulations in a COVID19 model scenario (described below) show that an optimally scheduled one month long quarantine can reduce the number of fatalities by as much as 44%, when compared to a one month long quarantine that is imposed too early.

Finally, before substantiating the statements we made above, we remark that there is one approach that is far more effective at reducing the total number of fatalities: selectively quarantining the high risk population until the general population develops herd immunity.
This shifts the profile of the eventually infected population away from the high risk group, and reduces the total number of fatalities by an order of magnitude.
The mathematical analysis of this is discussed in [CP20], and we limit our attention to quarantines that are imposed on the entire population.

## Comparing the final impact of short quarantines in a COVID19 model scenario.

Here we study a model scenario using COVID19 parameters taken from [CovidActNow].
The qualitative conclusions are not sensitive to these exact parameter values, though the quantitative results (e.g. 44% reduced fatalities) depend on them of course.
In our model scenario, we assume:

* Initially 0.01% of the total population infected. This is roughly as things were in the US on 03-22-2020.
* Outside quarantine, the basic reproduction number, $R_0$, is 2.4.
  Inside quarantine, $R_0$ is reduced to 0.8.
* The recovery time is 2 weeks.
* 7.3% of those infected require hospitalization, and there are 8 hospital beds per 1000 people. (There are currently 2 to 4 hospital beds per 1000 people in most states; but we assume that this number can be temporarily increased through make-shift measures.)
* 1% of those infected die, and this number is doubled when the hospital capacity is exceeded.

{# Namely, if these parameters are changed slightly, one long quarantine started early on causes more mortalities than having one quarantine (of the same length) started closer to when the infection peaks, or having multiple short quarantines (of the same total length) imposed at the right times. #}

Here is a comparison of the effects when a *one month long quarantine* is (1) imposed initially, (2) delayed to start when a larger fraction of the population is infected,  and (3) imposed intermittently, by dividing it into ten, 3-day periods which are started when a specified fraction of the population is infected.

<div class='text-center my-3 border'>
<img src='{{filesdir}}/onemonth-infections.png' class='mx-1' >
<img src='{{filesdir}}/onemonth-mortalities.png' class='mx-1' >
<p class='small text-justify mx-5'>
  Figure 1: Effects of a 30 day long quarantine when (1) imposed initially, (2) delayed to start when a larger fraction of the population is infected, and (3) imposed intermittently, by dividing it into ten, periods each of which are three days long.
  Left: Percentage infections vs time. Right: fatalities (%) vs time.
</p>
</div>

As can be seen from the first figure, a one month quarantine imposed early on *only shifts the curve*, and **doesn't flatten it**.
If we look at the cumulative fatalities (right figure), the initial one month quarantine only delayed the spike in fatalities.
At the end of 18 months, the number of fatalities was almost identical to those when no quarantine was imposed at all.

What made a difference?
Delaying the one month quarantine to day 75, when a little more than 11% of the population was infected, did in fact change the nature of things.
The total number of mortalities reduced by 44% in this case.
The same happened when we imposed the quarantine intermittently, in 10 periods of 3 days each.

Let's try this again, but this time we increase the quarantine length to 45 days:
<div class='text-center my-3 border'>
<img src='{{filesdir}}/45days-infections.png' class='mx-1' >
<img src='{{filesdir}}/45days-mortalities.png' class='mx-1' >
<p class='small text-justify mx-5'>
  Figure 2: Effects of a 45 day long quarantine when (1) imposed initially, (2) delayed to start closer to when the infection peaks, and (3) imposed intermittently, by dividing it into ten, periods each of which are three days long.
  Left: Percentage infections vs time. Right: fatalities (%) vs time.
</p>
</div>

Again, we see the exact same effect.
The quarantine imposed initially only shifts the curve, and doesn't flatten it.
It *does not affect the total number of fatalities at the end of 18 months*.
Delaying the quarantine, or imposing it intermittently (this time broken down into 15, 3 day periods) does indeed reduce the total number of fatalities.
The exact numbers from our simulations are shown below.

<div class='text-center my-3 border mb-5'>
  <table class='table border'>
    <thead>
      <tr>
        <th></th>
        <th scope='col'>30 day quarantine</th>
        <th scope='col'>45 day quarantine</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope='row'>Imposed initially</th>
        <td>1.50%</td>
        <td>1.50%</td>
      </tr>
      <tr>
        <th scope='row'>Delayed</th>
        <td>0.84%</td>
        <td>0.80%</td>
      </tr>
      <tr>
        <th scope='row'>Imposed intermittently</th>
        <td>0.80%</td>
        <td>0.78%</td>
      </tr>
      <tr>
        <th scope='row'>Control (no quarantine)</th>
        <td>1.50%</td>
        <td>1.50%</td>
      </tr>
    </tbody>
  </table>
  <p class='small'>
    Table 1: Fatalities (%) after 18 months for 30 and 45 day quarantines when imposed initially, on a delay or intermittently.
  </p>
</div>


## The impact of varying the quarantine length on the eventual number of fatalities.

We now see how the total number of fatalities changes as we vary the length of the quarantine.
As before, we study three cases: (1) The entire quarantine is imposed initially, (2) the quarantine is delayed to start closer to when the infection peaks, and (3) the quarantine is divided into many short 3-day long periods of the same total length.
Again, we see that if the quarantine is shorter than a year, then delaying it produces a dramatic reduction on the total number of fatalities.

<div class='text-center my-3 border'>
<img src='{{filesdir}}/mortality-vs-length.png' class='mx-1' >
<p class='small text-justify mx-5'>
  Figure 3: Each curve shows percentage of fatalities after 18months, vs the quarantine length, when (1) the entire quarantine is imposed initially, (2) the quarantine is delayed to start closer to when the infection peaks, and (3) the quarantine is divided into many short 3-day long periods of the same total length.
</p>
</div>

One notable fact that can be see from the above figure is that the largest reduction in the number of fatalities  per additional day of quarantine is obtained when the quarantine is shorter than a month.
The reason for this is that with the parameters chosen in our simulations quarantines shorter than a month can not ensure that the hospital capacity is not exceeded.
This leads to a higher mortality when the infection peaks, resulting in larger number of fatalities at the end of our time period (18 months).

## Are gains obtained from delaying quarantines solely due to exceeding the hospital capacity?

As we've seen above, delaying quarantines to when the infection peaks significantly reduces the total number of fatalities.
Is this solely due to the fact that the mortality rate is higher when the health care capacity is exceeded?
To address this we again study the total number of fatalities as we vary the length of the quarantine.
We study the same three cases as before (1) the entire quarantine is imposed initially, (2) the quarantine is delayed to start closer to when the infection peaks, and (3) the quarantine is divided into many 3-day long periods of the same total length.
However, this time we assume that the mortality is the same both above and below the hospital capacity.


<div class='text-center my-3 border'>
<img src='{{filesdir}}/mortality-vs-length-nohc.png' class='mx-1' >
<p class='small text-justify mx-5'>
  Figure 3: Each curve shows percentage of fatalities after 18months, vs the quarantine length, when the mortality above and below the hospital capacity are the same.
  Case 1: the entire quarantine is imposed initially.
  Case 2: the quarantine is delayed to start closer to when the infection peaks.
  Case 3: the quarantine is divided into many 3-day periods of the same total length.
</p>
</div>

In this case we still reduce the total number of fatalities.
With no quarantine, or with a 30 day quarantine imposed early, 0.88% of the total population dies at the end of 18 months.
When a 30 day quarantine is imposed to start on day 89, only 0.76% of the total population dies at the end of 18 months.
This is a reduction of 13.2%.
While significant, this isn't as large as the 44% reduction obtained  when the hospital capacity was taken into consideration.

## Conclusions

1. Imposing quarantines when relatively few people are infected is only useful if the quarantine is long enough to stop the outbreak.
  If the outbreak hasn't been stopped, then when the quarantine is lifted the curve will simply be shifted and not flattened.
  The cumulative number of people that eventually get infected is essentially unchanged, as is the cumulative number of fatalities.
2. Imposing quarantines when a larger fraction of the population is infected *does in fact help*! Even if it hasn't stopped the outbreak, it reduces the number of people that eventually contract the disease, and it reduces the total number of fatalities. It can also be used stop the hospital capacity from being exceeded.


## Appendix: The equations used in the above models.

We use a standard SIR model to study the growth of the infection (see for instance [SIRWiki]  or [Weiss13]), and we describe it briefly here:
Let $S$ denote the number of *susceptible* or healthy people, $I$ denote the number of infected people and $R$ denote the number of people that recovered, and $D$ denote the number that died from the infection.
Let $P = S + I + R$ be the total number of people alive.
Now the evolution of these quantities is given by
\begin{align*}
  \partial_t S &= -\beta \frac{S I}{P} \\
  \partial_t I &= +\beta \frac{S I}{P} - \gamma I\\
  \partial_t R &= (1 - M) \gamma I\\
  \partial_t D &= M \gamma I\,.
\end{align*}
Here $\gamma = 1/14$ is the recovery rate, $\beta = R_0 \gamma$ is the infection rate, and $M$ is the IFR (infection fatality ratio).
We assume $M = .01$ if $H_R I/P < H_C$, and $0.02$ otherwise.
Here $H_R = .073$ is the chance that someone infected requires hospitalization, and $H_C = 8/1000$ is the hospital capacity.



## References

1. Data and parameters on COVID19 were taken from [LiuEA20] and [CovidActNow].
2. The SIR model used in numerical simulations is described in [SIRWiki] and [Weiss13].
3. All code for the above numerical simulations is [[{{filesdir}}/quarantine-vs-mortality.ipynb|here]]
4. Selectively quarantining high risk groups, which has the potential to save many more lives, is described here: [CP20]
 

[LiuEA20]: https://academic.oup.com/jtm/article/27/2/taaa021/5735319
[SIRWiki]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
[CP20]: https://math.cmu.edu/~wes/covid.html
[CovidActNow]: https://covidactnow.org/
[Weiss13]: http://people.math.gatech.edu/~weiss/uploads/5/8/6/1/58618765/weiss_the_sir_model_and_the_foundations_of_public_health.pdf
