# Part of case-study #2: Air balloon
# Developers: Khramchikhina A., Peshkov Y., Sanzhanova A., Yurshenaite A.
#

import ru_local as ru


def main():
    '''
    Main function.
    :return: None
    '''

    mass_skin = float(input(ru.MASS_SKIN))
    volume_l = float(input(ru.VOLUME_L))
    t_outside_c = float(input(ru.T_OUTSIDE_C))
    pressure = 10**5
    molar_mass = 29 * (10**(-3))
    gas_constant = 8.31
    specific_heat = 1_000
    
    t_outside_k = t_outside_c + 273.15
    volume_m3 = volume_l * (10**(-3))
    t_inside_k = (t_outside_k*molar_mass*volume_m3*pressure) / \
                 (molar_mass*pressure*volume_m3 - mass_skin*t_outside_k*gas_constant)
    t_inside_c = t_inside_k - 273.15
    t_inside_f = t_outside_c*9/5 + 32
    mass_air = pressure*molar_mass*volume_m3 / gas_constant*t_outside_k
    delta_t = t_inside_k - t_outside_k
    quantity_heat = specific_heat * mass_air * delta_t
        
    print(f'{ru.T_INSIDE_C} = {round(t_inside_c)}')
    print(f'{ru.T_INSIDE_K} = {round(t_inside_k)}')
    print(f'{ru.T_INSIDE_F} = {round(t_inside_f)}')
    print(f'{ru.QUANTITY_HEAT} = {round(quantity_heat)}')


if __name__ == '__main__':
    main()
    
