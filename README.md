## Classification of dominant gaz in a room
## Objective
The goal of this project is to be able to classify (identify) dominant gaz in room given input data measured by 4 MQ sensors (MQ-135, MQ-9, MQ-7 and MQ-6).

An arduino nano, connected to the 4 sensors through its analog inputs, is used to collect data and send it to Raspberry pi via USB cable every 10 secondes. The Raspberry Pi runs a Node-red web server to collect the data and forward this data to a Flask local web service that run a model to predict the type of gaz present in the room.

To build the model, training data is required. So I've collected around 8000 observations during which the 4 sensors are exposed to 5 differents types of polluant gas : CO2/Smoke (4522 observations), Alchool (996), Flammable gas (780), exhaust gas (696) and CO (336). Please find attached these data in csv formatted file.
So let's begin!
