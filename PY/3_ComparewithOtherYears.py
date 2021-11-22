#%%
import pandas as pd
import geopandas as gpd
import wget
import time
from pdfminer.high_level import extract_text
import os

d20 = pd.read_csv( r"C:\Users\csucuogl\Desktop\20201121_RentStabilzedUnits.csv" )
d18 = pd.read_csv( r"C:\Users\csucuogl\Dropbox\TASC Application\DATA\RentSt\rentstab_counts_for_pluto_19v1_bbls.csv")

print( 'Units at 20: {} \nUnits at 18: {}'.format( len(d20),len(d18)) )

display( d20.head() )
display( d18.head() )

# %%

#Filter 2018 data by 2020 bbls to get the difference
ddif = d18[ ~d18['ucbbl'].isin( d20['bbl'].tolist() ) ]

print( '{} Units are not matching'.format( len( ddif) ) )
display( ddif.head() )

# %% Download a few and check

data_folder = r'C:\Users\csucuogl\Desktop\Tax_Scraped'

def get_Download(bbl,period,doc_type):
    #This is the new format for web queries
    url2= 'https://a836-edms.nyc.gov/dctm-rest/repositories/dofedmspts/StatementSearch?' + \
            'bbl={bbl}&stmtDate={period}&stmtType={doc_type}'.format(
                period=period, bbl=bbl, doc_type=doc_type)

    file_path = "{period}_{bbl}.pdf".format(period=period, bbl=bbl, doc_type=doc_type)
    #wget waits for the data to be downloaded
    response = wget.download(url=url2, out= os.path.join(data_folder,file_path) )
    return file_path
    time.sleep( 0.1 )

def read_Doc( file_path ):

    pdf = os.path.join(data_folder, file_path )
    text = extract_text( pdf )

    if "Rent Stabilization" in text:
        text = text.split( '# Apts' ,1 )[1] 
        text = text.split( 'RS fee identifiers' ,1 )[0] 
        text = text.split( '\n' )

        apt = text[1] 
        bbl = file_path.split("_")[1].split(".")[0]
        t_date = file_path.split("_")[0]

        url2= 'https://a836-edms.nyc.gov/dctm-rest/repositories/dofedmspts/StatementSearch?' + \
            'bbl={bbl}&stmtDate={period}&stmtType={doc_type}'.format(
                period=t_date, bbl=bbl, doc_type="SOA")
        
        return [bbl,t_date,file_path,url2,apt]
    else:
        return "NA"

#%%Get a a sample 

for i in range(20):
    print( "----------------------------------")
    sample_b = ddif.sample(1)
    bbl = sample_b['ucbbl'].tolist()[0]
    print( bbl , sample_b['uc2018'].tolist()[0] )
    pdf_path = get_Download(bbl,'20201121','SOA')
    print( read_Doc(pdf_path) )

# %%
