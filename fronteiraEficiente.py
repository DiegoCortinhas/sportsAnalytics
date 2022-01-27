def FronteiraEficiente(data): 

  df_front = pd.DataFrame(columns=data.columns)

 

  for i in range(0,data.shape[0]):

    flag = True

    for j in range(0,data.shape[0]):

      if i != j:

        if data.iloc[i][0] < data.iloc[j][0] and data.iloc[i][1] > data.iloc[j][1]:

          flag = False

          break

    

    if flag == True :

      df_front = df_front.append(data.iloc[i])

      

  return df_front