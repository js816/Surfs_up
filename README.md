# Overview of the project 

## Purpose

The purpose of this analysis was to investigate and understand the weather on the island of Oahu in Hawaii--site of my proposed surf and shake shop.  My shop will feature a wide variety of items related to surfing.  It will also offer sweet and heat-busting treats including popular flavors of ice cream and shakes.  This analysis generated the summary statistics of local temperature observations during the months of June and December.  

## Data analyzed

A database of nearly 20,000 temperature observations from nine weather stations was provided.  These observations occurred from January 1, 2010 through August 23, 2017.  


# Results

## June temperatures

When filtered for observations made during June from the eight years of data available, 1,700 unique values were analyzed.  The average temperature observed during June was 74.9°F while the median was 75°.  The minimum observed temperature was 64° and the maximum was 85°.  All summary statistics are shown in the table below.

![Jun_temps](https://user-images.githubusercontent.com/82730954/123551618-3313ad00-d738-11eb-9fe5-c0d319a35597.PNG)

## December temperatures

During the month of December in the seven years available, there were 1,517 observations that averaged 71.0°F.  The median was also 71°.  The lowest temperature observed was 56° and the highest was 83°.  All summary statistics are shown on the table below.

![Dec_temps](https://user-images.githubusercontent.com/82730954/123551625-3c9d1500-d738-11eb-8221-ea3ba6196da8.PNG)

## Key points

From the analysis of the data, spanning nearly eight years, several key points can be drawn:

- The average temperature on Oahu falls less than 4° from June to December.  Therefore, there’s likely to be strong demand for all things surfing and ice cream in both the summer and winter months.

- December’s standard deviation is slightly higher than that that observed in June.  The minimum observation in December was only 8° less than that observed in June.  However, December’s high temperature and 3rd quartile value fall only 2-3° below those of June.  The 1st quartile values differ only by 4°.  Again, the data support that the demand will likely remain high year-round.

- The interquartile range (IQR) measures the variance of the middle half of the data--from the 25th percentile to the 75th percentile.  For both June and December, half of the observed temperatures have a narrow distribution.  The IQR for June was 4° and for December was 5°.  The data continue to support a steady demand for surfing and ice cream.  Histograms for both periods of analysis are shown below.

![Jun_hist](https://user-images.githubusercontent.com/82730954/123551630-46bf1380-d738-11eb-870e-5b352ea9e2bb.PNG)

![Dec_hist](https://user-images.githubusercontent.com/82730954/123551635-4a529a80-d738-11eb-9ec3-8ea25e31c068.PNG)

# Summary

Overall, the data investigated thus far point to a steady demand for ice cream and all things related to surfing.  The small variance in the data support high demand year-round.

# Opportunities for further investigation

There are several other queries that could provide valuable insight.  For example, also analyzing other weather data such as precipitation, cloudiness, humidity, and the feels-like temperature would provide additional insight to either strengthen or weaken the results of the analysis thus far.

Additionally, to determine if there are large variances based upon location on Oahu, the data could be grouped by each observation station.

The analysis could also be updated to include more recent data to investigate if the patterns observed above have continued to hold true.

The code developed for this study could easily be adapted to evaluate data for other locations around Hawaii to help pinpoint prime places for further expansion of the surf and shake concept.
