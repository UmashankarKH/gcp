import pickle
import sys
import os
import sklearn.ensemble
import sklearn.ensemble._forest
import sklearn.tree
import sklearn.tree._classes

# Map all old module paths → new locations
sys.modules['sklearn.ensemble.forest'] = sklearn.ensemble._forest
sys.modules['sklearn.tree.tree'] = sklearn.tree._classes

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'randomForestRegressor.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("Model re-saved successfully!")