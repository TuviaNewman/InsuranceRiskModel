Thanks for taking the time out to take a look at my work :-)

This repo holds all the files of a POC for an Insurance Risk model. The model decides whether a policy is too risky to accept.

There are many different parts of the POC:

### Presentation:
Risk_Model.pptx is a short and concise presentation for the non-technical product owners on the problem, our solution (the model), and how it all works and fits
together.

### Two notebooks:
1. Risk_model_EDA_and_v1: 
This notebook has a general EDA as I get a first look at the data. It also has an incorrect train of thought that I pursued before finding an answer about the 
work that cleared up a lot for me. In the spirit of transparency I left it in. 

2. Risk_model_v2: 
This notebook is more focused on modeling the problem and makes the assumption that you have looked over the EDA part of the first notebook. 

(Note: The map plots dont show up in git. After working on the problem for a long time, it just doesnt work. So unfortunately there are some plots that 
cant be seen without downlaoding and running the notebook locally.)  

### Dockerfile, predict.py & requirements:
Together these files can be used to create a microservice for the Risk Model.
The Dockerfile can be built and run. It containerizes the predict.py file and serialized models so they can be deployed to almost anywhere.
Obviously a full production system needs a lot more than this, but this is the first step that is necessary in order to deploy a model.

### Folders:
The data, media, and models folders hold just that. Data, media and pickled models. (There is nothing really interesting in these, they can be ignored.)

Enjoy!
