import urllib.request
import json
import pandas as pd
from sqlalchemy import create_engine ,text
from urllib.parse import quote




def main():

    engine = create_engine('postgresql+psycopg2://postgres:%s@localhost/red30' %quote('Rodopsin@7') )
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    Apidatafetch = urllib.request.urlopen(url)
    if Apidatafetch.getcode() == 200:
        data = Apidatafetch.read().decode("utf-8")
    else :
        print("Received an error from server, cannot retrieve results " +
              str(Apidatafetch.getcode()))

    if data != None:

        TheJson = json.loads(data)
        Features = pd.json_normalize(TheJson['features']).columns
        # Features.to_csv('TheFeaturesEarthquake.csv')
        ColumnName = []
        for key in Features:
            if len(key.split(".")) == 2:
                ColumnName.append(key.split(".")[1].upper())
            else:
                ColumnName.append(key.upper())
        FeaturesData = pd.json_normalize(TheJson['features'])
        FeaturesUpdated = pd.DataFrame(FeaturesData)
        FeaturesUpdated.columns = ColumnName
        del FeaturesUpdated['TYPE']


        with engine.connect() as session:

                FeaturesUpdated.to_sql('apipandaupload', engine)
                result = session.execute(text(' Select * from apipandaupload '))
                resultdf = pd.DataFrame(result)
                resultdf.to_csv('ApiPandaUpload.csv')















































if __name__ == "__main__":
    main()