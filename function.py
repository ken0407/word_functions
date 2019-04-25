def make_feature_DF(statements,dictionary):
    dictionary_ = dictionary
    feature_df = pd.DataFrame(columns=dictionary_)
        
    statements_ = statements
    for i,sentence in enumerate(statements_):
        init = [0 for _ in range(len(dictionary))]
        s = pd.Series(init,index=dictionary,name=i)
        for index in dictionary:
            if index in sentence:
                s["{}".format(index)] = 1
        feature_df = feature_df.append(s)
    return feature_df
