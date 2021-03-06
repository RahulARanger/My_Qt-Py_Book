import os
filename = "open.svg"
print(os.getcwd())
print(os.path.relpath(os.path.join(
            os.path.join(
                os.path.dirname(
                    os.path.dirname(__file__)
                ), "Resources"
            ), filename
        ), __file__), )
