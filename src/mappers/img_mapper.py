class ImgMapper:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def model_val_assign(self, param):
        if self.view.get(param) is not None:
            setattr(self.model, param, self.view[param])

    def model_mapping(self):
        if self.view and self.model:
            self.model_val_assign('id')
            self.model_val_assign('name')
            self.model_val_assign('src')


