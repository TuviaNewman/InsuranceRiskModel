import pandas as pd
from flask import Flask, request, jsonify
import dill
dill._dill._reverse_typemap['ClassType'] = type


class RiskModel:
    """
    Model for blocking risky requests
    """

    def __init__(self):
        """
        Load model on class initialization
        """
        with open('models/models_and_thresholds.pickle', 'rb') as f:
            self.renters_model, self.renters_threshold, self.homeowners_model, self.homeowners_threshold, self.columns \
                = dill.load(f)

    def predict(self, feature_dict):
        """
        Return decision for single request.
        feature_dict: dictionary of features where keys are feature names and values are feature values.
        returns: boolean. False iff we reject policy request.
        """
        product = feature_dict.get('product', 'ho4')
        request = pd.DataFrame(feature_dict, columns=self.columns, index=[0])

        if product == 'ho4':
            proba = self.renters_model.predict_proba(request)
            decision = True if proba[0][1] > self.renters_threshold else False

        else:
            proba = self.homeowners_model.predict_proba(request)
            decision = True if proba[0][1] > self.homeowners_threshold else False

        return decision

# create flask app
app = Flask(__name__)
# load risk model
rm = RiskModel()

@app.route('/test')
def root():
    """
    route for testing if service is running
    """
    return "Risk Model service is up and running :)"

@app.route('/predict',  methods=['POST'])
def predict():
    """
    route for using our risk model
    will return true in the Accept Policy? field if we should accept the policy, else false
    Example json: 
        {
            'id':2492008697672104938, 
            'state':'NM', 
            'postal_code':87043, 
            'product':'ho4', 
            'user_id':-9160046293075786063, 
            'high_risk_dog':0, 
            'has_fire_alarm':true, 
            'has_burglar_alarm':true, 
            'portable_electronics':0.0, 
            'fire_housing_proximity':'5', 
            'previous_policies':0, 
            'user_age':39.0, 
            'card_type':'credit'
        }"
    """
    # convert input to json format
    data = request.get_json()
    # predict with risk model
    final_decision = rm.predict(data)
    # output response to stdout
    return jsonify({"Accept policy?": final_decision})
    

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)


    
