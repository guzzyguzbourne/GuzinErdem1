
# coding: utf-8

# # Homework 1
# **11.10.2017**

# In this work, you will use the [Online Retail Data Set](http://archive.ics.uci.edu/ml/datasets/online+retail), a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

# * Download the data file in Excel format. Use the `xlrd` module to parse the data. This module is not in the standard library, but it is part of the Anaconda distribution.
# * Using the data, answer the following questions:
#  1. Which order (identified with the `InvoiceNo` field) has the largest total?
#  1. Which item (identified with the `StockCode` field) has been sold the most, in terms of item counts?
#  1. Which item (identified with the `StockCode` field) brought the largest revenue?
#  1. How many unique items are sold, and how many unique customers have been served? Use the `Counter` function of the `collections` module.

# To process the data, use only basic built-in Python data structures we have discussed so far. No _pandas_ or similar packages yet, please.

# Provide your code and answers in the form of a Jupyter notebook with the name `yourname_DA501_HW1.ipynb`, where you change `yourname` accordingly, and email it to _mkozturk@sabanciuniv.edu_ no later than 21.10.2017, 13:00.

# In[310]:


import xlrd
wb  = xlrd.open_workbook("Online_Retail.xlsx")
pairs = []
for i in range(2, 15):
    pairs.append([sheet.cell(i, j).value for j in range(2, 4)])
print(pairs)


# In[36]:


import xlrd
wb  = xlrd.open_workbook("Online_Retail.xlsx")
sheets =wb.sheets()
print(sheets[0].nrows)


# In[39]:


import xlrd
wb  = xlrd.open_workbook("Online_Retail.xlsx")
sheets =wb.sheets()
total = 0.0
for row in range(1, sheets[0].nrows):
    total = total + sheets[0].cell_value(row, 5)
print (total)


# In[ ]:


import xlrd
wb  = xlrd.open_workbook("Online_Retail.xlsx")
sheets =wb.sheets()
total = 0.0
if 
for row in range(1, sheets[0].nrows):
    total = total + sheets[0].cell_value(row, 5)
print (total)


# In[144]:


import xlrd
wb  = xlrd.open_workbook("Online.xlsx")
sheets =wb.sheets()
total = 0.0
for row in range(1, sheets[0].nrows):
    total = total + sheets[0].cell_value(row, 5)
print (total)


# In[145]:


import xlrd
wb  = xlrd.open_workbook("Online.xlsx")
pairs = []
for i in range(1, sheets[0].nrows):
    pairs.append([sheet.cell(i, j).value for j in range(0, 6)])
print(pairs)


# In[191]:


import xlrd
wb  = xlrd.open_workbook("Online.xlsx")
pairs = []
for i in range(1, sheets[0].nrows):
    pairs.append([sheet.cell(i, j).value for j in range(0, 6)])
print(pairs[0:1])


# In[83]:


total=0
while i in range (0,((sheets[0].nrows)-1)):
    if pairs[i][0]==pairs[i+1][0]:
        total += pairs[i][5]
        i+=1
print(total)


# In[147]:


print(pairs[0][0])


# In[148]:


print(pairs[1][0])


# In[149]:


print(pairs[1][5])


# In[203]:


total=0
i=0
while i < 6:
    if pairs[i][0]==pairs[i+1][0]:
        total += pairs[i][5]
        i+=1
print(total)


# In[ ]:


total1=0
total2=0
i=0
while i <=7:
    if pairs[i][0]==pairs[i+1][0]:
        total1 += pairs[i][5]
        y=total1
        y+=pairs[i+1][5]
        i+=1
        print(pairs[i][0],y)
    elif pairs[i+1][0]==pairs[i+2][0]:
        total2 += pairs[i+1][5]
        z=total2
        z+=pairs[i+2][5]
        i+=1
        print(pairs[i+1][0],z)


# In[ ]:


total1=0
total2=0
i=0
while i <=7:
    if pairs[i][0]==pairs[i+1][0]:
        total1 += pairs[i][5]
        y=total1
        y+=pairs[i+1][5]
        i+=1
        print(pairs[i][0],y)
    elif pairs[i+1][0]==pairs[i+2][0]:
        total2 += pairs[i+1][5]
        z=total2
        z+=pairs[i+2][5]
        i+=1
        print(pairs[i+1][0],z)


