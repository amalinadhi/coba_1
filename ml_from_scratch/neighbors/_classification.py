from ._base import NearestNeighbor

class KNeighborsClassifier(NearestNeighbor):
    def __init__(self):
        super().__init__()
        pass

    def check_classifier(self):
        print("cheked classifier")