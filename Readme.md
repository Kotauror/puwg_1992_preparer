# A support tool for the [Churchy](https://github.com/Kotauror/churchy) project.

The purpose of using it is transforming coordinates as presented in the Polish e-mapa services, that is [PUGW 1992 aka EPSG:2081](https://gis-support.pl/baza-wiedzy-2/podstawy-gis/uklady-wspolrzednych-w-praktyce/) to the WSG84 format that's used on Google Maps.

### How to use it

1. Get the PUGW 1992 coordinates. I was getting them from https://polska.e-mapa.net/ as per image no 1 and 2 below.
![instruction1](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction1.png)

![instruction2](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction2.png)

2. Replace the `sample_puwg_1992_data.csv` file with your coordinates.
3. Run `python3 swapiner.py`. It prints the result but also copies to clipboard.  
4. Once you have the output of `python3 swapiner.py`, go to http://www.karto.pl/narzedzia/wspolrzedne and input it in the left box (make sure that 1992[metry] is selected), see image no 3 below for details. 

![instruction3](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction3.png)

5. Copy them to the `sample_wsg84_data.csv` file and run the `db_prepper.py`. 
6. Copy over the result - it can now be inserted into the DB!

To test run `pytest` 

Image 1
![instruction1](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction1.png)

Image 2
![instruction2](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction2.png)

Image 3
![instruction3](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction3.png)
