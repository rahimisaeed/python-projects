
with open('sample_string_data.txt') as sample_text:
    daily_sales = sample_text.read()
sample_text.close()

daily_sales_replaced = daily_sales.replace(';,;', ';')
daily_transactions = daily_sales_replaced.split(',')


daily_transactions_split = []
for data in daily_transactions:
    daily_transactions_split.append(data.split(';'))


transactions_clean = []
for data in daily_transactions_split:
    transaction_clean = []
    for element in data:
        transaction_clean.append(element.strip(" "))
    transactions_clean.append(transaction_clean)

costumer = []
sale = []
thread_sold = []

for data in transactions_clean:
    costumer.append((data[0].strip('\n')).strip(' '))
    sale.append(((data[1].strip(' ')).strip('\n')).strip('$'))
    thread_sold.append((data[2].strip('\n')).replace('&', '-'))


total_sales = 0
for item in sale:
    total_sales += float(item)
