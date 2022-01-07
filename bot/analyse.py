from bot import analyse_post, bot_activation
import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def trois_pop():
    symb = bot_activation()
    populaire = sorted(symb, key = symb.get, reverse=True)[:3]
    start = "2016-01-01"
    end = "2021-01-01"
    one = yf.download(populaire[0], start, end)
    two = yf.download(populaire[1], start, end)
    three = yf.download(populaire[2], start, end)

    one['Open'].plot(label = populaire[0], figsize = (15,7))
    two['Open'].plot(label = populaire[1])
    three['Open'].plot(label = populaire[2])
    
    plt.title(('Stock Prices of the three most popular stocks on Reddit',populaire), fontdict=None, loc='center', pad=None)
    plt.legend()
    plt.show()
trois_pop()

