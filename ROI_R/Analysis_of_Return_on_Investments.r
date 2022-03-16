# Analysis of Return on Investments with PortfolioAnalytics and PerformanceAnalytics packages

# Packages
install.packages("PortfolioAnalytics")
install.packages("quantmod")
install.packages("PerformanceAnalytics")
install.packages("zoo")
install.packages("plotly")
library(PortfolioAnalytics)
library(quantmod)
library(PerformanceAnalytics)
library(zoo)
library(plotly)

# Getting the stock data of companies listed on the american stock exchange
getSymbols(c("MSFT", "SBUX", "IBM", "AAPL", "^GSPC", "AMZN"))

# Creating a dataframe and adjusting the stock price
prices.data <- merge.zoo(MSFT[,6], SBUX[,6], IBM[,6], AAPL[,6], GSPC[,6], AMZN[,6])

# Calculating the return
returns.data <- CalculateReturns(prices.data)
returns.data <- na.omit(returns.data)

# Defining the names
colnames(returns.data) <- c("MSFT", "SBUX", "IBM", "AAPL", "^GSPC", "AMZN")

# Saving a vector with the return mean and covariance matrix
meanReturns <- colMeans(returns.data)
covMat <- cov(returns.data)

# Defining the name of assets in the investment portfolio
# This defines the portfolio specification
port <- portfolio.spec(assets = c("MSFT", "SBUX", "IBM", "AAPL", "^GSPC", "AMZN"))


# Adding constraints

# Box
port <- add.constraint(port, type = "box", min = 0.05, max = 0.8)

# Leverage
port <- add.constraint(portfolio = port, type = "full_investment")

# Generating random portfolios. This basically creates a viable portfolio set
# that satisfy the conditions (constraints)
# List of all available constraints:
# https://cran.r-project.org/web/packages/PortfolioAnalytics/vignettes/portfolio_vignette.pdf
rportfolios <- random_portfolios(port, permutations = 500000, rp_method = "sample")

# Getting the minimum variance of the investment portfolio
minvar.port <- add.objective(port, type = "risk", name = "var")
print(minvar.port)

# Optimizing
minvar.opt <- optimize.portfolio(returns.data, minvar.port, optimize_method = "random", rp = rportfolios)
print(minvar.opt)

# Generating maximum return from your investment portfolio
maxret.port <- add.objective(port, type = "return", name = "mean")

# Optimizing
maxret.opt <- optimize.portfolio(returns.data, maxret.port, optimize_method = "random", rp = rportfolios)

# Generating a vector of returns
minret <- 0.06/100
maxret <- c(maxret.opt$weights %*% meanReturns)
vec <- seq(minret, maxret, length.out = 100)

# Now that we have the minimum variance as well as the maximum return portfolios,
# we can build the most efficient investment frontier.
# Let's add a weight concentration objective as well as ensure that we don't have investment portfolios
# very concentrated.
eff.frontier <- data.frame(Risk = rep(NA, length(vec)),
                           Return = rep(NA, length(vec)), 
                           SharpeRatio = rep(NA, length(vec)))

frontier.weights <- mat.or.vec(nr = length(vec), nc = ncol(returns.data))
colnames(frontier.weights) <- colnames(returns.data)

?optimize.portfolio

# We can use the random optimization method (more efficient) or ROI (R Optimization Infrastructure)
# We will use random, but it is very time-consuming (a few hours)
for(i in 1:length(vec)){
  eff.port <- add.constraint(port, type = "return", name = "mean", return_target = vec[i])
  eff.port <- add.objective(eff.port, type = "risk", name = "var")

  eff.port <- optimize.portfolio(returns.data, eff.port, optimize_method = "random")
  
  eff.frontier$Risk[i] <- sqrt(t(eff.port$weights) %*% covMat %*% eff.port$weights)
  
  eff.frontier$Return[i] <- eff.port$weights %*% meanReturns
  
  eff.frontier$Sharperatio[i] <- eff.port$Return[i] / eff.port$Risk[i]
  
  frontier.weights[i,] = eff.port$weights
  
  print(paste(round(i/length(vec) * 100, 0), "% concluído..."))
}

feasible.sd <- apply(rportfolios, 1, function(x){
  return(sqrt(matrix(x, nrow = 1) %*% covMat %*% matrix(x, ncol = 1)))
})

feasible.means <- apply(rportfolios, 1, function(x){
  return(x %*% meanReturns)
})

feasible.sr <- feasible.means / feasible.sd


# Plot with Plotly
p <- plot_ly() %>%
  add_trace(x = feasible.sd, y = feasible.means, color = feasible.sr, 
             mode = "markers", type = "scattergl", showlegend = F,
             
             marker = list(size = 3, opacity = 0.5, 
                           colorbar = list(title = "Sharpe Ratio"))) %>% 
  
  add_trace(data = eff.frontier, x = ~Risk, y = ~Return, mode = "markers", 
            type = "scattergl", showlegend = F, 
            marker = list(color = "#F7C873", size = 5)) #%>% 


# Reshape
frontier.weights.melt <- reshape2::melt(frontier.weights)


q <- frontier.weights.melt %>%
      group_by(Var2) %>%
      plot_ly(x = ~Var1, y = ~value, type = "bar") %>%
      layout(title = "Pesos dos Portfolios Através da Fronteira", barmode = "stack",
             xaxis = list(title = "Index"),
             yaxis = list(title = "Pesos(%)", tickformat = ".0%"))

# Plot
p
q