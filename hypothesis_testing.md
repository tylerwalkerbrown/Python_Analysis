# Hypothesis Testing


```python
import pandas as pd
import numpy as np 
import math 
import scipy.stats as stats 
import matplotlib.pyplot as plt
%matplotlib inline
import os
```


```python
#df - contains all original data 
#total_sample - 100 observations from df total column 
#h_mean - hypothesis mean variable using int(df['total'].mean())
#N - sample size 
#dev - standard deviation of the population 
```


```python
os.chdir("Desktop/mojo")
```


```python
#Customer order data between the years 2019-Current 
df = pd.read_csv("orders.csv")
```


```python
#Orginal shape of the data that will be tested 
df.shape
```




    (11228, 31)




```python
#Multiple different columns with NAs but non in our total column that would impact the analysis 
df.isna().sum()
```




    MyUnknownColumn                0
    date/time                      0
    settlement id                  0
    type                           0
    order id                     153
    sku                          242
    description                    0
    quantity                     242
    marketplace                  267
    account type                   0
    fulfillment                  335
    order city                   335
    order state                  335
    order postal                 335
    tax collection model        1661
    product sales                  0
    product sales tax              0
    shipping credits               0
    shipping credits tax           0
    gift wrap credits              0
    giftwrap credits tax           0
    Regulatory Fee                 0
    Tax On Regulatory Fee          0
    promotional rebates            0
    promotional rebates tax        0
    marketplace withheld tax       0
    selling fees                   0
    fba fees                       0
    other transaction fees         0
    other                          0
    total                          0
    dtype: int64




