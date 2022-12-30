import pandas as pd

def exportcsv(data):

    df = pd.DataFrame(data)

    df.to_csv('Movies.csv', index=False)

    # df.to_pickle('Movies.pickle')

    # df.to_html('Movies.html',index=False)

    return True