# In[ ]:


total1=0
total2=0
i=0
while i <=5:
    if pairs[i][0]==pairs[i+1][0]:
        


# In[206]:


total1=0
total2=0
i=0
while i <=7:
    if pairs[i][0]==pairs[i+1][0]:
        total1 += pairs[i][5]
        y=total1
        y+=pairs[i+1][5]
        i+=1
        print(pairs[i][0],y)
    elif pairs[i+2][0]==pairs[i+3][0]:
        total2 += pairs[i+2][5]
        z=total2
        z+=pairs[i+3][5]
        i+=1
        print(pairs[i+2][0],z)


# In[207]:


total1=0
total2=0
i=0
while i <=7:
    if pairs[i][0]==pairs[i+1][0]:
        total1 += pairs[i][5]
        y=total1
        y+=pairs[i+1][5]
        i+=1
        print(pairs[i][0],y)
    elif pairs[i+1][0]==pairs[i+2][0]:
        total2 += pairs[i+1][5]
        z=total2
        z+=pairs[i+1][5]
        i+=1
        print(pairs[i+1][0],z)


# In[ ]:


total1=0
total2=0
i=0
while i <=7:
    if pairs[i][0]==pairs[i+1][0]:
        total1 += pairs[i][5]
        y=total1
        y+=pairs[i+1][5]
           print(pairs[i][0],y)   


# In[215]:


from collections import Counter
import xlrd
wb  = xlrd.open_workbook("Online.xlsx")
sheets =wb.sheets()
Counter(words).most_common(2)


# In[216]:


import xlrd
wb  = xlrd.open_workbook("Online.xlsx")
data = []
for i in range(1, sheets[0].nrows):
    data.append([sheet.cell(i, j).value for j in range(0, 6)])
print(data)


# In[248]:


x=[]
i=0
toplam=0
while i<3:
    if data[i][0]!=data[i+1][0]:
        break
    toplam+=data[i][5]
    
print (data[i][0],toplam)


# In[302]:


total1=0
total2=0
i=0
while True:
    if pairs[i][0]==pairs[i+1][0]:
        total1 += pairs[i][5]
        y=total1
        y+=pairs[i+1][5]
        i+=1
        print(pairs[i][0],y)
    elif pairs[i][0]!=pairs[i+1][0]:
        i+=1
        pass


# In[ ]:


total1=0
total2=0
i=0
while True:
    if pairs[i][0]==pairs[i+1][0]:
        total1 += pairs[i][5]
        y=total1
        y+=pairs[i+1][5]
        print(pairs[i][0],y)
    elif pairs[i][0]!=pairs[i+1][0]:
        pass
    i+=1


# In[ ]:


L=[]
while True:
    a=L[i][0]
    if L[i+1][0]==a
    L.append


# In[ ]:


import xlrd
wb  = xlrd.open_workbook("Online.xlsx")
pairs = []
for i in range(1, sheets[0].nrows):
    pairs.append([sheet.cell(i, j).value for j in range(0, 6)])
print(pairs[0:1])


# In[371]:


import xlrd
wb  = xlrd.open_workbook("cem data.xlsx")
sheets =wb.sheets()

data1 = []
data2 = []
for i in range(1, sheets[0].nrows):
    data1.append([sheet.cell(i, 0).value])
    data2.append([sheet.cell(i, 5).value])
print(list(data1))
print(list(data2))


# In[301]:


x=0
toplam=0
while x<5:
    if pairs[x][0]==pairs[x+1][0]:
        toplam += pairs[x][6]
    else:
        print [pairs[x][0],toplam]
    x+1


# In[287]:


print(data1[0])


# In[288]:


sum(data2)


# In[309]:


while i<5:
    x=data1[i]
    if data1[i]==data1[i+1]:
        toplam += data2[i+1]
        i+=1
print(data1[i],toplam)


# In[375]:


sheets =wb.sheets()
satir = sheets[0].nrows
siparis = []

for i in range(0,sheets[0].nrows):
    if sheets.cell(i,1) != sheets.cell(i+1,1):
        siparis.append(sheets.cell(i,1))

print(siparis)

#for i in range(2, 15):
#    pairs.append([sheet.cell(i, j).value for j in range(2, 4)])
#print(pairs)