```python
#Examining the top 5 observations 
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MyUnknownColumn</th>
      <th>date/time</th>
      <th>settlement id</th>
      <th>type</th>
      <th>order id</th>
      <th>sku</th>
      <th>description</th>
      <th>quantity</th>
      <th>marketplace</th>
      <th>account type</th>
      <th>...</th>
      <th>Regulatory Fee</th>
      <th>Tax On Regulatory Fee</th>
      <th>promotional rebates</th>
      <th>promotional rebates tax</th>
      <th>marketplace withheld tax</th>
      <th>selling fees</th>
      <th>fba fees</th>
      <th>other transaction fees</th>
      <th>other</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Jan 1, 2019 8:11:26 AM PST</td>
      <td>11005303231</td>
      <td>Order</td>
      <td>114-5086551-9187423</td>
      <td>MD-LPVW-5TS5</td>
      <td>Premium Copper Sulfate 99% Pure Powder 5lb. By...</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>-2.92</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>16.57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Jan 1, 2019 8:11:26 AM PST</td>
      <td>11005303231</td>
      <td>Order</td>
      <td>113-6825798-2657058</td>
      <td>7W-GLQ4-WIJ4</td>
      <td>Premium Alfalfa Pellets Animal Feed (Rabbits, ...</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>-2.70</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>15.28</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Jan 1, 2019 8:11:26 AM PST</td>
      <td>11005303231</td>
      <td>Order</td>
      <td>113-6754176-8077821</td>
      <td>4X-B0MA-QO7J</td>
      <td>Premium Green Sand By Old Cobblers Farm 5lbs.</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>-2.25</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Jan 1, 2019 8:11:29 AM PST</td>
      <td>11005303231</td>
      <td>Order</td>
      <td>112-7475081-4111461</td>
      <td>5L-SJVP-1RKD</td>
      <td>Premium Winter Rye Grass Seed by Old Cobblers ...</td>
      <td>2.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>-9.46</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>53.53</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Jan 1, 2019 8:11:29 AM PST</td>
      <td>11005303231</td>
      <td>Order</td>
      <td>114-5674036-5513855</td>
      <td>4X-B0MA-QO7J</td>
      <td>Premium Green Sand By Old Cobblers Farm 5lbs.</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0.0</td>
      <td>-2.25</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>12.74</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 31 columns</p>
</div>




```python
#Looking at the bottom 5 observations
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MyUnknownColumn</th>
      <th>date/time</th>
      <th>settlement id</th>
      <th>type</th>
      <th>order id</th>
      <th>sku</th>
      <th>description</th>
      <th>quantity</th>
      <th>marketplace</th>
      <th>account type</th>
      <th>...</th>
      <th>Regulatory Fee</th>
      <th>Tax On Regulatory Fee</th>
      <th>promotional rebates</th>
      <th>promotional rebates tax</th>
      <th>marketplace withheld tax</th>
      <th>selling fees</th>
      <th>fba fees</th>
      <th>other transaction fees</th>
      <th>other</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11223</th>
      <td>6823</td>
      <td>Sep 30, 2022 3:42:20 AM PDT</td>
      <td>16602880141</td>
      <td>Order</td>
      <td>113-3530057-7075450</td>
      <td>MG-LVLI-PC3K</td>
      <td>Premium Winter Rye Grass Seeds 10 lbs, Non-GMO...</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>-2.14</td>
      <td>-3.90</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>22.09</td>
    </tr>
    <tr>
      <th>11224</th>
      <td>6824</td>
      <td>Sep 30, 2022 8:22:13 AM PDT</td>
      <td>16602880141</td>
      <td>Order</td>
      <td>114-3328297-8061055</td>
      <td>CL-BC88-IS7F</td>
      <td>Premium Winter Rye Seeds 5 lbs, Non-GMO, Cover...</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>-1.14</td>
      <td>-2.85</td>
      <td>-7.38</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.76</td>
    </tr>
    <tr>
      <th>11225</th>
      <td>6825</td>
      <td>Sep 30, 2022 10:33:23 AM PDT</td>
      <td>16602880141</td>
      <td>Order</td>
      <td>113-4014824-6102633</td>
      <td>SY-EDGB-9OV6</td>
      <td>Old Cobblers Farm Winter Rye Seeds Non-GMO, Co...</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>-1.62</td>
      <td>-4.05</td>
      <td>-8.96</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>13.98</td>
    </tr>
    <tr>
      <th>11226</th>
      <td>6826</td>
      <td>Sep 30, 2022 7:15:53 PM PDT</td>
      <td>16602880141</td>
      <td>Order</td>
      <td>113-1000255-8863412</td>
      <td>CL-BC88-IS7F</td>
      <td>Premium Winter Rye Seeds 5 lbs, Non-GMO, Cover...</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>-1.14</td>
      <td>-2.85</td>
      <td>-7.38</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.76</td>
    </tr>
    <tr>
      <th>11227</th>
      <td>6827</td>
      <td>Sep 30, 2022 7:31:56 PM PDT</td>
      <td>16602880141</td>
      <td>Order</td>
      <td>111-4036945-1867443</td>
      <td>GW-08IK-ZKDL</td>
      <td>Old Cobblers Farm Rock Phosphate Fertilizer Or...</td>
      <td>1.0</td>
      <td>amazon.com</td>
      <td>Standard Orders</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>-1.19</td>
      <td>-2.85</td>
      <td>-7.07</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>9.07</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 31 columns</p>
</div>




```python
#Looking at the mean amount spent to create a null hypothesis 
print("Null - Population average customer at OCF spends",int(df['total'].mean()))
print("Alternative - Population average is =!",int(df['total'].mean()))
```

    Null - Population average customer at OCF spends 24
    Alternative - Population average is =! 24



```python
#Subsetting the total columns sample that will be examined in a hypothesis testing using 100 rows of data 
sample = df['total'][np.argsort(np.random.random(5000))[:100]]
```


```python
#Storing the sample mean, pop mean, sample size and standard deviation 
sample_mean = int(sample.mean())
h_mean = int(df['total'].mean())
N = len(sample)
dev = np.std(df['total'])
print("Sample mean = ", sample_mean)
print("Hypothesis mean = ", h_mean)
print("Sample size = ", N )
print("Standard deviation = ", dev)
```

    Sample mean =  26
    Hypothesis mean =  24
    Sample size =  100
    Standard deviation =  31.931755790059995



```python
# Z-score 
z = (sample_mean - h_mean)/(dev/math.sqrt(N))
print("Z-score = ", z)
```

    Z-score =  0.6263357433738667



```python
# P value 
p_value = stats.norm.sf(abs(z))
print("P-value = ", p_value)
```

    P-value =  0.26554737326007005


Rejecting the null of the average customer spending $24 on average 


```python

```
