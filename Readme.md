# A support tool for the [Churchy](https://github.com/Kotauror/churchy) project.


## Transforming coordinates from e-mapa services

The purpose of using it is transforming coordinates as presented in the Polish e-mapa services, that is [PUGW 1992 aka EPSG:2081](https://gis-support.pl/baza-wiedzy-2/podstawy-gis/uklady-wspolrzednych-w-praktyce/) to the WSG84 format that's used on Google Maps.

### How to use it

1. Get the PUGW 1992 coordinates. I was getting them from https://polska.e-mapa.net/ as per images below.


![instruction1](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction1.png)


![instruction2](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction2.png)

1. Replace the `sample_puwg_1992_data.csv` file with your coordinates.
2. Run `python3 swapiner.py`. It prints the result but also copies to clipboard.  
3. Once you have the output of `python3 swapiner.py`, go to http://www.karto.pl/narzedzia/wspolrzedne and input it in the left box (make sure that 1992[metry] is selected).

![instruction3](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction3.png)

1. Copy them to the `sample_wsg84_data.csv` file and run the `db_prepper.py`. 
2. Copy over the result - it can now be inserted into the DB!


## Transforming coordinates from https://mapy.geoportal.gov.pl/

Transforming coordinates from https://mapy.geoportal.gov.pl/ requires an additional step. The benefit of this service is that it allows us to select polygons (and hence selecting the green area within th plot), but it's impossible to export the coordinates in a digestable way, so we need a bit of łopatologia to get there. 

1. Go to https://mapy.geoportal.gov.pl/imap/Imgp_2.html?gpmap=gp0
2. Follow the instruction as per the image below

![instruction4](https://github.com/Kotauror/puwg_1992_preparer/blob/main/images/instruction4.png)


3. The content that you've copied, paste it to the `sample_polluted_1992_data.csv` file. 
4. Run `unpollute_puwg_1992_data.py`.
5. Do the steps from the paragraph above. 


To test run `pytest` 