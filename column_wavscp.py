import pandas as pd
column1 = pd.read_csv('/home/laishram/Downloads/wav.scp', delim_whitespace=True, usecols = [0])
print(column1) 
column1=column1.values.tolist()

column2 = pd.read_csv('/home/laishram/Downloads/wav.scp', delim_whitespace=True, usecols = [1])
print(column2)        
column2=column2.values.tolist()

ffmpeg_var1=["ffmpeg"]*1261
print (ffmpeg_var1)
#ffmpeg_var2=[" -ar 8000 -f wav - |"]*1256
#print(ffmpeg_var2)
# dataset={
#     column1,ffmpeg_var1,column2,ffmpeg_var2
# }

new_columns=pd.DataFrame(c,ffmpeg_var1,column2)
print(new_columns)

with open("test.txt", 'a') as f:
    df_string = new_columns.to_string()
    f.write(df_string)