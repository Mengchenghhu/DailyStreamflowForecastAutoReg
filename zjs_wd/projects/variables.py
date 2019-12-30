import pandas as pd
import os
root_path = os.path.dirname(os.path.abspath('__file__'))
lags_dicts={}
for wv_l in [
    'db2-1','db2-2','db2-3','db5-1','db5-2','db5-3',
    'db10-1','db10-2','db10-3','db15-1','db15-2','db15-3',
    'db20-1','db20-2','db20-3','db25-1','db25-2','db25-3',
    'db30-1','db30-2','db30-3','db35-1','db35-2','db35-3',
    'db40-1','db40-2','db40-3','db45-1','db45-2','db45-3',
    'bior 3.3-1','bior 3.3-2','bior 3.3-3','coif3-1','coif3-2','coif3-3',
    'haar-1','haar-2','haar-3'
]:
    pacf_data = pd.read_csv(root_path+'/zjs_wd/data/'+wv_l+'/PACF.csv')
    up_bounds=pacf_data['UP']
    lo_bounds=pacf_data['LOW']
    subsignals_pacf = pacf_data.drop(['ORIG','UP','LOW'],axis=1)
    lags_dict={}
    for signal in subsignals_pacf.columns.tolist():
        # print(subsignals_pacf[signal])
        lag=0
        for i in range(subsignals_pacf[signal].shape[0]):
            if abs(subsignals_pacf[signal][i])>0.5 and abs(subsignals_pacf[signal][i])>up_bounds[0]:
                lag=i
        lags_dict[signal]=lag
    lags_dicts[wv_l]=lags_dict
    
variables={
    'lags_dict':lags_dicts,
    'full_len' :6574,
    'train_len' :5260,
    'dev_len' : 657,
    'test_len' : 657,
}

print('variables:{}'.format(variables))

# lags_dict={
#     'db2-1':{'D1':20,'A1':20},
#     'db2-2':{'D1':20,'D2':20,'A2':20},
#     'db2-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db2-4':{20,20,20,20,20},
#     # 'db2-5':{20,20,20,20,20,18},
#     # 'db2-6':{20,20,20,20,20,20,20},
#     # 'db2-7':{20,20,20,20,20,20,20,20},
#     # 'db2-8':{20,20,20,20,20,20,20,20,20},
#     # 'db2-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db2-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db2-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db2-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'db5-1':{'D1':20,'A1':20},
#     'db5-2':{'D1':20,'D2':20,'A2':20},
#     'db5-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db5-4':{20,20,20,20,20},
#     # 'db5-5':{20,20,20,20,19,20},
#     # 'db5-6':{20,20,20,20,19,20,19},
#     # 'db5-7':{20,20,20,20,19,20,19,20},
#     # 'db5-8':{20,20,20,20,19,20,19,20,19},
#     # 'db5-9':{20,20,20,20,19,20,19,20,19,20},
#     # 'db5-10':{20,20,20,20,19,20,19,20,19,19,19},
#     # 'db5-11':{20,20,20,20,19,20,19,20,19,19,19,19},
#     # 'db5-12':{20,20,20,20,19,20,19,20,19,19,19,19,19},
#     'db10-1':{'D1':20,'A1':20},
#     'db10-2':{'D1':20,'D2':20,'A2':20},
#     'db10-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db10-4':{20,20,20,20,20},
#     # 'db10-5':{20,20,20,20,20,20},
#     # 'db10-6':{20,20,20,20,20,20,20},
#     # 'db10-7':{20,20,20,20,20,20,20,20},
#     # 'db10-8':{20,20,20,20,20,20,20,20,20},
#     # 'db10-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db10-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db10-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db10-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'db15-1':{'D1':20,'A1':20},
#     'db15-2':{'D1':20,'D2':20,'A2':20},
#     'db15-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db15-4':{20,20,20,20,20},
#     # 'db15-5':{20,20,20,20,20,20},
#     # 'db15-6':{20,20,20,20,20,20,20},
#     # 'db15-7':{20,20,20,20,20,20,20,20},
#     # 'db15-8':{20,20,20,20,20,20,20,20,20},
#     # 'db15-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db15-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db15-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db15-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'db20-1':{'D1':20,'A1':20},
#     'db20-2':{'D1':20,'D2':20,'A2':20},
#     'db20-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db20-4':{20,20,20,20,20},
#     # 'db20-5':{20,20,20,20,20,20},
#     # 'db20-6':{20,20,20,20,20,20,20},
#     # 'db20-7':{20,20,20,20,20,20,20,20},
#     # 'db20-8':{20,20,20,20,20,20,20,20,20},
#     # 'db20-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db20-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db20-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db20-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'db25-1':{'D1':20,'A1':20},
#     'db25-2':{'D1':20,'D2':20,'A2':20},
#     'db25-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db25-4':{20,20,20,20,20},
#     # 'db25-5':{20,20,20,20,20,20},
#     # 'db25-6':{20,20,20,20,20,20,20},
#     # 'db25-7':{20,20,20,20,20,20,20,20},
#     # 'db25-8':{20,20,20,20,20,20,20,20,20},
#     # 'db25-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db25-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db25-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db25-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'db30-1':{'D1':20,'A1':20},
#     'db30-2':{'D1':20,'D2':20,'A2':20},
#     'db30-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db30-4':{20,20,20,20,20},
#     # 'db30-5':{20,20,20,20,20,20},
#     # 'db30-6':{20,20,20,20,20,20,19},
#     # 'db30-7':{20,20,20,20,20,20,20,20},
#     # 'db30-8':{20,20,20,20,20,20,20,20,20},
#     # 'db30-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db30-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db30-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db30-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'db35-1':{'D1':20,'A1':20},
#     'db35-2':{'D1':20,'D2':20,'A2':20},
#     'db35-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db35-4':{20,20,20,20,20},
#     # 'db35-5':{20,20,20,20,20,20},
#     # 'db35-6':{20,20,20,20,20,20,20},
#     # 'db35-7':{20,20,20,20,20,20,20,20},
#     # 'db35-8':{20,20,20,20,20,20,20,20,20},
#     # 'db35-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db35-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db35-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db35-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'db40-1':{'D1':20,'A1':20},
#     'db40-2':{'D1':20,'D2':20,'A2':20},
#     'db40-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db40-4':{20,20,20,20,20},
#     # 'db40-5':{20,20,20,20,20,20},
#     # 'db40-6':{20,20,20,20,20,20,20},
#     # 'db40-7':{20,20,20,20,20,20,20,20},
#     # 'db40-8':{20,20,20,20,20,20,20,20,20},
#     # 'db40-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db40-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db40-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db40-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'db45-1':{'D1':20,'A1':20},
#     'db45-2':{'D1':20,'D2':20,'A2':20},
#     'db45-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'db45-4':{20,20,20,20,20},
#     # 'db45-5':{20,20,20,20,20,20},
#     # 'db45-6':{20,20,20,20,20,20,20},
#     # 'db45-7':{20,20,20,20,20,20,20,20},
#     # 'db45-8':{20,20,20,20,20,20,20,20,20},
#     # 'db45-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'db45-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'db45-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'db45-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
#     'haar-1':{'D1':20,'A1':19},
#     'haar-2':{'D1':20,'D2':20,'A2':17},
#     'haar-3':{'D1':20,'D2':20,'D3':20,'A3':17},
#     # 'haar-4':{20,20,20,20,17},
#     # 'haar-5':{20,20,20,20,20,1},
#     # 'haar-6':{20,20,20,20,20,1,1},
#     # 'haar-7':{20,20,20,20,20,1,1,1},
#     # 'haar-8':{20,20,20,20,20,1,1,1,1},
#     # 'haar-9':{20,20,20,20,20,1,1,1,1,1},
#     # 'haar-10':{20,20,20,20,20,1,1,1,1,1,1},
#     # 'haar-11':{20,20,20,20,20,1,1,1,1,1,1,1},
#     # 'haar-12':{20,20,20,20,20,1,1,1,1,1,1,1,1},

