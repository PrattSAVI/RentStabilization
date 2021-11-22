
#%%
import os
import time
import pandas as pd
import wget
pd.set_option("max_columns",None)

PERIODS = {
    #'20120817 - Quarterly Property Tax Bill.pdf',
    ('20180601', 'SOA'): 'June 1, 2018 - Quarterly Property Tax Bill.pdf',
    ('20180223', 'SOA'): 'February 23, 2018 - Quarterly Property Tax Bill.pdf',
    ('20180115', 'NOPV'): 'January 15, 2018 - Notice of Property Value.pdf',
    ('20171117', 'SOA'):  'November 17, 2017 - Quarterly Property Tax Bill.pdf',
    ('20170825', 'SOA'):  'August 25, 2017 - Quarterly Property Tax Bill.pdf',
    ('20170602', 'SOA'): 'June 2, 2017 - Quarterly Property Tax Bill.pdf',
    ('20170224', 'SOA'): 'February 24, 2017 - Quarterly Property Tax Bill.pdf',
    ('20170115', 'NOPV'): 'January 15, 2017 - Notice of Property Value.pdf',
    ('20161118', 'SOA'): 'November 18, 2016 - Quarterly Property Tax Bill.pdf',
    ('20160826', 'SOA'): 'August 26, 2016 - Quarterly Property Tax Bill.pdf',
    ('20160219', 'SOA'): 'February 19, 2016 - Quarterly Property Tax Bill.pdf',
    ('20160115', 'NOPV'): 'January 15, 2016 - Notice of Property Value.pdf',
    ('20160115', 'TAR'): 'January 15, 2016 - Tentative Assessment Roll.html',
    ('20160603', 'SOA'): 'June 3, 2016 - Quarterly Property Tax Bill.pdf',
    ('20080822', 'SOA'): 'August 22, 2008 - Quarterly Statement of Account.html',
    ('20140822', 'SOA'): 'August 22, 2014 - Quarterly Property Tax Bill.pdf',
    ('20130823', 'SOA'): 'August 23, 2013 - Quarterly Property Tax Bill.pdf',
    ('20110826', 'SOA'): 'August 26, 2011 - Quarterly Statement of Account.pdf',
    ('20100827', 'SOA'): 'August 27, 2010 - Quarterly Statement of Account.pdf',
    ('20090828', 'SOA'): 'August 28, 2009 - Quarterly Statement of Account.pdf',
    ('20081219', 'SOA'): 'December 19, 2008 - Quarterly Statement of Account.html',
    ('20110218', 'SOA'): 'February 18, 2011 - Quarterly Statement of Account.pdf',
    ('20090220', 'SOA'): 'February 20, 2009 - Quarterly Statement of Account.html',
    ('20150220', 'SOA'): 'February 20, 2015 - Quarterly Property Tax Bill.pdf',
    ('20140221', 'SOA'): 'February 21, 2014 - Quarterly Property Tax Bill.pdf',
    ('20130222', 'SOA'): 'February 22, 2013 - Quarterly Property Tax Bill.pdf',
    ('20120224', 'SOA'): 'February 24, 2012 - Quarterly Statement of Account.pdf',
    ('20100226', 'SOA'): 'February 26, 2010 - Quarterly Statement of Account.pdf',
    ('20050115', 'NOPV'): 'January 15, 2005 - Notice of Property Value.html',
    ('20060115', 'NOPV'): 'January 15, 2006 - Notice of Property Value.html',
    ('20070115', 'NOPV'): 'January 15, 2007 - Notice of Property Value.html',
    ('20080115', 'NOPV'): 'January 15, 2008 - Notice of Property Value.html',
    ('20090115', 'NOPV'): 'January 15, 2009 - Notice of Property Value.html',
    ('20100115', 'NOPV'): 'January 15, 2010 - Notice of Property Value.pdf',
    ('20100115', 'TAR'): 'January 15, 2010 - Tentative Assessment Roll.html',
    ('20110115', 'NOPV'): 'January 15, 2011 - Notice of Property Value.pdf',
    ('20110115', 'TAR'): 'January 15, 2011 - Tentative Assessment Roll.html',
    ('20120115', 'NOPV'): 'January 15, 2012 - Notice of Property Value.pdf',
    ('20120115', 'TAR'): 'January 15, 2012 - Tentative Assessment Roll.html',
    ('20130115', 'NOPV'): 'January 15, 2013 - Notice of Property Value.pdf',
    ('20130115', 'TAR'): 'January 15, 2013 - Tentative Assessment Roll.html',
    ('20140115', 'NOPV'): 'January 15, 2014 - Notice of Property Value.pdf',
    ('20140115', 'TAR'): 'January 15, 2014 - Tentative Assessment Roll.html',
    ('20150115', 'NOPV'): 'January 15, 2015 - Notice of Property Value.pdf',
    ('20150115', 'TAR'): 'January 15, 2015 - Tentative Assessment Roll.html',
    ('20110610', 'SOA'): 'June 10, 2011 - Quarterly Statement of Account.pdf',
    ('20100611', 'SOA'): 'June 11, 2010 - Quarterly Statement of Account.pdf',
    ('20080613', 'SOA'): 'June 13, 2008 - Quarterly Statement of Account.html',
    ('20150605', 'SOA'): 'June 5, 2015 - Quarterly Property Tax Bill.pdf',
    ('20090606', 'SOA'): 'June 6, 2009 - Quarterly Statement of Account.pdf',
    ('20140606', 'SOA'): 'June 6, 2014 - Quarterly Property Tax Bill.pdf',
    ('20130607', 'SOA'): 'June 7, 2013 - Quarterly Property Tax Bill.pdf',
    ('20120608', 'SOA'): 'June 8, 2012 - Quarterly Property Tax Bill.pdf',
    ('20111118', 'SOA'): 'November 18, 2011 - Quarterly Statement of Account.pdf',
    ('20101119', 'SOA'): 'November 19, 2010 - Quarterly Statement of Account.pdf',
    ('20091120', 'SOA'): 'November 20, 2009 - Quarterly Statement of Account.pdf',
    ('20141121', 'SOA'): 'November 21, 2014 - Quarterly Property Tax Bill.pdf',
    ('20131122', 'SOA'): 'November 22, 2013 - Quarterly Property Tax Bill.pdf',
    ('20121130', 'SOA'): 'November 30, 2012 - Quarterly Property Tax Bill.pdf',
}

