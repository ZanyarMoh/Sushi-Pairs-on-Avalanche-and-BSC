import pandas as pd

file1 = open('pairs_list_AVAX.txt', 'r')
avax_kashi_pairs = file1.readlines()

file2 = open('address_list_AVAX.txt', 'r')
avax_address_list = []
for address in file2:
    avax_address_list.append(address[7:])
file3 = open('info_list_AVAX.txt', 'r')
avax_info = file3.readlines()

info_counter = 0
all_data = [['Asset/Collateral', 'Pool Address', 'TVL', 'Borrowed', 'Supply APR', 'Available', 'Borrow APR']]
for i in range(len(avax_kashi_pairs)):
    data = []
    data.append(avax_kashi_pairs[i].replace('\n', ''))
    data.append(avax_address_list[i].replace('\n', ''))
    
    data.append(avax_info[info_counter].replace('\n', ''))
    info_counter += 1
    data.append(avax_info[info_counter].replace('\n', ''))
    info_counter += 1
    data.append(avax_info[info_counter].replace('\n', ''))
    info_counter += 1
    data.append(avax_info[info_counter].replace('\n', ''))
    info_counter += 1
    data.append(avax_info[info_counter].replace('\n', ''))
    info_counter += 1
    all_data.append(data)
avax_kashi_pairs = pd.DataFrame(all_data[1:], columns=all_data[0])
avax_kashi_pairs.to_csv('avax_kashi_pairs.csv')
