# ETF data - Market Sentiment Analysis
In our the final project, we continue the study in ETF_Analysis.ipynb but focus on the market sentiment analysis. The goal is to  find out the relationship between ETF price and market sentiment, and build a model that could predict ETF price.  

## Hypothesis  
* The price has a positive correlation with news sentiment score and popularity online.  
* There is some relationship between ETF price and quality  
* Different industry will react differently when facing the same event, so as the related ETF price reaction and fluctuation to news.  

## Code structure  
**[Crawler]**      
- [x] ETF data(1 for each sector)  
- [x] finance news(Reuters/CNBC)   
- [x] google trend(interest over time)  
- [x] set up the data files    

**[Sentiment Score]**      
- [x] sentiment word list  
- [x] sentiment model  
- [x] get data of each sector     
 

**[Analysis]** 
- [x] google trend    
- [x] visualize ETF data(Technical Analysis)  
- [x] check whether the news is leading indicator  
- [x] price and volume relationship  

**[Invest Strategy]**      
- [ ] backtesting  
- [x] strategy#1 MA_crossover     
- [x] strategy#2 RSI  
- [x] strategy#3 OBA(price-volume)    
- [x] strategy#4 market sentiment(base on the score)    



