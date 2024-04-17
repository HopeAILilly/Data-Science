class Univariate():
    def QuanQual(dataset):
        Quan=[]
        Qual=[]
        for columnname in dataset.columns:
            if dataset[columnname].dtypes=='O':
                Qual.append(columnname)
            else:
                Quan.append(columnname)    
        return Quan, Qual
        