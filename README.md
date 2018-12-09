<img width="50%" src="http://ultro.browning.edu/images/UltroLogo6.png"/>
<p> Browning Ultro Website</p> 

# Installation Instructions

1. Clone this repo
  
    ```shell
    git clone https://github.com/gescalona1/ultro.browning.edu.git
    ```

2. Install [Conda](https://conda.io/miniconda.html)

3. Make the conda environment
	
    ```shell
    conda env create -f environment.yml
    ```
4. Activate the source

    ```shell
    source activate ultrowebsite
    ```
5. Migrations

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Run server
    
    ```shell
    python manage.py runserver
    ```