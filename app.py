from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model=pickle.load('Model/model.pickle', 'rb')