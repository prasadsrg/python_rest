from models.vendor_model import VendorModel


class VendorHelper:

    @staticmethod
    def model_mapping(model, view):

        # VendorModel(
        #     id=view.get('id', None),
        #     name=view.get('name', None),
        #     title=view.get('title', None),
        #     logo=view.get('logo', None),
        #     status=view.get('status', None)
        # )
        print(view.get('logo', None))
        model.id = view.get('id', None)
        model.name = view.get('name', None)
        model.title = view.get('title', None)
        model.logo = view.get('logo', None)
        model.status = view.get('status', None)

