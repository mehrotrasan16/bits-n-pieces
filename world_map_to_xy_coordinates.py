#Ref: https://github.com/NikolayOskolkov/tSNE_vs_UMAP_GlobalStructure/blob/master/tSNE_vs_UMAP.ipynb

import cartopy
import matplotlib
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from skimage.io import imread
import cartopy.io.shapereader as shpreader

shapename = 'admin_0_countries'
countries_shp = shpreader.natural_earth(resolution='110m',
                                        category='cultural', name=shapename)

plt.figure(figsize = (20, 15))
ax = plt.axes(projection=ccrs.Miller())
ax.outline_patch.set_visible(False)
ax.set_extent([-180, 180, -50, 70])
for country in shpreader.Reader(countries_shp).records(): 
    #print(country.attributes['NAME_LONG'])
    if country.attributes['NAME_LONG'] in ['United States','Canada', 'Mexico']:
        ax.add_geometries(country.geometry, ccrs.Miller(),
                          label=country.attributes['NAME_LONG'], color = 'black')
        plt.savefig('NorthAmerica.png')
plt.close()
        
plt.figure(figsize = (20, 15))
ax = plt.axes(projection=ccrs.Miller())
ax.outline_patch.set_visible(False)
ax.set_extent([-180, 180, -50, 70])
for country in shpreader.Reader(countries_shp).records(): 
    if country.attributes['NAME_LONG'] in ['Brazil','Argentina', 'Peru', 'Uruguay', 'Venezuela', 
                                           'Columbia', 'Bolivia', 'Colombia', 'Ecuador', 'Paraguay']:
        ax.add_geometries(country.geometry, ccrs.Miller(),
                          label=country.attributes['NAME_LONG'], color = 'black')
        plt.savefig('SouthAmerica.png')
plt.close()

plt.figure(figsize = (20, 15))
ax = plt.axes(projection=ccrs.Miller())
ax.outline_patch.set_visible(False)
ax.set_extent([-180, 180, -50, 70])
for country in shpreader.Reader(countries_shp).records(): 
    if country.attributes['NAME_LONG'] in ['Australia']:
        ax.add_geometries(country.geometry, ccrs.Miller(),
                          label=country.attributes['NAME_LONG'], color = 'black')
        plt.savefig('Australia.png')
plt.close()


plt.figure(figsize = (20, 15))
ax = plt.axes(projection=ccrs.Miller())
ax.outline_patch.set_visible(False)
ax.set_extent([-180, 180, -50, 70])
for country in shpreader.Reader(countries_shp).records(): 
    if country.attributes['NAME_LONG'] in ['Russian Federation', 'China', 'India', 'Kazakhstan', 'Mongolia', 
                                          'France', 'Germany', 'Spain', 'Ukraine', 'Turkey', 'Sweden', 
                                           'Finland', 'Denmark', 'Greece', 'Poland', 'Belarus', 'Norway', 
                                           'Italy', 'Iran', 'Pakistan', 'Afganistan', 'Iraq', 'Bulgaria', 
                                           'Romania', 'Turkmenistan', 'Uzbekistan' 'Austria', 'Ireland', 
                                           'United Kingdom', 'Saudi Arabia', 'Hungary']:
        ax.add_geometries(country.geometry, ccrs.Miller(),
                          label=country.attributes['NAME_LONG'], color = 'black')
        plt.savefig('Eurasia.png')
plt.close()


