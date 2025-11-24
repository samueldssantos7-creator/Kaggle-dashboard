class Model:
    def __init__(self, model):
        self.model = model

    def save(self, filepath):
        import joblib
        joblib.dump(self.model, filepath)

    @classmethod
    def load(cls, filepath):
        import joblib
        model = joblib.load(filepath)
        return cls(model)