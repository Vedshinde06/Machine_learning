{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f5d51310",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:42.619143Z",
     "iopub.status.busy": "2025-03-04T17:15:42.618757Z",
     "iopub.status.idle": "2025-03-04T17:15:43.692108Z",
     "shell.execute_reply": "2025-03-04T17:15:43.690756Z"
    },
    "papermill": {
     "duration": 1.08406,
     "end_time": "2025-03-04T17:15:43.694008",
     "exception": false,
     "start_time": "2025-03-04T17:15:42.609948",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/kaggle/input/titanicdataset-traincsv/train.csv\n"
     ]
    }
   ],
   "source": [
    "# This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
    "# For example, here's several helpful packages to load\n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "\n",
    "# Input data files are available in the read-only \"../input/\" directory\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "import os\n",
    "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "    for filename in filenames:\n",
    "        print(os.path.join(dirname, filename))\n",
    "\n",
    "# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n",
    "# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "90fe1b9b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:43.710994Z",
     "iopub.status.busy": "2025-03-04T17:15:43.710507Z",
     "iopub.status.idle": "2025-03-04T17:15:43.734838Z",
     "shell.execute_reply": "2025-03-04T17:15:43.733847Z"
    },
    "papermill": {
     "duration": 0.034844,
     "end_time": "2025-03-04T17:15:43.736957",
     "exception": false,
     "start_time": "2025-03-04T17:15:43.702113",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv('/kaggle/input/titanicdataset-traincsv/train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a2bc0305",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:43.753081Z",
     "iopub.status.busy": "2025-03-04T17:15:43.752692Z",
     "iopub.status.idle": "2025-03-04T17:15:43.787522Z",
     "shell.execute_reply": "2025-03-04T17:15:43.786246Z"
    },
    "papermill": {
     "duration": 0.044704,
     "end_time": "2025-03-04T17:15:43.789488",
     "exception": false,
     "start_time": "2025-03-04T17:15:43.744784",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "22a719dd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:43.806529Z",
     "iopub.status.busy": "2025-03-04T17:15:43.806112Z",
     "iopub.status.idle": "2025-03-04T17:15:43.822769Z",
     "shell.execute_reply": "2025-03-04T17:15:43.821485Z"
    },
    "papermill": {
     "duration": 0.027912,
     "end_time": "2025-03-04T17:15:43.824833",
     "exception": false,
     "start_time": "2025-03-04T17:15:43.796921",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "new_df = df[['Age','Pclass','SibSp','Parch','Survived']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e90b6ac1",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:43.840999Z",
     "iopub.status.busy": "2025-03-04T17:15:43.840638Z",
     "iopub.status.idle": "2025-03-04T17:15:43.845266Z",
     "shell.execute_reply": "2025-03-04T17:15:43.844172Z"
    },
    "papermill": {
     "duration": 0.014871,
     "end_time": "2025-03-04T17:15:43.847108",
     "exception": false,
     "start_time": "2025-03-04T17:15:43.832237",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "new_df = new_df.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b61809b0",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:43.863069Z",
     "iopub.status.busy": "2025-03-04T17:15:43.862713Z",
     "iopub.status.idle": "2025-03-04T17:15:43.874179Z",
     "shell.execute_reply": "2025-03-04T17:15:43.872835Z"
    },
    "papermill": {
     "duration": 0.021563,
     "end_time": "2025-03-04T17:15:43.876341",
     "exception": false,
     "start_time": "2025-03-04T17:15:43.854778",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
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
       "      <th>Age</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>26.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>35.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Age  Pclass  SibSp  Parch  Survived\n",
       "0  22.0       3      1      0         0\n",
       "1  38.0       1      1      0         1\n",
       "2  26.0       3      0      0         1\n",
       "3  35.0       1      1      0         1\n",
       "4  35.0       3      0      0         0"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e8803b56",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:43.895378Z",
     "iopub.status.busy": "2025-03-04T17:15:43.895015Z",
     "iopub.status.idle": "2025-03-04T17:15:43.902201Z",
     "shell.execute_reply": "2025-03-04T17:15:43.901174Z"
    },
    "papermill": {
     "duration": 0.018933,
     "end_time": "2025-03-04T17:15:43.904155",
     "exception": false,
     "start_time": "2025-03-04T17:15:43.885222",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "new_df.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0d434591",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:43.920734Z",
     "iopub.status.busy": "2025-03-04T17:15:43.920341Z",
     "iopub.status.idle": "2025-03-04T17:15:43.925946Z",
     "shell.execute_reply": "2025-03-04T17:15:43.924584Z"
    },
    "papermill": {
     "duration": 0.01581,
     "end_time": "2025-03-04T17:15:43.927694",
     "exception": false,
     "start_time": "2025-03-04T17:15:43.911884",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "x=new_df.iloc[:,:4]\n",
    "y=new_df.iloc[:,-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "01b8a31c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:43.944112Z",
     "iopub.status.busy": "2025-03-04T17:15:43.943783Z",
     "iopub.status.idle": "2025-03-04T17:15:45.774405Z",
     "shell.execute_reply": "2025-03-04T17:15:45.773318Z"
    },
    "papermill": {
     "duration": 1.84123,
     "end_time": "2025-03-04T17:15:45.776536",
     "exception": false,
     "start_time": "2025-03-04T17:15:43.935306",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import cross_val_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "cf823224",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:45.793480Z",
     "iopub.status.busy": "2025-03-04T17:15:45.792945Z",
     "iopub.status.idle": "2025-03-04T17:15:46.080225Z",
     "shell.execute_reply": "2025-03-04T17:15:46.079155Z"
    },
    "papermill": {
     "duration": 0.29781,
     "end_time": "2025-03-04T17:15:46.082084",
     "exception": false,
     "start_time": "2025-03-04T17:15:45.784274",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6933333333333332"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(cross_val_score(LogisticRegression(),x,y,scoring='accuracy',cv=20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7628d50c",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.098803Z",
     "iopub.status.busy": "2025-03-04T17:15:46.098340Z",
     "iopub.status.idle": "2025-03-04T17:15:46.104802Z",
     "shell.execute_reply": "2025-03-04T17:15:46.103509Z"
    },
    "papermill": {
     "duration": 0.016953,
     "end_time": "2025-03-04T17:15:46.106695",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.089742",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "new_df['Family_size'] = new_df['SibSp'] + new_df['Parch'] + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "aa069122",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.123659Z",
     "iopub.status.busy": "2025-03-04T17:15:46.123270Z",
     "iopub.status.idle": "2025-03-04T17:15:46.127982Z",
     "shell.execute_reply": "2025-03-04T17:15:46.126847Z"
    },
    "papermill": {
     "duration": 0.014904,
     "end_time": "2025-03-04T17:15:46.129658",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.114754",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "def myfunc(num):\n",
    "    if num == 1:\n",
    "        return 0\n",
    "    elif num >1 and num <= 4:\n",
    "        return 1\n",
    "    else:\n",
    "        return 2\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8296ecab",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.146057Z",
     "iopub.status.busy": "2025-03-04T17:15:46.145715Z",
     "iopub.status.idle": "2025-03-04T17:15:46.151779Z",
     "shell.execute_reply": "2025-03-04T17:15:46.150751Z"
    },
    "papermill": {
     "duration": 0.016311,
     "end_time": "2025-03-04T17:15:46.153565",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.137254",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myfunc(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "40d8634e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.170075Z",
     "iopub.status.busy": "2025-03-04T17:15:46.169740Z",
     "iopub.status.idle": "2025-03-04T17:15:46.175043Z",
     "shell.execute_reply": "2025-03-04T17:15:46.174157Z"
    },
    "papermill": {
     "duration": 0.015318,
     "end_time": "2025-03-04T17:15:46.176741",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.161423",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "new_df['Family_type'] = new_df['Family_size'].apply(myfunc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3bad35ab",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.193387Z",
     "iopub.status.busy": "2025-03-04T17:15:46.193036Z",
     "iopub.status.idle": "2025-03-04T17:15:46.206554Z",
     "shell.execute_reply": "2025-03-04T17:15:46.205444Z"
    },
    "papermill": {
     "duration": 0.023723,
     "end_time": "2025-03-04T17:15:46.208452",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.184729",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
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
       "      <th>Age</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Family_size</th>\n",
       "      <th>Family_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>26.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>35.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>885</th>\n",
       "      <td>39.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>27.0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>19.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>26.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>32.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>714 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Age  Pclass  SibSp  Parch  Survived  Family_size  Family_type\n",
       "0    22.0       3      1      0         0            2            1\n",
       "1    38.0       1      1      0         1            2            1\n",
       "2    26.0       3      0      0         1            1            0\n",
       "3    35.0       1      1      0         1            2            1\n",
       "4    35.0       3      0      0         0            1            0\n",
       "..    ...     ...    ...    ...       ...          ...          ...\n",
       "885  39.0       3      0      5         0            6            2\n",
       "886  27.0       2      0      0         0            1            0\n",
       "887  19.0       1      0      0         1            1            0\n",
       "889  26.0       1      0      0         1            1            0\n",
       "890  32.0       3      0      0         0            1            0\n",
       "\n",
       "[714 rows x 7 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "26197c2a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.226328Z",
     "iopub.status.busy": "2025-03-04T17:15:46.225996Z",
     "iopub.status.idle": "2025-03-04T17:15:46.231469Z",
     "shell.execute_reply": "2025-03-04T17:15:46.230433Z"
    },
    "papermill": {
     "duration": 0.01635,
     "end_time": "2025-03-04T17:15:46.233266",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.216916",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "new_df.drop(columns=['SibSp','Parch'], inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "36c56112",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.255144Z",
     "iopub.status.busy": "2025-03-04T17:15:46.254786Z",
     "iopub.status.idle": "2025-03-04T17:15:46.265410Z",
     "shell.execute_reply": "2025-03-04T17:15:46.264275Z"
    },
    "papermill": {
     "duration": 0.023076,
     "end_time": "2025-03-04T17:15:46.267237",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.244161",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
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
       "      <th>Age</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Family_size</th>\n",
       "      <th>Family_type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>22.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>26.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>35.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Age  Pclass  Survived  Family_size  Family_type\n",
       "0  22.0       3         0            2            1\n",
       "1  38.0       1         1            2            1\n",
       "2  26.0       3         1            1            0\n",
       "3  35.0       1         1            2            1\n",
       "4  35.0       3         0            1            0"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "adb90f63",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.284717Z",
     "iopub.status.busy": "2025-03-04T17:15:46.284004Z",
     "iopub.status.idle": "2025-03-04T17:15:46.290312Z",
     "shell.execute_reply": "2025-03-04T17:15:46.289170Z"
    },
    "papermill": {
     "duration": 0.01679,
     "end_time": "2025-03-04T17:15:46.291943",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.275153",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "x2= new_df.drop(columns=['Survived'])\n",
    "x3= new_df.drop(columns=['Survived','Family_size'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9c1589ae",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.309223Z",
     "iopub.status.busy": "2025-03-04T17:15:46.308857Z",
     "iopub.status.idle": "2025-03-04T17:15:46.597217Z",
     "shell.execute_reply": "2025-03-04T17:15:46.596026Z"
    },
    "papermill": {
     "duration": 0.299496,
     "end_time": "2025-03-04T17:15:46.599277",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.299781",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7046428571428571"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(cross_val_score(LogisticRegression(),x2,y,scoring='accuracy',cv=20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6b170d67",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:46.618410Z",
     "iopub.status.busy": "2025-03-04T17:15:46.618041Z",
     "iopub.status.idle": "2025-03-04T17:15:47.004777Z",
     "shell.execute_reply": "2025-03-04T17:15:47.003374Z"
    },
    "papermill": {
     "duration": 0.397758,
     "end_time": "2025-03-04T17:15:47.006970",
     "exception": false,
     "start_time": "2025-03-04T17:15:46.609212",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7003174603174602"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(cross_val_score(LogisticRegression(),x3,y,scoring='accuracy',cv=20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "3a54d9a3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.028051Z",
     "iopub.status.busy": "2025-03-04T17:15:47.027693Z",
     "iopub.status.idle": "2025-03-04T17:15:47.297223Z",
     "shell.execute_reply": "2025-03-04T17:15:47.295789Z"
    },
    "papermill": {
     "duration": 0.280421,
     "end_time": "2025-03-04T17:15:47.299115",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.018694",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6933333333333332"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(cross_val_score(LogisticRegression(),x,y,scoring='accuracy',cv=20))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53c6c8ee",
   "metadata": {
    "papermill": {
     "duration": 0.008177,
     "end_time": "2025-03-04T17:15:47.317551",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.309374",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Feature Spliting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "369d0982",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.334841Z",
     "iopub.status.busy": "2025-03-04T17:15:47.334466Z",
     "iopub.status.idle": "2025-03-04T17:15:47.342312Z",
     "shell.execute_reply": "2025-03-04T17:15:47.341376Z"
    },
    "papermill": {
     "duration": 0.01856,
     "end_time": "2025-03-04T17:15:47.344034",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.325474",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                                Braund, Mr. Owen Harris\n",
       "1      Cumings, Mrs. John Bradley (Florence Briggs Th...\n",
       "2                                 Heikkinen, Miss. Laina\n",
       "3           Futrelle, Mrs. Jacques Heath (Lily May Peel)\n",
       "4                               Allen, Mr. William Henry\n",
       "                             ...                        \n",
       "886                                Montvila, Rev. Juozas\n",
       "887                         Graham, Miss. Margaret Edith\n",
       "888             Johnston, Miss. Catherine Helen \"Carrie\"\n",
       "889                                Behr, Mr. Karl Howell\n",
       "890                                  Dooley, Mr. Patrick\n",
       "Name: Name, Length: 891, dtype: object"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Name']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "eceb57c8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.361806Z",
     "iopub.status.busy": "2025-03-04T17:15:47.361386Z",
     "iopub.status.idle": "2025-03-04T17:15:47.373427Z",
     "shell.execute_reply": "2025-03-04T17:15:47.372471Z"
    },
    "papermill": {
     "duration": 0.022871,
     "end_time": "2025-03-04T17:15:47.375199",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.352328",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Braund</td>\n",
       "      <td>Mr. Owen Harris</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Cumings</td>\n",
       "      <td>Mrs. John Bradley (Florence Briggs Thayer)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Heikkinen</td>\n",
       "      <td>Miss. Laina</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Futrelle</td>\n",
       "      <td>Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Allen</td>\n",
       "      <td>Mr. William Henry</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>Montvila</td>\n",
       "      <td>Rev. Juozas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>Graham</td>\n",
       "      <td>Miss. Margaret Edith</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Johnston</td>\n",
       "      <td>Miss. Catherine Helen \"Carrie\"</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>Behr</td>\n",
       "      <td>Mr. Karl Howell</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>Dooley</td>\n",
       "      <td>Mr. Patrick</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             0                                            1\n",
       "0       Braund                              Mr. Owen Harris\n",
       "1      Cumings   Mrs. John Bradley (Florence Briggs Thayer)\n",
       "2    Heikkinen                                  Miss. Laina\n",
       "3     Futrelle           Mrs. Jacques Heath (Lily May Peel)\n",
       "4        Allen                            Mr. William Henry\n",
       "..         ...                                          ...\n",
       "886   Montvila                                  Rev. Juozas\n",
       "887     Graham                         Miss. Margaret Edith\n",
       "888   Johnston               Miss. Catherine Helen \"Carrie\"\n",
       "889       Behr                              Mr. Karl Howell\n",
       "890     Dooley                                  Mr. Patrick\n",
       "\n",
       "[891 rows x 2 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " df['Name'].str.split(',', expand=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "42307d3a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.393271Z",
     "iopub.status.busy": "2025-03-04T17:15:47.392938Z",
     "iopub.status.idle": "2025-03-04T17:15:47.402696Z",
     "shell.execute_reply": "2025-03-04T17:15:47.401491Z"
    },
    "papermill": {
     "duration": 0.020746,
     "end_time": "2025-03-04T17:15:47.404482",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.383736",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0                                  Mr. Owen Harris\n",
       "1       Mrs. John Bradley (Florence Briggs Thayer)\n",
       "2                                      Miss. Laina\n",
       "3               Mrs. Jacques Heath (Lily May Peel)\n",
       "4                                Mr. William Henry\n",
       "                          ...                     \n",
       "886                                    Rev. Juozas\n",
       "887                           Miss. Margaret Edith\n",
       "888                 Miss. Catherine Helen \"Carrie\"\n",
       "889                                Mr. Karl Howell\n",
       "890                                    Mr. Patrick\n",
       "Name: 1, Length: 891, dtype: object"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " df['Name'].str.split(',', expand = True)[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "0f67bba9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.424193Z",
     "iopub.status.busy": "2025-03-04T17:15:47.423567Z",
     "iopub.status.idle": "2025-03-04T17:15:47.439636Z",
     "shell.execute_reply": "2025-03-04T17:15:47.438279Z"
    },
    "papermill": {
     "duration": 0.028729,
     "end_time": "2025-03-04T17:15:47.441805",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.413076",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mr</td>\n",
       "      <td>Owen Harris</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mrs</td>\n",
       "      <td>John Bradley (Florence Briggs Thayer)</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Miss</td>\n",
       "      <td>Laina</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mrs</td>\n",
       "      <td>Jacques Heath (Lily May Peel)</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mr</td>\n",
       "      <td>William Henry</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>Rev</td>\n",
       "      <td>Juozas</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>Miss</td>\n",
       "      <td>Margaret Edith</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Miss</td>\n",
       "      <td>Catherine Helen \"Carrie\"</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>Mr</td>\n",
       "      <td>Karl Howell</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>Mr</td>\n",
       "      <td>Patrick</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         0                                       1     2\n",
       "0       Mr                             Owen Harris  None\n",
       "1      Mrs   John Bradley (Florence Briggs Thayer)  None\n",
       "2     Miss                                   Laina  None\n",
       "3      Mrs           Jacques Heath (Lily May Peel)  None\n",
       "4       Mr                           William Henry  None\n",
       "..     ...                                     ...   ...\n",
       "886    Rev                                  Juozas  None\n",
       "887   Miss                          Margaret Edith  None\n",
       "888   Miss                Catherine Helen \"Carrie\"  None\n",
       "889     Mr                             Karl Howell  None\n",
       "890     Mr                                 Patrick  None\n",
       "\n",
       "[891 rows x 3 columns]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " df['Name'].str.split(',', expand = True)[1].str.split('.', expand=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f00e2e8d",
   "metadata": {
    "papermill": {
     "duration": 0.009341,
     "end_time": "2025-03-04T17:15:47.459991",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.450650",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Creating a new colums for titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "ced08893",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.479065Z",
     "iopub.status.busy": "2025-03-04T17:15:47.478728Z",
     "iopub.status.idle": "2025-03-04T17:15:47.487295Z",
     "shell.execute_reply": "2025-03-04T17:15:47.486212Z"
    },
    "papermill": {
     "duration": 0.019967,
     "end_time": "2025-03-04T17:15:47.489089",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.469122",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df['Titles'] =  df['Name'].str.split(',', expand = True)[1].str.split('.', expand=True)[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a2262931",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.507860Z",
     "iopub.status.busy": "2025-03-04T17:15:47.507499Z",
     "iopub.status.idle": "2025-03-04T17:15:47.522304Z",
     "shell.execute_reply": "2025-03-04T17:15:47.520926Z"
    },
    "papermill": {
     "duration": 0.026548,
     "end_time": "2025-03-04T17:15:47.524428",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.497880",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
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
       "      <th>Titles</th>\n",
       "      <th>Name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mr</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mrs</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Miss</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mrs</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mr</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>Rev</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>Miss</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>Miss</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>Mr</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>Mr</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    Titles                                               Name\n",
       "0       Mr                            Braund, Mr. Owen Harris\n",
       "1      Mrs  Cumings, Mrs. John Bradley (Florence Briggs Th...\n",
       "2     Miss                             Heikkinen, Miss. Laina\n",
       "3      Mrs       Futrelle, Mrs. Jacques Heath (Lily May Peel)\n",
       "4       Mr                           Allen, Mr. William Henry\n",
       "..     ...                                                ...\n",
       "886    Rev                              Montvila, Rev. Juozas\n",
       "887   Miss                       Graham, Miss. Margaret Edith\n",
       "888   Miss           Johnston, Miss. Catherine Helen \"Carrie\"\n",
       "889     Mr                              Behr, Mr. Karl Howell\n",
       "890     Mr                                Dooley, Mr. Patrick\n",
       "\n",
       "[891 rows x 2 columns]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['Titles', 'Name']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "1386a0f8",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.543843Z",
     "iopub.status.busy": "2025-03-04T17:15:47.543498Z",
     "iopub.status.idle": "2025-03-04T17:15:47.565327Z",
     "shell.execute_reply": "2025-03-04T17:15:47.564282Z"
    },
    "papermill": {
     "duration": 0.033517,
     "end_time": "2025-03-04T17:15:47.566950",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.533433",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
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
       "      <th>Survived</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Titles</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>the Countess</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mlle</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sir</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ms</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Lady</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mme</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mrs</th>\n",
       "      <td>0.792000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Miss</th>\n",
       "      <td>0.697802</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Master</th>\n",
       "      <td>0.575000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Col</th>\n",
       "      <td>0.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Major</th>\n",
       "      <td>0.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dr</th>\n",
       "      <td>0.428571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mr</th>\n",
       "      <td>0.156673</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Jonkheer</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rev</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Don</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Capt</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Survived\n",
       "Titles                \n",
       "the Countess  1.000000\n",
       "Mlle          1.000000\n",
       "Sir           1.000000\n",
       "Ms            1.000000\n",
       "Lady          1.000000\n",
       "Mme           1.000000\n",
       "Mrs           0.792000\n",
       "Miss          0.697802\n",
       "Master        0.575000\n",
       "Col           0.500000\n",
       "Major         0.500000\n",
       "Dr            0.428571\n",
       "Mr            0.156673\n",
       "Jonkheer      0.000000\n",
       "Rev           0.000000\n",
       "Don           0.000000\n",
       "Capt          0.000000"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('Titles')[['Survived']].mean().sort_values(by='Survived', ascending=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "26e5ade9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.586495Z",
     "iopub.status.busy": "2025-03-04T17:15:47.586070Z",
     "iopub.status.idle": "2025-03-04T17:15:47.593467Z",
     "shell.execute_reply": "2025-03-04T17:15:47.592330Z"
    },
    "papermill": {
     "duration": 0.019158,
     "end_time": "2025-03-04T17:15:47.595272",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.576114",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-29-bf12d666d6e7>:3: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!\n",
      "You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.\n",
      "A typical example is when you are setting values in a column of a DataFrame, like:\n",
      "\n",
      "df[\"col\"][row_indexer] = value\n",
      "\n",
      "Use `df.loc[row_indexer, \"col\"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "\n",
      "  df['IS_married'].loc[df['Titles'] == 'Mrs'] = 1\n",
      "<ipython-input-29-bf12d666d6e7>:3: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df['IS_married'].loc[df['Titles'] == 'Mrs'] = 1\n"
     ]
    }
   ],
   "source": [
    "df['IS_married']=0\n",
    "#df['IS_married'].loc[df['Titles']=='Mrs']=1\n",
    "df['IS_married'].loc[df['Titles'] == 'Mrs'] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d2a15e96",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.614993Z",
     "iopub.status.busy": "2025-03-04T17:15:47.614635Z",
     "iopub.status.idle": "2025-03-04T17:15:47.620506Z",
     "shell.execute_reply": "2025-03-04T17:15:47.619145Z"
    },
    "papermill": {
     "duration": 0.017856,
     "end_time": "2025-03-04T17:15:47.622251",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.604395",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "df.loc[df['Titles'] == 'Mrs', 'IS_married'] = 1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "73c85673",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-03-04T17:15:47.641899Z",
     "iopub.status.busy": "2025-03-04T17:15:47.641560Z",
     "iopub.status.idle": "2025-03-04T17:15:47.661796Z",
     "shell.execute_reply": "2025-03-04T17:15:47.660674Z"
    },
    "papermill": {
     "duration": 0.032232,
     "end_time": "2025-03-04T17:15:47.663629",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.631397",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/usr/local/lib/python3.10/dist-packages/pandas/io/formats/format.py:1458: RuntimeWarning: invalid value encountered in greater\n",
      "  has_large_values = (abs_vals > 1e6).any()\n",
      "/usr/local/lib/python3.10/dist-packages/pandas/io/formats/format.py:1459: RuntimeWarning: invalid value encountered in less\n",
      "  has_small_values = ((abs_vals < 10 ** (-self.digits)) & (abs_vals > 0)).any()\n",
      "/usr/local/lib/python3.10/dist-packages/pandas/io/formats/format.py:1459: RuntimeWarning: invalid value encountered in greater\n",
      "  has_small_values = ((abs_vals < 10 ** (-self.digits)) & (abs_vals > 0)).any()\n"
     ]
    },
    {
     "data": {
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
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "      <th>Titles</th>\n",
       "      <th>IS_married</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>Nasser, Mrs. Nicholas (Adele Achem)</td>\n",
       "      <td>female</td>\n",
       "      <td>14.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>237736</td>\n",
       "      <td>30.0708</td>\n",
       "      <td>NaN</td>\n",
       "      <td>C</td>\n",
       "      <td>Mrs</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>374</th>\n",
       "      <td>375</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Palsson, Miss. Stina Viola</td>\n",
       "      <td>female</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>349909</td>\n",
       "      <td>21.0750</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "      <td>Miss</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>558</th>\n",
       "      <td>559</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Taussig, Mrs. Emil (Tillie Mandelbaum)</td>\n",
       "      <td>female</td>\n",
       "      <td>39.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>110413</td>\n",
       "      <td>79.6500</td>\n",
       "      <td>E67</td>\n",
       "      <td>S</td>\n",
       "      <td>Mrs</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>256</th>\n",
       "      <td>257</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Thorne, Mrs. Gertrude Maybelle</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17585</td>\n",
       "      <td>79.2000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>C</td>\n",
       "      <td>Mrs</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>398</th>\n",
       "      <td>399</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Pain, Dr. Alfred</td>\n",
       "      <td>male</td>\n",
       "      <td>23.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>244278</td>\n",
       "      <td>10.5000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "      <td>Dr</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>885</th>\n",
       "      <td>886</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Rice, Mrs. William (Margaret Norton)</td>\n",
       "      <td>female</td>\n",
       "      <td>39.0</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>382652</td>\n",
       "      <td>29.1250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "      <td>Mrs</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "      <td>Mr</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>832</th>\n",
       "      <td>833</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Saad, Mr. Amin</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2671</td>\n",
       "      <td>7.2292</td>\n",
       "      <td>NaN</td>\n",
       "      <td>C</td>\n",
       "      <td>Mr</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>61</th>\n",
       "      <td>62</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Icard, Miss. Amelie</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>113572</td>\n",
       "      <td>80.0000</td>\n",
       "      <td>B28</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Miss</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>81</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Waelens, Mr. Achille</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>345767</td>\n",
       "      <td>9.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "      <td>Mr</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass                                    Name  \\\n",
       "9             10         1       2     Nasser, Mrs. Nicholas (Adele Achem)   \n",
       "374          375         0       3              Palsson, Miss. Stina Viola   \n",
       "558          559         1       1  Taussig, Mrs. Emil (Tillie Mandelbaum)   \n",
       "256          257         1       1          Thorne, Mrs. Gertrude Maybelle   \n",
       "398          399         0       2                        Pain, Dr. Alfred   \n",
       "885          886         0       3    Rice, Mrs. William (Margaret Norton)   \n",
       "889          890         1       1                   Behr, Mr. Karl Howell   \n",
       "832          833         0       3                          Saad, Mr. Amin   \n",
       "61            62         1       1                     Icard, Miss. Amelie   \n",
       "80            81         0       3                    Waelens, Mr. Achille   \n",
       "\n",
       "        Sex   Age  SibSp  Parch    Ticket     Fare Cabin Embarked Titles  \\\n",
       "9    female  14.0      1      0    237736  30.0708   NaN        C    Mrs   \n",
       "374  female   3.0      3      1    349909  21.0750   NaN        S   Miss   \n",
       "558  female  39.0      1      1    110413  79.6500   E67        S    Mrs   \n",
       "256  female   NaN      0      0  PC 17585  79.2000   NaN        C    Mrs   \n",
       "398    male  23.0      0      0    244278  10.5000   NaN        S     Dr   \n",
       "885  female  39.0      0      5    382652  29.1250   NaN        Q    Mrs   \n",
       "889    male  26.0      0      0    111369  30.0000  C148        C     Mr   \n",
       "832    male   NaN      0      0      2671   7.2292   NaN        C     Mr   \n",
       "61   female  38.0      0      0    113572  80.0000   B28      NaN   Miss   \n",
       "80     male  22.0      0      0    345767   9.0000   NaN        S     Mr   \n",
       "\n",
       "     IS_married  \n",
       "9             0  \n",
       "374           0  \n",
       "558           0  \n",
       "256           0  \n",
       "398           0  \n",
       "885           0  \n",
       "889           0  \n",
       "832           0  \n",
       "61            0  \n",
       "80            0  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sample(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a860032",
   "metadata": {
    "papermill": {
     "duration": 0.009442,
     "end_time": "2025-03-04T17:15:47.683472",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.674030",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d451d223",
   "metadata": {
    "papermill": {
     "duration": 0.009657,
     "end_time": "2025-03-04T17:15:47.703778",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.694121",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf4b818d",
   "metadata": {
    "papermill": {
     "duration": 0.009339,
     "end_time": "2025-03-04T17:15:47.722500",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.713161",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9303f347",
   "metadata": {
    "papermill": {
     "duration": 0.009345,
     "end_time": "2025-03-04T17:15:47.741528",
     "exception": false,
     "start_time": "2025-03-04T17:15:47.732183",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 11657,
     "sourceId": 16098,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 30918,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 8.885328,
   "end_time": "2025-03-04T17:15:48.472035",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-03-04T17:15:39.586707",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
