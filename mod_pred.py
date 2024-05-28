import skops.io as sio

unknown_types = sio.get_untrusted_types(file='./model_files/model.skops')
model = sio.load('./model_files/model.skops', trusted=unknown_types)

labels = {0: 'No', 1: 'Yes'}

def mod_pred(X):
    pred = model.predict(X)[0]
    if pred == 1:
        prob = model.predict_proba(X).flatten()[1]
    else:
        prob = model.predict_proba(X).flatten()[0]

    return "Model predicts '{}' with {:.2f} probability.".format(labels[pred], prob)
