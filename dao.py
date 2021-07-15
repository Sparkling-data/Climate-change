import cx_Oracle
import json
import collections  # 데이터를 어떤 구조로 관리할 것이가를 의미하는 자료 구조를 지원하는 library
import pandas as pd


class chart_dao:

    def chart2(self):
        #data = []
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()
        cur.execute("select * from co2tem")
        conn.commit()
        rows = cur.fetchall()
        v = []  # v 변수에 python 구조의 dic 구조로 저장 -> data 변수로 json 포멧으로 변환
        for row in rows:
            # print(row)
            d = collections.OrderedDict()

            d['year'] = row[0]
            # print(d)
            d['co2_den'] = row[1]
            d['temgap'] = row[2]

            v.append(d)  # 이미 존재하는 list의 마지막 요소로 저장(add)
            # print("-----------")
            # print(v)
        data = json.dumps(v)  # json 포멧으로 자동 변환
        # print(data)
        # df = pd.DataFrame(v)
        # print(df)
        # print(type(df))
        # # df.columns = ['year', 'co2_den', 'temgap']
        # df.to_excel('C:/20205-lab/project/Climate/climate.xlsx', index=False)
        # # print(df)

        # data = '{"year":"' + str(row[0]) + \
        #     '", "co2_den":"' + str(row[1]) + \
        #     '"," temgap":"' + str(row[2])+'"}'
        # print(data)
        # return data
        # print(data)   리스트 형식으로 만든 다음 판다스 로 저장

        # print(data)
        # print(type(data))

        cur.close()
        conn.close()
        # print(data)
        # print("_________")
        return data


if __name__ == "__main__":
    chart_dao.chart2()
