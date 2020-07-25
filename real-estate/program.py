import os
import csv

try:
    import statistics
except:
    #error code instead
    import statistics_standin_for_py2 as statistics

from data_types import Purchase

def print_heaer():
    print('---------------------------------------')
    print('      Real Estate Data Mining App')
    print('---------------------------------------')
    print()

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder,'data','SacramentoRealEstateTransactions2008.csv')

def load_file_basic(filename):
    # with open(filename, 'r', encoding='utf-8') as f: #python3 - encoding is OK
    with open(filename, 'r') as f:
        header = f.readline()
        print('found header: ', header)

        lines = []
        for line in f:
            line_data = line.split(',')
            lines.append(line_data)
        
        print(lines[:5])

def load_file(filename):
    with open(filename, 'r') as f:
        # read by DictReader()
        reader = csv.DictReader(f)
        purchases = []
        for row in reader:
            # print(row)
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        # print(purchases[0].__dict__)

        # read by reder()
        # header = f.readline()
        # print(header)
        # reader = csv.reader(f, delimiter=',')

        # for row in reader:
        #     print(type(row), row)
        #     beds = row[4]
    return purchases
            
def query_data(data):
    data.sort(key=lambda x: x.price)
    high_purchase = data[-1]
    print('The most expensive house is ${:,}'.format(high_purchase.price))
    low_purchase = data[0]
    print('The lease expensive house is ${:,}'.format(low_purchase.price))

    # Average price house?
    prices = []
    for pur in data:
        prices.append(pur.price)
    ave_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(ave_price)))

    # average price of 2 bedrooms house
    prices = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)
    ave_price = statistics.mean(prices)
    print('The average home price of a 2-bedroom home is ${:,}'.format(int(ave_price)))

    # ** Make List with condition
    prices = [
        p.price # projection or items
        for p in data # the set to process
    ]
    ave_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(ave_price)))

    two_bed_homes = [
        p # projection or items
        for p in data  # the set to process
        if p.beds == 2 # test / condition
    ]
    ave_price = statistics.mean([p.price for p in two_bed_homes])
    ave_baths = statistics.mean([p.baths for p in two_bed_homes])
    ave_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    # ave_sqft = statistics.mean([p.sq__ft for p in two_bed_homes[:5]]) # first 5 hosmes
    print('The average home price of a 2-bedroom home is ${:,}, baths={}, sq ft={:,}'
        .format(int(ave_price), round(ave_baths, 1), round(ave_sqft, 1)))

    # ** Make tuple with condition
    two_bed_homes2 = (
        p # projection or items
        for p in data  # the set to process
        if announce(p, '2-bedromms, found {}'.format(p.beds )) and p.beds == 2 # test / condition
    )
    homes = []
    for h in two_bed_homes2:
        if len(homes) > 5:
            break
        homes.append(h)
    ave_price = statistics.mean((announce(p.price, 'price') for p in homes))
    ave_baths = statistics.mean((p.baths for p in homes))
    ave_sqft = statistics.mean((p.sq__ft for p in homes))
    # ave_sqft = statistics.mean([p.sq__ft for p in two_bed_homes[:5]]) # first 5 hosmes
    print('The average home price of a 2-bedroom home is ${:,}, baths={}, sq ft={:,}'
        .format(int(ave_price), round(ave_baths, 1), round(ave_sqft, 1)))

def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item

def main():
    print_heaer()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


if __name__ == '__main__': 
    main()