feature_names = ['CountryName',
 'CountryCode',
 'IndicatorName',
 'IndicatorCode',
 'Year',
 'Value']

row_vals = ['Arab World',
 'ARB',
 'Adolescent fertility rate (births per 1,000 women ages 15-19)',
 'SP.ADO.TFRT',
 '1960',
 '133.56090740552298']

def lists2dict(list1, list2):
    zipped_list = zip(list1, list2)
    rs_dict = dict(list(zipped_list))
    return rs_dict

rs_fxn = lists2dict(feature_names, row_vals)
print(rs_fxn)
