# ETF data - Market Sentiment Analysis
As the final project, continue the study in ETF_Analysis.ipynb but focus on the market sentiment analysis. The goal is to  find out the relationship between ETF price and market sentiment, and build a model that could indicate ETF price.  

## Hypothesis  
* The price has a positive correlation with news sentiment score and popularity online.  
* There's some relationship between ETF price and quality  
* Different industry will react differently when facing the same event, so as the related ETF price reaction and fluctuation to news.  

## Code structure  
**[Crawler]**      
- [x] ETF data(1 for each sector)  
- [x] finance news(Reaters/CNBC/Google Finance)   
- [x] google trend(interest over time)  
- [x] set up the data files    

**[Sentiment Score]**      
- [x] sentiment word list  
- [ ] sentiment model  
- [ ] get data of each sector     
 

**[Analysis]** 
- [x] google trend    
- [ ] visualize ETF data(Technical Analysis)  
- [ ] check whether the news is leading indicator  
- [x] price and volume relationship  

**[Invest Strategy]**      
- [ ] backtesting  
- [x] strategy#1 MA_crossover     
- [x] strategy#2 RSI  
- [ ] strategy#3 OBA(price-volume)    
- [ ] strategy#4 market sentiment(base on the score)    



