# Week 5 Practical: **MAGICC** Reduced Complexity Climate Model (Model for the Assessment of Greenhouse Gas Induced Climate Change)
[practical handbook link](https://github.com/Haru-Tachibana/Environmental-Modelling/blob/main/Practical/Week%205%20MAGICC%20climate%20modelling/MAGICC_Practical_FINAL.docx)\
[MAGICC website](https://live.magicc.org/) - sign in with your uni email.\
<br>
**Objectives:**
1) Simulate global average temperature for the future, up to the end of the century, for two different scenarios of future greenhouse gas emissions.

2) Explore what effect model choices can have on the simulated results, namely changing the number of layers that are used in the model to represent the ocean.

3) Simulate the effect of volcanic eruptions on the climate, separately for large volcanic eruptions such as those seen in recent centuries, and for a super-volcano eruption like what happened 74,000 years ago.

## Part 1: 
Every model need input data. We will use two different emissions scenarios as input datasets for our two respective simulations.
1. **SSP5-8.5** - has **high greenhouse gas emissions** in the future (a typical world without climate action, i.e., limited/ no climate policy to reduce global emissions of GHGs)
2. **SSP1-1.9** - has **low GHGs emissions**, a future world with **strong climate action**, in line with the 2015 United Nations Paris Agreement.
<br>

We will run the two scenarios separately.\
We will compare them afterwards.

![compare SSP5-8.5 (solid line) with SSP1-1.9](https://github.com/Haru-Tachibana/Environmental-Modelling/blob/main/Practical/Week%205%20MAGICC%20climate%20modelling/compare.png)
*Fig.1 - the trends of GHGs emissions for two scenarios.*

### The effects of numbers of ocean layers on the simulation results
![](https://climateextremes.org.au/wp-content/uploads/what-does-climate-model-resolution-mean_V2-700x523.png)\
Read this article: [What does climate model resolution mean?](https://climateextremes.org.au/what-does-climate-model-resolution-mean/)
>MAGICC uses 50 layers for the ocean as a default.\
>Do a simulation for SSP5-8.5 with just 10 layers, to see if it make a difference to the simulated climate.

**Summary:**
- The simulated global mean surface temperature is **0.18°C cooler** with 10-ocean-layer model than the 50-ocean-layer model. (The difference between the two simulations is only due to the number of layers in the ocean).
- This shows that choices and decisions on how you setup your model can affect the results. A difference in global average temperature of 0.18°C is not small.
- However, you will see that the climate simulated by the model is more sensitive to the greenhouse gas emissions than it is to choices on number of layers in the ocean – this is because there is a larger difference in temperature between the SSP5-8.5 and SSP1-1.9 scenarios, than there is between the 10 layer and 50 layer simulations.
- it's not a physically based model (numerical eqation based model), therefore, it's quite hard to understand why the number of ocean layers will lead to a change in simulated values.
