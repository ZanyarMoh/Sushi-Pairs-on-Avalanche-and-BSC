import pandas as pd

file1 = open('pairs_list_BSC.txt', 'r')
bsc_kashi_pairs = file1.readlines()

file2 = open('address_list_BSC.txt', 'r')
bsc_address_list = []
for address in file2:
    bsc_address_list.append(address[7:])
file3 = open('info_list_BSC.txt', 'r')
bsc_info = file3.readlines()

info_counter = 0
all_data = [['Asset/Collateral', 'Pool Address', 'TVL', 'Borrowed', 'Supply APR', 'Available', 'Borrow APR']]
for i in range(len(bsc_kashi_pairs)):
    data = []
    data.append(bsc_kashi_pairs[i].replace('\n', ''))
    data.append(bsc_address_list[i].replace('\n', ''))
    
    data.append(bsc_info[info_counter].replace('\n', ''))
    info_counter += 1
    data.append(bsc_info[info_counter].replace('\n', ''))
    info_counter += 1
    data.append(bsc_info[info_counter].replace('\n', ''))
    info_counter += 1
    data.append(bsc_info[info_counter].replace('\n', ''))
    info_counter += 1
    data.append(bsc_info[info_counter].replace('\n', ''))
    info_counter += 1
    all_data.append(data)
bsc_kashi_pairs = pd.DataFrame(all_data[1:], columns=all_data[0])
bsc_kashi_pairs.to_csv('bsc_kashi_pairs.csv')
