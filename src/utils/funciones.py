

def crossv(model, x, y):
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(model, x, y, scoring="f1_micro", cv=3, n_jobs=-1, verbose=2)
    mean_score = scores.mean()
    return print(f'F1 scores: {scores}\nF1 micro mean: {mean_score}')

def metrics(x,y):
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    acc = accuracy_score(x,y)
    f1 = f1_score(x,y,average=None)
    f1av = np.mean( f1_score(x,y,average=None))
    #MATRIZ DE CONFUSION
    from sklearn.metrics import ConfusionMatrixDisplay
    disp = ConfusionMatrixDisplay.from_predictions(x, y)
    disp.ax_.set_title("Confusion Matrix from Predictions")
    return print(f'Accuracy score: {acc} \nF1 Score: {f1}\nMean F1: {f1av}'), plt.show()

def graph_feat(model,X):
    feat_impor = pd.DataFrame(model.feature_importances_)
    fimport = feat_impor.set_axis(X.columns, axis='index')
    fimport.sort_values(by=[0], ascending= False, inplace = True)
    from matplotlib import pyplot as plt
    fig = plt.figure(figsize=(12, 8))
    plt.barh(fimport.index, fimport[0])
    plt.xlabel('Feature Importances')
    plt.xticks(rotation = 90)
    plt.ylabel('Feature Labels')
    plt.title('Comparacion de la importancia de las variables')
    return plt.show()
