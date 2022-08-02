import pandas as pd

def writeExcelFile(ProductsCode,excelFileName):

    df = pd.DataFrame(columns=['Ürün Kodu','Renk Kodu'])

    for index,productCode in enumerate(ProductsCode):
        product = []
        print(productCode)
        product.append(productCode.replace("Ürün Kodu:",'').strip().replace(' ','').split('-')[0])
        product.append(productCode.replace("Ürün Kodu:",'').strip().replace(' ','').split('-')[1])
        print(product)
        df.loc[index] = product

    
    df.to_excel(f'{excelFileName}.xlsx',sheet_name='Product')