
import pandas as pd 
import dataframe as df

# the file variable input for these functions is a deserialized dataframe, it is a pandas.dataframe object
def daily_roi_income(file):
    # bar graph
    #for Roi Income find the dates and credit received on that day
    #csv_df = pd.read_csv(file)
    #return the Date & Credit values where Remark is 'Roi Income'
    roi = file.loc[file.Remark=='Roi Income', ['Date','Credit', 'Debit']]

    return roi

def sum_roi_income(file):
    # number tab
    #total return on trading pool holdings only for present moment
    #csv_df = pd.read_csv(file)
    sum_roi = file.loc[file.Remark=='Roi Income', ['Date','Credit']]
    sum_roi = sum_roi.Credit.sum()
    sum_roi = str(round(sum_roi,6)) + ' ' + 'BTC'
    
    return sum_roi

def sum_binary_income(file):
    # number tab
    #total return from binary bonus
    #csv_df = pd.read_csv(file)
    sum_binary = file.loc[file.Remark=='Binary Income', ['Date','Credit']]
    sum_binary = sum_binary.Credit.sum()
    sum_binary = round(sum_binary,6)

    return sum_binary
#print(sum_binary_income())


def cumsum_total_income(file):
    # line graph for dashboard
    # determine the cumulative incomes for MTI over time
    # for x in file:
    #     df = pd.read_json(x, orient='columns') # deserialis json to dataframe
    #     #print(df)
    #     return df
    #df = pd.read_json(file[0], orient='columns') # deserialised dataframe
    #print(df)
    #df = pd.DataFrame(file)
    df = file[file.Remark.isin(['Binary Income','Referral Bonus','Roi Income'])][['Date','Credit']]
    #print(df)
    df['Income'] = df['Credit'].cumsum() 
    #print(df)
    
    return df #returns dataframe
#print(total_income)    


def sum_total_income(file):
    # number tab for dashboard
    csv_df = cumsum_total_income(file)
    # Sum of incomes for present time
    sum_income = str(csv_df['Credit'].sum().round(6)) + ' ' + 'BTC'
    
    return sum_income  


def cumsum_current_holdings(file):
    # line graph for dashboard
    # this is the credit minus the debit column to give current holdings over time
    #  Total holdings 
    csv_data = pd.read_csv(file)
    holdings_cumsum = csv_data.loc[:, ['Date', 'Credit','Debit']]
    holdings_cumsum['Difference'] = holdings_cumsum['Credit'] - holdings_cumsum['Debit']
    #holdings_t.drop('Credit', axis=1)
    holdings_cumsum['Holdings'] = holdings_cumsum['Difference'].cumsum()
    holdings_cumsum = holdings_cumsum[['Date','Holdings']]
    
    return holdings_cumsum



def sum_current_holdings(file):
    # number tab for dashboard
    # this is the credit minus the debit column to give current holdings total sum for current time
    # Total holdings 
    holdings_sum = cumsum_current_holdings(file)
    holdings_sum = holdings_sum['Holdings'].sum().round(6)
    
    return holdings_sum

#print(holdings_cumsum()) 