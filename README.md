# Emotion Recognition

A real-time implementation of emotion recognition made with PyTorch and OpenCV. Visit [here](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data) for more details about the dataset used for the training.

## Quick Start
### Install
1. Clone the repository
```bash
git clone https://github.com/hash-ir/Emotion-Recognition.git
cd Emotion-Recognition
```
2. For running the IPython notebook `Emotion Recognition.ipynb`, the following tools are required:
* [PyTorch](https://pytorch.org/get-started/locally/)
* [Open CV](https://pypi.org/project/opencv-python/)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)

An alternative is to make a conda environment from the `environment.yaml` file included in the repository:
```bash
conda env create -f environment.yaml
```
3. Once the dependencies are installed, replace the path of `haarcascade_frontalface_default.xml` with your path. Something like the following:
```bash
/home/<username>/anaconda3/lib/python3.x/site-packages/cv2/data/haarcascade_frontalface_default.xml
```
```bash
/home/<username>/anaconda3/lib/python3.x/site-packages/cv2/data/haarcascade_frontalface_default.xml
```

### Usage
1. For training, download the dataset from [here](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data), extract and put `fer2013.csv` in the root directory.
2. For testing, execute the first cell, network architecture code cell and last two code cells. Real-time testing requires webcam!

## Author(s)
* **Hashir Ahmad** - *full project* - [GitHub](https://github.com/hash-ir)

## License
This work is licensed under the [MIT License](https://github.com/hash-ir/Emotion-Recognition/blob/master/LICENSE).
