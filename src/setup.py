import os
import setuptools

readme_path = os.path.join("..", "README.md")
with open(readme_path, "r") as f:
    long_description = f.read()

include_package_data=True,
package_data = {
'' : ['<path>/data.csv', '<path>/circle.csv'],
},

setuptools.setup(
    name                            = "tutorial-orquestra-sklearn",
    version                         = "0.1.0",
    author                          = "Zapata Computing, Inc.",
    author_email                    = "info@zapatacomputing.com",
    description                     = "Training models with scikit-learn in orquestra.",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/zapatacomputing/tutorial-orquestra-sklearn",
    packages                        = setuptools.find_packages(where = "python"),
    package_dir                     = {"" : "python"},
    include_package_data            = True,
    package_data                    = {'' : ['*.csv']},
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        "pandas",
        "sklearn",
        "numpy"
   ],
)