{
 "cells": [
  {
   "cell_type": "code",
   "id": "initial_id",
   "metadata": {
    "collapsed": True,
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:39.488655Z",
     "start_time": "2026-11-19T01:32:39.461775900Z"
    }
   },
   "source": [
    "import glob\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "from preproccer2 import target_enc"
   ],
   "outputs": [],
   "execution_count": 104
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.182320700Z",
     "start_time": "2026-11-19T01:32:39.490653800Z"
    }
   },
   "cell_type": "code",
   "source": [
    "folder_path=r\"C:\\Users\\Dell\\Downloads\\archive (27)\"\n",
    "all_file=glob.glob(folder_path+\"/*.csv\")\n",
    "for file in all_file:\n",
    "    df_list=[]\n",
    "    for file in all_file:\n",
    "\n",
    "     df=pd.read_csv(file)\n",
    "     df.columns=df.columns.str.strip().str.lower().str.replace(' ', '',regex=True)\n",
    "    df=df.rename(columns={'tax(£)':'tax'})\n",
    "    df_list.append(df)\n",
    "combined_df=pd.concat(df_list,ignore_index=True)\n",
    "print(combined_df.columns.to_list())\n",
    "combined_df.to_csv(r\"C:\\Users\\Dell\\Downloads\\car price.csv\",index=False)\n"
   ],
   "id": "f47e3a66b3c7c017",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['model', 'year', 'price', 'transmission', 'mileage', 'fueltype', 'tax', 'mpg', 'enginesize']\n"
     ]
    }
   ],
   "execution_count": 105
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.210812700Z",
     "start_time": "2026-11-19T01:32:40.184321900Z"
    }
   },
   "cell_type": "code",
   "source": "df=pd.read_csv(r\"C:\\Users\\Dell\\Downloads\\car price.csv\")",
   "id": "244cc56ee015219",
   "outputs": [],
   "execution_count": 106
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.226951500Z",
     "start_time": "2026-11-19T01:32:40.211813400Z"
    }
   },
   "cell_type": "code",
   "source": "df.shape",
   "id": "36dd05674cc810ed",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(15157, 9)"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 107
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.259820600Z",
     "start_time": "2026-11-19T01:32:40.229952500Z"
    }
   },
   "cell_type": "code",
   "source": [
    "df.info()\n",
    "df.head()"
   ],
   "id": "41cdc24a2487fee4",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 15157 entries, 0 to 15156\n",
      "Data columns (total 9 columns):\n",
      " #   Column        Non-Null Count  Dtype  \n",
      "---  ------        --------------  -----  \n",
      " 0   model         15157 non-null  object \n",
      " 1   year          15157 non-null  int64  \n",
      " 2   price         15157 non-null  int64  \n",
      " 3   transmission  15157 non-null  object \n",
      " 4   mileage       15157 non-null  int64  \n",
      " 5   fueltype      15157 non-null  object \n",
      " 6   tax           15157 non-null  int64  \n",
      " 7   mpg           15157 non-null  float64\n",
      " 8   enginesize    15157 non-null  float64\n",
      "dtypes: float64(2), int64(4), object(3)\n",
      "memory usage: 1.0+ MB\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "    model  year  price transmission  mileage fueltype  tax   mpg  enginesize\n",
       "0   T-Roc  2019  25000    Automatic    13904   Diesel  145  49.6         2.0\n",
       "1   T-Roc  2019  26883    Automatic     4562   Diesel  145  49.6         2.0\n",
       "2   T-Roc  2019  20000       Manual     7414   Diesel  145  50.4         2.0\n",
       "3   T-Roc  2019  33492    Automatic     4825   Petrol  145  32.5         2.0\n",
       "4   T-Roc  2019  22900    Semi-Auto     6500   Petrol  150  39.8         1.5"
      ],
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>model</th>\n",
       "      <th>year</th>\n",
       "      <th>price</th>\n",
       "      <th>transmission</th>\n",
       "      <th>mileage</th>\n",
       "      <th>fueltype</th>\n",
       "      <th>tax</th>\n",
       "      <th>mpg</th>\n",
       "      <th>enginesize</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>T-Roc</td>\n",
       "      <td>2019</td>\n",
       "      <td>25000</td>\n",
       "      <td>Automatic</td>\n",
       "      <td>13904</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>145</td>\n",
       "      <td>49.6</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>T-Roc</td>\n",
       "      <td>2019</td>\n",
       "      <td>26883</td>\n",
       "      <td>Automatic</td>\n",
       "      <td>4562</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>145</td>\n",
       "      <td>49.6</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>T-Roc</td>\n",
       "      <td>2019</td>\n",
       "      <td>20000</td>\n",
       "      <td>Manual</td>\n",
       "      <td>7414</td>\n",
       "      <td>Diesel</td>\n",
       "      <td>145</td>\n",
       "      <td>50.4</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>T-Roc</td>\n",
       "      <td>2019</td>\n",
       "      <td>33492</td>\n",
       "      <td>Automatic</td>\n",
       "      <td>4825</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>145</td>\n",
       "      <td>32.5</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>T-Roc</td>\n",
       "      <td>2019</td>\n",
       "      <td>22900</td>\n",
       "      <td>Semi-Auto</td>\n",
       "      <td>6500</td>\n",
       "      <td>Petrol</td>\n",
       "      <td>150</td>\n",
       "      <td>39.8</td>\n",
       "      <td>1.5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 108
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.282183200Z",
     "start_time": "2026-11-19T01:32:40.261821500Z"
    }
   },
   "cell_type": "code",
   "source": "df.isna().sum()",
   "id": "ff635095bfcf121d",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "model           0\n",
       "year            0\n",
       "price           0\n",
       "transmission    0\n",
       "mileage         0\n",
       "fueltype        0\n",
       "tax             0\n",
       "mpg             0\n",
       "enginesize      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 109
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.299203500Z",
     "start_time": "2026-11-19T01:32:40.283184100Z"
    }
   },
   "cell_type": "code",
   "source": [
    "df.duplicated().sum()\n",
    "df.drop_duplicates(keep='first',inplace=True)\n",
    "df.reset_index(drop=True,inplace=True)"
   ],
   "id": "17739c21f4e06929",
   "outputs": [],
   "execution_count": 110
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.326996900Z",
     "start_time": "2026-11-19T01:32:40.301207700Z"
    }
   },
   "cell_type": "code",
   "source": "print(df.describe())",
   "id": "a946224ada43dff9",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "               year         price        mileage           tax           mpg  \\\n",
      "count  14893.000000  14893.000000   14893.000000  14893.000000  14893.000000   \n",
      "mean    2017.237561  16807.898073   22202.155845    112.529040     53.772625   \n",
      "std        2.054808   7735.548874   21003.362610     63.684422     13.617682   \n",
      "min     2000.000000    899.000000       1.000000      0.000000      0.300000   \n",
      "25%     2016.000000  10990.000000    6000.000000     30.000000     46.300000   \n",
      "50%     2017.000000  15494.000000   16558.000000    145.000000     53.300000   \n",
      "75%     2019.000000  20995.000000   32000.000000    145.000000     60.100000   \n",
      "max     2020.000000  69994.000000  212000.000000    580.000000    188.300000   \n",
      "\n",
      "         enginesize  \n",
      "count  14893.000000  \n",
      "mean       1.600483  \n",
      "std        0.460393  \n",
      "min        0.000000  \n",
      "25%        1.200000  \n",
      "50%        1.600000  \n",
      "75%        2.000000  \n",
      "max        3.200000  \n"
     ]
    }
   ],
   "execution_count": 111
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.553083Z",
     "start_time": "2026-11-19T01:32:40.328993200Z"
    }
   },
   "cell_type": "code",
   "source": [
    "from sklearn.ensemble import IsolationForest\n",
    "X=df[['price','tax','mpg']]\n",
    "iso=IsolationForest(contamination=0.01,n_estimators=100,random_state=10)\n",
    "z=iso.fit_predict(X)==-1\n",
    "print(\"num of iso\",int(z.sum()))\n"
   ],
   "id": "d88ef7dfd4a43acf",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "num of iso 148\n"
     ]
    }
   ],
   "execution_count": 112
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.587610400Z",
     "start_time": "2026-11-19T01:32:40.556084100Z"
    }
   },
   "cell_type": "code",
   "source": [
    "cols_clip=['price','tax','mpg']\n",
    "for col in cols_clip:\n",
    "    q1=df[col].quantile(0.25)\n",
    "    q3=df[col].quantile(0.75)\n",
    "    iqr = q3-q1\n",
    "    lower=q1-1.5*iqr\n",
    "    upper=q3+1.5*iqr\n",
    "    if col in ['price','tax','mpg']:\n",
    "        lower=max(0,lower)\n",
    "        df[col]=df[col].clip(lower=lower,upper=upper)\n",
    "print(df[['price','tax','mpg']].describe())"
   ],
   "id": "b7a8339eef846c1b",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              price           tax           mpg\n",
      "count  14893.000000  14893.000000  14893.000000\n",
      "mean   16649.471698    112.416404     53.213187\n",
      "std     7198.519351     63.121857     10.327065\n",
      "min      899.000000      0.000000     25.600000\n",
      "25%    10990.000000     30.000000     46.300000\n",
      "50%    15494.000000    145.000000     53.300000\n",
      "75%    20995.000000    145.000000     60.100000\n",
      "max    36002.500000    317.500000     80.800000\n"
     ]
    }
   ],
   "execution_count": 113
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.623698Z",
     "start_time": "2026-11-19T01:32:40.595609300Z"
    }
   },
   "cell_type": "code",
   "source": [
    "c=df.select_dtypes(include='object').columns\n",
    "for col in c:\n",
    "    print(df[col].value_counts())\n"
   ],
   "id": "38b33abb3bfec531",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "model\n",
      "Golf               4797\n",
      "Polo               3244\n",
      "Tiguan             1743\n",
      "Passat              878\n",
      "Up                  846\n",
      "T-Roc               716\n",
      "Touran              349\n",
      "Touareg             347\n",
      "T-Cross             294\n",
      "Golf SV             263\n",
      "Sharan              258\n",
      "Arteon              243\n",
      "Scirocco            240\n",
      "Amarok              111\n",
      "Caravelle            99\n",
      "CC                   95\n",
      "Tiguan Allspace      91\n",
      "Beetle               83\n",
      "Shuttle              61\n",
      "Caddy Maxi Life      59\n",
      "Jetta                32\n",
      "California           15\n",
      "Caddy Life            8\n",
      "Eos                   7\n",
      "Caddy                 6\n",
      "Caddy Maxi            4\n",
      "Fox                   4\n",
      "Name: count, dtype: int64\n",
      "transmission\n",
      "Manual       9256\n",
      "Semi-Auto    3695\n",
      "Automatic    1942\n",
      "Name: count, dtype: int64\n",
      "fueltype\n",
      "Petrol    8414\n",
      "Diesel    6251\n",
      "Hybrid     142\n",
      "Other       86\n",
      "Name: count, dtype: int64\n"
     ]
    }
   ],
   "execution_count": 114
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.758755300Z",
     "start_time": "2026-11-19T01:32:40.626697500Z"
    }
   },
   "cell_type": "code",
   "source": "sns.barplot(df['fueltype'].value_counts())\n",
   "id": "6014eb991d1c568c",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='fueltype', ylabel='count'>"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ],
      "image/png": "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5PLLL5eff/5ZPv/8c0+9bd++3eu8eLqD1ONh3XPPPVKnTp1T1nndddfJAw88IDfeeKNUqVLFq6ykx8I5ycnJppWnqLi4ONM6WDSkXH311dK3b1/zXilKf7DoqYO6desmt956q3n/FH/v6JHx77//fnNoEd1HoOxpvWj4WbZsmamz6tWry+DBg6V///4yd+5cTz3oZ1X398EMpOGWtOTrNHgu5eA1+PTTT13Tp08/ZfmTTz7p2rNnj7leqVIl12uvvebav3+/KycnxzymVq1apuzZZ591FRYWmsu6devMsi1btrgmTpzo2rt3r2vDhg2u8PBwV1RUlGv8+PGurKws15EjR1zz5s1z1alTx/N827dvd913332Ovx421nViYqLrxIkTrltuucXc1np88MEHzfXmzZubOvvyyy9dM2fOdGVnZ7v69u3reeyUKVNcmzZtck2ePNm1bNkyV3p6uis2Ntanx1LnZVfXWs9a38WXJyUludS1117ruuGGG0y9JyQkeMofffRR16pVq8x1/eyuXbvWlZaWZuovNzfX9fDDD3vuq59zvcyaNcv1/vvvn/Le6dixoys/P981e/Zs15IlS1yrV682z12hQgXHPwvl9RIXF2fqyV0HRS9az7r/7t+/v9knHz9+3NSH/u3evburZ8+erl27drmef/558zcvL8/15ptvmvu619GmTRvXTz/95Dp69Khr8+bNXu8H3X+vXLnStXDhQlPv/fr1c/z1KKOL4xvApYy/FJ955hnX1q1bzfUxY8a4vv/+e1e9evVc1apVM0EmNTXVsyPTL0G9uB+rO0X9cNSoUcMTcj7++GPXjz/+6GrQoIFZrjvMNWvWeD5cfBk6V9d60frSMFv8S0zrfcSIEZ77XXfddWbHePHFF5v3ggbfhg0bespHjhzpSk5OLvGx1HnZ1rXWs4aXAQMGeF2GDx/uCUB6v99//931+OOPex731VdfuZ544glPANIwpD+A9PYdd9xhvlz1S9b9Of/kk0+8nrfoe0c/00899ZSnbMaMGQSgMq53fe31MxYREXHacg00K1as8ArD+ldvawBSkyZNMj9Yr7zySlPf9957rynXz+3BgwdNsKlSpYr5PGtQ6tGjhycAqccee8wVExPjql69epnv05y42NHGZelAaB33c9NNN8mjjz4q77//vuneeuyxx2TIkCHyxx9/SH5+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"
     },
     "metadata": {},
     "output_type": "display_data",
     "jetTransient": {
      "display_id": None
     }
    }
   ],
   "execution_count": 115
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:40.903658100Z",
     "start_time": "2026-11-19T01:32:40.777754700Z"
    }
   },
   "cell_type": "code",
   "source": "sns.barplot(df['transmission'].value_counts(normalize=True))",
   "id": "e64cd83cc5c68fb0",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='transmission', ylabel='proportion'>"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ],
      "image/png": "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"
     },
     "metadata": {},
     "output_type": "display_data",
     "jetTransient": {
      "display_id": None
     }
    }
   ],
   "execution_count": 116
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:32:41.186144200Z",
     "start_time": "2026-11-19T01:32:40.904657900Z"
    }
   },
   "cell_type": "code",
   "source": "sns.heatmap(df.corr(numeric_only=True),annot=True)\n",
   "id": "ee8d062ef8be97ba",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ],
      "image/png": "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"
     },
     "metadata": {},
     "output_type": "display_data",
     "jetTransient": {
      "display_id": None
     }
    }
   ],
   "execution_count": 117
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:35:30.128065300Z",
     "start_time": "2026-11-19T01:35:30.093550500Z"
    }
   },
   "cell_type": "code",
   "source": "df.corr(numeric_only=True)['price'].drop(\"price\").sort_values(ascending=False)",
   "id": "b4c81ec13c2c323e",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year          0.643126\n",
       "enginesize    0.569789\n",
       "tax           0.508240\n",
       "mileage      -0.540378\n",
       "mpg          -0.687249\n",
       "Name: price, dtype: float64"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 123
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:40:50.331387200Z",
     "start_time": "2026-11-19T02:40:50.304799600Z"
    }
   },
   "cell_type": "code",
   "source": [
    "from sklearn.model_selection import train_test_split, KFold\n",
    "\n",
    "X=df.drop(['price'],axis=1)\n",
    "y=df['price']\n",
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=10)"
   ],
   "id": "acdd5a24f3be1d9f",
   "outputs": [],
   "execution_count": 160
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:40:52.357390900Z",
     "start_time": "2026-11-19T02:40:52.311465300Z"
    }
   },
   "cell_type": "code",
   "source": [
    "from sklearn.preprocessing import StandardScaler,TargetEncoder\n",
    "from sklearn.model_selection import KFold\n",
    "encoder={}\n",
    "kf=KFold(n_splits=5,random_state=10,shuffle=True)\n",
    "\n",
    "for col in X.select_dtypes(include='object').columns:\n",
    "    te=TargetEncoder(smooth='auto',cv=kf)\n",
    "    X_train[[col]]=te.fit_transform(X_train[[col]],y_train)\n",
    "    X_test[[col]]=te.transform(X_test[[col]])\n",
    "    encoder[col]=te\n"
   ],
   "id": "72c2c1c3d5dc63fc",
   "outputs": [],
   "execution_count": 161
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:41:21.080968200Z",
     "start_time": "2026-11-19T02:41:21.051697800Z"
    }
   },
   "cell_type": "code",
   "source": [
    "sc=StandardScaler()\n",
    "X_train=sc.fit_transform(X_train)\n",
    "X_test=sc.transform(X_test)"
   ],
   "id": "cabb3d359a719d54",
   "outputs": [],
   "execution_count": 162
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T01:49:35.767058500Z",
     "start_time": "2026-11-19T01:49:35.726849200Z"
    }
   },
   "cell_type": "code",
   "source": "print(pd.DataFrame(X_train).describe())",
   "id": "af75a1d88a428d67",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                  0             1             2             3             4  \\\n",
      "count  1.191400e+04  1.191400e+04  1.191400e+04  1.191400e+04  1.191400e+04   \n",
      "mean  -1.216642e-16  3.038026e-14 -6.595988e-14  7.246176e-17 -6.595988e-14   \n",
      "std    1.000042e+00  1.000042e+00  1.000042e+00  1.000042e+00  1.000042e+00   \n",
      "min   -1.013487e-01 -7.978984e+00 -1.722653e+00 -1.061226e+00 -1.722653e+00   \n",
      "25%   -4.462810e-02 -6.119986e-01 -3.462035e-01 -7.742457e-01 -3.462035e-01   \n",
      "50%   -2.422788e-02 -1.208662e-01  1.488522e-01 -2.623541e-01  1.488522e-01   \n",
      "75%    2.867434e-03  8.613985e-01  8.063786e-01  4.686241e-01  8.063786e-01   \n",
      "max    3.286723e+01  1.352531e+00  1.113480e+00  9.080403e+00  1.113480e+00   \n",
      "\n",
      "                  5             6             7  \n",
      "count  1.191400e+04  1.191400e+04  1.191400e+04  \n",
      "mean  -3.757277e-17  9.780847e-17 -1.634117e-16  \n",
      "std    1.000042e+00  1.000042e+00  1.000042e+00  \n",
      "min   -1.787076e+00 -2.677429e+00 -3.481597e+00  \n",
      "25%   -1.311301e+00 -6.698592e-01 -8.722610e-01  \n",
      "50%    5.125004e-01  9.029270e-03 -2.482162e-03  \n",
      "75%    5.125004e-01  6.685209e-01  8.672966e-01  \n",
      "max    3.248203e+00  2.676091e+00  3.476633e+00  \n"
     ]
    }
   ],
   "execution_count": 138
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:41:26.159634700Z",
     "start_time": "2026-11-19T02:41:26.084732800Z"
    }
   },
   "cell_type": "code",
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.metrics import mean_squared_error,r2_score\n",
    "regressor=LinearRegression()\n",
    "regressor.fit(X_train,y_train)\n",
    "y_pred=regressor.predict(X_test)\n",
    "print(r2_score(y_test,y_pred))\n",
    "\n"
   ],
   "id": "42e8a4c421ebe6cb",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8790936594904439\n"
     ]
    }
   ],
   "execution_count": 163
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:41:41.843428900Z",
     "start_time": "2026-11-19T02:41:32.939907900Z"
    }
   },
   "cell_type": "code",
   "source": [
    "rf=RandomForestRegressor(n_estimators=500,random_state=10,max_depth=15,min_samples_leaf=5)\n",
    "rf.fit(X_train,y_train)\n",
    "\n",
    "y_pred=rf.predict(X_test)\n",
    "print('R2',r2_score(y_test,y_pred))\n",
    "print(r2_score(y_test,rf.predict(X_test)))\n",
    "print(r2_score(y_train,rf.predict(X_train)))\n"
   ],
   "id": "35e014ed8f52f7f7",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "R2 0.9548766179603645\n",
      "0.9548766179603645\n",
      "0.9733068496872413\n"
     ]
    }
   ],
   "execution_count": 164
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:01:25.786494800Z",
     "start_time": "2026-11-19T01:58:27.735924Z"
    }
   },
   "cell_type": "code",
   "source": [
    "param_grid={\n",
    "    'n_estimators':[100,200,300,400,500],\n",
    "    'max_depth':[5,10,15,20,25],\n",
    "    'min_samples_leaf':[5,10,15,20,25],\n",
    "    'criterion':['squared_error']\n",
    "}\n",
    "grid=GridSearchCV(\n",
    "    estimator=rf,\n",
    "    param_grid=param_grid,\n",
    "    scoring='r2',\n",
    "    cv=5,\n",
    "    n_jobs=-1\n",
    ")\n",
    "grid.fit(X_train,y_train)\n",
    "y_pred=grid.predict(X_test)\n",
    "print(r2_score(y_test,y_pred))\n",
    "print(grid.best_params_)\n",
    "print(grid.best_score_)"
   ],
   "id": "fd3883f2ae60e9c8",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9317291528224125\n",
      "{'criterion': 'squared_error', 'max_depth': 15, 'min_samples_leaf': 5, 'n_estimators': 500}\n",
      "0.9307606071077444\n"
     ]
    }
   ],
   "execution_count": 148
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:42:12.196383600Z",
     "start_time": "2026-11-19T02:42:12.006220800Z"
    }
   },
   "cell_type": "code",
   "source": [
    "import joblib\n",
    "final_model=rf\n",
    "artifact={\n",
    "    'model':final_model,\n",
    "    'encoders':encoder,\n",
    "    'scaler':sc,\n",
    "    'features':list(X.columns),\n",
    "}\n",
    "joblib.dump(artifact,'car_price_model.pkl')\n",
    "print(\"saving model\")\n"
   ],
   "id": "813a0a50646625e6",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "saving model\n"
     ]
    }
   ],
   "execution_count": 165
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:42:20.427281700Z",
     "start_time": "2026-11-19T02:42:20.180970400Z"
    }
   },
   "cell_type": "code",
   "source": [
    "load=joblib.load('car_price_model.pkl')\n",
    "print(load.keys())\n",
    "print(type(load))"
   ],
   "id": "3bc8fb616c4fe764",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['model', 'encoders', 'scaler', 'features'])\n",
      "<class 'dict'>\n"
     ]
    }
   ],
   "execution_count": 166
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-19T02:47:42.371413100Z",
     "start_time": "2026-11-19T02:47:41.605079Z"
    }
   },
   "cell_type": "code",
   "source": [
    "import gradio as gr\n",
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "# 1. تحميل الموديل والأدوات المحفوظة\n",
    "bundle = joblib.load(\"car_price_model.pkl\")\n",
    "model = bundle[\"model\"]\n",
    "encoders = bundle[\"encoders\"]\n",
    "scaler = bundle[\"scaler\"]\n",
    "features = bundle[\"features\"]\n",
    "\n",
    "# 2. قوائم الاختيارات للـ Dropdowns\n",
    "if \"df\" in globals():\n",
    "  models_list = sorted(df[\"model\"].astype(str).str.strip().unique().tolist())\n",
    "  trans_list = sorted(\n",
    "      df[\"transmission\"].astype(str).str.strip().unique().tolist()\n",
    "  )\n",
    "  fuel_list = sorted(df[\"fueltype\"].astype(str).str.strip().unique().tolist())\n",
    "else:\n",
    "  models_list = [\"Golf\", \"Polo\", \"Passat\", \"Tiguan\", \"Fiesta\", \"Focus\", \"Beetle\"]\n",
    "  trans_list = [\"Manual\", \"Automatic\", \"Semi-Auto\"]\n",
    "  fuel_list = [\"Petrol\", \"Diesel\", \"Hybrid\", \"Electric\"]\n",
    "\n",
    "\n",
    "# 3. دالة التنبؤ\n",
    "def predict_car_price(\n",
    "    model_name, year, mileage, tax, mpg, enginesize, transmission, fueltype\n",
    "):\n",
    "  input_df = pd.DataFrame([{\n",
    "      \"model\": str(model_name).strip(),\n",
    "      \"year\": int(year),\n",
    "      \"mileage\": float(mileage),\n",
    "      \"tax\": float(tax),\n",
    "      \"mpg\": float(mpg),\n",
    "      \"enginesize\": float(enginesize),\n",
    "      \"transmission\": str(transmission).strip(),\n",
    "      \"fueltype\": str(fueltype).strip(),\n",
    "  }])\n",
    "\n",
    "  for col, enc in encoders.items():\n",
    "    if col in input_df.columns:\n",
    "      input_df[col] = enc.transform(input_df[[col]])\n",
    "\n",
    "  input_df = input_df[features]\n",
    "  input_scaled = scaler.transform(input_df)\n",
    "  pred_price = model.predict(input_scaled)[0]\n",
    "\n",
    "  return (\n",
    "      f\"### £ {pred_price:,.2f}\\n\"\n",
    "      f\"**الموديل:** {model_name} | **السنة:** {int(year)} | **الممشى:**\"\n",
    "      f\" {int(mileage):,} mi\"\n",
    "  )\n",
    "\n",
    "\n",
    "# 4. تصميم الواجهة بـ gr.Blocks\n",
    "custom_css = \"\"\"\n",
    ".gradio-container { max-width: 980px !important; margin: auto !important; }\n",
    ".result-box { border: 1px solid #3b82f6; border-radius: 12px; padding: 16px; }\n",
    "\"\"\"\n",
    "\n",
    "with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:\n",
    "  gr.Markdown(\"# 🚗 نظام توقع أسعار السيارات\\nتقدير فوري للسعر باستخدام نموذج **Random Forest** (بيانات سوق السيارات البريطاني).\")\n",
    "\n",
    "  with gr.Row():\n",
    "    with gr.Column(scale=1):\n",
    "      gr.Markdown(\"### 📋 البيانات الأساسية\")\n",
    "      model_input = gr.Dropdown(\n",
    "          choices=models_list,\n",
    "          value=models_list[0] if models_list else None,\n",
    "          label=\"الموديل (Model)\",\n",
    "      )\n",
    "      year_input = gr.Number(label=\"سنة الصنع (Year)\", value=2019, precision=0)\n",
    "      mileage_input = gr.Number(label=\"الممشى (Mileage)\", value=22000)\n",
    "      trans_input = gr.Dropdown(\n",
    "          choices=trans_list,\n",
    "          value=trans_list[0] if trans_list else None,\n",
    "          label=\"ناقل الحركة (Transmission)\",\n",
    "      )\n",
    "\n",
    "    with gr.Column(scale=1):\n",
    "      gr.Markdown(\"### ⚙️ المواصفات الفنية\")\n",
    "      fuel_input = gr.Dropdown(\n",
    "          choices=fuel_list,\n",
    "          value=fuel_list[0] if fuel_list else None,\n",
    "          label=\"نوع الوقود (Fuel Type)\",\n",
    "      )\n",
    "      engine_input = gr.Number(\n",
    "          label=\"سعة المحرك باللتر (Engine Size)\", value=1.6\n",
    "      )\n",
    "      mpg_input = gr.Number(label=\"استهلاك الوقود (MPG)\", value=52.0)\n",
    "      tax_input = gr.Number(label=\"الضريبة السنوية (Tax)\", value=145)\n",
    "\n",
    "  predict_btn = gr.Button(\"🔍 احسب السعر المتوقع\", variant=\"primary\", size=\"lg\")\n",
    "\n",
    "  with gr.Group(elem_classes=\"result-box\"):\n",
    "    gr.Markdown(\"### 💰 السعر التقديري\")\n",
    "    output_box = gr.Markdown(\n",
    "        \"أدخل بيانات السيارة واضغط على **احسب السعر المتوقع** لعرض النتيجة.\"\n",
    "    )\n",
    "\n",
    "  gr.Examples(\n",
    "      examples=[\n",
    "          [\"Golf\", 2019, 18000, 145, 55.0, 1.5, \"Manual\", \"Petrol\"],\n",
    "          [\"Polo\", 2017, 35000, 20, 60.0, 1.0, \"Manual\", \"Petrol\"],\n",
    "          [\"Tiguan\", 2020, 15000, 150, 44.0, 2.0, \"Automatic\", \"Diesel\"],\n",
    "      ],\n",
    "      inputs=[\n",
    "          model_input,\n",
    "          year_input,\n",
    "          mileage_input,\n",
    "          tax_input,\n",
    "          mpg_input,\n",
    "          engine_input,\n",
    "          trans_input,\n",
    "          fuel_input,\n",
    "      ],\n",
    "      outputs=output_box,\n",
    "      fn=predict_car_price,\n",
    "      cache_examples=False,\n",
    "      label=\"أمثلة سريعة للتجربة\",\n",
    "  )\n",
    "\n",
    "  predict_btn.click(\n",
    "      fn=predict_car_price,\n",
    "      inputs=[\n",
    "          model_input,\n",
    "          year_input,\n",
    "          mileage_input,\n",
    "          tax_input,\n",
    "          mpg_input,\n",
    "          engine_input,\n",
    "          trans_input,\n",
    "          fuel_input,\n",
    "      ],\n",
    "      outputs=output_box,\n",
    "  )\n",
    "\n",
    "demo.launch()"
   ],
   "id": "49e24829336ef581",
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Dell\\AppData\\Local\\Temp\\ipykernel_18948\\3583757142.py:61: UserWarning: The parameters have been moved from the Blocks constructor to the launch() method in Gradio 6.0: theme, css. Please pass these parameters to launch() instead.\n",
      "  with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* Running on local URL:  http://127.0.0.1:7863\n",
      "* To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ],
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7863/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data",
     "jetTransient": {
      "display_id": None
     }
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 173
  },
  {
   "metadata": {},
   "cell_type": "code",
   "outputs": [],
   "execution_count": None,
   "source": "",
   "id": "bdb27107f324327b"
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
