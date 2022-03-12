## Marketing Analytics

Marketing Analytics comprehends the processes and technologies that enable the professionals of Marketing to evaluate the success of their initiatives, to understand the effectiveness of their marketing campaigns, and to make informed decisions about their marketing campaigns.  Marketing Analytics is a field of study that is concerned with the analysis of marketing data and the use of statistical techniques to analyze and interpret the data. Marketing Analytics measures the Marketing campaigns collecting datas ans analyzing them, like ROI (Return on Investment), Cost Per Click, Cost Per Lead, Cost Per Customer, etc. In toher words, Marketing Analytics shows if the marketing campaigns are effective or not.  

## Test A/B: What is it?

As análises de Testes A/B são comumente realizadas por Analistas e Cientistas de dados. Usually performed by analysts and data scientists, the A/B test have as target to understand if a new version of a product or service is better than the previous one or to compare different versions of the same segment.

## How to do it?

Usually have 5 steps to do an A/B test:

1. Set up the experiment;

2. Execute the hypotesys test and register the success rate of each group;

3. Build the plot of the difference between the two samples;

4. Calculate the statistical power;

5. Avaliation of the size of the samples.

## Note: The dataset is in brazilian portuguese. This does not impact understanding.

---

# **The A/B Test**

- First Step: Set up the experiment

- Secound Step: The Experiment Executions
    
    > **Execution #1: Setting up the experiment.**

        Do Pages with User Reviews Increase Online Product Sales?

        Variant A: Shows the current number of user reviews and user ratings.

        Variant B: Does not show user reviews on the site.

        **Obs:**
        Please note that, due to the registration of data and time associated with each event, you can technically execute a hypothesis test continuously as each event is observed.

        No entanto, a questão difícil é saber quando parar assim que uma variante for considerada significativamente melhor do que outra ou isso precisa acontecer de forma consistente por um determinado período de tempo? Quanto tempo até você decidir que nenhuma variante é melhor que a outra? Converse com a área de negócio para definir a melhor abordagem para o teste e apresentaremos algumas dicas durante este trabalho. However, it is difficult to know when to stop when one variant is considered significantly better than the other or does it need to happen consistently over a certain period of time? How long until you decide that none of the variants is better than the other? Those questions are the most difficult parts associated with the A/B test and general analysis. Tip: The best person to give you the best way is the business/marketing area response.
    
        For now, consider that you need to make a decision based on the data provided. If you want to assume that the variant A is better, unless the new variant proves to be definitely better in a Type I error rate of 5%, what should be your null and alternative hypotheses? 
        You can define your hypotheses in terms of words or notation as $p_{A}$ and $p_{B}$, which are the conversion probabilities for the new and old variants.

        - H0: PB - PA = 0
        - H1: PB - PA > 0

        H0 says that the difference of probability of the two groups is equal to zero.
        H1 says that the difference of probability of the two groups is greater than zero.
    
    > **Execution #2: Execute the Hypothesis Test - We execute the hypothesis test and register the success rate of each group.**

        Statistical power or sensitivity.

        Igual a 1 - $\beta$. (VER COMO FAZER O BETA)

        Normally 80% is used for most analyses. It is the probability of rejecting the null hypothesis when the null hypothesis is actually false.

        Parameters that we will use to execute the test:

            1- 1- Alpha (Significance Level) $\alpha$: normally 5%; probability of rejecting the null hypothesis when the null hypothesis is actually true.

            2- Beta $\beta$: probabilidade de aceitar a hipótese nula quando a hipótese nula é realmente falsa. 2- Beta: probability of accepting the null hypothesis when the null hypothesis is actually false.

    > **Execution #3: Distribution Plot.** 

        The creation of the distribution plot of the difference between the two samples and compared the results. We can compare the two groups by drawing the distribution of the control group and calculating the probability of obtaining the result of our test group.

    > **Execution #4: Statistical Power**

        Statistical Power and Significance. It is easier to define the statistical power and significance by first showing how they are represented in the null and alternative hypothesis plot. We can return a visualization of the statistical power by adding the parameter show_power = True.


        **(CORRIGIR - ACHO QUE É EXECUTIOM #3)**
        Note about [Null Hypothesis](https://en.wikipedia.org/wiki/Null_hypothesis) and [Alternative Hypothesis](https://en.wikipedia.org/wiki/Alternative_hypothesis):
           
            **The Null Hypothesis is that the change in the design for the test group would not result in any change in the conversion rate.**

            **The Alternative Hypothesis is that the change in the design for the test group would result in a change in the conversion rate.**

            The Null Hypothesis will be a normal distribution with a mean of zero and a standard deviation equal to the standard deviation of the group.
            The Alternative Hypothesis is the same as the Null Hypothesis, but the mean is located in the difference in conversion rate, d_hat. This makes sense because we can calculate the difference in conversion rates directly from the data, but the normal distribution represents possible values. 

            Z Formula:

                $$z = \frac{(\bar{x_1}-\bar{x_2})-D_0}{\sqrt{\sigma_1^{2}/n_1+\sigma_{2}^{2}/n_2}}$$

                $$z = \frac{(\hat{p_1}-\hat{p_2})-0}{\sqrt{\hat{p}\hat{q}(\frac{1}{n_1}+\frac{1}{n_2})}}$$

        **(A PARTIR DAQUI)**
            The green shaded area represents the statistical power and the calculated value for the power is also displayed on the graph. The gray dashed lines in the graph above represent the confidence interval (95% for the graph above) for the null hypothesis. Statistical power is calculated by finding the area under the alternative hypothesis distribution and outside the null hypothesis confidence interval.

            After running our experiment, we get a resulting conversion rate for both groups. If we calculate the difference between the conversion rates, we end up with a result, the difference or the effect of the web page design change, not showing user reviews. Our task is to determine which population this result came from, the null hypothesis or the alternative hypothesis.

            The area under the curve of the alternative hypothesis is equal to 1. If the alternative design (no evaluations) is actually better, the power is the probability that we accept the alternative hypothesis and reject the null hypothesis and is equal to the area shaded in green (true positive). The opposite area under the alternative curve is the probability of not rejecting the null hypothesis and rejecting the alternative hypothesis (false negative). This is known as beta A/B testing or hypothesis testing and is shown below.        

            If the null hypothesis is true and there really is no difference between the control and test groups, the significance level is the probability that we reject the null hypothesis and accept the alternative hypothesis (false positive). A false positive is when we mistakenly conclude that the new design is better. This value is low because we want to limit this probability.

            Often, an issue will be provided with a desired confidence level rather than a significance level. A typical 95% confidence level for an A/B test corresponds to a significance level of 0.05.   

            Experiments are normally configured for a minimum desired power of 80%. If our new design is indeed better, we want our experiment to show that there is at least an 80% probability that this is the case. We know that if we increase the sample size for each group, we will decrease the pooled variance for our null and alternative hypothesis. This will make our distributions much narrower and can increase statistical power. Let's take a look at how sample size will directly affect our results. 

    > **Execution #5 - Influence of Sample Size on A/B Testing**        



Python code that performs the same calculation for the minimum sample size:

    $$ n_A = k*n_B $$

$$ n_B = (\frac{p_A(1-p_A)}{k}+p_B(1-p_B)) (\frac{Z_{1-\alpha} + Z_{1-\beta}}{p_A-p_B})^{2}$$

$$ n = \frac{2(\bar{p})(1-\bar{p})(Z_{1-\beta}+Z_{1-\alpha})^2}{(p_B-p_A)^2}$$