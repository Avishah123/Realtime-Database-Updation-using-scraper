import pandas as pd

list_previous = [['', 'NSEFUT', '(AK) AKD-HR', 'BANKNIFTY 27MAY2021', '0', '0.00', '200', '32,265.20', '-201 ', '32,265.20', '34,202.90', '-387,540.00', ''], ['', 'NSEFUT', '(AK) AKD-HR', 'ITC 27MAY2021', '3200', '213.10', '0', '0.00', '3200 ', '213.10', '209.95', '-10,080.00', ''], ['', 'NSEFUT', '(AK) AKD-HR', 'NATIONALUM 27MAY2021', '17000', '71.70', '0', '0.00', '17000 ', '71.70', '72.20', '8,500.00', ''], ['', 'NSEFUT', '(AK) AKD-HR', 'NIFTY 27MAY2021', '0', '0.00', '450', '14,714.95', '-450 ', '14,714.95', '15,132.00', '-187,672.50', ''], ['', 'MCXFUT', '(AKH) AKH-NVD', 'GOLD 04JUN2021', '100', '47,676.00', '100', '48,295.75', '0 ', '0.00', '48,420.00', '61,975.45', ''], ['', 'NSEFUT', '(AKH) AKH-NVD', 'BANDHANBNK 27MAY2021', '1000', '281.70', '0', '0.00', '1000 ', '281.70', '299.25', '17,550.00', ''], ['', 'NSEFUT', '(AKH) AKH-NVD', 'BHARTIARTL 27MAY2021', '1851', '562.85', '0', '0.00', '1851 ', '562.85', '528.70', '-63,211.65', '']]
list_current = [['', 'NSEFUT', '(AK) AKD-HR', 'BANKNIFTY 27MAY2021', '0', '0.00', '200', '32,265.20', '-200 ', '32,265.20', '34,202.90', '-387,540.00', ''], ['', 'NSEFUT', '(AK) AKD-HR', 'ITC 27MAY2021', '3200', '213.10', '0', '0.00', '3200 ', '213.10', '209.95', '-10,080.00', ''], ['', 'NSEFUT', '(AK) AKD-HR', 'NATIONALUM 27MAY2021', '17000', '71.70', '0', '0.00', '17000 ', '71.70', '72.20', '8,500.00', ''], ['', 'NSEFUT', '(AK) AKD-HR', 'NIFTY 27MAY2021', '0', '0.00', '450', '14,714.95', '-450 ', '14,714.95', '15,132.00', '-187,672.50', ''], ['', 'MCXFUT', '(AKH) AKH-NVD', 'GOLD 04JUN2021', '100', '47,676.00', '100', '48,295.75', '0 ', '0.00', '48,420.00', '61,975.45', ''], ['', 'NSEFUT', '(AKH) AKH-NVD', 'BANDHANBNK 27MAY2021', '1000', '281.70', '0', '0.00', '1000 ', '281.70', '299.25', '17,550.00', ''], ['', 'NSEFUT', '(AKH) AKH-NVD', 'BHARTIARTL 27MAY2021', '1851', '562.85', '0', '0.00', '1851 ', '562.85', '528.70', '-63,211.65', '']]

df_current_data = pd.DataFrame(list_previous)
df_current_data.columns = ['Decoy', 'Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'positionNET',
                              'Avi',
                              'Avg_qty', 'Net', 'Nets']
y = df_current_data.drop('Decoy', axis=1, inplace=True)
z = df_current_data.drop('Nets', axis=1, inplace=True)




df_previous_data = pd.DataFrame(list_current)
df_previous_data.columns = ['Decoy', 'Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'positionNET',
                              'Avi',
                              'Avg_qty', 'Net', 'Nets']
y = df_previous_data.drop('Decoy', axis=1, inplace=True)
z = df_previous_data.drop('Nets', axis=1, inplace=True)






# Will pass it as a list
# 1. Connvert the list into pandas dataframe
# 2. compare the data
# 3. convert the dataframe into a list

def compare(df_current,df_previous):
    df1 = df_previous
    df2 = df_current

    df1.columns = ['Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'position-NET',
                       'Avi',
                       'Avg_qty', 'Net']

    df2.columns = ['Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'position-NET',
                   'Avi',
                   'Avg_qty', 'Net']

    df_join = df1.merge(right=df2,
                        left_on=df1.columns.to_list(),
                        right_on=df2.columns.to_list(),
                        how='outer')
    # %%
    df1.rename(columns=lambda x: x + '_file1', inplace=True)
    df2.rename(columns=lambda x: x + '_file2', inplace=True)
    # %%
    df_join = df1.merge(right=df2,
                        left_on=df1.columns.to_list(),
                        right_on=df2.columns.to_list(),
                        how='outer')

    records_present_in_df2_not_in_df1 = df_join.loc[
        df_join[df1.columns.to_list()].isnull().all(axis=1), df2.columns.to_list()]


    # %%
    df2 = records_present_in_df2_not_in_df1

    df2.columns = ['Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'position-NET',
                   'Avi',
                   'Avg_qty', 'Net']

    print(df2)

    return df2





def compare_col_wise_final(df_current,df_previous):
    df2 = df_previous
    df1 = df_current

    df1.columns = ['Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'positionNET',
                   'Avi',
                   'Avg_qty', 'Net']

    df2.columns = ['Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'positionNET',
                   'Avi',
                   'Avg_qty', 'Net']



    df_join = df1.merge(right=df2,
                        left_on=df1.columns.to_list(),
                        right_on=df2.columns.to_list(),
                        how='outer')
    # %%
    df1.rename(columns=lambda x: x + '_file1', inplace=True)
    df2.rename(columns=lambda x: x + '_file2', inplace=True)
    # %%
    df_join = df1.merge(right=df2,
                        left_on=df1.columns.to_list(),
                        right_on=df2.columns.to_list(),
                        how='outer')

    records_present_in_df2_not_in_df1 = df_join.loc[
        df_join[df1.columns.to_list()].isnull().all(axis=1), df2.columns.to_list()]

    # %%
    df6 = records_present_in_df2_not_in_df1
    print(' Data in df2 not in df1')
    print(df6)

    df6.columns = ['Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'positionNET',
                   'Avi',
                   'Avg_qty', 'Net']

    df1.columns = ['Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'positionNET',
                   'Avi',
                   'Avg_qty', 'Net']

    df2.columns = ['Name', 'Subname', 'Subname2', 'QTY', 'Avg', 'Avg_price', 'position', 'positionNET',
                   'Avi',
                   'Avg_qty', 'Net']

    change_avg = df2[~df2.positionNET.isin(df1.positionNET)]
    # print('Printing change in Avg here')
    # print(change_avg)
    df3 =change_avg
    print('Below is the change in postionNet')
    print(df3)

    print('Below we will print the combined of both')
    final =pd.concat([df6,change_avg])
    print(final)


compare_col_wise_final(df_current_data,df_previous_data)

# def compare_main(current,previous):
#     if(len(current.index) == len(previous.index)):
#         print('Enter the first if statement of the compare_main function')
#         y =compare_col_wise(current,previous)
#         print('The value of y is printed here')
#         print(y)
#         # Return Data to List Final
#     else :
#         print('Entered the else part of the compare_main function')
#         temp_df = compare(current,previous)
#         previous.append(temp_df, ignore_index=True)
#         print('The value of x is printed here')
#         x= compare_col_wise(current,previous)
#         print(x)
# #       #Temp panda dataframe
#
#
#
#
# # Function Name , parameters passing through it and Type of input to it
#
# 1.
