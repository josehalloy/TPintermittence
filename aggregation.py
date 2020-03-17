import numpy as np
import matplotlib.pyplot as plt

trait_dir = "./TRAITEMENTS/" # repertoire
filename = "eCO2mix_RTE_Occitanie_Annuel-Definitif_2018"

hours_1 = np.loadtxt(trait_dir + filename + '.hours')
data_1 = np.loadtxt(trait_dir + filename + '.data')

filename = "eCO2mix_RTE_Hauts-de-France_Annuel-Definitif_2018"

hours_2 = np.loadtxt(trait_dir + filename + '.hours')
data_2 = np.loadtxt(trait_dir + filename + '.data')

periode = hours_1

# source à utiliser
source = 2 

source_1 = data_1[ source,:]
source_2 = data_2[ source,:]

plot_gaussienne = True


def plot_temporelle( queldata, hours):
    # exemple de figure obtenue avec les données
    figname = " série temporelle "
    plt.close(figname)
    plt.figure(figname)
    plt.plot( hours, queldata )

def relative_variation(queldata):
    # Quel décalage temporel utiliser ?
    # attention à vérifer l'incrément de temps sur le fichier horaire !
    dt = 2
    queldata = (queldata[ dt:: ] - queldata[ :-dt: ]) / np.mean(queldata)
    # ajouter une gaussienne de même moyenne et écart type que la distribution ?
    mean = np.mean( queldata) # moyenne de la gaussienne
    std = np.std( queldata) # écart type de la gaussienne
    if plot_gaussienne:
        # paramètres de la gaussienne
        x_min = np.min( queldata)
        x_max = np.max( queldata)
        xx = np.linspace( x_min, x_max, 100)
        yy = 1 / (std * np.sqrt(2 * np.pi)) * np.exp( - (xx - mean)**2 / (2 * std**2) )
        plt.plot( xx, yy  , linewidth=2, color='r')

    print('')
    print('Sur la periode considérée, on releve la moyenne et l ecart type:')
    print('moyenne')
    print( mean)
    print('ecart type')
    print( std )
    print('')

    return queldata


# exemple de figures obtenue avec les données
figname = " agregation_temp "
plt.close(figname)
plt.figure(figname)
plt.plot( periode,  source_1 , 'r')
plt.plot( periode, source_2 , 'g')
plt.plot( periode, source_1 + source_2, 'b' )

plt.xlabel('Abs [unités ?]')
plt.ylabel('Ord [unités ?]')

figname = " agregationt_dist "
plt.close(figname)
plt.figure(figname)
plt.hist( relative_variation( source_1 )   , bins=100, log=1, density=1, color='r' )
plt.hist( relative_variation( source_2 )     , bins=100, log=1, density=1, color='g')
plt.hist( relative_variation(  source_1 + source_2 ), bins=100, log=1, density=1, color='b' )

plt.xlabel('Abs [unités ?]')
plt.ylabel('Ord [unités ?]')



plt.show(block=False)

