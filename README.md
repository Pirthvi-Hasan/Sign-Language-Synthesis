# Sign Language Synthesis

### Idea
Sign language is a mode of communication used by deaf and dumb people using hand gestures. The problem here is that these hand gestures can only be understood by people who have learnt it. Hence the idea is to convert these hand gestures into speech so that even normal people may understand and communicate with them.

### Modules
> Extracting Hand Coordinates.
> 
> Predicting Hand Gestures.
> 
> Speech Synthesis.

### Dataset
The dataset consists of images containing Alphabets ‘A-Z' in **American Sign Language (ASL)**, used by deaf and dumb people to communicate with each other.

*Link* : [ASL Dataset](https://www.kaggle.com/grassknoted/asl-alphabet)

### Directories
> [Parallel](https://github.com/Pirthvi-Hasan/Sign-Language-Synthesis/tree/main/Parallel) - Parallelized implementation of above modules using Ray library in Python.
> 
> [Resources](https://github.com/Pirthvi-Hasan/Sign-Language-Synthesis/tree/main/Resources) - Program files to extract hand coordinates from images, train a machine learning model to predict hand signs. 
> 
> [WebApp](https://github.com/Pirthvi-Hasan/Sign-Language-Synthesis/tree/main/WebApp) - A web application for Sign Language Synthesis deployed in **Flask (Python)**.
