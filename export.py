import pandas as pd

def exportcsv(data):

    df = pd.DataFrame(data)

    df.to_csv('Movies.csv', index=False)

    return True

