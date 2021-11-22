
#%%

import pandas as pd
import os
import PyPDF2
from pdfminer.high_level import extract_text

folder = r"C:\Users\csucuogl\Desktop\Tax_Test"
print( 'Go!' )

# %% Convert PDF to Dataframe

df = pd.DataFrame( columns = ['bbl','tax_time','file','url','Rent_St'] )
count = 0

for f in os.listdir( folder ):
    #check = False #Is bill has Stabilization
    pdf = os.path.join(folder, f )
    text = extract_text( pdf )

    if "Rent Stabilization" in text:
        text = text.split( '# Apts' ,1 )[1] 
        text = text.split( 'RS fee identifiers' ,1 )[0] 
        text = text.split( '\n' )

        apt = text[1] 
        bbl = f.split("_")[1].split(".")[0]
        t_date = f.split("_")[0]

        url2= 'https://a836-edms.nyc.gov/dctm-rest/repositories/dofedmspts/StatementSearch?' + \
            'bbl={bbl}&stmtDate={period}&stmtType={doc_type}'.format(
                period=t_date, bbl=bbl, doc_type="SOA")
        
        df.loc[len(df.index)] = [bbl,t_date,f,url2,apt] #Add to the end 
    else:
        #os.remove( pdf )
        continue
    
    count = count + 1
    if count % 250 == 0: print( count ) 

df.to_csv( os.path.join(folder,"{}_RentStabilzedUnits.csv".format(t_date) ) )

df.head()

#%%

# %%