plt.figure(figsize = (20, 15))
ax = plt.axes(projection=ccrs.Miller())
ax.outline_patch.set_visible(False)
ax.set_extent([-180, 180, -50, 70])
for country in shpreader.Reader(countries_shp).records(): 
    if country.attributes['NAME_LONG'] in ['Libya', 'Algeria', 'Niger', 'Marocco', 'Egypt', 'Sudan', 'Chad',
                                           'Democratic Republic of the Congo', 'Somalia', 'Kenya', 'Ethiopia', 
                                           'The Gambia', 'Nigeria', 'Cameroon', 'Ghana', 'Guinea', 'Guinea-Bissau',
                                           'Liberia', 'Sierra Leone', 'Burkina Faso', 'Central African Republic', 
                                           'Republic of the Congo', 'Gabon', 'Equatorial Guinea', 'Zambia', 
                                           'Malawi', 'Mozambique', 'Angola', 'Burundi', 'South Africa', 
                                           'South Sudan', 'Somaliland', 'Uganda', 'Rwanda', 'Zimbabwe', 'Tanzania',
                                           'Botswana', 'Namibia', 'Senegal', 'Mali', 'Mauritania', 'Benin', 
                                           'Nigeria', 'Cameroon']:
        ax.add_geometries(country.geometry, ccrs.Miller(),
                          label=country.attributes['NAME_LONG'], color = 'black')
        plt.savefig('Africa.png')
plt.close()


rng = np.random.RandomState(123)
plt.figure(figsize = (20, 15))
matplotlib.rcParams.update({'font.size': 22})


N_NorthAmerica = 10000
data_NorthAmerica = imread('NorthAmerica.png')[::-1, :, 0].T
X_NorthAmerica = rng.rand(4 * N_NorthAmerica, 2)
i, j = (X_NorthAmerica * data_NorthAmerica.shape).astype(int).T
X_NorthAmerica = X_NorthAmerica[data_NorthAmerica[i, j] < 1]
X_NorthAmerica = X_NorthAmerica[X_NorthAmerica[:, 1]<0.67]
y_NorthAmerica = np.array(['brown']*X_NorthAmerica.shape[0])
plt.scatter(X_NorthAmerica[:, 0], X_NorthAmerica[:, 1], c = 'brown', s = 50)

N_SouthAmerica = 10000
data_SouthAmerica = imread('SouthAmerica.png')[::-1, :, 0].T
X_SouthAmerica = rng.rand(4 * N_SouthAmerica, 2)
i, j = (X_SouthAmerica * data_SouthAmerica.shape).astype(int).T
X_SouthAmerica = X_SouthAmerica[data_SouthAmerica[i, j] < 1]
y_SouthAmerica = np.array(['red']*X_SouthAmerica.shape[0])
plt.scatter(X_SouthAmerica[:, 0], X_SouthAmerica[:, 1], c = 'red', s = 50)

N_Australia = 10000
data_Australia = imread('Australia.png')[::-1, :, 0].T
X_Australia = rng.rand(4 * N_Australia, 2)
i, j = (X_Australia * data_Australia.shape).astype(int).T
X_Australia = X_Australia[data_Australia[i, j] < 1]
y_Australia = np.array(['darkorange']*X_Australia.shape[0])
plt.scatter(X_Australia[:, 0], X_Australia[:, 1], c = 'darkorange', s = 50)

N_Eurasia = 10000
data_Eurasia = imread('Eurasia.png')[::-1, :, 0].T
X_Eurasia = rng.rand(4 * N_Eurasia, 2)
i, j = (X_Eurasia * data_Eurasia.shape).astype(int).T
X_Eurasia = X_Eurasia[data_Eurasia[i, j] < 1]
X_Eurasia = X_Eurasia[X_Eurasia[:, 0]>0.5]
X_Eurasia = X_Eurasia[X_Eurasia[:, 1]<0.67]
y_Eurasia = np.array(['blue']*X_Eurasia.shape[0])
plt.scatter(X_Eurasia[:, 0], X_Eurasia[:, 1], c = 'blue', s = 50)

N_Africa = 10000
data_Africa = imread('Africa.png')[::-1, :, 0].T
X_Africa = rng.rand(4 * N_Africa, 2)
i, j = (X_Africa * data_Africa.shape).astype(int).T
X_Africa = X_Africa[data_Africa[i, j] < 1]
y_Africa = np.array(['darkgreen']*X_Africa.shape[0])
plt.scatter(X_Africa[:, 0], X_Africa[:, 1], c = 'darkgreen', s = 50)

plt.title('Original World Map Data Set', fontsize = 25)
plt.xlabel('Dimension 1', fontsize = 22); plt.ylabel('Dimension 2', fontsize = 22)

plt.show()