#     'bior 3.3-1':{'D1':20,'A1':20},
#     'bior 3.3-2':{'D1':20,'D2':20,'A2':20},
#     'bior 3.3-3':{'D1':20,'D2':20,'D3':20,'A3':19},
#     # 'bior 3.3-4':{20,20,20,19,19},
#     # 'bior 3.3-5':{20,20,20,19,19,3},
#     # 'bior 3.3-6':{20,20,20,19,19,3,3},
#     # 'bior 3.3-7':{20,20,20,19,19,3,3,3},
#     # 'bior 3.3-8':{20,20,20,19,19,3,3,3,3},
#     # 'bior 3.3-9':{20,20,20,19,19,3,3,3,3,3},
#     # 'bior 3.3-10':{20,20,20,19,19,3,3,3,3,3,3},
#     # 'bior 3.3-11':{20,20,20,19,19,3,3,3,3,3,3,3},
#     # 'bior 3.3-12':{20,20,20,19,19,3,3,3,3,3,3,3,3},
    
#     'coif3-1':{'D1':20,'A1':20},
#     'coif3-2':{'D1':20,'D2':20,'A2':20},
#     'coif3-3':{'D1':20,'D2':20,'D3':20,'A3':20},
#     # 'coif3-4':{20,20,20,20,20},
#     # 'coif3-5':{20,20,20,20,20,20},
#     # 'coif3-6':{20,20,20,20,20,20,20},
#     # 'coif3-7':{20,20,20,20,20,20,20,20},
#     # 'coif3-8':{20,20,20,20,20,20,20,20,20},
#     # 'coif3-9':{20,20,20,20,20,20,20,20,20,20},
#     # 'coif3-10':{20,20,20,20,20,20,20,20,20,20,20},
#     # 'coif3-11':{20,20,20,20,20,20,20,20,20,20,20,20},
#     # 'coif3-12':{20,20,20,20,20,20,20,20,20,20,20,20,20},
# }

