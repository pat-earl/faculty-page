title: Scheduling quarantines to reduce the number of fatalities during an outbreak.
subtitle: Authors: <a href='https://scholar.google.com/citations?user=CcGX9ccAAAAJ&hl=en'>Yuanyuan Feng</a>, <a href='{{site_url}}'>Gautam Iyer</a> and <a href='https://ins.sjtu.edu.cn/people/leili/'>Lei Li</a>
summary: During the spread of an infectious disease, how does a quarantine impact the total number of infected people, and the total number of fatalities? Here we see that if the qurantine is not long enough to stop the outbreak, then it has the biggest impact on the total number of fatalities (and the total number of infected people) if it is imposed around the time the infection peaks. In the scenario considered here (with parameters chosen from currently available COVID19 data), a imposing a 30-day quarantine at such a time reduces the reduces the number of fatalities by 30--40% when when compared to a 30-day quarantine imposed too early.

{#
<div class='alert alert-info small'>
<b>Under Construction:</b>
We are still working on this article, and it may change before the final version is released.
</div>
#}

Suppose a quarantine is imposed during the outbreak of an infectious disease.
How does it impact the total number of infected individuals, and the total number of fatalities?
The best case scenario is when the quarantine completely contains the outbreak.
In this case, a very small number of individuals are infected, and the disease is eradicated.

Unfortunately, there are two major drawbacks of this scenario:

1. Since very few individuals have been exposed to the disease, the population *does not* have herd immunity.
   If the disease is re-introduced, it will spread rapidly, infecting a large number of individuals.
   Currently (March 2020), projections from [Healthdata] show that COVID19 will be contained in 2-3 months -- however, after the end of the first wave of the epidemic an estimated $97$% of the population will still be susceptible.

2. The length of the quarantine required to contain the disease may be too long for society to withstand.
   For instance, on 2020-03-22 there were about 30,000 people (about 0.01% of the total population) infected with COVID19 in the US.
   A conservative estimate for the basic reproduction number (or $R_0$) of COVID19 is $2.4$.
   If using social distancing and quarantines we could reduce this to $0.8$, then such a quarantine would need to be imposed for *6 months* to bring the infection levels down to levels where containment is possible.

Thus we may (eventually) have to consider the possibility that infection to spreads through the general population.
What we study here is the following:

> *In the event that the infection does spread through the general population, can a short (say 1 month) quarantine help? Will it reduce the total number of infections and fatalities, or does it only delay the inevitable?*

Before getting into the specifics of the model and our analysis, we summarize our findings:

> 1. A short quarantine imposed when very few people are infected, only delays the spread of the infection. Namely, after the quarantine is lifted, the infection will spike to the same levels it would have without any quarantine.
> Once the infection has run its course, the total number of people who eventually contract the disease, and the total number of fatalities is almost identical to that if there was no quarantine at all.
> In other words, *a short quarantine imposed when very few people are infected will only shift the curve right, and not flatten it.*
> 2. On the other hand, a quarantine (of the same length) imposed when a larger fraction of the population is infected can reduce the total number of people that will eventually be be infected, and also reduces the total number of fatalities. *Such quarantines do in fact flatten the curve.*

The first point above is well known to experts.
The second point, however, has not received much attention.
As an illustrative example, suppose we impose a 30 day quarantine when the hospital occupancy reaches a certain threshold.
Then, in a model scenario that will be described in detail below, here is how the number of fatalities after 18 months varies.

<div class='text-center my-3 border' id='fig1'>
  <img src='{{filesdir}}/fatalities-v-hoccup-30.png' class='px-5 img-fluid' >
  <p class='small text-justify mx-5 mt-3'>
    Figure 1: Percentage of fatalities after 18months, vs the hospital occupancy threshold at which a 30 day long is started.
  </p>
</div>

In this scenario we see that if a 30 day quarantine is started when the hospital occupancy is close to capacity, the number of fatalities is about $38$% lower than if a 30 day quarantine was started when the hospital occupancy is very low.
While the exact hospital occupancy threshold that minimizes the number of fatalities varies depending on the actual parameters (recovery time, $R_0$, etc.), *the optimal threshold is typically not attained when the number of infections (or the hospital occupancy) is very small.*

Practically, the parameters involved can't be determined precisely enough to compute the exact threshold at which a 30 day quarantine should be started so that the minimum in <a href='#fig1'>Figure 1</a> is attained.
One can, however, still schedule the quarantine to reduce the total number of fatalities as follows: Wait until the hospitals are close to capacity (say $85$%).
Impose a quarantine until hospital capacity frees up (say reaches $75$%).
If the infection spikes to $85$% again (as it may), then repeat the above procedure.
Using this strategy we won't a priori know the length of the quarantine -- however, we will always ensure the hospital capacity is not exceeded, and moreover such quarantines still reduce the number of fatalities significantly compared to a quarantine of the same length imposed when there are very few infected people.

Finally we remark that if a "high risk" population can be successfully identified, then the total number of fatalities can be significantly reduced by selectively quarantining them.
Indeed, if they are quarantined while the infection is spreading through the low risk population, very few of the high risk population contract the infection, and so very few of them die.
After the infection has run its course amongst the low risk population, the quarantine on the high risk population is lifted and they are released back into the general population.
At this point, however, the general population has herd immunity and there are very few infected individuals.
Thus the chance of individuals from the high risk population getting infected is very low, and there will be very few new infections amongst the high risk population.
This leads to a greatly reduced mortality rate, and has been suggested by various sources (see for instance [CP20]).


## Imposing 30-day quarantines based on hospital occupancy.

We now numerically study a model scenario in which a 30 day quarantine is started based on the hospital occupancy.
This is the scenario used to generate <a href='#fig1'>Figure 1</a>, and all our parameters are based on the COVID19 pandemic, with data taken from [CovidActNow].
In our model scenario, we assume:

* Initially $0.01$% of the total population infected. This is roughly as things were in the US on 2020-03-22.
* Outside quarantine, the basic reproduction number ($R_0$) is $2.4$, and inside quarantine, $R_0 = 0.8$. (To illustrate that model behaviour is typical, we will later compute the number of fatalities after 18 months when $R_0$ varies between $2$ and $6$ outside quarantine, and between $0.5$ and $1.5$ inside quarantine.)
* The recovery time is 14 days, and those who recover develop immunity.
* $7.3$% of those infected require hospitalization, and there are 8 hospital beds per 1000 people. (There are currently 2 to 4 hospital beds per 1000 people in most states; but we assume that this number can be temporarily increased through make-shift measures.)
* $1$% of those infected die, and this number is doubled when the hospital capacity is exceeded.
* The number of infected individuals varies according to the standard SIR model (see [SIRWiki] or [Weiss13]). We generate confidence intervals by using a stochastic process to randomly vary $R_0$ assuming a with a $3\sigma$ confidence interval of $1$ outside quarantine, and $0.4$ inside quarantine. Our methodology for generating confidence intervals is described at the end.

We begin with numerical simulations comparing the effects of having no quarantine at all with having a *one month long quarantine* imposed starting on day $0$, when only $0.01$% of the population is infected.

<div class='container my-3 border' id='fig2'>
  <div class='row'>
    <div class='col-md-6'>
      <img src='{{filesdir}}/q30-start-infections.png' class='img-fluid' >
    </div>
    <div class='col-md-6'>
      <img src='{{filesdir}}/q30-start-fatalities.png' class='img-fluid' >
    </div>
    <div class='col-12'>
      <p class='small text-justify mx-5 mt-3'>
        Figure 2: Comparison of the effects of a 30 day long quarantine starting on day 0, and having no quarantine at all.
        The number of fatalities after 18 months is almost identical.
      </p>
    </div>
  </div>
</div>

As can be seen from the above, a one month quarantine starting early reaches almost the same infection levels, and fatality levels as having no quarantine at all.
That is, such a quarantine *only shifts the curve*, and **doesn't flatten it**.

Next we perform the same comparison, except this time we start the quarantine when the hospital occupancy is $85$%.
Here are the results:

<div class='container my-3 border' id='fig3'>
  <div class='row'>
    <div class='col-md-6'>
      <img src='{{filesdir}}/q30-min-infections.png' class='img-fluid' >
    </div>
    <div class='col-md-6'>
      <img src='{{filesdir}}/q30-min-fatalities.png' class='img-fluid' >
    </div>
    <div class='col-12'>
      <p class='small text-justify mx-5 mt-3'>
        Figure 3: Comparison of the effects of a 30 day long quarantine starting on when the hospitals are at 85% capacity (day 77), and having no quarantine at all.
        The number of fatalities is reduced by about $38$%.
      </p>
    </div>
  </div>
</div>

As expected, we see a quick down turn in the number of infections when the quarantine is imposed.
When the quarantine is lifted, the general population has not yet achieved herd immunity, and the infection starts spreading again.
The second time, however, the population achieves herd immunity before the hospital capacity is exceeded and the infection dies out.
When one keeps track of the number of fatalities (shown above), we see that in this scenario the total number of fatalities is reduced by about $38$%.

One can also vary the hospital occupancy threshold at which a 30 day quarantine is started.
The results of this are in <a href='#fig1'>Figure 1</a>, which shows clearly that quarantines started when the hospitals are closer to capacity reduce the number of fatalities significantly ($38$% in our scenario).

A heuristic explanation for this is as follows: the more infected people there are, the more new infections we have per day.
Thus imposing a quarantine when there are more infected people (and thus higher hospital occupancy) stops a larger number of new infections.
However, if one waits too long, the number of infections reaches (or even passes) its peak.
After this point, imposing a quarantine doesn't help much as the population already has herd immunity.
*Thus there is some optimal threshold at which the quarantine is most effective.
While this threshold will vary depending on the actual parameters (recovery time, $R_0$, etc.), the optimal threshold is typically not attained when the number of infections (or the hospital occupancy) is very small.*

To substantiate the last statement, we now study the number of fatalities for all  $R_0$ between  $2$ and $6$ outside quarantine, and between $0.5$ and $1.5$ inside quarantine.
We compute the number of fatalities after 18 months if no quarantine is imposed.
Then we compute the maximum reduction in the number of fatalities if a 30 day quarantine is started at the optimal time.
Here are the results.


<div class='container my-3 border'>
  <div class='row'>
    <div class='col-md-6'>
      <img src='{{filesdir}}/fatalities-vs-R0.png' class='img-fluid' >
    </div>
    <div class='col-md-6'>
      <img src='{{filesdir}}/reduction-in-fatalities.png' class='img-fluid' >
    </div>
    <div class='col-12'>
      <p class='small text-justify mx-5 mt-3'>
        Left: Percentage of fatalities after 18 months if no quarantine is imposed.
        Right: Reduction in the percentage of fatalities after 18 months if a 30 day quarantine is started at the optimal time.
      </p>
    </div>
  </div>
</div>

First if a 30 day quarantine is started on day $0$ (when $0.01$% of the population is infected), the number of fatalities after 18 months is almost identical to that if there were no quarantine at all.
The reduction obtained in the figure on the right above is by delaying the quarantine to start at the optimal time.
The optimal time is found numerically and in the above ranges of $R_0$, it occurs when the hospital occupancy is between $60$% and $240$%.



## Imposing and lifting quarantines based on hospital occupancy.

Now we study the effect of imposing quarantines when the hospital occupancy reaches some threshold (say 85%), and lifting them when the occupancy drops to a lower threshold (say 75%).
If the infection spreads again after the quarantine is lifted, then we impose a quarantine again when the hospital capacity reaches 85%, and lift it when it drops to 75%, and repeat this procedure as often as needed.
Here what the infection levels and fatalities look like in this scenario:


<div class='container my-3 border'>
  <div class='row'>
    <div class='col-md-6'>
      <img src='{{filesdir}}/q-high-low-infections.png' class='img-fluid' >
    </div>
    <div class='col-md-6'>
      <img src='{{filesdir}}/q-high-low-fatalities.png' class='img-fluid' >
    </div>
    <div class='col-12'>
      <p class='small text-justify mx-5 mt-3'>
        Figure 4: The infection levels, and fatalities when a quarantine is imposed whenever the hospital occupancy reaches 85% of capacity, and lifted when it reaches 75% of capacity.
        In this case the population spends about 34 days in quarantine.
      </p>
    </div>
  </div>
</div>

Here the population spends about $34$ days in quarantine, and the fatalities after $18$ months are reduced by about $41$%.

We now study the behavior of fatalities after 18 months as we vary the hospital occupancy at which the quarantine is imposed. We always lift the quarantine when the hospital occupancy is 10% lower than when the quarantine was imposed, though this number could be varied as well.
Here are the results:

<div class='container my-3 border'>
  <div class='row'>
    <div class='col-md-6'>
      <img src='{{filesdir}}/fatalities-v-hoccup-threshold.png'
        class='img-fluid' >
    </div>
    <div class='col-md-6'>
      <img src='{{filesdir}}/fatalities-v-qtime.png' class='img-fluid' >
    </div>
    <div class='col-12'>
      <p class='small text-justify mx-5 mt-3'>
        Figure 5: Fatalities after 18 months as we vary the hospital occupancy at which the quarantine is imposed.
        The quarantine is lifted when the hospital occupancy is 10% lower than when the quarantine was imposed.
        The first figure shows the fatalities after 18 months vs the hospital occupancy when the quarantine was first imposed.
        The second figure figure shows the fatalities after 18 months vs the average time the population spends in quarantine.
      </p>
    </div>
  </div>
</div>

Clearly the lower the level at which the quarantine is imposed, the longer the population spends in quarantine, and the lower the fatalities are after 18 months.
This is of course expected.
What is interesting, however, is when the total quarantine length is roughly below 40 days, the fatalities after 18 months decreases steeply with the quarantine length.
After the 40 day mark it decreases much slower.
The reason for this is that in this scenario quarantines shorter than about 40 days can't completely stop the hospital capacity from being exceeded.
Thus each additional day of quarantine reduces the amount of time the hospital capacity is exceed, having a larger impact on the final number of fatalities.

{#
If we impose/lift quarantines below 30% hospital occupancy in the above scenario, we would need to increase our time horizon as the epidemic would not have run its course in 18 months.
In this case the time spent in quarantine also increases considerably (more than 6 months at 10% hospital occupancy).
The final number of fatalities, however, decreases very slowly.
#}

One can, in fact, theoretically compute the minimum value the final number of fatalities attains provided the quarantine doesn't contain the outbreak.
Indeed, if the outbreak isn't contained by the quarantine, then the population eventually acquires herd immunity.
This happens when the fraction of susceptible people in the surviving population is at most $1 / R_0 \approx 0.42$. 
The remainder in the surviving population have recovered from the virus.
Since we a $1$% mortality rate if the hospital capacity is never exceeded, it follows that the fraction of the initial population that died is at least
$$
    0.01 \left( 1 - \frac{0.99}{R_0 - .01} \right)
    \approx 0.59\%\,.
$$
Achieving this minimum value, however, will require quarantine times that are considerably longer (more than 6 months).

## The infinite hospital capacity case

Suppose now that the hospitals had infinite capacity.
Can the number of fatalities still be reduced by imposing a quarantine differently?
It turns out that even in this case we can reduce the number of fatalities by imposing a quarantine.
As before, there is a critical threshold at which a quarantine of a fixed length (say 30 days) is most effective.
For short quarantines this threshold is typically *not* when the hospital occupancy is very low.

To illustrate this point concretely, we now perform the exact same comparisons as we did in Figures <a href='#fig2'>2</a> and <a href='#fig3'>3</a>.
Except this time we assume that the hospital capacity is infinite; or equivalently, we assume that the mortality rate above and below the hospital capacity is the same ($1$%).
To make the comparison easier, we still plot the original hospital capacity, and reference infection levels in terms of the original hospital capacity.

<div class='container my-3 border' id='fig6'>
  <div class='row'>
    <div class='col-md-6'>
      <img src='{{filesdir}}/ihc-q30-start-fatalities.png'
        class='img-fluid' >
    </div>
    <div class='col-md-6'>
      <img src='{{filesdir}}/ihc-q30-min-fatalities.png' class='img-fluid' >
    </div>
    <div class='col-12'>
      <p class='small text-justify mx-5 mt-3'>
        Figure 6: In both these figures we assume the mortality rate above and below the hospital capacity are the same.
        The first figure shows fatalities vs time when a 30 day quarantine is started initially (day 0, when hospital occupancy is $0.09$%).
        The second figure shows fatalities vs time when a 30 day quarantine is started on day 89, when hospital occupancy is $175$%.
      </p>
    </div>
  </div>
</div>

<div class='text-center my-3 border' id='fig7'>
  <img src='{{filesdir}}/ihc-fatalities-v-qstart-30.png' class='px-5 img-fluid' >
  <p class='small text-justify mx-5 mt-3'>
    Figure 7: Fatalities after 18 months vs the day when a one month quarantine is started. In this case the mortality rate is again assumed to be the same both above and below the hospital capacity.
  </p>
</div>

In this scenario, the above figures show that final number of fatalities is reduced when the quarantine is imposed closer to when the infection peaks.
The maximum reduction in the number of fatalities is about 14%, and is achieved when the quarantine is started on day 89 (just a few days away from the peak without quarantine).
While reduction of the number of fatalities by 14% is still significant, it is not as large as the 38% reduction obtained when the hospital capacity was taken into consideration.

These exact values are of course parameter dependent, and will vary depending on the scenario considered.
The minimum, however, is typically not attained if the quarantine is imposed during the early stages of the outbreak, unless the quarantine is long enough to reach containment levels.
To illustrate this point we now compute the fatalities after 18 months when $R_0$ varies between $2$ and $6$ outside quarantine, and between $0.5$ and $1.5$ inside quarantine.

<div class='container my-3 border'>
  <div class='row'>
    <div class='col-md-6'>
      <img src='{{filesdir}}/ihc-fatalities-vs-R0.png' class='img-fluid' >
    </div>
    <div class='col-md-6'>
      <img src='{{filesdir}}/ihc-reduction-in-fatalities.png' class='img-fluid' >
    </div>
    <div class='col-12'>
      <p class='small text-justify mx-5 mt-3'>
        Left: Percentage of fatalities after 18 months if no quarantine is imposed.
        Right: Reduction in the percentage of fatalities after 18 months if a 30 day quarantine is started at the optimal time.
        In both these figures the mortality rate above and below the hospital capacity is assumed to be the same.
      </p>
    </div>
  </div>
</div>

As before if a 30 day quarantine is started on day 0, the number of fatalities after 18 months is almost identical to that if there was no quarantine at all.
The reduction shown in the figure on the right is obtained by delaying the quarantine to start at the optimal time.
This optimal time is found numerically and in the above ranges of $R_0$, it occurs when the hospital occupancy is between 115% and 335% of capacity.


## Methodology used to perform simulations.

We now briefly describe the methodology used to generate all the above simulations.
A standard compartmental model is used to study the growth of the infection (see for instance [SIRWiki]  or [Weiss13]).
To describe this model briefly, let $S$ denote the number of *susceptible* or healthy people, $I$ denote the number of *infected* people and $R$ denote the number of people that *recovered*, and $D$ denote the number that *died* from the infection.
Let $P = S + I + R$ be the total number of people alive at a given time.
Now the evolution of these quantities is given by
\begin{align*}
  \partial_t S &= -\beta \frac{S I}{P} \\
  \partial_t I &= +\beta \frac{S I}{P} - \gamma I\\
  \partial_t R &= (1 - M) \gamma I\\
  \partial_t D &= M \gamma I\,.
\end{align*}
Here $\gamma = 1/14$ is the recovery rate, $\beta = R_0 \gamma$ is the infection rate, and $M$ is the IFR (infection fatality ratio).
We assume $M$ is very close to $.01$ when the hospital occupancy is well below capacity, and increases to close to $0.02$ when the hospital occupancy is well above capacity.
We achieve this by choosing
$$
  M = 0.01 + \frac{0.01}{2}\Bigl(
        \tanh\Bigl( 40\Bigl( \frac{I}{P} - \frac{H_C}{H_R} \Bigr) \Bigr)
        + 1 \Bigr)
$$
Here $H_R = .073$ is the chance that someone infected requires hospitalization, and $H_C = 8/1000$ is the hospital capacity.
The mean in all the simulations performed above is computed using a standard forward difference scheme for the above equations.

To generate confidence intervals, simply varying $R_0$ in the expected range produces bad results.
Instead we choose $R_0$ to be a stochastic process whose distribution is a truncated Gaussian with mean and variance matching the specified values (i.e.\ mean 2.4 outside quarantine, and 0.8 inside quarantine).
Since the randomness stems from the population that is currently infected, it is reasonable require the process to decorrelate on a time scale comparable to the recovery time.
This leads us to choosing $R_0 = X^+$, where $X$ is Gaussian process
$$
  dX_t = -\theta (X - \mu) \, dt + \sigma \, dW_t\,,
$$
with Gaussian initial data.
Here $\mu$ and $\sigma$ are the mean and standard deviation of $R_0$, respectively, and $\theta = 2\gamma$.
When a quarantine is imposed or lifted, $\mu$ and $\sigma$ change immediately, and the mean and variance of $X$ will approach the new values exponentially.

We compute 10,000 realizations of solutions to the SIR system with this random $R_0$, and shade the 95% confidence intervals in all our plots.
Note, the central solid line is not the mean of these solutions.
Instead, it is the true solution to the deterministic SIR system of equations shown above.

## Conclusions

1. A short quarantine imposed when very few people are infected, only delays the spread of the infection. Namely, after the quarantine is lifted, the infection will spike to the same levels it would have without any quarantine. Once the infection has run its course, the total number of people who eventually contract the disease, and the total number of fatalities is almost identical to that if there was no quarantine at all. (This point is well known.)
2. Imposing quarantines when a larger fraction of the population is infected *does in fact help*! They reduce (or even eliminate) the time when the hospital capacity is exceeded, having a direct impact on the number of fatalities.
Moreover, they also reduce the number of people that eventually contract the disease, and so further reduce the total number of fatalities. In the model scenario considered here, the number of fatalities after 18 months reduces by about $38$%.

In summary -- if all other measures fail, and it looks like Coronavirus will spread amongst the general population, then the number of fatalities can be reduced substantially by imposing a quarantine at the right time (typically when the hospital occupancy is high). This number can be reduced even further (by an order of magnitude) if the "high risk" population can be successfully identified and selectively quarantined.


## References

1. Data and parameters on COVID19 were taken from [LiuEA20], [CovidActNow] and [FergusonEA20].
2. The SIR model used in numerical simulations is described in [SIRWiki] and [Weiss13].
3. All code for the above numerical simulations is [[{{filesdir}}/quarantine-vs-mortality-ci.ipynb|here]]
4. Selectively quarantining high risk groups, which has the potential to save many more lives, is described here: [CP20]
 

[LiuEA20]: https://academic.oup.com/jtm/article/27/2/taaa021/5735319
[SIRWiki]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
[CP20]: https://math.cmu.edu/~wes/covid.html
[CovidActNow]: https://covidactnow.org/
[Weiss13]: http://people.math.gatech.edu/~weiss/uploads/5/8/6/1/58618765/weiss_the_sir_model_and_the_foundations_of_public_health.pdf
[Healthdata]: https://covid19.healthdata.org/projections
[FergusonEA20]: https://www.imperial.ac.uk/media/imperial-college/medicine/sph/ide/gida-fellowships/Imperial-College-COVID19-NPI-modelling-16-03-2020.pdf
