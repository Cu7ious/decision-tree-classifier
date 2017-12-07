#!/Users/user/anaconda2/envs/classifier/bin/python

from sys import argv
from sklearn import tree

features = [[140, 0], [130, 0], [150, 1], [170, 1]]
'''
Features map:
  0: weight (n grams)
  1: texture
    0: smooth,
    1: bumpy
'''

labels = [0, 0, 1, 1]
'''
Labels map:
  0: apple
  1: orange
'''

# Create the empty classsifier
clf = tree.DecisionTreeClassifier()

# Revrite clf with `fit` learning algorhitm
clf = clf.fit(features, labels)

# Translate digital representation
# of the result into textual
def make_prediction (weight=0, texture=""):
    if (weight == 0 and texture == ""):
        prediction = clf.predict([[140, 0]])
        print """
Prediction for data example:
  weight: 140g,
  texture: smooth
"""
    else:
        try:
            weight = eval(weight)
        except SyntaxError:
            print "Error: Invalid type of weight, it should be a number"
            print "Exiting..."
            quit()


        if (texture != "bumpy" and texture != "smooth"):
            print "Error: Invalid type of texture, it should be"
            print "exactly 'bumpy' or 'smooth'"
            print "Exiting..."
            quit()

        texture = 1 if "bumpy" else 0
        prediction = clf.predict([[weight, texture]])

    if (prediction == 0):
        prediction = "it's an APPLE (0)"
    elif (prediction == 1):
        prediction = "it's an ORANGE (1)"

    print "Prediction Result:", prediction


if (len(argv) != 1):
    if (argv[1] == "-p" or argv[1] == "--prompt"):
        u_weight = raw_input("Input the fruit weight: ")
        u_texture = raw_input("Input the texture [bumpy|smooth]: ")

        make_prediction(u_weight, u_texture)

    elif (argv[1] == "-d"):
        args = " ".join(map(str, argv[2:])).split(",")

        d_weight = args[0].strip()
        d_texture = args[1].strip()

        make_prediction(d_weight, d_texture)

    elif (argv[1] == "-e"):
        make_prediction()
else:
        print """
Fruits Classifier
=================
Predicts if it's an apple or an orange
    -e show an example
    -p prompt data
    -d with inline data (-d 150,smooth)
"""
