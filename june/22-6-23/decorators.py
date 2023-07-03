def car(text):
    return text.upper()


def brand(text):
    return text.lower()


def logo(text):
    return text.title()


def model(func):
    model_name = func("This is rolls royce spectre from RR.")
    print(model_name)


model(car)
model(brand)
model(logo)
