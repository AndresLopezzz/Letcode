class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

## Lo que se hizo aquí fué que se pensó como una grafica, en la que el primer dia, el cual tiene un precio especifico, que es el numero en lista, se compara al dia siguiente,
## para poder ver primero cual es el precio más bajo en el que se puede comprar para luego tener más beneficio, y se busca para comprar el que de más ganancia por lo que se itera
## y se compara la ganancia actual de la iteracion con la historica "maxP" para ver si es la ganancia mayor o cambiarla

#SOLUCION EN UNA LINEA POR ALGUNA RAZON:
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return max(j - k for j,k in zip(prices, accumulate(prices,min)))