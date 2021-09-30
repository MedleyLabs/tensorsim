# tensorsim
Create simulated predictions based off ground truth data

## Introduction

The typical workflow for a machine learning project to go is roughly:

1. Data preparation
2. Model building
3. Model deployment

This approach falls short at mitigating risk during model deployment. For 
example, you could create a model with excellent accuracy. Yet it turns out that 
your users hate using it. Or the model latency is prohibitive.

Instead, tensorsim allows you to do things slightly differently:

1. Simulate the model deployment with ground truth data
2. Assess the value created by the model
3. If it's promising, do the typical workflow above

Let's say you have ground truth data in the form of medical images and 
associated diagnoses. And you want to simulate a model that predicts the 
diagnosis of each image with 80% accuracy.

With tensorsim, you can quickly deploy an API that returns a random image and 
a simulated prediction:

* 80% of the time, the API will return the correct diagnosis
* 20% of the time, the API will deliberately return an incorrect diagnosis

Now you provide real radiologists with a UI that shows a medical image and the
simulated prediction for the diagnosis. You compare the performance of
radiologists using the simulated predictions to the control radiologists who do
not receive any predictions.

If the radiologists do better with simulated predictions, you get evidence that
the model will be useful. And that evidence de-risks going through the expensive
process of data preparation and model building.

## Installation

`pip install tensorsim`

## Usage

Coming soon...!