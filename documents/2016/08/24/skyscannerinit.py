

from skyscanner.skyscanner import FlightsCache
flights_cache_service = FlightsCache('jo589288824052881828733295359792')


origin = input("Please enter where youre traveling from")

dest = input("Please enter where youre traveling to")

result = flights_cache_service.get_result(
    country='US',
    currency='USD',
    locale='en-US',
    originplace=origin+'-sky',
    destinationplace=dest+'-sky',
    outbounddate='2016-08-28',
    inbounddate='2016-08-31',
    adults=1).parsed


cheaps =  result['Itineraries']


cheaps[0]['PricingOptions']
print()

# for i in result:
# print(i)