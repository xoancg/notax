import mvc.model as model
import mvc.view as view


def init_app():
    model.init_model()
    view.init_view()


if __name__ == "__main__":
    init_app()
