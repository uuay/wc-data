import requests
import pandas as pd
import json
import xmltodict

class GovAPIScratcher:

    def __init__(self):
        with open('config.json', 'r') as f:
            config = json.load(f)

        self.baseUrl = config['DEFAULT']['govService']['url']
        self.crtiKey = config['DEFAULT']['govService']['testKey']
        self.callTp = config['DEFAULT']['govService']['callTp']
        self.charTrgterArray = config['DEFAULT']['govService']['charTrgterArray']
        self.numOfRows = config['DEFAULT']['govService']['numOfRows']

        # self.lifeArray = ['00'+str(i) for i in range(1, 7)]
        self.lifeArray = ['002']
        # obstKiArray = [str(i)+'0' for i in range(1, 10)] + [str(i)+'0' for i in range(ord('A'), ord('F')+1)]
        self.obstKiArray = ['10']
        self.obstLvArray = ['2']
        # self.obstLvArray = [str(i) for i in range(1, 7)]

    def request(self, url, params):
        response = requests.get(url=url, params=params)
        result = json.loads(json.dumps(xmltodict.parse(response.content))).get('wantedList').get('servList')
        return result

    def scratchIdToDataFrame(self, url, params):
        result = self.request(url, params)
        list = [[r.get('servId'), params.get('lifeArray'), params.get('obstKiArray'), params.get('obstLvArray')] for r in result]
        print(list)
        df = pd.DataFrame(data=list, columns=['servId', 'life', 'obstKi', 'obstLv'])
        return df

    def scratchForId(self, filepath):
        print('=============start')

        df = pd.DataFrame(columns=['servId', 'life', 'obstKi', 'obstLv'])
        for life in self.lifeArray:
            for obstKi in self.obstKiArray:
                for obstLv in self.obstLvArray:
                    params = {
                        'crtiKey': self.crtiKey,
                        'charTrgterArray': self.charTrgterArray,
                        'callTp': self.callTp,
                        'numOfRows': self.numOfRows,
                        'lifeArray': life,
                        'obstKiArray': obstKi,
                        'obstLvArray': obstLv
                    }
                    subDf = self.scratchIdToDataFrame(url=self.baseUrl, params=params)
                    df = df.append(subDf)
        df.to_csv(filepath, mode='w')

    def scratchForAll(self, filepath):
        params = {
            'crtiKey': self.crtiKey,
            'charTrgterArray': self.charTrgterArray,
            'callTp': self.callTp,
            'numOfRows': self.numOfRows
        }
        response = self.request(url=self.baseUrl, params=params)
        print(response)
        df = pd.DataFrame(columns=list(response[0].keys()))
        for n in response:
            subDF = pd.DataFrame(data = [n.values()], columns = list(n.keys()))
            df = df.append(subDF)
        df.to_csv(filepath, mode='w')


object = GovAPIScratcher()
# object.scratchForId("./test.csv")
object.scratchForAll("./all.csv")
