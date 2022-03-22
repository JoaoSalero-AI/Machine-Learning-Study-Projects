# <font color='blue'>Netflix's Movie Recommender System</font>

## Part 1 Problem Definition

<p>
Netflix's goal is to connect people to the movies they love. To help customers find these movies, they've developed a world-class movie recommendation system: CinematchSM. Your job is to predict whether someone will like a movie based on how much they liked other movies or not. Netflix uses these predictions to make personal movie recommendations based on each customer's unique tastes. And while <b> Cinematch </b> is doing very well, it can always be improved.
</p>
<p> There are several interesting alternative approaches to how Cinematch works that netflix hasn't tried. Some are described in the literature, others are not. We're curious to know if any of them can beat Cinematch by making better predictions. Because frankly, if there's a much better approach, it could make a big difference to our customers and our business. </p>

Goals:

1. Predict the rating a user would give a movie they haven't rated yet.
2. Minimize the difference between predicted and actual assessment (RMSE and MAPE).

Restrictions:

1. Some form of interpretability.

<p>
Netflix provided a lot of anonymized rating data and a prediction accuracy bar that is 10% better than what Cinematch can do on the same training dataset. Accuracy is a measure of how closely predicted movie ratings match subsequent actual ratings.
</p>


 - [Netflix Proze](https://www.netflixprize.com/rules.html)
 - [Dataset by Kaggle](https://www.kaggle.com/netflix-inc/netflix-prize-data)

 ---

 ### Note #01: Attention before Exploratory Data Analysis  
     Working with 100 Million Records is not easy and it can consume a lot of computational resources. Some tips:

    1- Close all files and software on your computer. Leave only what is really necessary;
    2- Consider using a cloud environment or even a cluster of computers if possible;
    3- Reduce the size of each file. Here are some suggestions for "File Splitter" software:

        http://www.fastfilejoiner.com/
        https://www.gdgsoft.com/gsplit/download
        http://www.kcsoftwares.com/?kfk
--- </n>
## Part 2 Soon