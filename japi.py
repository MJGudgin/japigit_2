import urllib.request

def getStockData(symbol):

	queryURL='https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + symbol + '&apikey=U6RW72ZH8YPZ1WLS'

	connection = urllib.request.urlopen(queryURL)

	responseString = connection.read().decode()
	
	return responseString
	
def main():

	i = "null"
	while i != "quit":
		i = input("Enter a stock symbol: ")
		if i != "quit":
			print()
			APIReturn = getStockData(i)
			print(APIReturn)
			
			s = APIReturn.split('price": "')[1]
			s = s.split('"')[0]
			print()
			print("The current price of " + i + " is: $" + s)
			print()
		

		
main()