PERIODS = {
    ('20201121', 'SOA'):  'Nov 21, 2020 - Quarterly Property Tax Bill.pdf',
    #('20191119', 'SOA'):  'November 29, 2019 - Quarterly Property Tax Bill.pdf',
    #('20171117', 'SOA'):  'November 17, 2017 - Quarterly Property Tax Bill.pdf',
}

BOROUGHS = {
    'MN': '1',
    'BX': '2',
    'BK': '3',
    'QN': '4',
    'SI': '5',
    }

print('Yes!')

#%% Multiple Dwelling Registeration
# I am using this data as the basis of the scraping. instead of uing the whole Pluto
#https://data.cityofnewyork.us/Housing-Development/Multiple-Dwelling-Registrations/tesw-yqqr

dw = pd.read_csv( r"C:\Users\csucuogl\Downloads\Multiple_Dwelling_Registrations.csv" )
dw = dw.drop('HouseNumber,LowHouseNumber,HighHouseNumber,StreetName,StreetCode,Zip,CommunityBoard,LastRegistrationDate,RegistrationEndDate'.split(",") , axis = 1)
dw['BoroID'] = dw['BoroID'].astype(str)
dw['Block'] = dw['Block'].astype(str)
dw['Lot'] = dw['Lot'].astype(str)

#Construct BBL for the multi-dwell units
dw['bbl'] = dw['BoroID'] + dw['Block'].str.zfill(5) + dw['Lot'].str.zfill(4)
dw = dw.sort_values(by="bbl")
dw = dw.drop_duplicates(subset='bbl',keep='first')

dw['count'] = [i+1 for i in range(len(dw))]
dw.head()

#%% Scrape Here

#Just incase. I don't thnk this is necessary


data_folder = r'C:\Users\csucuogl\Desktop\Tax_Scraped'

def get_Download(bbl,period,doc_type):
    
    #This is the new format for web queries
    url2= 'https://a836-edms.nyc.gov/dctm-rest/repositories/dofedmspts/StatementSearch?' + \
            'bbl={bbl}&stmtDate={period}&stmtType={doc_type}'.format(
                period=period, bbl=bbl, doc_type=doc_type)

    file_path = "{period}_{bbl}.pdf".format(period=period, bbl=bbl, doc_type=doc_type)
    #wget waits for the data to be downloaded
    response = wget.download(url=url2, out= os.path.join(data_folder,file_path) )

    time.sleep( 0.1 )

#Get files in the folder
def get_Done():
    files = [i.split('.')[0].split("_") for i in os.listdir( data_folder )]
    df = pd.DataFrame( columns = ['date','bbl'] , data = files)
    return df

downloaded = get_Done()

downloaded.head()

#%%
for p in PERIODS: #For each November
    print( p )
    period = p[0]
    doc_type = p[1]
    f_data = downloaded[ downloaded['date'] == period ]
    dw2 = dw[ ~dw['bbl'].isin( f_data['bbl'].tolist() ) ]

    for i,r in dw2.iterrows(): 

        get_Download( r['bbl'] , period , doc_type )
        
        if r['count'] % 250 == 0: print( "{x}% is done".format( x = int(r['count']*100 / len(dw))) )


# %%
dw2

# %%
